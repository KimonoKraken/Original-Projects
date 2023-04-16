This program monitors the House Stock Watcher API, which monitors the purchase and sale of stocks from U.S. Congress Officials. When there is a new transaction, the program will text a phone number or list of phone numbers an update in the following format:

"Rep {representative name} {type_of_transaction} {amount of transaction} of {stock ticker} {stock sector} on {transaction date}"

This program runs on an infinite loop and checks the API for new transactions every 1 minute.
