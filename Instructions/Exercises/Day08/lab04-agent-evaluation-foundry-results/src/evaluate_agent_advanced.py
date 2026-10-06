"""
Advanced Azure AI Foundry Agent Evaluation Lab

This script runs an SDK-based evaluation for an existing Azure AI Foundry Agent.

Main flow:
1. Connect to Foundry project.
2. Generate rubric evaluator from agent context.
3. Continue even if SDK polling fails after rubric creation.
4. Upload JSONL dataset.
5. Add generated rubric and built-in evaluators.
6. Create evaluation.
7. Run evaluation against the agent.
8. Print Foundry portal report URL and save a local summary file under results/.

Why this workaround is included:
In some environments, the rubric evaluator is created successfully in Foundry,
but the SDK polling step fails with:
"Foundry-Features: Evaluations=V1Preview header required."

This script submits the rubric generation request, waits briefly, then uses the
known evaluator name directly for the next evaluation steps.

Run from the lab root folder:
    python src/evaluate_agent_advanced.py
"""

import json
import os
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.core.exceptions import HttpResponseError
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import (
    AgentEvaluatorGenerationJobSource,
    EvaluatorGenerationInputs,
    EvaluatorGenerationJob,
    TestingCriterionAzureAIEvaluator,
)
from openai.types.eval_create_params import DataSourceConfigCustom


ROOT_DIR = Path(__file__).resolve().parents[1]
DATASET_PATH = ROOT_DIR / "data" / "test_queries.jsonl"
RESULTS_DIR = ROOT_DIR / "results"
RESULTS_DIR.mkdir(exist_ok=True)


def require_env(name: str) -> str:
    value = os.getenv(name)

    if not value:
        raise ValueError(
            f"Missing required environment variable: {name}. "
            f"Check your .env file in the lab root folder."
        )

    return value


def get_foundry_feature_headers():
    foundry_features = os.getenv(
        "FOUNDRY_FEATURES",
        "Evaluations=V1Preview"
    )

    if foundry_features:
        return {
            "Foundry-Features": foundry_features
        }

    return None


def build_clients():
    load_dotenv(ROOT_DIR / ".env")

    endpoint = require_env("AZURE_AI_PROJECT_ENDPOINT")
    model_deployment = require_env("AZURE_AI_MODEL_DEPLOYMENT_NAME")
    agent_name = require_env("AGENT_NAME")
    agent_version = os.getenv("AGENT_VERSION") or None

    credential = DefaultAzureCredential()

    project_client = AIProjectClient(
        endpoint=endpoint,
        credential=credential,
        allow_preview=True
    )

    openai_client = project_client.get_openai_client()

    return project_client, openai_client, model_deployment, agent_name, agent_version


