# Lab: Monitor Your Azure AI Foundry Project 
 
> Using Azure Monitor metrics, alerts, diagnostic settings, and logs 
 
| Project | AgenticAIEngineer | 
|---|---| 
| Platform | Microsoft Azure Portal / Microsoft Foundry | 
| Lab Type | Monitoring and observability | 
 
## 1. Lab Overview 
 
In this lab, you will monitor the Microsoft Foundry project named **AgenticAIEngineer** from the Azure portal. 
 
You will explore the **Monitoring** section, understand the purpose of each monitoring option, and create a Metrics view with multiple Azure OpenAI metrics. 
 
## 2. Main Objective 
 
The main objective of this lab is to understand how to monitor an Azure AI Foundry project so that usage, performance, availability, and troubleshooting signals can be reviewed from one place. 
 
## 3. Learning Outcomes 
 
By the end of this lab, you will be able to: 
 
- Sign in to the Azure portal and open the **AgenticAIEngineer** Foundry project. 
- Identify the monitoring options available in the resource menu. 
- Understand the purpose of **Alerts, Metrics, Diagnostic settings, and Logs**. 
- Build a metric chart using at least five Azure OpenAI metrics. 
- Review operational signals such as request count, data usage, latency, and availability. 
 
## 4. Prerequisites 
 
Before starting this lab, make sure you have: 
 
- Azure portal access with the provided credentials. 
- Access to the **AgenticAIEngineer** Microsoft Foundry project. 
- Sufficient permissions to view Monitoring and Metrics for the resource. 
- Recent activity on the project so that metrics can display meaningful values. 
 
> [!TIP] 
> Recent activity on the project helps ensure that the selected metrics display meaningful data. 
 
## 5. Step-by-Step Instructions 
 
### Step 1: Sign in to the Azure Portal 
 
1. Open Microsoft Edge or any supported browser. 
2. Go to the **Azure portal**. 
3. Sign in using the credentials provided for the lab. 
4. Wait for the Azure portal home page to load. 
 
### Step 2: Open the Foundry Project 
 
1. In the Azure portal search bar, type **Foundry**. 
2. From the search results, open the **Foundry** resource or service. 
3. Select the project named **AgenticAIEngineer**. 
4. Confirm that the **AgenticAIEngineer** project overview page is displayed. 
 
### Step 3: Expand the Monitoring Section 
 
1. From the left menu, scroll down until the **Monitoring** section is visible. 
2. Expand **Monitoring** to view the available monitoring options. 
3. Review the available options before opening **Metrics**. 
 
> [!NOTE] 
> The Monitoring section provides different tools for viewing metrics, configuring alerts, routing diagnostic data, and investigating logs. 
 
## 6. Understand the Monitoring Options 
 
The Monitoring section contains several options that help with operational visibility. 
 
| Monitoring Option | Purpose | How It Helps in This Lab | 
|---|---|---| 
| **Alerts** | Notifies administrators when a configured metric or log condition is met. | Helps understand how monitoring can be made proactive instead of manually checking charts. | 
| **Metrics** | Displays numeric time-series data such as request count, latency, and availability. | Main area used in this lab to build a monitoring chart. | 
| **Diagnostic settings** | Routes platform logs and metrics to destinations such as Log Analytics, Storage Account, or Event Hub. | Helps understand how monitoring data can be retained or sent for advanced analysis. | 
| **Logs** | Allows detailed log data to be queried, usually using KQL, when diagnostic data is available. | Helps investigate detailed events and troubleshoot issues. | 
 
## 7. Open Metrics 
 
1. Under **Monitoring**, select **Metrics**. 
2. Confirm that the scope is set to **AgenticAIEngineer**. 
3. Set the time range to an appropriate value, such as **Local Time: Last 24 hours**. 
4. Select **Add metric** to start adding metrics to the chart. 
 
> [!TIP] 
> You can change the time range later if the selected period does not contain enough activity. 
 
## 8. Add Metrics to the Chart 
 
> [!NOTE] 
> Add **at least five metrics** to the chart. Repeat the **Add metric** process for each metric listed below. 
 
### Metric 1: Azure OpenAI Requests 
 
