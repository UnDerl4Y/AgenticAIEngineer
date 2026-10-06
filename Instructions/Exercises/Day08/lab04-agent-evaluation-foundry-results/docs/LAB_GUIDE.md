# Lab Guide: Advanced Agent Evaluation with Foundry Portal Result Review

## Scenario

You are working as an AI solution engineer. Your team has already created an Azure AI Foundry Agent. Before releasing it to users, you need to evaluate how well it responds to typical user queries.

In this lab, you automate the evaluation using Python SDK and then review the results in the Azure AI Foundry portal.

## Exercise 1: Review the dataset

Open:

```text
data/test_queries.jsonl
```

Each line contains one test query:

```jsonl
{"query": "Help me understand how to submit an employee expense claim."}
```

You can replace these queries with your own agent-specific test cases.

## Exercise 2: Configure the lab

Open `.env` and provide:

```env
AZURE_AI_PROJECT_ENDPOINT=
AZURE_AI_MODEL_DEPLOYMENT_NAME=
AGENT_NAME=
```

Use values from your Azure AI Foundry project.

## Exercise 3: Run evaluation script

Run:

```bash
python src/evaluate_agent_advanced.py
```

The script will:

1. Connect to the Foundry project.
2. Generate a rubric evaluator from the agent.
3. Upload the JSONL dataset.
4. Add built-in evaluators.
5. Create an evaluation.
6. Run evaluation against the agent.
7. Print the report URL.

## Exercise 4: Understand rubric dimensions

During execution, the script prints rubric dimensions generated from the agent context.

Discuss with learners:

- What criteria is the agent being judged on?
- Are these criteria suitable for the business use case?
- Should additional evaluation checks be added?

## Exercise 5: Review results in Foundry portal

After completion, open the report URL printed in terminal.

If the URL is not shown:

1. Open Azure AI Foundry.
2. Select your project.
3. Open **Evaluations**.
4. Select the latest evaluation run.

Review these areas:

- Overall run status.
- Number of passed and failed test cases.
- Agent Quality score.
- Coherence score.
- Violence safety score.
- Per-row query result.
- Evaluator reasoning.

## Exercise 6: Improve and re-evaluate

Choose one failed or weak result.

Update one of the following:

- Agent instructions.
- Agent knowledge source.
- Agent tool configuration.
- Dataset query wording.

Run the script again and compare the new result with the previous run.

## Completion criteria

The lab is complete when learners can:

- Run the SDK-based evaluation successfully.
- Open evaluation results in Foundry portal.
- Explain why at least one test case passed or failed.
- Suggest one improvement to the agent based on evaluator feedback.
