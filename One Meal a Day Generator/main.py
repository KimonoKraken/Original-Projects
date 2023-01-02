from tkinter import *
import random
import os

BACKGROUND_COLOR = "#B1DDC6"


# ----------------------------  Foods  ------------------------------- #


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

# Non-sweet fruit dictionary and their associated calories per cup
non_sweet_fruits = {
    "Sweet Potato": 114,
    "Cucumber": 16,
    "Squash": 63,
    "Zucchini": 19,
    "Avocados": 234,
    "Olives": 160,
    "Pumpkin": 30,

}


# Fruit dictionary and their associated calories per cup
fruits = {
    "Apples": 57,
    "Blueberries": 80,
    "Bananas": 200,
    "Raspberries": 15,
    "Strawberries": 9,
    "Mango": 17,
    "Melon": 60,
    "Blackberries": 12,
    "Oranges": 85,
    "Kiwis": 110,
    "Dates": 414,
    "Dragonfruit": 136,
    "Pears": 92,
    "Apricots": 79,
    "Plums": 76,

}


# ----------------------------  MEAL GENERATION  ------------------------------- #


def radio_used():
    print(radio_state.get())


def submitted():
    is_correct = True
    if is_correct:
        sex = radio_state.get()
        if sex == 1:
            sex = "male"
        else:
            sex = "female"
        age_value = float(spinbox_age.get())
        height_value = float(spinbox_height.get())
        current_weight_value = float(spinbox1_weight.get())
        goal_weight_value = float(spinbox2_weight.get())
        weeks_to_goal = float(spinbox_weeks.get())
        activity_level = spinbox_activity.get()

        if current_weight_value > goal_weight_value:
            difference_in_weight = current_weight_value - goal_weight_value
        elif current_weight_value < goal_weight_value:
            difference_in_weight = goal_weight_value - current_weight_value
        else:
            difference_in_weight = 0

        # calculating bmr
        bmr_men = (10 * (current_weight_value / 2.2)) + (6.25 * (height_value * 2.54)) - (5 * age_value) + 5
        if sex == "female":
            bmr_men -= 166
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
        goal_bmr = 0
        if current_weight_value > goal_weight_value:
            goal_bmr = round(bmr_men - ((difference_in_weight * 3500) / (weeks_to_goal * 7)))
        if current_weight_value < goal_weight_value:
            goal_bmr = round(bmr_men + ((difference_in_weight * 3500) / (weeks_to_goal * 7)))
        if current_weight_value == goal_weight_value:
            goal_bmr = bmr_men


        regenerate_suggested_meal = True

        while regenerate_suggested_meal:
            # Choosing random meat
            recommended_meat = random.choice(list(proteins))

            # Choosing random non-sweet fruit
            recommended_non_sweet_fruit = random.choice(list(non_sweet_fruits))

            # Choosing random fruit
            recommended_fruit = random.choice(list(fruits))

            # Calculating how many oz of the selected meat is needed in the meal
            meat_in_lbs = round((((goal_bmr * 0.92) / proteins[recommended_meat]) / 16), 1)
            amount_of_meat_lbs = (round(meat_in_lbs, 1))

            # Calculating how many cups of the selected non-sweet fruit is needed in the meal
            amount_of_non_sweet_fruit_cups = round((goal_bmr * 0.05) / non_sweet_fruits[recommended_non_sweet_fruit])
            while amount_of_non_sweet_fruit_cups == 0:
                recommended_non_sweet_fruit = random.choice(list(non_sweet_fruits))
                amount_of_non_sweet_fruit_cups = round((goal_bmr * 0.05) / non_sweet_fruits[recommended_non_sweet_fruit])

            # Calculating how many cups of the selected fruit is needed in the meal
            amount_of_fruit_cups = round((goal_bmr * 0.03) / fruits[recommended_fruit])
            while amount_of_fruit_cups == 0:
                recommended_fruit = random.choice(list(fruits))
                amount_of_fruit_cups = round((goal_bmr * 0.05) / fruits[recommended_fruit])

            regenerate_suggested_meal = False
            canvas.itemconfig(meal_generated_label, text="You could eat:")
            canvas.itemconfig(meal_generated_label_5, text=f"Everyday to reach your goal \n     weight in {weeks_to_goal} weeks.")
            if meat_in_lbs == 1:
                canvas.itemconfig(meal_generated_label_2, text=f"{meat_in_lbs}lb of {recommended_meat}", fill="darkred")
            else:
                canvas.itemconfig(meal_generated_label_2, text=f"{meat_in_lbs}lbs of {recommended_meat}", fill="darkred")
            if amount_of_non_sweet_fruit_cups == 1:
                canvas.itemconfig(meal_generated_label_3, text=f"{amount_of_non_sweet_fruit_cups} cup of "
                                                               f"{recommended_non_sweet_fruit}", fill="darkred")
            else:
                canvas.itemconfig(meal_generated_label_3, text=f"{amount_of_non_sweet_fruit_cups} cups of "
                                                               f"{recommended_non_sweet_fruit}", fill="darkred")
            if amount_of_fruit_cups == 1:
                canvas.itemconfig(meal_generated_label_4, text=f"{amount_of_fruit_cups} cup of "
                                                               f"{recommended_fruit}", fill="darkred")
            else:
                canvas.itemconfig(meal_generated_label_4, text=f"{amount_of_fruit_cups} cups of "
                                                               f"{recommended_fruit}", fill="darkred")

    else:
        pass


