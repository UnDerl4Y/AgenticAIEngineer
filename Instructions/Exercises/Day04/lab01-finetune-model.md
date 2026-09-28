---
lab:
  title: Fine-tune a language model
  description: Learn how to use your own training data to fine-tune a model and customize its behavior.
  level: 300
  duration: 90
  islab: true
  status: 'released'
---

# Fine-tune a language model

**Prompt engineering** means giving a language model instructions for a specific task or conversation. For example, you can tell a model, *"Act as a credit analyst and explain your decision with the key factors."* The model follows those instructions for that interaction.

**Fine-tuning** is different. Instead of relying only on instructions, you provide the model with example inputs and the responses you expect. The model learns those patterns and can follow the desired behavior more consistently.

### Real-world example

Imagine a bank wants an AI assistant to review business loan applications. You could give it examples showing how to assess:

* Company documents
* Compliance requirements
* Financial ratios
* Credit history
* Industry risk

For example, if a company's financial information is incomplete, the training examples can show the assistant that it should **identify the missing information instead of making assumptions**.

In this exercise, you will build a **credit risk management assistant** that follows this type of assessment consistently.

## What you will do

1. **Test the prepared `gpt-5.4-mini` model** in the playground and observe how it responds to credit-risk scenarios.
2. **Create a supervised fine-tuning job** using `gpt-4.1` and the provided training data.
3. **Test the fine-tuned model** and compare its responses with the prepared base model.

The goal is to understand how example-based training can make a model's behavior more consistent for a specific use case.

This exercise takes approximately **90 minutes**.

> **Note:** Fine-tuning depends on cloud capacity and can take 60 minutes or longer. Some portal features are in preview or under active development, so you may see warnings or unexpected behavior. You can continue with the playground-testing tasks while the job runs.

## Prerequisites

Before you start, ensure that you have:

