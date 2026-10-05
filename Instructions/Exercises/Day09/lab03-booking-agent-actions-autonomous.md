# Lab 3: Incorporate flows and actions and enable autonomous capabilities

## Create agent flows

### Scenario

In this exercise, you will:

* Create an agent flow

### What you will learn

* How to create a tool for running an agent flow in Copilot Studio

### High-level lab steps

* Create an agent flow to retrieve Dataverse data
* Create an agent flow to create Dataverse data

### Prerequisites

* Must have completed Previous exercise: Work with entities

### Detailed steps

## Exercise 1 - Create a tool to retrieve data from Dataverse

Microsoft Copilot Studio can access data in Microsoft Dataverse using agent flows.

### Task 1.1 - Create agent flow to retrieve a property

1. Navigate to the Microsoft Copilot Studio portal https://copilotstudio.microsoft.com and ensure you are in the appropriate environment.
2. Select Agents from the left navigation pane.
3. Select the Real Estate Booking Service you created in the earlier lab.
4. Select the Tools tab.
5. Select + Add a tool.
6. Select Agent flow.
7. Select the trigger step When an agent calls the flow and select + Add an input.
8. Select Text.
9. Enter Bedrooms for Input and Number of Bedrooms for Please enter your input.
10. Select Save draft near the upper-right of the page.
11. Select the + icon between the two steps in the flow to add a new action.
12. Enter Dataverse in the Search field and select See more for the Microsoft Dataverse connector.
13. Select the List rows action.
14. If prompted for authentication, enter Lab connection for Connection name, select OAuth for Authentication Type, and select Sign in, and use your tenant credentials and Allow access.

> Note: If you see a 'Failed to create OAuth connection' error, you may need to allow popups in your browser.

15. Select Real Estate Properties for table name.
16. Enter contoso_bedrooms eq  (with a space after eq) in the Filter Rows field.
17. With the Filter Rows field still selected, select the lightning icon to its right, then select the Bedrooms parameter.

> Important: Ensure there is a space between eq and Bedrooms.

18. Select Save draft near the upper-right of the page.
19. Select the Respond to Copilot action in the authoring canvas and select + Add an output.
20. Select Text.
21. Enter PropertyId for Enter a name
22. Select the Enter a value to respond with field, and select fx (Insert Expression).
23. Enter the following expression into the top field:

```text
first(outputs('List_rows')?['body/value'])['contoso_realestatepropertyid']
```

24. Select Add.
25. Select + Add an output.
26. Select Text.
27. Enter PropertyName for Enter a name.
28. Select the Enter a value to respond with field, and select fx (Insert Expression).
29. Enter the following expression:

```text
first(outputs('List_rows')?['body/value'])['contoso_propertyname']
```

30. Select Add.
31. Click on the ellipse… icon and select More. Select the Settings tab in the Respond to Copilot pane.
32. Ensure that Asynchronous Response is set to Off.
33. Select Save draft near the upper-right of the page.
34. Wait for the save to complete, then select Publish.
35. In the Your agent flow published successfully! pop-up, select Go back to agent.
36. Select the agent flow tool that you just created from the left pane
37. In the Details section click on Edit, update the Flow Name to Get Property
38. Update the Description to Get properties with the right number of bedrooms.
39. Select Save
40. Select the Tools tab and see the Get Property flow you created.

### Task 1.2 - Add the Get Property tool to the topic

1. Click on Agents from the left pane, click on the Real estate booking agent.
2. Select the Topics tab.
3. Select the Book Showing topic.
4. Select the + icon below the How many bedrooms do you need question? node, select Add a tool, select the Tool tab, and then select the Get Property agent flow. Select Numberofbedrooms for Bedrooms
5. Select the ellipses (...) in the Which property do you want to see? question node and select Delete.
6. Select the + icon under the Action node and select Send a message.
7. In the Enter a message field, enter Property  (with a space following it).
8. In the same node, select the {X} (Insert variable) icon and select the PropertyName variable.
9. Select Save.

