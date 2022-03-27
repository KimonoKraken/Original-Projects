logo = """
  ,88~-_        e    e           e      888~-_   
 d888   \      d8b  d8b         d8b     888   \  
88888    |    d888bdY88b       /Y88b    888    | 
88888    |   / Y88Y Y888b     /  Y88b   888    | 
 Y888   /   /   YY   Y888b   /____Y88b  888   /  
  `88_-~   /          Y888b /      Y88b 888_-~   
"""

# Protein dictionary and their associated calories per oz
proteins = {
    "Beef Ribeye": 83,
    "NY Strip Steak": 33,
    "Chicken Thighs": 50,
    "Ground Lamb": 80,
    "Ground Beef": 94,
    "Beef Chuck": 78,
    "Pork Ribs": 100,
    "Flap Steak": 40,
    "Chicken Drumsticks": 34,
    "Ground Bison": 63,
    "Pork Shoulder": 76,
    "Pork Tenderloin": 41,

}

# Fruit dictionary and their associated calories per cup
fruits = {
    "Apples": 57,
    "Blueberries": 80,
    "Bananas": 200,
    "Raspberries": 15,
    "Strawberries": 9,
    "Mango": 17,
    "Blackberries": 12,
    "Avocados": 234,
    "Oranges": 85,
    "Kiwis": 110,
    "Dates": 414,
    "Dragonfruit": 136,
    "Pears": 92,
    "Apricots": 79,
    "Plums": 76,

}

import random
import os


def clearconsole():
    """Clears the console as you play the game"""
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


print(logo)
print("Welcome to the Animal-Based One Meal a Day (OMAD)\nWeight Loss Calculator and Meal Generator!\n\n")

# Collecting user inputs
sex = input("Are you male or female?\n").lower()
age = int(input("\nHow old are you?\n"))
height = int(input("\nHow tall are you in inches?\nEx. For 5'11\", type 71.\n"))
current_weight = int(input("\nWhat is your current weight (lbs)?\n"))
goal_weight = int(input("\nWhat is your goal weight (lbs)?\n"))
timeline = int(input("\nHow many weeks do you have to reach your goal weight?\n"))
activity_level = int(input(
    "\nOn a scale of 1 to 5: 1 being little or no exercise, and 5 being intense daily exercise, how active are you?\n"))

# Calculating how many pounds user wants to lose or gain
if current_weight > goal_weight:
    difference_in_weights = current_weight - goal_weight
else:
    difference_in_weights = goal_weight - current_weight

# Base metabolic rate calculation for men
bmr_men = (10 * (current_weight / 2.2)) + (6.25 * (height * 2.54)) - (5 * age) + 5
# BMR adjusted for women
if sex == "female":
    bmr_men -= 166

# Calculating user's Base Metabolic Rate (BMR)
if activity_level == 1:
    bmr_men *= 1.2
if activity_level == 2:
    bmr_men *= 1.37
if activity_level == 3:
    bmr_men *= 1.54
if activity_level == 4:
    bmr_men *= 1.71
if activity_level == 5:
    bmr_men *= 1.9
bmr_men = round(bmr_men)

# Calculating goal BMR, or goal daily calorie intake
if current_weight > goal_weight:
    goal_bmr = round(bmr_men - ((difference_in_weights * 3500) / (timeline * 7)))
if current_weight < goal_weight:
    goal_bmr = round(bmr_men + ((difference_in_weights * 3500) / (timeline * 7)))

regenerate_suggested_meal = True

while regenerate_suggested_meal == True:
    # Choosing random meat
    recommended_meat = random.choice(list(proteins))

    # Choosing random fruit
    recommended_fruit = random.choice(list(fruits))

    # Calculating how many oz of the selected meat is needed in the meal
    meat_in_lbs = (((goal_bmr * 0.95) / proteins[recommended_meat]) / 16)
    amount_of_meat_lbs = (round(meat_in_lbs, 1))

    # Calculating how many cups of the selected fruit is needed in the meal
    amount_of_fruit_cups = round((goal_bmr * 0.05) / fruits[recommended_fruit])
    while amount_of_fruit_cups == 0:
        recommended_fruit = random.choice(list(fruits))
        amount_of_fruit_cups = round((goal_bmr * 0.05) / fruits[recommended_fruit])

    clearconsole()
    if amount_of_meat_lbs == 1 and amount_of_fruit_cups > 1:
        print(
            f"\nYou could eat {amount_of_meat_lbs} lb of {recommended_meat} and {amount_of_fruit_cups} cups of {recommended_fruit} every day to reach your goal weight of {goal_weight} in {timeline} weeks.")
    elif amount_of_meat_lbs > 1 and amount_of_fruit_cups == 1:
        print(
            f"\nYou could eat {amount_of_meat_lbs} lbs of {recommended_meat} and {amount_of_fruit_cups} cup of {recommended_fruit} every day to reach your goal weight of {goal_weight} in {timeline} weeks.")
    else:
        print(
            f"\nYou could eat {amount_of_meat_lbs} lbs of {recommended_meat} and {amount_of_fruit_cups} cups of {recommended_fruit} every day to reach your goal weight of {goal_weight} in {timeline} weeks.")

    regenerate = input("\nDo you want to generate a new meal? Type 'y' or 'n' and press enter: ")

    if regenerate == "n":
        regenerate_suggested_meal = False