- An active [Azure subscription](https://azure.microsoft.com/free/)
- A web browser
- A Microsoft Foundry project prepared by your trainer or lab environment
- The **gpt-5.4-mini** model available for the initial playground test
- The **gpt-4.1** model available for the supervised fine-tuning job
- Permission to create fine-tuning jobs and upload datasets

> The project and required models are already prepared for this exercise. Do not create a new project or add another base model.

# Verify the existing project

Microsoft Foundry projects organize the models, resources, data, and other assets used to build an AI solution.

1. Open the [Microsoft Foundry portal](https://ai.azure.com) and sign in with your Azure credentials if you haven’t already. Close any tips or quick-start panes that appear.
1. On the home page, ensure that you are in the **hakunamatata** project.
1. Open the model playground and confirm that the prepared **gpt-5.4-mini** model is available.

    > **Tip**: If you cannot find the project or gpt-5.4-mini, check with your trainer before continuing.

# Download the training data

1. Open the [training dataset](https://github.com/Kiran-255666/AgenticAIEngineer/blob/main/labfiles/Day03/lab04-fine-tuning/credit_risk_management.jsonl) in a browser.
1. Download the file and save it locally as `credit_risk_management.jsonl`.

    > **Important**: Your browser may save the file with a `.txt` extension. If it does, rename the file so that its name ends in `.jsonl`.

# Start a fine-tuning job

Start the job now. It may take a while, so you can test gpt-5.4-mini in the playground while the fine-tuning job runs.

1. In the Foundry portal, select **Fine-tune** in the left navigation.

    ![Fine-tuning page with an arrow pointing to Start fine-tuning.](../../media/fine-tune-001.png)

1. Select **Start fine-tuning**.
1. In **Basic details**, configure the job as follows:

    - **Customization method**: Supervised
    - **Model**: gpt-4.1
    - **Training type**: Data Zone

    ![Basic details page showing Supervised, gpt-4.1, and Data Zone selected.](../../media/fine-tune-002.png)

1. Select **Next**.
1. In **Datasets**, under **Training data source**, select **Upload or drag and drop**. Upload `credit_risk_management.jsonl`.
1. Confirm that the upload finishes and that the Dataset preview displays the file content and JSONL rows.
1. Leave **Validation data source (optional)** empty.

    ![Datasets page showing travel-finetune-hotel.jsonl uploaded and previewed.](../../media/fine-tune-003.png)

1. Select **Next** to open **Optional settings**.
1. Configure or confirm these settings:

    - **Display name**: Keep the generated name, or enter `ft-credit`
    - **Seed**: Keep the default value, **Random**
    - **Automatically deploy model after job completion**: Turn this on
    - **Deployment type**: Developer
    - **Hyperparameter tuning**: Keep **Default** selected for batch size, number of epochs, and learning-rate multiplier

    ![Optional settings page showing a generated display name, Random seed, automatic deployment control, and default hyperparameters.](../../media/fine-tune-004.png)

1. Select **Submit** to start the job.

> **Note:** Fine-tuning and deployment can take **60 minutes or longer**.

> **Tip:** To save time, you can skip the fine-tuning and deployment process and use the fine-tuned model that has already been prepared for you. In the left panel, select **Models** and choose **`-1-mini-2025-04-14-ft-e964800ce9314ff48f02e707134951d8-ft-credit`**.

![Snippet](../../media/w8.png)

# Test gpt-5.4-mini in the playground

> **Tip:** Keep a copy of the **prompts and model responses in Notepad** as you work through the steps. This will make it easier to compare the **base model and fine-tuned model** later.

While the fine-tuning job is running, test the prepared **gpt-5.4-mini** model in the playground. This will help you see how different instructions affect the model's responses.

1. Open the model playground for **gpt-5.4-mini**.

2. In the chat pane, enter the following question:

```text
What can you do?
```

Review the response. It may be general because no task-specific instructions have been provided yet.

3. In the **Instructions** field, enter:

```text
You are an AI assistant that helps assess the creditworthiness of business clients.
```

4. Ask the same question again:

```text
What can you do?
```

Compare this response with the previous one. The model may now focus more on helping with business credit assessment, but the behavior is still relatively general.

5. Replace the instructions with the following more detailed credit risk prompt:

```text
You are an AI credit risk management assistant that helps assess the creditworthiness of business clients. Your objective is to evaluate company documents, compliance status, financial ratios, external credit information, and industry risk using the provided credit risk assessment rules.

Do not invent missing financial or compliance information.

Clearly identify missing documents or data and explain how they affect the assessment.
```

6. Test the model using the following questions. For each response, record the **answer, tone, and writing style in Notepad**. You will use these responses later when testing the fine-tuned model.

**Question 1**

```text
What documents are required to start a credit risk assessment?
```

**Question 2**

```text
The client uploaded only the GST Certificate. Can we pass the document verification step?
```

**Question 3**

```text
A company has a Current Ratio of 1.56, Debt-to-Equity of 1.86, and Net Profit Margin of 5.56%. How many points does it receive for these three financial metrics?
```

**Question 4**

```text
How does industry risk affect the credit score?
```

**Question 5**

```text
What happens if a sanctions or compliance match is confirmed?
```

7. Keep the responses in Notepad. You will compare these **gpt-5.4-mini base-model responses** with the responses from the **fine-tuned model** in the next section.


# Review the training data

The training file contains examples of the behavior and writing style that you want the fine-tuned model to learn.

1. Open the downloaded `credit_risk_management.jsonl` file in a text editor.

2. Review the JSONL entries. The first entry should look similar to the following example, formatted for readability:

```json
{"messages": [
  {
    "role": "system",
    "content": "You are an AI credit risk management assistant that helps assess the creditworthiness of business clients. Your objective is to evaluate company documents, compliance status, financial ratios, external credit information, and industry risk using the provided credit risk assessment rules. Do not invent missing financial or compliance information. Clearly identify missing documents or data and explain how they affect the assessment."
  },
  {
    "role": "user",
    "content": "What documents are required to start a credit risk assessment?"
  },
  {
    "role": "assistant",
    "content": "The assessment requires both the Company Registration Certificate and GST Certificate. The company name must match exactly across the client information and both certificates. The assessment should also verify the company's legal status, sanctions or adverse compliance records, financial statements for the last two financial years, and the latest external credit score or rating."
  }
]}
```

Each entry includes system instructions, a credit-risk-related user question, and an assistant response that you want the model to learn. These examples help the fine-tuned model produce more consistent credit risk assessments and follow the defined scoring rules.

### Test the fine-tuned model

1. In the left navigation, select **Models**.

2. Find and open the prepared fine-tuned model:

   **`-1-mini-2025-04-14-ft-e964800ce9314ff48f02e707134951d8-ft-credit`**

> **Tip:** Fine-tuning and deployment can take **60 minutes or longer**. To save time, you can skip waiting for the fine-tuning job and use the fine-tuned model that has already been prepared for you.

3. Open the fine-tuned model in the **model playground**.

4. In the **Instructions** field, enter the **same credit risk management prompt** used when testing the base model:

```text
You are an AI credit risk management assistant that helps assess the creditworthiness of business clients. Your objective is to evaluate company documents, compliance status, financial ratios, external credit information, and industry risk using the provided credit risk assessment rules.

Do not invent missing financial or compliance information.

Clearly identify missing documents or data and explain how they affect the assessment.
```

5. Ask the **same five questions** that you tested with the base **gpt-5.4-mini** model:

**Question 1**

```text
What documents are required to start a credit risk assessment?
```

**Question 2**

```text
The client uploaded only the GST Certificate. Can we pass the document verification step?
```

**Question 3**

```text
A company has a Current Ratio of 1.56, Debt-to-Equity of 1.86, and Net Profit Margin of 5.56%. How many points does it receive for these three financial metrics?
```

**Question 4**

```text
How does industry risk affect the credit score?
```

**Question 5**

```text
What happens if a sanctions or compliance match is confirmed?
```

6. Compare these responses with the **base model responses saved in Notepad**. Look for differences in:

   * **Response consistency**
   * **Tone and writing style**
   * **Adherence to the credit risk instructions**
   * **Use of the defined credit risk assessment rules**
   * **Handling of missing information**
   * **Accuracy and completeness of the responses**

> **Tip:** Use the responses you saved in Notepad as a direct reference when comparing the two models. This makes it easier to see what changed after fine-tuning.

## Conclusion

In this lab, you learned how **fine-tuning** can make a language model more consistent for a specific use case.

You first tested **gpt-5.4-mini** in the playground and used different instructions to see how they affected the model's responses. You then worked with a **credit risk management dataset** in JSONL format and used it to fine-tune **gpt-4.1**. Finally, you tested the prepared fine-tuned model using the same credit risk questions and compared its responses with the **gpt-5.4-mini** responses saved in Notepad.

The main takeaway is that fine-tuning is useful when you want a model to consistently follow **task-specific behavior, terminology, response patterns, or business rules**.

In real-world applications, you can use fine-tuning for use cases such as **customer support, document processing, financial analysis, classification, coding assistants, and internal business workflows**. You are not limited to the models used in this lab. You can explore other supported models and choose an approach based on your application's requirements, cost, performance, and complexity.

You can also combine fine-tuning with **prompt engineering, RAG, and tools** depending on the problem you are solving.

**By completing this lab, you have gone through the complete fine-tuning workflow: preparing training examples, starting a fine-tuning job, testing the base model, testing the fine-tuned model, and comparing their responses.**