## Exercise 2 - Create a tool to create data in Dataverse

Microsoft Copilot Studio can create data in Microsoft Dataverse using agent flows.

### Task 2.1 - Create agent flow to make a booking

1. Select the Tools tab in Real Estate Booking Service.
2. Select + Add a tool.
3. Select Agent flow.
4. Select Save draft and wait for the agent flow to save.
5. Select the Overview tab
6. Select Edit in the Details section.
7. Rename the flow Create Booking Request
8. Select Save.
9. Select the Designer tab.
10. Select the trigger step When an agent calls the flow and select + Add an input.
11. Select Text.
12. Enter PropertyId for Input and Property for Please enter your input.
13. Select + Add an input.
14. Select Text.
15. Enter ViewerName for Input and Viewer Name for Please enter your input.
16. Select + Add an input.
17. Select Text.
18. Enter ViewerEmail for Input and Viewer Email for Please enter your input.
19. Select the + icon between the two steps in the flow to add a new action.
20. Enter Dataverse in the Search field and select See more for the Microsoft Dataverse connector.
21. Select the Add a new row action.
22. Select Booking Requests for table name.
23. Enter Agent booking in the Booking Name field.
24. Select Show all under Advanced parameters.
25. Enter contoso_bookingrequests() in the Property (Real Estate Properties) field, move the cursor within the parentheses, select the lightning icon, then select the PropertyId parameter.
26. Select the Viewer Email field, select the lightning icon, then select the ViewerEmail parameter.
27. Select the Viewer Name field, select the lightning icon, then select the ViewerName parameter.
28. Select the Respond to Copilot action.
29. Click on ellipse… icon. Click on More -> select the Settings tab.
30. Ensure that Asynchronous Response is set to Off.
31. Select Save draft in the upper-right of the window.
32. Wait for the save to complete, then select Publish.

### Task 2.2 - Validate your tools

1. Select Agents and open your Real Estate Booking Service agent.
2. Select the Tools tab and validate that both of your agent flows are in the list. If not, select +Add a tool > Flow > and select the missing agent flow. Select Add and configure.

### Task 2.3 - Add the Create Booking Request tool to the topic

1. Select the Topics tab.
2. Select the Book Showing topic.
3. Select the + icon below the Message node at the bottom, select Add a tool, then select the Create Booking Request flow.
4. Select the PropertyId variable for the PropertyId input parameter.
5. Select the Name variable for the ViewerName input parameter.
6. Select the EmailAddress variable for the ViewerEmail input parameter.
7. Select the + icon below the new Action node, select Topic management, select Go to another topic and select End of Conversation.
8. Select Save.

## Exercise 3 - Test your agent

### Task 3.1 - Make a booking request

1. If closed, select the Test icon in the upper-right of the page to open the testing panel.
2. Select the ellipses ... menu at the top of the testing panel in the upper-right of the page.
3. If it's not enabled, enable Track between topics.
4. Select the Start new test session icon at the top of the testing panel.
5. When the Conversation Start message appears, your agent will start a conversation. In response, enter a trigger phrase for the topic that you've created:

```text
I want to book a real estate showing
```

6. Enter a name and email address.
7. After you supply the information, an Adaptive Card displays the information that you entered and asks if the details are correct. Select Yes.
8. Select House for the type of property prompt.
9. Enter 3 for the number of bedrooms prompts.
10. Enter Tomorrow 2:00 PM to the What date and time do you want to see the property? prompt.
11. Select Yes to the Did that answer your question? prompt.
12. Select any rating.
13. Enter No to the Can I help with anything else? prompt.

### Task 3.2 - Verify the booking request

1. If it's not still open, navigate to https://make.powerapps.com in a new tab.
2. Make sure you are in the appropriate environment.
3. Select Apps in the left navigation.
4. Select Play on the Real Estate Property Management model-driven app.
5. In the left navigation, select Booking Requests. View the booking request your agent just created for you.

Congratulations, you have completed Lab3. Please close the current document and move to the next one.