1. Select **Add metric**. 
2. Keep the **Scope** as `AgenticAIEngineer`. 
3. Select the appropriate **Metric Namespace**, such as **Cognitive Services / Azure OpenAI metrics**. 
4. In the **Metric** dropdown, select **Azure OpenAI Requests**. 
5. Set **Aggregation** to **Sum**. 
6. Confirm that the metric appears as a chip above the chart. 
 
> [!TIP] 
> **Why this metric is useful:** Shows the total number of Azure OpenAI requests during the selected time range. 
 
### Metric 2: Data In 
 
1. Select **Add metric**. 
2. Keep the **Scope** as `AgenticAIEngineer`. 
3. Select the appropriate **Metric Namespace**, such as **Cognitive Services / Azure OpenAI metrics**. 
4. In the **Metric** dropdown, select **Data In**. 
5. Set **Aggregation** to **Sum**. 
6. Confirm that the metric appears as a chip above the chart. 
 
> [!TIP] 
> **Why this metric is useful:** Shows how much input data is sent to the service. 
 
### Metric 3: Time Between Token 
 
1. Select **Add metric**. 
2. Keep the **Scope** as `AgenticAIEngineer`. 
3. Select the appropriate **Metric Namespace**, such as **Cognitive Services / Azure OpenAI metrics**. 
4. In the **Metric** dropdown, select **Time Between Token**. 
5. Set **Aggregation** to **Average**. 
6. Confirm that the metric appears as a chip above the chart. 
 
> [!TIP] 
> **Why this metric is useful:** Shows the average delay between streamed tokens and helps review response streaming performance. 
 
### Metric 4: Time to First Byte 
 
1. Select **Add metric**. 
2. Keep the **Scope** as `AgenticAIEngineer`. 
3. Select the appropriate **Metric Namespace**, such as **Cognitive Services / Azure OpenAI metrics**. 
4. In the **Metric** dropdown, select **Time to First Byte**. 
5. Set **Aggregation** to **Average**. 
6. Confirm that the metric appears as a chip above the chart. 
 
> [!TIP] 
> **Why this metric is useful:** Shows how quickly the service starts returning a response after a request is submitted. 
 
### Metric 5: Azure OpenAI Availability Rate 
 
1. Select **Add metric**. 
2. Keep the **Scope** as `AgenticAIEngineer`. 
3. Select the appropriate **Metric Namespace**, such as **Cognitive Services / Azure OpenAI metrics**. 
4. In the **Metric** dropdown, select **Azure OpenAI Availability Rate**. 
5. Set **Aggregation** to **Average**. 
6. Confirm that the metric appears as a chip above the chart. 
 
> [!TIP] 
> **Why this metric is useful:** Shows service availability during the selected time range. 
 
## 9. Optional Metrics to Explore 
 
After adding the required five metrics, you can explore additional metrics such as: 
 
| Metric | Purpose | 
|---|---| 
| **Time to Last Byte** | Helps review how long it takes for the complete response to be returned. | 
| **Time to Response** | Helps review overall response time. | 
| **Processed Fine-Tuned Training Hours** | Shows processed fine-tuning training time. | 
| **Generated Completion Tokens** | Shows the number of generated completion tokens. | 
| **Generated Prompt Tokens** | Shows the number of tokens used in prompts. | 
| **Total Tokens** | Shows the total number of tokens processed. | 
 
## 10. Review the Metrics Chart 
 
1. Review the chart after all selected metrics have been added. 
2. Check whether the lines or values show request activity, data usage, latency, or availability patterns. 
3. Use the legend below the chart to identify each metric. 
4. Use the time range selector to review another time window if required. 
5. Optionally, select **Save to dashboard** if the chart needs to be reused later. 
 
> [!NOTE] 
> The chart provides a quick operational view of the selected metrics. Use the time range and legend to focus on specific signals. 
 
## 11. Lab Conclusion 
 
In this lab, you monitored the **AgenticAIEngineer** Microsoft Foundry project from the Azure portal. 
 
You explored the **Monitoring** section and learned how **Alerts, Metrics, Diagnostic settings, and Logs** support operational visibility. 
 
### Key Takeaway 
 
> [!TIP] 
> Monitoring provides visibility into how an AI resource is being used and how it is performing. Metrics provide a quick operational view, while diagnostic settings and logs support deeper troubleshooting and analysis. 