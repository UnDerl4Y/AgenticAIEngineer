# Advanced Lab: Azure AI Foundry Agent Evaluation using Python SDK and Portal Results

## Lab purpose

This advanced lab teaches learners how to automate evaluation for an existing Azure AI Foundry Agent using the Python SDK, and then review the evaluation results in the Azure AI Foundry portal.

This is the advanced version because learners do not only test the agent manually. They run a structured evaluation using:

- A JSONL test dataset.
- A generated rubric evaluator based on the agent context.
- Built-in evaluators such as violence and coherence.
- An evaluation run that returns a Foundry portal report URL.
- Portal-based result analysis.

## Learning objectives

By the end of this lab, learners will be able to:

1. Prepare a JSONL dataset for agent evaluation.
2. Connect to an Azure AI Foundry project using Python SDK.
3. Generate a rubric evaluator from an existing agent.
4. Configure built-in evaluators.
5. Run evaluation against a Foundry Agent.
6. Open and review the evaluation result in Azure AI Foundry portal.
7. Identify failed cases and suggest improvements to the agent.

## Lab directory structure

```text
AdvancedAgentEvaluationLab_FoundryPortalResults/
├── data/
│   └── test_queries.jsonl
├── docs/
│   ├── LAB_GUIDE.md
│   └── TRAINER_NOTES.md
├── results/
│   └── evaluation_run_summary.json    # Created after running the script
├── src/
│   └── evaluate_agent_advanced.py
├── .env.example
├── requirements.txt
├── setup.sh
└── README.md
```

## Prerequisites

Before starting this lab, ensure you have:

- Python 3.8 or later.
- Azure CLI installed.
- Azure login completed using `az login`.
- Azure AI Foundry project.
- Existing Azure AI Foundry Agent or hosted agent.
- GPT model deployment in the same project, for example `gpt-4o-mini` or `gpt-4o`.
- Foundry User role on the Foundry project.

## Setup steps

### Step 1: Extract the lab ZIP

Extract the ZIP file and open the folder in Visual Studio Code.

### Step 2: Create virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux/Bash:

```bash
python -m venv .venv
source .venv/bin/activate
```

### Step 3: Install packages

```bash
pip install -r requirements.txt
```

### Step 4: Sign in to Azure

```bash
az login
```

### Step 5: Configure environment variables

Copy `.env.example` to `.env`.

Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

macOS/Linux/Bash:

```bash
cp .env.example .env
```

Update these values in `.env`:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-foundry-resource>.services.ai.azure.com/api/projects/<your-project-name>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o-mini
AGENT_NAME=<your-agent-name>
```

Optional:

```env
AGENT_VERSION=
BUILTIN_EVALUATORS=builtin.violence,builtin.coherence
```

## Run the lab

From the root folder, run:

```bash
python src/evaluate_agent_advanced.py
```

## Expected output

The script will show:

1. Rubric evaluator generation status.
2. Generated rubric dimensions.
3. Dataset upload confirmation.
4. Built-in evaluator configuration.
5. Evaluation ID.
6. Evaluation run ID.
7. Final status.
8. Foundry portal report URL.

A local summary file will also be created:

```text
results/evaluation_run_summary.json
```

## Review result in Azure AI Foundry portal

After the script completes:

1. Copy the `Foundry portal report URL` from the terminal output and open it in a browser.
2. If the URL is not available, open Azure AI Foundry manually.
3. Select the same project used in `.env`.
4. Go to **Evaluations**.
5. Open the evaluation run created by the script.
6. Review:
   - Overall evaluation status.
   - Test case pass/fail results.
   - Evaluator-level results.
   - Agent Quality rubric result.
   - Built-in evaluator result, for example Coherence and Violence.
   - Failed cases and evaluator reasoning.

## Suggested learner activity

Ask learners to identify:

- Which query received the weakest score?
- Did the agent fail due to missing information, poor instruction following, tool usage, or unclear response?
- What change should be made to the agent instructions?
- After improving the agent, rerun the evaluation and compare results.

## Troubleshooting

### Missing environment variable

Check whether `.env` exists and values are filled correctly.

### Authentication error

Run:

```bash
az login
az account show
```

### Agent not found

Use the exact agent name from Azure AI Foundry. Agent name is case-sensitive in many SDK scenarios.

### Model deployment error

Use the deployment name from the project, not only the model name.

### Evaluation feature unavailable

Some evaluation features may depend on region and availability. If rubric generation or safety evaluation is unavailable, use the portal-based evaluation path or try the lab in a supported Foundry project region.