def generate_rubric_evaluator(project_client, model_deployment, agent_name):
    print("\n[1/6] Generating rubric evaluator from agent context...")

    evaluator_name = os.getenv("RUBRIC_EVALUATOR_NAME")

    if not evaluator_name:
        evaluator_name = f"agent-quality-{uuid.uuid4().hex[:8]}"

    evaluator_display_name = os.getenv(
        "RUBRIC_EVALUATOR_DISPLAY_NAME",
        "Agent Quality"
    )

    job = EvaluatorGenerationJob(
        inputs=EvaluatorGenerationInputs(
            model=model_deployment,
            evaluator_name=evaluator_name,
            evaluator_display_name=evaluator_display_name,
            sources=[
                AgentEvaluatorGenerationJobSource(
                    agent_name=agent_name
                )
            ],
        )
    )

    headers = get_foundry_feature_headers()

    print(f"  Requested rubric evaluator name: {evaluator_name}")
    print(f"  Rubric display name: {evaluator_display_name}")

    poller = None

    try:
        if headers:
            try:
                poller = project_client.beta.evaluators.begin_create_generation_job(
                    job=job,
                    headers=headers
                )
            except TypeError:
                poller = project_client.beta.evaluators.begin_create_generation_job(
                    job=job,
                    extra_headers=headers
                )
        else:
            poller = project_client.beta.evaluators.begin_create_generation_job(
                job=job
            )

        print("  Rubric generation request submitted.")

    except HttpResponseError as ex:
        print("  Rubric generation request failed before submission.")
        print(f"  Error: {ex.message}")
        raise

    except Exception as ex:
        print("  Rubric generation request failed before submission.")
        print(f"  Error: {ex}")
        raise

    # Best-effort polling only.
    # In some environments, the evaluator gets created in Foundry but polling fails.
    if poller:
        try:
            poll_attempts = int(os.getenv("RUBRIC_POLL_ATTEMPTS", "3"))

            for attempt in range(1, poll_attempts + 1):
                print(f"  Checking rubric generation status attempt {attempt}/{poll_attempts}...")

                try:
                    status = poller.status()
                    print(f"  Rubric generation status: {status}")
                except Exception as status_error:
                    print("  Could not read rubric status from SDK poller.")
                    print(f"  Status polling issue: {status_error}")
                    break

                try:
                    if poller.done():
                        rubric_evaluator = poller.result()

                        print(
                            f"  Generated rubric evaluator: "
                            f"{rubric_evaluator.name} v{rubric_evaluator.version}"
                        )

                        try:
                            print("  Review rubric dimensions below:")

                            for dim in rubric_evaluator.definition.dimensions:
                                print(
                                    f"   - {dim.id} | weight {dim.weight} | "
                                    f"{dim.description}"
                                )

                        except Exception:
                            print("  Rubric dimensions could not be printed from SDK result.")

                        return rubric_evaluator.name

                except Exception as poll_error:
                    print("  SDK polling failed after rubric request submission.")
                    print("  Continuing with the requested evaluator name.")
                    print(f"  Polling issue: {poll_error}")
                    break

                time.sleep(5)

        except Exception as polling_error:
            print("  Rubric generation request was submitted, but polling could not complete.")
            print(f"  Polling error: {polling_error}")

    wait_seconds = int(os.getenv("RUBRIC_AVAILABLE_WAIT_SECONDS", "30"))

    print(
        f"  Waiting {wait_seconds} seconds for rubric evaluator to become available in Foundry..."
    )

    time.sleep(wait_seconds)

    print(f"  Continuing with rubric evaluator name: {evaluator_name}")

    return evaluator_name


def upload_dataset(project_client):
    print("\n[2/6] Uploading JSONL test dataset to Foundry...")

    if not DATASET_PATH.exists():
        raise FileNotFoundError(f"Dataset file not found: {DATASET_PATH}")

    dataset_name = os.getenv("DATASET_NAME", "agent-test-queries")

    dataset_version = os.getenv("DATASET_VERSION")

    if not dataset_version:
        dataset_version = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")

    dataset = project_client.datasets.upload_file(
        name=dataset_name,
        version=dataset_version,
        file_path=str(DATASET_PATH),
    )

    print(f"  Dataset uploaded: {dataset.name} v{dataset.version}")
    print(f"  Dataset id: {dataset.id}")

    return dataset


def create_testing_criteria(rubric_evaluator_name, model_deployment):
    print("\n[3/6] Creating testing criteria...")

    testing_criteria = [
        TestingCriterionAzureAIEvaluator(
            type="azure_ai_evaluator",
            name="Agent Quality",
            evaluator_name=rubric_evaluator_name,
            initialization_parameters={
                "deployment_name": model_deployment
            },
            data_mapping={
                "query": "{{item.query}}",
                "response": "{{sample.output_items}}",
            },
        )
    ]

    print(f"  Added rubric evaluator: {rubric_evaluator_name}")

    builtins = os.getenv(
        "BUILTIN_EVALUATORS",
        "builtin.violence,builtin.coherence"
    )

    for evaluator_name in [x.strip() for x in builtins.split(",") if x.strip()]:
        display_name = (
            evaluator_name
            .replace("builtin.", "")
            .replace("_", " ")
            .title()
        )

        kwargs = {
            "type": "azure_ai_evaluator",
            "name": display_name,
            "evaluator_name": evaluator_name,
            "data_mapping": {
                "query": "{{item.query}}",
                "response": "{{sample.output_text}}",
            },
        }

        if evaluator_name == "builtin.coherence":
            kwargs["initialization_parameters"] = {
                "deployment_name": model_deployment
            }

        testing_criteria.append(
            TestingCriterionAzureAIEvaluator(**kwargs)
        )

        print(f"  Added built-in evaluator: {evaluator_name}")

    return testing_criteria


