# Lab 2: Work with entities

## Scenario

In this exercise, you will:

* Create and use entities

## What you will learn

* How to create and use entities to improve the agent

## High-level lab steps

* Create entities
* Use entities in nodes

## Prerequisites

* Must have completed previous exercise: Manage nodes

## Detailed steps

### Exercise 1 - Create entities

Microsoft Copilot Studio uses entities to understand user intent. There are many prebuilt entities included for commonly used information. You can create custom entities for your specific purpose.

#### Task 1.1 - View prebuilt entities

1. Navigate to the Microsoft Copilot Studio portal https://copilotstudio.microsoft.com and ensure you are in the appropriate environment.
2. Select Agents from the left navigation pane.
3. Select the Real Estate Booking Service agent you created in the earlier lab.
4. Select Settings in the upper-right of the screen.
5. Select the Entities tab. You should see a list of the prebuilt entities for your agent.

#### Task 1.2 - Create the property type entity

1. Select + Add an entity and select + New entity.
2. Select the Closed list tile.
3. Enter Property Type in the Name field.
4. Enter Apartment in the Enter item field and select Add.
5. Enter Condominium in the Enter item field and select Add.
6. Enter Duplex in the Enter item field and select Add.
7. Enter House in the Enter item field and select Add.
8. Select + Synonyms for Apartment, enter Flat and select the + icon and select Done.
9. Select + Synonyms for Condominium, enter Townhouse and select the + icon and select Done.
10. Select + Synonyms for House, enter Single-family home and select the + icon and select Done.
11. Enable Smart matching.
12. Select Save.
13. Once the entity is saved, close the Property Type window.

#### Task 1.3 - Create number of bedrooms entity

1. Select + Add an entity and select + New entity.
2. Select the Regular expression (Regex) tile.
3. Enter Number of Bedrooms in the Name field.
4. Enter [1-5] in the Pattern field.
5. Select Save.
6. Once the entity is saved, close the Number of Bedrooms pane.
7. Select the X icon in the top-right to close out of Settings and return to your agent.

### Exercise 2 - Use entities to improve the agent

Use entities in the conversational flow to improve the agent.

#### Task 2.1 - Use entities

1. Select the Topics tab.

2. Select the Book Showing topic.

3. Select the + icon between the Condition and property Question nodes, then select Ask a question.

4. In the Enter a message field, enter the following text:

   What type of property do you want to see?

5. Select Property Type for Identify.

6. Select Select options for user and check the Display option for all four values.

7. Select the variable in Save user response as and enter PropertyType for Variable name

8. Select the + icon below the new Question node and select Ask a question.

9. In the Enter a message field, enter the following text:

   How many bedrooms do you need?

10. Select Number of Bedrooms for Identify.

11. Click on Var1 under the Save user response as and enter NumberofBedrooms for Variable name

12. Select Save.

Congratulations, you have completed Lab2. Please close the current document and move to the next one.