# ---------------------------- UI SETUP ------------------------------- #


# window
window = Tk()
window.title("Animal-Based One-Meal-a-Day (OMAD)")
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=50)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
current_path = os.path.dirname(__file__)                #New variable to finding new path for resources, no difference where you move a programm.
background_img = PhotoImage(file=os.path.join(current_path, "card_front.png"))         #Now path to file its - new path from os. + file_name.
card_background = canvas.create_image(400, 263, image=background_img)             
logo_img = PhotoImage(file=os.path.join(current_path,"omad.PNG"))                       #Now path to file its - new path from os. + file_name.
logo = canvas.create_image(395, 95, image=logo_img)
calc_img = PhotoImage(file=os.path.join(current_path,"calc2.png"))                      #Now path to file its - new path from os. + file_name.
calc = canvas.create_image(555, 315, image=calc_img)
canvas.grid(row=0, column=0, columnspan=1)

# Labels
intro_label = canvas.create_text(395, 195, text="Welcome to the Animal-Based One Meal a Day (OMAD)"
                                                "\n        Weight Loss Calculator and Meal Generator!", font=("arial", 12, "normal"))

# "You could eat" label
meal_generated_label = canvas.create_text(555, 257, text="", font=("arial", 8, "bold"))
# Recommended meat label
meal_generated_label_2 = canvas.create_text(555, 270, text="", font=("arial", 10, "bold"))
# Recommended non sweet fruit label
meal_generated_label_3 = canvas.create_text(555, 285, text="", font=("arial", 10, "bold"))
# Recommended sweet fruit label
meal_generated_label_4 = canvas.create_text(555, 300, text="", font=("arial", 10, "bold"))
# "to reach your goal" label
meal_generated_label_5 = canvas.create_text(555, 320, text="", font=("arial", 7, "bold"))

# Male or female
male_female = canvas.create_text(200, 235, text="Are you male or female?", fill="darkgreen", font=("arial", 12, "normal"))
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Male", value=1, variable=radio_state, bg="white", command=radio_used)
radiobutton2 = Radiobutton(text="Female", value=2, variable=radio_state, bg="white", command=radio_used)
radiobutton1.place(x=290, y=225)
radiobutton2.place(x=340, y=225)

# Age
age = canvas.create_text(175, 265, text="How old are you?", fill="darkgreen", font=("arial", 12, "normal"))
spinbox_age = Spinbox(from_=18, to=100, width=5)
spinbox_age.place(x=250, y=257)

# Height
height = canvas.create_text(206, 295, text="How tall are you in inches?", fill="darkgreen", font=("arial", 12, "normal"))
spinbox_height = Spinbox(from_=55, to=84, width=5)
spinbox_height.place(x=310, y=290)
height2 = canvas.create_text(200, 310, text="Ex. For 5'11\", select 71.", fill="darkgreen", font=("arial", 8, "normal"))

# Current weight
current_weight = canvas.create_text(225, 335, text="What's your current weight (lbs)?", fill="darkgreen", font=("arial", 12, "normal"))
spinbox1_weight = Spinbox(from_=100, to=600, width=5)
spinbox1_weight.place(x=350, y=325)
spinbox_value = spinbox1_weight.get()

# Goal weight
goal_weight = canvas.create_text(217, 365, text="What's your goal weight (lbs)?", fill="darkgreen", font=("arial", 12, "normal"))
spinbox2_weight = Spinbox(from_=100, to=600, width=5)
spinbox2_weight.place(x=350, y=357)

# Weeks to goal
weeks = canvas.create_text(232, 398, text="How many weeks to hit your goal?", fill="darkgreen", font=("arial", 12, "normal"))
spinbox_weeks = Spinbox(from_=8, to=52, width=5)
spinbox_weeks.place(x=355, y=389)

# Activity Level
activity = canvas.create_text(253, 435, text="On a scale of 1 to 5, how active are you?", fill="darkgreen", font=("arial", 12, "normal"))
activity = canvas.create_text(250, 450, text="1= not active, 5= very active", fill="darkgreen", font=("arial", 8, "normal"))

spinbox_activity = Spinbox(from_=1, to=5, width=5)
spinbox_activity.place(x=420, y=430)

# Submit Button
submit_button = Button(text="Generate a Meal", command=submitted, width=40)
submit_button.place(x=250, y=468)


window.mainloop()
