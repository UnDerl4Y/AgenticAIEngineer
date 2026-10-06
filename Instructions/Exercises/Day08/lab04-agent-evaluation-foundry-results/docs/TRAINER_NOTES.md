# Trainer Notes: Advanced Agent Evaluation Lab

## Recommended positioning

Use this lab after learners complete:

1. Create an agent in Azure AI Foundry.
2. Test the agent in the playground.
3. Understand basic evaluation concepts.
4. Run a simple portal-based evaluation.

This lab is the automation-focused version.

## Suggested course flow

```text
Lab 1: Create and test an Agent in Azure AI Foundry
Lab 2: Run Agent Evaluation from Foundry Portal
Lab 3: Advanced Agent Evaluation using Python SDK
Lab 4: Review results, improve agent, and re-evaluate
```

## Key explanation for learners

Evaluation is not the same as chatting with the agent.

Manual chat testing checks only a few examples. Evaluation checks the agent against a dataset and applies consistent scoring criteria.

## What makes this advanced

This lab includes:

- SDK-based execution.
- Environment configuration.
- Dataset upload.
- Generated rubric evaluator.
- Built-in evaluator configuration.
- Automated evaluation run.
- Portal result review.
- Re-evaluation workflow.

## Demo script for trainer

Use this explanation:

> In this lab, we are treating our agent like a software component that needs quality validation before release. The dataset acts like our test cases. The rubric evaluator acts like our scoring framework. Built-in evaluators add additional checks. After the script runs, we review the result in Foundry portal and decide what needs improvement.

## Common learner issues

### Learner uses model name instead of deployment name

Clarify that the script needs the deployment name configured inside the Foundry project.

### Learner cannot authenticate

Ask them to run:

```bash
az login
az account show
```

### Learner cannot find result

Ask them to use one of these options:

1. Open the report URL printed by the script.
2. Open Azure AI Foundry > Project > Evaluations > Latest run.

### Learner gets region-related issue

Explain that some evaluation capabilities can depend on feature availability in the selected project region. Use a supported project region or demonstrate from the trainer environment.

## Recommended discussion questions

1. Why should we evaluate agents before deployment?
2. Why is a dataset better than one-time manual testing?
3. What does a failed test case tell us?
4. How can evaluation be used as a release gate?
5. How would this lab fit into CI/CD or AgentOps?
