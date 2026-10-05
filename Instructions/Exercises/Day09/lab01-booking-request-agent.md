# Lab1: Building a Booking Request Agent with Copilot Studio 

## Create a Power Platform environment

### Power Platform Admin Center

Before you start the lab exercises, you must create a development environment for you to work in.

1. Open a web browser and navigate to the **Power Platform admin center** https://admin.powerplatform.microsoft.com/manage/environments. If you are already signed in with your **@hackable.in** account, ensure you sign out first, then sign in with the new **@justlabs.online** account provided for this lab.
1. If prompted, choose the option to stay signed in.
1. Close any pop-up messages that are displayed.

### Create a new environment

1. In the sidebar, select **Manage**.
1. In the **Environments** page, select **+ New**.
   ![Environment page's select new.](../../media/ClickNew.png)
1. In the **New environment** panel, set **Type** to Trial and **Region** to the default region shown (a local region provides quicker data access).
   ![Environment page's Type and Region.](../../media/TypeRegion.png)
1. Enter your name in the **Name** field.
   ![Environment page's set Your Name.](../../media/YourName.png)
1. Expand **Change default settings**. You'll see **Add a Dataverse data store?** and **Pay-as-you-go with Azure?**. Toggle **Add a Dataverse data store?** to **Yes**.
   ![Environment page's select new.](../../media/ToggleYes.png)
   > [!NOTE]
   > Pay-as-you-go with Azure is unavailable for Trial environments — only Production and Sandbox environments support this setting.

1. Select **Next**. In the **Add Dataverse** panel, set the following:
   - **Language**: leave as it is if already English (United States), otherwise select English (United States) and move to the next field
   - **Currency**: leave as default
   - **Security group**: Click **+ Select** and in **Edit security group** find **open access** click **None** and Click **Done**
   ![Environment Done Button.](../../media/done.png)
   - **URL**: leave as default
   - **Enable Dynamics 365 apps?**: leave as it is (locked to No), move to the next field
   - **Deploy sample apps and data?**: No

   > [!NOTE]
   > Currency defaults based on your region (for example, INR for India). Enable Dynamics 365 apps is disabled for Trial environments — it's only available for Production or Sandbox environments.
   
   ![Environment Save Button.](../../media/Save.png)

1. Select **Save** and wait until the environment state is **Ready** (use **Refresh** to update the display).

   > [!NOTE]
   > Environment provisioning can take several minutes depending on tenant configuration.

   ![Environment created in the Power Platform Admin center.](../../media/environment-created.png)

### Access Copilot Studio

1. In a new browser tab, open **Copilot Studio** https://copilotstudio.microsoft.com/ and sign in if prompted.

   ![Copilot Studio interface.](../../media/olduserxp.png)

   <details>
   <summary>Does your interface look different? Click here</summary>
   
   ![Copilot Studio interface.](../../media/newuserxp.png)

   Select **...** (More options) at the bottom of the page. Under **Explore**, select **Open Classic Experience**. These labs use the **Classic Experience**.
   
   </details>

2. Look at the **upper-right corner** of the page. Just to the left of the **Settings** ⚙️ icon, you will see the **Environment Selector** showing your current environment.

   ![Environment.](../../media/u1.png)

3. Check the **Environment Selector**. If your *named environment* is already displayed, use it.

   <details>
   <summary>Can't see your named environment? Click here</summary>

   a. Select the **Environment Selector**.

   ![Environment Selector.](../../media/u1.png)

   b. The **Switch environment** menu will open.

   ![Environment Selector.](../../media/u2.png)

   c. Under **Supported environments**, select your **named environment**.

   ![Environment Selector.](../../media/u3.png)

   d. Your **named environment** should now be shown in the **Environment Selector**.

   ![Environment Selector.](../../media/u4.png)

   </details>

## Import Dataverse solution 

In this exercise, you'll import a Dataverse solution to use in the following exercises 

### Exercise 1 – Import solution 

In this exercise, you will import a Dataverse solution into your environment that contains 
the tables needed for the labs. 

#### Task 1.1 – Download solution 

1. Open the following link to download the **Bookings_1_0_0_0.zip** file: https://vectorsenselabs.blob.core.windows.net/isodata/Accelerate-Agentic_AI/Bookings_1_0_0_0?sp=r&st=2026-02-16T20:07:28Z&se=2027-03-03T04:22:28Z&spr=https&sv=2024-11-04&sr=b&sig=81FJ9Yp9L9xQqzHSXUSpz70FCTX%2BKDjL1MQpV3sls3A%3D

#### Task 1.2 – Import solution

1. In a new browser tab, navigate to https://make.powerapps.com.

2. If prompted, sign in using your **@justlabs.online** credentials.

3. Ensure **India** is selected as the country/region, then select **Get Started**.

4. In the upper-right corner, verify that your recently created environment is selected.

   <details>
   <summary>Need to switch environments? Click here</summary>

   Select the **Environment** dropdown. Under **Build apps with Dataverse**, select your recently created environment.

   </details>

5. In the left navigation, select Solutions. 
6. In the top bar, select Import solution. 
7. Select Browse and locate the Bookings_1_0_0_0.zip file from your Downloads folder and select Open. 
8. Select Next. 
9. Select Import. 

The solution will import in the background. This may take a 2-3 minutes. You may refresh the window. 

> **TIP** Wait until the solution has finished importing before continuing to the next step. 

10. When the solution has imported successfully, open the Bookings solution. 

   ![Environment Selector.](../../media/Bookings.png)

11. In the left navigation, select the **Overview** tab.

   ![Environment Selector.](../../media/PublishApp.png)

12. Select **Publish all customizations** and wait for the process to complete. This may take approximately **2–3 minutes**.

13. You could verify it by a green notification appears at the top confirming **Publish all customizations succeeded**.

#### Task 1.3 – Set preferred solution 

1. Select **← Back to Solutions** in the left pane.

2. On the **Current preferred solution** card, select **Manage**.

   ![Environment Selector.](../../media/SolManage.png)

3. For **Set your preferred solution** Select Bookings (contoso). 

   ![Environment Selector.](../../media/preferredsolutionbooking.png)

4. Select Apply.

#### Task 1.4 – Test data 

1. Click on Bookings

   ![Environment Selector.](../../media/ClickBookingsAgain.png)

2. In the left navigation of the Bookings solution, select the Objects tab. 

3. Select the **ellipses …** menu for the **Real Estate Property Management** Model-Driven App, and select **Play**. This is a simple model-driven app that will allow you to create new Real Estate Property records.

   ![Environment Selector.](../../media/ModelDrivenAppPlay.png)

4. Select + New. 

   ![Environment Selector.](../../media/NewNewNew.png)

4. Enter the following data: 

   a. **Property Name:** 1100 High Villas 

   b. **Owner:** Ensure it is set to **Copilot User X**, where **X** is your assigned number.

   c. **Asking Price:** 250,000 

   d. **Street:** Main Avenue 

   e. **City:** Redmond 

   f. **Bedrooms:** 3 

   g. **Bathrooms:** 2 

5. Select Save & Close. 

6. Select + New. 

7. Enter the following data: 

   a. **Property Name:** 555 Oak Lane 

   b. **Owner:** Ensure it is set to **Copilot User X**, where **X** is your assigned number.

   c. **Asking Price:** 300,000 

   d. **Street:** Oak Lane 

   e. **City:** Denver 

   f. **Bedrooms:** 4 

   g. **Bathrooms:** 3 

8. Select Save & Close. 

> **Note:** Now you have 2 Active Real Estate Properties in the view. 

## Build an initial agent 

### Scenario 

In this exercise, you will: 

• Create and name an agent 

• Add description for what the agent should do 

• Configure Generative AI answers 

### What you will learn 

• How to create an agent using natural language 

• How to configure Generative AI answers for an agent 

### High-level lab steps 

• Create a new agent 

• Tell your agent what its primary purpose is and how it should act 

• Add Generative AI instructions 

### Prerequisites 

• Must have completed above **Exercise: Import Dataverse solution**

### Exercise 1 - Create agent 

In this exercise, you will access the Microsoft Copilot Studio portal, the Developer environment and create a new agent. 

#### Create an agent

1. Open **Copilot Studio** https://copilotstudio.microsoft.com/ and make sure you are using the **Classic Experience**.

2. Under "Start building from scratch", select Agent.

   ![Environment Selector.](../../media/OneAgent.png)

3. In the Name your agent dialog, enter **`Real Estate Booking Service`**

   ![Environment Selector.](../../media/TwoAgent.png)

4. Expand **Agent Settings** and verify the **Solution** is set to **Bookings**.

5. Leave the automatically generated **Schema name** as it is.

6. Select Create.

7. Wait for the agent to be provisioned to edit the following things.

8. Once the agent provisions, update the following details:

   **Name:** `Real Estate Booking Service`

   **Description:** `Create bookings for real estate properties`

9. Click Save.

10. In the Instructions section, enter: **`Create an agent for topics relating to creating bookings for real estate properties`**

11. Click Save.

12. In the **Test your agent** pane on the right, enter **`How do I make a booking?`** and press **Enter**.

   ![Environment Selector.](../../media/ThreeAgent.png)

13. Review the response and leave this window open for now.

### Exercise 2 - Add Generative AI answers 

In this exercise, you will access the Microsoft Copilot Studio portal and add knowledge that the agent will use to answer questions by using Generative AI. 

#### Task 2.1 - Disable generative orchestration 

1. Select Settings. 

2. For Use generative AI orchestration for your agent's responses? Select **`No - Use  classic orchestration, limiting responses to the content and behavior defined in your agent's topics`**. This turns Orchestration off for the purpose of this lab. 

3. Select Save. 

4. Wait for the changes to save, then select **X** at the top to close the **Settings** window.

#### Task 2.2 – Add a knowledge source 

1. Select the Knowledge tab. 

2. Select **+ Add knowledge**.

3. Select **Public websites** 

4. In the Public website link text box, enter **`https://word.cloud.microsoft/`** . 

5. Select **Add** .

6. Select **Add to agent**. 

7. Select the Overview tab. 

8. Select the **ellipses ... *** menu at the top of the **Test your agent** pane. 

9. Enable Track between topics. 

10. At the top of the **Test your agent pane**, select the **Start new test session** by clicking **+* symbol.

11. In the Ask a question or describe what you need text box, enter **`How do I boost real estate promotion?`** 

12. View your agent response. 

   ![Environment Selector.](../../media/FiveAgent.png)

13. Select **Publish** at the top of the page.

14. Enable **Force newest version**, then select **Publish** again.

15. Wait until the publishing process completes successfully before continuing.

## Manage topics 

### Scenario 

In this exercise, you will: 

• Manage existing topics 

• Create and edit topics by using natural language 

• Create a topic manually by using trigger phrases 

### What you will learn 

• How to configure agent topics 

### High-level lab steps 

• Disable topics 

• Create new and edit topics with natural language 

• Create a new topic and add trigger phrases 

### Prerequisites 

• Must have completed above **Exercise: Build an initial agent** 

### Detailed steps 

#### Exercise 1 - Remove topics 

In this exercise, you will remove topics in an agent. 

##### Task 1.1 – Disable topics 

1. Navigate to the Microsoft Copilot Studio portal https://copilotstudio.microsoft.com and ensure you are in classic experince UI and in the appropriate environment.

2. Select Agents from the left navigation pane. 

3. Select the **Real Estate Booking Service** agent you created earlier. 

   ![Environment Selector.](../../media/EarlierAgent.png)

4. Select the **Topics** tab. 

5. Toggle Enabled to Off for the Start Over topic. 

   ![Environment Selector.](../../media/OffStartOverOff.png)

#### Exercise 2 - Create topics with natural language 

In this exercise, you will create topics in an agent and add trigger phrases. 

##### Task 2.1 – Add a topic using copilot 

1. Select **+ Add a topic** and select **Add from description with Copilot**. A new window appears.
 
2. In the **Name your topic** text box, enter **`Customer Details`**. 

3. In the **Create a topic to...** text box, enter **`Ask the customer for their name and email address`**.

4. Select **Create**. 

5. Select **Save**. 

##### Task 2.2 – Update nodes with natural language 

1. If the Test your agent pane is open, close the pane. 

2. If the Edit with Copilot pane is not shown on the right side of the Customer Details pane, select the Copilot icon in the upper part of the authoring canvas. 

   ![Environment Selector.](../../media/CopilotIcon.png)

3. Select the second Question node What is your email address? 

4. In the Edit with Copilot panel, in the What do you want to do? field, enter the following text: 

Change "What is your email address?" to say thank you to the Name variable from the previous node and then proceed to ask the email address question. 

5. Select Update. 

**Note:** The message should be updated to include the Name variable from the prior node, and should look similar to the screenshot above. If Edit with copilot did not update the question node correctly, select Undo, and retry with a different prompt. 

6. Select Save. 

##### Task 2.3 – Add nodes with natural language 

In addition to adding updating existing nodes, you can use Copilot to add new ones. 

1. Make sure that no node is selected by selecting the empty space in the authoring 
canvas. 
2. In the Edit with Copilot panel, in the What do you want to do? field, enter the following text: 

Summarize the information collected in an adaptive card 

3. Select Update. 
4. A message node with an Adaptive Card is added to the end of the topic. 
5. Make sure that no node is selected by selecting the empty space in the authoring 
canvas. 
6. In the What do you want to do? field, enter the following text: 

Add a new multiple choice question to prompt the user if the details are correct with two options Yes or No 

7. Select Update. 
8. A new question node is added to the end of the topic with options for the user to 
select. 
9. Select Save. 

##### Task 2.4 - Test the topic 

1. If the Test your agent panel is closed, select the Test icon in the upper-right of the 
page. 
2. Select the Start new test session icon at the top of the testing panel. 
3. In the Ask a question or describe what you need text box, enter Customer 
information. 
4. Enter your name and email address. 
5. Select Yes. 
6. Select Save 

#### Exercise 3 - Author topics manually 

Topics can be created manually by adding trigger phrases. 

##### Task 3.1 - Create a topic from blank 

1. Select the Topics tab in the top bar of Real Estate Booking Service. 
2. Select + Add a topic and select From blank. 
3. Select the Details icon to open the Topic details dialog (you may need to select More 
> Details). 
4. In the Name field, enter the following text: 

Book Showing 

5. In the Display Name field, enter the following text: 

Book a Real Estate Showing 

6. In the Description field, enter the following text: 

Select the property and requested date and create a booking request 

7. Select Save. 

##### Task 3.2 - Add trigger phrases 

1. Select Edit under User says a phrase in the Trigger. 
2. Enter I want to book a real estate showing under Add phrases and select the + icon. 
3. Enter Schedule a real estate showing under Add phrases and select the + icon. 
4. Enter Arrange the viewing for a real estate property under Add phrases and select the + icon. 
5. Enter Set up an appointment to view a house under Add phrases and select the + icon. 
6. Enter Plan a property viewing under Add phrases and select the + icon. 
7. Select Save. 

## Manage nodes 

### Scenario 

In this exercise, you will: 

• Author the conversational flow 
• Manage variables 

### What you will learn 

• How to add nodes to a topic to author the conversational flow 

### High-level lab steps 

• Configure variable scope 
• Create and edit nodes 
• Test the agent and configure authentication 

### Prerequisites 

• Must have completed above exercise: Manage topics 

### Detailed steps 

#### Exercise 1 - Variable scope 

Enable variables to be be accessed by other topics. 

##### Task 1.1 - Configure the scope of the variables 

1. Navigate to the Copilot Studio portal https://copilotstudio.microsoft.com and ensure you 
are in the appropriate environment. 
2. Select Agents from the left navigation pane. 
3. Select the Real Estate Booking Service agent you created in the earlier lab. 
4. Select the Topics tab. 
5. Select the Customer Details topic. 
6. Select Variables in the top bar to open the Variables pane (you may need to select 
More > Variables). 
7. Select and expand Topic variables. 
8. Select the right-hand check boxes for the three topic variables. 
9. Select Save. 

#### Exercise 2 - Author topics manually 

The conversational flow in a topic can be created manually by adding nodes. 

##### Task 2.1 - Add a message node 

1. Select the Topics tab. 
2. Select the Book Showing topic. 
3. Select the + icon under the Trigger node and select Send a message. 
4. In the Enter a message field, enter the following text: 

Hi, I can help you with booking a real estate property showing. 

5. Select Save. 

##### Task 2.2 - Add a Topic management node 

1. Select the + icon under the Message node, then select Topic management > Go to 
another topic > Customer Details. 
2. Select Save. 

##### Task 2.3 - Add condition node 

1. Select the + icon under the Topic node and select Add a condition. 
2. In the Condition node, select the DetailsCorrect variable. 
3. Select is equal to. 
4. Select Yes. 
5. Select Save. 

##### Task 2.4 - Add question nodes 

1. Select the + icon under the left Condition node and select Ask a question. 
2. In the Enter a message field, enter the following text: 

Which property do you want to see? 

3. Select User's entire response for Identify. 
4. Click on Var1 in the Save user response as and enter PropertyName for Variable 
name. 
5. Select Save. 
6. Select the + icon under the new Question node and select Ask a question. 
7. In the Enter a message field, enter the following text: 

What date and time do you want to see the property? 

8. Select Date and time for Identify. 
9. Click on Var1 under the Save user response as and enter VisitDateTime for Variable 
name 
10. Select the + icon under the left Question node and select Send a messsage. 
11. In the Enter a message field, enter the following text: 

Great! Let me get that scheduled for you. 

12. Select Save. 

##### Task 2.5 - Test the agent 

1. If the Test your agent panel is not open, select the Test icon in the upper-right of the 
page to open the testing panel. 
2. Select the ellipses ... menu at the top of the testing panel in the upper-right of the 
page. 
3. If it's not enabled, enable Track between topics. 
4. Select the Start new test session icon at the top of the testing panel. 
5. When the Conversation Start message appears, your agent will start a conversation. 
In response, enter a trigger phrase for the topic that you've created: 

I want to book a real estate showing 

6. The agent responds with the "What is your name?" question, as shown in the 
following image. 
7. Enter your name. 
8. Enter your email address. 
9. After you supply the information, an Adaptive Card displays the information that you 
entered and asks if the details are correct. Select Yes. 
10. Enter 555 Oak Lane, Denver, CO 80203 to the Which property to you want to see? 
prompt 
11. Enter Tomorrow 10:00 AM to the What date and time do you want to see the 
property? prompt. 

#### Exercise 3 - Configure authentication 

##### Task 3.1 - Configure authentication 

1. Select Settings in the upper-right of Real Estate Booking Service. 
2. Select the Security tab. 
3. Select Authentication. 
4. Select No authentication. 
5. Select Save. 
6. Select Save in the confirmation window. 
7. Select the X in the upper-right to close out of the Settings. 

Congratulations, you have completed Lab1. Please close the current document and move to 
the next one.