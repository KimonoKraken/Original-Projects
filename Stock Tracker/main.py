import requests
import json
import time
from datetime import datetime, timedelta
from twilio.rest import Client

API_URL = "https://house-stock-watcher-data.s3-us-west-2.amazonaws.com/data/all_transactions.json"
TWILIO_ACCOUNT_SID = "ENTER YOUR ACCOUNT SID HERE"
TWILIO_AUTH_TOKEN = "ENTER YOUR AUTH TOKEN HERE"
TWILIO_FROM_NUMBER = "+1----------"
YOUR_PHONE_NUMBER = "+1----------"


client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

response = requests.get(API_URL)
data = json.loads(response.text)

last_transaction_date_str = ""  # store the date of the last transaction sent via SMS

while True:
    response = requests.get(API_URL)
    new_data = json.loads(response.text)
    new_transactions = [t for t in new_data if t["transaction_date"] > last_transaction_date_str]
    for transaction in new_transactions:
        transaction_date_str = transaction["transaction_date"]
        try:
            transaction_date = datetime.strptime(transaction_date_str, "%Y-%m-%d")
            # format transaction date to SMS-friendly version
            formatted_date_str = datetime.strftime(transaction_date, "%-m/%-d/%Y")
        except ValueError:
            continue
        if datetime.today() - transaction_date <= timedelta(days=20):
            ticker = transaction["ticker"]
            if ticker == "--":
                continue
            representative = transaction["representative"]
            if transaction["sector"] is None:
                sector = ""
            else:
                sector = " (" + transaction["sector"] + " sector" + ")"
            amount = transaction["amount"]
            if transaction["type"] == "purchase":
                type_of_transaction = "bought"
            elif transaction["type"] == "sale_full" or transaction["type"] == "sale_partial":
                type_of_transaction = "sold"
            else:
                type_of_transaction = "bought/sold"

            message = f"Rep {representative} {type_of_transaction} {amount} of {ticker}{sector} " \
                      f"on {formatted_date_str}"
            client.messages.create(to=YOUR_PHONE_NUMBER, from_=TWILIO_FROM_NUMBER, body=message)
        last_transaction_date_str = transaction_date_str
    time.sleep(60)  # waits for 1 minute before checking for new transactions again
