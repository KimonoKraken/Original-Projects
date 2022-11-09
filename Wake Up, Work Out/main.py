import smtplib
import datetime as dt
import random


my_email = "itswakeupworkout@gmail.com"
password = "vjnvtosbdqtytydh"

receiver_email = "dkmiamib@gmail.com"

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
weekday = now.weekday() # 0 = monday, 1 = tuesday, etc
today = f"{month}/{day}/{year}"


upper_body_beg = (
    "Push-Ups: 2 sets of 20",
    "Chin-Ups: 2 sets of 5",
    "Wall Handstand: 2 sets of 30 seconds",
)

upper_body_int = (
    "Feet Elevated Push-Ups: 2 sets of 20",
    "Pull-Ups: 2 sets of 10",
    "Feet Elevated Pike Push-Ups: 2 sets of 15",
    "Chin-Ups: 2 sets of 10",
    "Wall Handstand: 2 sets of 60 seconds",

)

upper_body_adv = (
    "Feet Elevated Push-Ups: 2 sets of 25",
    "Archer Push-Ups: 3 sets of 12 (6 per side)",
    "Archer Pull-Ups: 3 sets of 6 (3 per side)",
    "One-Arm Push-Ups: 3 sets of 12 (6 per side)",
    "Diamond Push-Ups: 3 sets of 20",
    "Handstand Push-Ups: 2 sets of 8",
)

lower_body_beg = (
    "Squats: 2 sets of 20",
    "Lunges: 2 sets of 10 (each side)",
    "Hip Bridge: 2 sets of 20",
    "Lying Knee Tuck: 2 sets of 20",
)

lower_body_int = (
    "Jump Squats: 2 sets of 20",
    "Lunges: 2 sets of 20 (each side)",
    "Jump Lunges: 2 sets of 12 (each side)",
)

lower_body_adv = (
    "Pistol Squats: 3 sets of 10 (each side)",
    "Jump Squats: 3 sets of 15",
)


core = (
    "Plank: 2 minutes",
    "Bicycle Crunches: 30 each side",
    "V-Ups: 30 reps",
    "Crunches: 30 reps",
    "Sit-Ups: 30 reps",
    "Russian Twists: 30 each side",
    "Scissor Kicks: 30 each side",

)


def generate_workout():
    upper_body_beg_choice = random.choice(upper_body_beg)
    upper_body_int_choice = random.choice(upper_body_int)
    upper_body_adv_choice = random.choice(upper_body_adv)

    lower_body_beg_choice = random.choice(lower_body_beg)
    lower_body_int_choice = random.choice(lower_body_int)
    lower_body_adv_choice = random.choice(lower_body_adv)

    core_choice = random.choice(core)

    return f"Beginner Workout:\n\n{upper_body_beg_choice} \n{lower_body_beg_choice} \n{core_choice}\n\n\n" \
           f"Intermediate Workout: \n\n{upper_body_int_choice} \n{lower_body_int_choice} \n{core_choice}\n\n\n" \
           f"Advanced Workout: \n\n{upper_body_adv_choice} \n{lower_body_adv_choice} \n{core_choice}\n\n\n" \
           f"How to Use: If you're unable to complete the sets and reps required, " \
           f"feel free to split the reps up and complete more sets to finish all the reps. " \
           f"Once you're able to easily complete all sets and reps as written, move on to the next difficulty level."


with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        # to_addrs=birthday_person["email"],
                        to_addrs=receiver_email,
                        msg=f"Subject:Wake Up, Workout! {today} \n\n{generate_workout()}"
                        )

