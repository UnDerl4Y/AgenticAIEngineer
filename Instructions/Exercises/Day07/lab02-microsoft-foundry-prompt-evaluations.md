---
lab:
   title: Microsoft Foundry Prompt Evaluations
   description: Learn how to evaluate generative AI applications in Microsoft Foundry using dataset-based evaluations to assess response quality, relevance, coherence, and safety.
   level: 300
   duration: 25
   islab: true
   status: 'released'
---

# Microsoft Foundry Prompt Evaluations

Microsoft Foundry provides evaluation capabilities to help you assess the quality, reliability, and safety of generative AI responses. Using dataset-based evaluations, you can measure responses against evaluation criteria such as relevance, coherence, and safety. Reviewing these evaluation results can help you identify areas for improvement in prompts, datasets, and model configuration before using a generative AI solution in a real-world or production scenario.

In this exercise, you'll explore how to create a dataset-based evaluation in Microsoft Foundry, configure the evaluation scope and criteria, and review the results.

This exercise will take approximately **25** minutes.

## Prerequisites

To complete this exercise, you need:

- Active Azure subscription.
- Access to Microsoft Foundry.
- Permission to use or deploy the required model.
- Prepared JSONL dataset for evaluation.
- Browser access to the Microsoft Foundry portal.

# Open Azure AI Foundry

1. Open Microsoft Edge.
2. Go to the Microsoft Foundry portal: https://ai.azure.com/
3. Sign in using the provided credentials.
4. Select the project `hakunamatata1`.

## Go to Evaluation

1. From the project page, click the **Build** tab on the top-right menu.

2. From the left navigation pane, select **Evaluation**.

3. Click **Create** to create a new evaluation.

4. Select **Target: Dataset** and click **Upload new dataset**.

5. Open the following GitHub folder and manually download the `credit_risk_management.jsonl` file:

   https://github.com/Kiran-255666/AgenticAIEngineer/tree/main/labfiles/Day07/lab02-microsoft-foundry-prompt-evaluations/

6. Give a name to the dataset, upload the downloaded dataset, and click **Upload**.

7. After the dataset is uploaded, click **Next**.

## Select Evaluation Scope

1. In the **Scope** section, select **Individual turns**. This option is suitable for this lab because the JSONL file contains separate question-and-response pairs rather than complete multi-turn conversations.

| Evaluation scope | Description |
| --- | --- |
| **Individual turns** | Use this option when each record contains a separate question and response, such as **Question** and **ExpectedResponse**. |

> **Important:** For this lab, select **Individual turns**. Do not change this setting.

2. Review the mapping based on the available columns, such as **Question** and **ExpectedResponse**. Do not change anything here and click **Next**.

## Criteria

1. In the **Criteria** section, observe the evaluators that are automatically suggested to assess the dataset responses.
2. Click **Next**.

## Submit the Evaluation

1. Review the evaluation configuration.
2. Provide a meaningful evaluation name.
3. Submit the evaluation run.

## Review Evaluation Results

1. Refresh the evaluation status if needed.
2. Open the completed evaluation run.
3. Review the scores, metrics, reasoning, and detailed data view.
4. Use the results to identify where prompt, model, or dataset improvements are required.

## Conclusion

In this exercise, you used a JSONL file in Microsoft Foundry to evaluate generative AI responses. You configured a dataset-based evaluation, selected the appropriate evaluation scope, reviewed the available evaluators, submitted the evaluation run, and reviewed the results.

In real-world scenarios, evaluation data may be provided in different formats, such as CSV, JSON, or other supported formats. While the input format may vary, the core evaluation process remains the same: prepare the data, configure the evaluation, run it, and review the results to identify areas for improvement.