---
lab:
    title: 'Integrate an AI agent with Foundry IQ'
    description: 'Use Azure AI Agent Service to develop an agent that uses Foundry IQ to search knowledge bases.'
    level: 300
    duration: 45
    islab: true
    status: 'released'
---

# Integrate an AI agent with Foundry IQ

**Note: We have already updated the mentioned files with the code mentioned in the instructions, but we would highly suggest going through it before executing it**

In this exercise, you'll configure an AI agent that uses Foundry IQ to search and retrieve information from a knowledge base. You'll use your existing Foundry project and deployed models, create a search resource and knowledge base with credit-risk assessment data, configure an agent, and then connect to it from Visual Studio Code.

This exercise should take approximately **45** minutes to complete.

## Prerequisites

Before starting this exercise, ensure you have:

- An [Azure subscription](https://azure.microsoft.com/free/)
- [Visual Studio Code](https://code.visualstudio.com/) installed on your local machine
- [Python 3.13](https://www.python.org/downloads/) or later installed
- An existing Foundry project with deployed chat and embedding models
- Basic familiarity with the Microsoft Foundry portal and Python programming

## Use your Foundry project and deployed models

This lab uses the Foundry project and deployed models that are already available to you. You don't need to create a new Foundry project or deploy a new model for this exercise.

1. In a web browser, open the [Foundry portal](https://ai.azure.com) and sign in using your Azure credentials.
1. Select your existing Foundry project **(hakunamatata1)** from the project selector.
1. On the project home page, verify that **gpt-5.4-mini** chat model and **text-embedding-3-small** embedding model are already deployed and available.
1. Keep the Foundry portal open. You'll use the existing chat model when creating the agent and knowledge base, and the existing embedding model when creating the knowledge source.

## Create an agent

Create an agent that will search the credit-risk knowledge base.

1. On the project home page, find the **Build an agent** card and select **Start building**.

2. Create an agent with a descriptive name, such as `credit-risk-assessment-agent`, and set the **Interaction mode** to **Text**.

3. Select **Create**.

4. After the agent is created, the agent playground opens. You'll now configure the agent with credit-risk assessment information from Foundry IQ.


## Configure data and Foundry IQ

> ****Important:**** The following resource creation steps are ****optional****. We have already provisioned the required Azure AI Search and Storage Account resources for this lab, so you can skip these steps and use the provided resources. You can still go through these steps separately to explore and learn how these resources are created and configured.

First, add instructions to your agent. Then create a search resource, upload the credit-risk assessment documents, and create a knowledge base that connects those documents to the agent.

1. Give your agent the following instructions:

    ```
    You are a helpful AI assistant for credit-risk assessment.
    You must ALWAYS search the knowledge base to answer questions about the company documents,
    financial information, credit bureau information, and credit-risk assessment rules.
    Provide detailed, accurate information and always cite your sources.
    If you don't find relevant information in the knowledge base, say so clearly.
    ```

1. Select **Save** to save your current agent configuration.
1. In the **Knowledge** section, expand the **Add** dropdown and select **Connect to Foundry IQ**. (Please select the one which your instrutor has created for you)
1. In the Foundry IQ setup window, select **Connect to an AI Search resource**, then select **Create new resource**.
1. Create a search resource with the following settings:

    - **Resource name**: A globally unique name
    - **Subscription**: Your Azure subscription
    - **Resource group**: Use the same resource group as your Foundry project  - **AgenticAIEngineer**
    - **Region**: The same location as your Foundry project
    - **Pricing tier**: Basic
    - **Foundry IQ Knowledge base capabilities**: Pause until next month

The search resource provides the retrieval layer for the knowledge base. Next, upload the source credit-risk assessment documents.

1. Open the prepared credit-risk assessment PDF files from `labfiles\Day05\lab05-integrate-agent-with-foundry-iq\data`.

    The folder contains the following files:

    ```
    company_documents.pdf
    financial_data.pdf
    credit_bureau_report.pdf
    credit_risk_assessment_rules.pdf
    ```

1. Open the [Azure portal](https://portal.azure.com). In the top search bar, search for **Storage accounts** and select **Storage accounts**.
1. Create a storage account with the following settings:

    - **Subscription**: Your Azure subscription
    - **Resource group**: Use the same resource group as your Foundry project - **AgenticAIEngineer**
    - **Storage account name**: A unique storage account name
    - **Region**: The same location as your Foundry project
    - **Primary service**: Azure Blob Storage or Azure Data Lake Storage
    - **Performance**: Standard
    - **Redundancy**: Locally-redundant storage (LRS)

1. Click Review + Create then Create again.
1. After the storage account is created, open it and select **Upload** from the top bar.
1. In the **Upload blob** pane, create a new container named `creditriskdocuments`.
1. Browse to the prepared credit-risk assessment files, select all four PDFs, and select **Upload**.
1. After the files are uploaded, navigate to the search service you created.
1. In the left pane, select **Security + networking** > **Keys**. For **API Access control**, select **Both** and confirm the selection.
1. Leave the Azure portal tab open. Return to the Foundry portal and refresh the page.
1. On the **Knowledge** page, select **Create a knowledge base**. Choose **Azure Blob Storage** as the knowledge source, then select **Connect**.
1. Configure the knowledge source with the following settings:

   * **Name**: `ks-creditriskdocuments`
   * **Description**: `Credit risk assessment documents`
   * **Storage account name**: Select your storage account
   * **Container name**: `creditriskdocuments`
   * **Authentication type**: API Key
   * **Content extraction mode**: minimal
   * **Embedding model**: Select your available deployed embedding model (text-embedding-3-small)
   * **Chat completions model**: Select your available deployed chat model (gpt-5.2)
   > **Note:** `gpt-5.4-mini` isn't available, so select `gpt-5.2` as the chat completions model.

1. Select **Create**.
1. On the knowledge base creation page, select your deployed chat model from the **Chat completions model** dropdown and leave the remaining settings unchanged.
1. Select **Save knowledge base**. Refresh the browser until the knowledge source status is **active**.
1. Select the back button to return to the **Knowledge** page, then select **Manage** next to the **Connection** dropdown.
1. Scroll to **Connected resources**, select your search service, and find the **Authentication** section.
1. Select **Key authentication**, then select **Edit authentication**.
1. Return to the Azure portal tab, which should still show the search service **Keys** page. Copy one key into the Foundry dialog, then select **Save**.

Your Foundry IQ knowledge base is now connected to the credit-risk assessment documents and ready for use by your agent.

## Configure the playground

1. Navigate back to your agent from the project home page. Select **View Deployments**, then select **Agents** from the side panel. Click the agent you created earlier, such as `credit-risk-assessment-agent`.

2. Under **Tools**, select **Knowledge**, click **Add**, and then select **Connect to Foundry IQ**.

3. In the **Connect to Foundry IQ** pop-up, configure the following:

   * **Connection**: `hakunamatata-srch-vtdm`
   * **Knowledge base**: `ks-creditriskdocuments`

   Then select **Connect**.

4. Click Save

## Test the agent in the playground

1. Test the agent with the following queries. Each query should ask the agent to retrieve the information from the **Foundry IQ knowledge source** connected to the agent:

   * `Using Foundry IQ, retrieve information from the connected knowledge source and tell me what documents are available for Apex Manufacturing Pvt Ltd. List each available document and include the company name and registration status mentioned in the documents.`

   * `Using Foundry IQ, retrieve the financial information for Apex Manufacturing Pvt Ltd for the financial year 2025 from the connected knowledge source. Include current assets, current liabilities, total debt, shareholders' equity, revenue, and net profit.`

   * `Using Foundry IQ, retrieve the external credit bureau information for Apex Manufacturing Pvt Ltd from the connected knowledge source. Tell me the external credit bureau score, industry, and credit bureau status, and mention whether any adverse records are reported.`


1. Review the responses. The agent should provide company-specific information, remain grounded in the available data, and may include citations or document references.
1. You can also use **Preview agent** for a more refined web application experience.
1. In the agent details page, copy the following information to a notepad. You'll use these values when configuring the client application:

    - **Agent name**: The name you created, such as `credit-risk-assessment-agent`
    - **Project endpoint**: Available from the project home page such as `https://hakunamatata11.services.ai.azure.com/api/projects/hakunamatata`

### Configure approval for tool calls

**Note: We have already updated the mentioned files with the code mentioned in the instructions, but we would highly suggest going through it before executing it**

By default, the Foundry IQ knowledge tool runs without asking for approval. To let your application review and control each knowledge-base lookup, configure the agent to require approval before it uses the tool.

> **Note**: The Foundry portal doesn't currently expose this approval setting. Configure it with the Foundry Toolkit for VS Code extension.

> **Note**: If the Foundry Toolkit extension is already installed and signed in from a previous lab, skip to step 3.

1. In Visual Studio Code, select **Extensions** from the left pane, or press **Ctrl+Shift+X**. Search for `Foundry Toolkit for VS Code` from Microsoft and select **Install** if it isn't already installed.

    > **Note**: The extension is currently listed as **Foundry Toolkit**, but some labels, commands, or older screenshots may still refer to **AI Toolkit**. In this lab, treat these names as the same extension experience.

    ![Screenshot of the Foundry Toolkit for VS Code extension in the Extensions Marketplace.](../../media/foundry-toolkit-extension.png)
   
1. Select the **Foundry Toolkit** icon in the sidebar and sign in to Azure if prompted.

    > **Note**: If you cannot sign in through Foundry Toolkit, select the Azure extension and sign in there. Then return to Foundry Toolkit to access your resources.

1. Under **Microsoft Foundry Resources**, choose **Set Default Project** and select the project used in this lab.
1. Expand the project. Under **Prompt Agents**, select `credit-risk-assessment-agent` to open **Agent Builder**.

    ![Screenshot of the Foundry Toolkit for VS Code extension in the Extensions Marketplace.](../../media/abc.png)
   
1. In the **Tools** section, add the **Azure AI Search** tool. Select the connection and knowledge base that you created earlier.

    > **Note**: The portal may add a **Web search** tool to new agents by default. Use the three dots on the **Azure AI Search** tool associated with your knowledge base, not another tool.

![Screenshot of the Foundry Toolkit for VS Code extension in the Extensions Marketplace.](../../media/zzz.png)

1. In **Require approval before using tools**, select **Ask for approval for all tools**. Save your changes if prompted.

Your agent now requests approval whenever it uses Foundry IQ. The Python client you complete next will prompt you to approve or deny each request.

# Connect to your agent from an app

Now that the agent and knowledge base work in the portal, use the provided Python application to communicate with the agent programmatically.

# Get the application files from GitHub

1. If you have already downloaded and extracted the repository in a previous lab, delete the existing ZIP file and the extracted folder. This will allow us to use the PowerShell commands in the following steps and help avoid long path issues.

2. Open a web browser and go to the [lab files on GitHub](https://github.com/Kiran-255666/AgenticAIEngineer).

3. On the repository page, select the green **`<> Code`** button, and then select **Download ZIP**.

4. Once the download finishes, extract the ZIP file.

5. Open ****PowerShell**** and run the following two commands to avoid long path issues:

```powershell
Copy-Item "C:\Users\agenticuser\Downloads\AgenticAIEngineer-main\AgenticAIEngineer-main\labfiles\Day05\lab05-integrate-agent-with-foundry-iq" "$env:USERPROFILE\Desktop\lab05-integrate-agent-with-foundry-iq" -Recurse

code "$env:USERPROFILE\Desktop\lab05-integrate-agent-with-foundry-iq" 
```

The first command copies the lab folder to your ****Desktop****, and the second command opens the copied folder directly in ****Visual Studio Code****.

This folder already contains the application files and the required code for this exercise.

6. You are now working from the ****Desktop**** folder, so there is no need to worry about the long path issue. Press ****Ctrl+Shift+`**** to open the integrated terminal.

7. In the terminal, enter the following commands to create and activate a virtual environment and install the required Python packages:

   ```
   python -m venv labenv
   .\labenv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

8. The ****.env**** file is already configured for you. You do not need to change any of the existing values.

### Review the agent client code

The required client code has already been added to **`agent_client.py`**. Review the file before running the application.

The client connects to the existing Foundry agent, creates a conversation, sends user messages, handles MCP approval requests for Foundry IQ lookups, and maintains conversation history.

### `send_message_to_agent`

The implementation is:

```python
def send_message_to_agent(user_message):
    """
    Send a message to the credit-risk agent and handle the response
    using the conversations API.
    """
    try:
        print("\nAgent: ", end="", flush=True)

        openai_client.conversations.items.create(
            conversation_id=conversation.id,
            items=[
                {
                    "type": "message",
                    "role": "user",
                    "content": user_message
                }
            ],
        )

        conversation_history.append({
            "role": "user",
            "content": user_message
        })

        response = openai_client.responses.create(
            conversation=conversation.id,
            extra_body={
                "agent_reference": {
                    "name": agent.name,
                    "type": "agent_reference"
                }
            },
            input=""
        )

        approval_request = None

        if hasattr(response, "output") and response.output:
            for item in response.output:
                if (
                    hasattr(item, "type")
                    and item.type == "mcp_approval_request"
                ):
                    approval_request = item
                    break

        if approval_request:
            print(
                f"[Approval required for: {approval_request.name}]\n"
            )
            print(f"Server: {approval_request.server_label}")

            approval_input = input(
                "Approve this action? (yes/no): "
            ).strip().lower()

            if approval_input in ["yes", "y"]:
                approval_response = {
                    "type": "mcp_approval_response",
                    "approval_request_id": approval_request.id,
                    "approve": True
                }
            else:
                approval_response = {
                    "type": "mcp_approval_response",
                    "approval_request_id": approval_request.id,
                    "approve": False
                }

            openai_client.conversations.items.create(
                conversation_id=conversation.id,
                items=[approval_response]
            )

            response = openai_client.responses.create(
                conversation=conversation.id,
                extra_body={
                    "agent_reference": {
                        "name": agent.name,
                        "type": "agent_reference"
                    }
                },
                input=""
            )

        if response and response.output_text:
            response_text = response.output_text
            print(f"{response_text}\n")

            conversation_history.append({
                "role": "assistant",
                "content": response_text
            })

            return response_text

        return None

    except Exception as e:
        print(f"\n\nError: {str(e)}\n")
        return None
````

This function sends the user's message to the Foundry agent and creates a response. If the agent needs to access the Foundry IQ knowledge source, it checks for an `mcp_approval_request` and asks the user to approve or deny the lookup. After the approval decision, it retrieves the agent's response and stores it in the conversation history.

### `display_conversation_history`

The implementation is:

```python
def display_conversation_history():
    """
    Display the full conversation history.
    """
    print("\n" + "=" * 60)
    print("CONVERSATION HISTORY")
    print("=" * 60 + "\n")

    for turn in conversation_history:
        role = turn["role"].upper()
        content = turn["content"]

        print(f"{role}: {content}\n")

    print("=" * 60 + "\n")
```

This function displays all user and agent messages stored in the current conversation history.

### `main`

The implementation is:

```python
def main():
    """
    Main interaction loop.
    """
    print("Credit Risk Assessment Agent")
    print("Ask questions about the credit-risk assessment.")
    print(
        "Type 'history' to see conversation history, "
        "or 'quit' to exit.\n"
    )

    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                continue

            if user_input.lower() == "quit":
                print("\nEnding conversation...")
                break

            if user_input.lower() == "history":
                display_conversation_history()
                continue

            send_message_to_agent(user_input)

        except KeyboardInterrupt:
            print("\n\nInterrupted by user.")
            break

        except Exception as e:
            print(f"\nUnexpected error: {str(e)}\n")

    print("\nConversation ended.")
```

The `main()` function provides the command-line interaction. It sends user questions to the agent, supports `history` for viewing the conversation, and uses `quit` to exit the application.

## Test the integration

1. In the integrated terminal, verify your Azure account:

   ```powershell
   az account show
   ```

   > **Note:** If you encounter an authentication issue, run `az logout`, then `az login`, and run `az account show` again.

2. Run the client:

   ```powershell
   python agent_client.py
   ```

3. Test the following queries. When prompted for approval, enter **`yes`** to allow the Foundry IQ knowledge-base lookup.

   **Available company documents**

   ```text
   What documents are available for Apex Manufacturing Pvt Ltd?
   ```

   **Financial information**

   ```text
   What financial information is available for Apex Manufacturing Pvt Ltd for 2025?
   ```

   **Financial ratio analysis**

   ```text
   What are the current ratio, debt-to-equity ratio, and net profit margin for Apex Manufacturing Pvt Ltd?
   ```

   **Credit bureau information**

   ```text
   What is the external credit bureau score and industry for Apex Manufacturing Pvt Ltd?
   ```

   **Credit-risk assessment rules**

   ```text
   What credit-risk assessment rules should be used for Apex Manufacturing Pvt Ltd?
   ```

4. Type `history` to view the complete conversation history.

5. Type `quit` when you are done testing.

### Expected output

The exact wording can vary because the responses are generated by the AI agent. After approving the Foundry IQ lookup, you should see responses similar to the following.

**Available company documents**

```text
The following documents are available for Apex Manufacturing Pvt Ltd:

- Company Registration Certificate
- GST Certificate

Company Name: Apex Manufacturing Pvt Ltd
Registration Status: Active

Both required documents are available and the company names match.
```

**Financial information**

```text
Financial information for Apex Manufacturing Pvt Ltd for 2025:

- Current Assets: 7,800,000
- Current Liabilities: 5,000,000
- Total Debt: 9,300,000
- Shareholders' Equity: 5,000,000
- Revenue: 9,000,000
- Net Profit: 500,000
```

**Financial ratio analysis**

```text
- Current Ratio = 1.56
- Debt-to-Equity Ratio = 1.86
- Net Profit Margin = 5.56%
```

**Credit bureau information**

```text
- External Credit Bureau Score: 720
- Industry: Manufacturing
- Credit Bureau Status: No adverse records reported
```

**Credit-risk assessment rules**

```text
The credit-risk assessment uses document verification,
compliance checks, financial ratio analysis, external credit
bureau information, and industry risk.

The scorecard includes:
- Compliance: 20
- Liquidity: 20
- Leverage: 15
- Profitability: 15
- External Credit Bureau: 15
- Industry Risk: 15
```

> **Note:** The exact response format and wording may differ. The important point is that the agent retrieves the relevant information from the connected Foundry IQ knowledge source and uses it to answer the questions.

### Review the results

Consider the following aspects of the agent's responses:

* **MCP approval flow**: The client requests approval before performing the Foundry IQ lookup.
* **Accuracy**: The agent retrieves information from the connected credit-risk assessment documents.
* **Citations**: The response may include source references when available.
* **Context awareness**: The same conversation is maintained across multiple questions.
* **Grounding**: The agent should indicate when relevant information is not available in the knowledge source.
* **Conversation history**: The `history` command displays the messages exchanged during the session.

## Summary

In this exercise, you:

* Connected a Python client to an existing Microsoft Foundry agent.
* Created and maintained a conversation using the Conversations API.
* Sent credit-risk assessment questions to the agent.
* Connected the agent to the Foundry IQ knowledge source.
* Implemented MCP approval handling so knowledge-base lookups require user approval.
* Retrieved company documents, financial information, financial ratios, credit bureau information, and credit-risk assessment rules from the connected knowledge source.
* Displayed available citations and maintained conversation history.
* Tested the complete approval-controlled knowledge retrieval workflow from a Python client application.