def create_evaluation(openai_client, testing_criteria):
    print("\n[4/6] Creating evaluation definition...")

    data_source_config = DataSourceConfigCustom(
        type="custom",
        item_schema={
            "type": "object",
            "properties": {
                "query": {
                    "type": "string"
                }
            },
            "required": ["query"],
        },
        include_sample_schema=True,
    )

    headers = get_foundry_feature_headers()
    kwargs = {}

    if headers:
        kwargs["extra_headers"] = headers

    retries = int(os.getenv("EVALUATION_CREATE_RETRIES", "12"))
    delay_seconds = int(os.getenv("EVALUATION_CREATE_RETRY_DELAY_SECONDS", "10"))

    last_error = None

    for attempt in range(1, retries + 1):
        try:
            print(f"  Creating evaluation attempt {attempt}/{retries}...")

            evaluation = openai_client.evals.create(
                name=os.getenv(
                    "EVALUATION_NAME",
                    "Advanced Agent Quality Evaluation"
                ),
                data_source_config=data_source_config,
                testing_criteria=testing_criteria,
                **kwargs
            )

            print(f"  Evaluation created: {evaluation.id}")
            return evaluation

        except Exception as ex:
            last_error = ex
            print(f"  Evaluation creation failed: {ex}")

            if attempt < retries:
                print("  Retrying after delay...")
                time.sleep(delay_seconds)

    raise RuntimeError(
        "Evaluation creation failed after retries. "
        "The rubric evaluator may not be available yet in Foundry."
    ) from last_error


def start_evaluation_run(openai_client, evaluation, dataset, agent_name, agent_version):
    print("\n[5/6] Starting evaluation run against the Foundry Agent...")

    target = {
        "type": "azure_ai_agent",
        "name": agent_name,
    }

    if agent_version:
        target["version"] = agent_version

    headers = get_foundry_feature_headers()
    kwargs = {}

    if headers:
        kwargs["extra_headers"] = headers

    eval_run = openai_client.evals.runs.create(
        eval_id=evaluation.id,
        name=os.getenv(
            "EVALUATION_RUN_NAME",
            "Agent Evaluation Run - SDK Lab"
        ),
        data_source={
            "type": "azure_ai_target_completions",
            "source": {
                "type": "file_id",
                "id": dataset.id,
            },
            "input_messages": {
                "type": "template",
                "template": [
                    {
                        "type": "message",
                        "role": "user",
                        "content": {
                            "type": "input_text",
                            "text": "{{item.query}}",
                        },
                    }
                ],
            },
            "target": target,
        },
        **kwargs
    )

    print(f"  Evaluation run started: {eval_run.id}")

    return eval_run


def monitor_run(openai_client, evaluation, eval_run, rubric_evaluator_name, agent_name):
    print("\n[6/6] Monitoring run status...")

    headers = get_foundry_feature_headers()
    kwargs = {}

    if headers:
        kwargs["extra_headers"] = headers

    while True:
        run = openai_client.evals.runs.retrieve(
            run_id=eval_run.id,
            eval_id=evaluation.id,
            **kwargs
        )

        print(f"  Current status: {run.status}")

        if run.status in ["completed", "failed", "cancelled"]:
            break

        time.sleep(5)

    report_url = getattr(run, "report_url", None)
    result_counts = getattr(run, "result_counts", None)

    print("\n========== Evaluation Completed ==========")
    print(f"Status: {run.status}")
    print(f"Foundry portal report URL: {report_url}")

    summary = {
        "completed_at_utc": datetime.now(timezone.utc).isoformat(),
        "evaluation_id": evaluation.id,
        "run_id": eval_run.id,
        "status": run.status,
        "report_url": report_url,
        "result_counts": str(result_counts),
        "rubric_evaluator_name": rubric_evaluator_name,
        "agent_name": agent_name,
        "note": (
            "Open the report URL or go to Azure AI Foundry > "
            "Project > Evaluations to review the result."
        ),
    }

    summary_file = RESULTS_DIR / "evaluation_run_summary.json"

    summary_file.write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8"
    )

    print(f"Local summary saved to: {summary_file}")

    return run


def main():
    project_client, openai_client, model_deployment, agent_name, agent_version = build_clients()

    rubric_evaluator_name = generate_rubric_evaluator(
        project_client,
        model_deployment,
        agent_name
    )

    dataset = upload_dataset(project_client)

    testing_criteria = create_testing_criteria(
        rubric_evaluator_name,
        model_deployment
    )

    evaluation = create_evaluation(
        openai_client,
        testing_criteria
    )

    eval_run = start_evaluation_run(
        openai_client,
        evaluation,
        dataset,
        agent_name,
        agent_version
    )

    monitor_run(
        openai_client,
        evaluation,
        eval_run,
        rubric_evaluator_name,
        agent_name
    )


if __name__ == "__main__":
    main()