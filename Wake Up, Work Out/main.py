import smtplib
import datetime as dt
import random
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError


# |------------------------------------GETTING EMAILS FROM MAILCHIMP API------------------------------------|#

# This is where subscribed members' emails will be saved to
emails = []

# Gets member info from MailChimp
try:
  client = MailchimpMarketing.Client()
  client.set_config({
    "api_key": "ENTER_API_KEY_HERE",
    "server": "ENTER_YOUR_SERVER_HERE"})

    # If members are currently subscribed, adds them to "emails" list
  response = client.lists.get_list_members_info("ENTER_YOUR_LIST_ID_HERE")
  for member in response['members']:
    if member['status'] == "subscribed":
      emails.append(member['email_address'])


except ApiClientError as error:
   print("Error: {}".format(error.text))


# |------------------------------------LOG IN FOR GMAIL------------------------------------|#

my_email = "ENTER_YOUR_GMAIL_HERE"
password = "ENTER_YOUR_GMAIL_APP_KEY_HERE"
unsub_link_url = "tinyurl.com/unsub321"


# |------------------------------------DATE FORMATTED FOR EMAIL TO BE SENT------------------------------------|#

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
weekday = now.weekday() # 0 = monday, 1 = tuesday, etc
today = f"{month}/{day}/{year}"


# |------------------------------------WORKOUTS------------------------------------|#
upper_body_beg = (
    "Push-Ups: 2 sets of 20",
    "Chin-Ups: 2 sets of 5",
    "Wall Handstand: 2 sets of 30 seconds",
    "Wide-Grip Push-Ups: 2 sets of 20",
    "Close-Grip Push-Ups: 2 sets of 20",
)

upper_body_int = (
    "Feet Elevated Push-Ups: 2 sets of 20",
    "Pull-Ups: 2 sets of 10",
    "Feet Elevated Pike Push-Ups: 2 sets of 15",
    "Chin-Ups: 2 sets of 10",
    "Wall Handstand: 2 sets of 60 seconds",
    "Diamond Push-Ups: 2 sets of 15",

)

upper_body_adv = (
    "Feet Elevated Push-Ups: 3 sets of 25",
    "Archer Push-Ups: 3 sets of 12 (6 per side)",
    "Archer Pull-Ups: 3 sets of 6 (3 per side)",
    "One-Arm Push-Ups: 3 sets of 12 (6 per side)",
    "Diamond Push-Ups: 3 sets of 20",
    "Handstand Push-Ups: 3 sets of 10",
)

lower_body_beg = (
    "Squats: 2 sets of 20",
    "Lunges: 2 sets of 10 (each side)",
    "Hip Bridge: 2 sets of 20",
    "Lying Knee Tuck: 2 sets of 20",
    "Wall Sits: 2 sets of 60 seconds",
)

lower_body_int = (
    "Jump Squats: 2 sets of 20",
    "Lunges: 2 sets of 20 (each side)",
    "Jump Lunges: 2 sets of 12 (each side)",
    "Close-Feet Squats: 2 sets of 20",
    "Wall Sits: 2 sets of 2 minutes",
)

lower_body_adv = (
    "Pistol Squats: 3 sets of 10 (each side)",
    "Jump Squats: 3 sets of 15",
    "Jumping Lunges: 3 sets of 15 (each side)",
    "Shrimp Squat: 3 sets of 10 (each side)",
)


core = (
    "Plank: 2 sets of 2 minutes",
    "Side Plank: 2 minutes (each side)",
    "Bicycle Crunches: 2 sets of 30 (each side)",
    "V-Ups: 2 sets of 30 reps",
    "Crunches: 2 sets of 30 reps",
    "Sit-Ups: 2 sets of 30 reps",
    "Russian Twists: 2 sets of 30 (each side)",
    "Scissor Kicks: 2 sets of 30 (each side)",
    "Leg Raises: 2 sets of 15",

)


# |------------------------------------FUNCTION TO GENERATE UNIQUE WORKOUT------------------------------------|#

def generate_workout():
    upper_body_beg_choice = random.choice(upper_body_beg)
    upper_body_int_choice = random.choice(upper_body_int)
    upper_body_adv_choice = random.choice(upper_body_adv)

    lower_body_beg_choice = random.choice(lower_body_beg)
    lower_body_int_choice = random.choice(lower_body_int)
    lower_body_adv_choice = random.choice(lower_body_adv)

    core_choice = random.choice(core)
    core_choice_2 = random.choice(core)

    return f"Beginner Workout: \n\n{upper_body_beg_choice} \n{lower_body_beg_choice} \n{core_choice}\n\n\n" \
           f"-------------------------------------------------------------------------------\n\n\n" \
           f"Intermediate Workout: \n\n{upper_body_int_choice} \n{lower_body_int_choice} \n{core_choice}\n\n\n" \
           f"-------------------------------------------------------------------------------\n\n\n" \
           f"Advanced Workout: \n\n{upper_body_adv_choice} \n{lower_body_adv_choice} \n{core_choice} \n{core_choice_2}\n\n\n" \
           f"-------------------------------------------------------------------------------\n\n\n" \
           f"How to Use: If you're unable to complete the sets and reps required, " \
           f"feel free to split the reps up and complete more sets to finish all the reps. " \
           f"Once you're able to easily complete all sets and reps as written, move on to the next difficulty level.\n\n\n\n\n\n" \


# |---------------------------------EMAILING THE EMAIL-LIST THE GENERATED WORKOUT---------------------------------|#


with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=emails,
                        msg=f"Subject:Wake Up, Workout! {today} \n\n{generate_workout()} \n\n To unsubscribe, click here: {unsub_link_url}"
                        )

