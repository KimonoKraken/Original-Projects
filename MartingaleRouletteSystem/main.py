"""
A martingale is a class of betting strategies that originated from and were popular in 18th-century France.
The simplest of these strategies was designed for a game in which the gambler wins the stake if a coin comes up
heads and loses if it comes up tails. The strategy had the gambler double the bet after every loss, so that the
first win would recover all previous losses plus win a profit equal to the original stake. Thus the strategy is
an instantiation of the St. Petersburg paradox.

In this program, num_times_won, (a player's successful attempt) is counted by each occurrence when player stops
playing and leaves the table with twice as much money as they started with.

trial_range constant can be adjusted to run this scenario as many times as you desire, to see what percentage of
the time you would leave the roulette table successful, while employing the martingale method.
"""

import random


# |-------------------------------- CONSTANTS --------------------------------| #
red = (1, 3, 5, 7, 9, 12, 14, 16, 18, 21, 23, 25, 27, 30, 32, 34, 36)
black = (2, 4, 6, 8, 10, 11, 13, 15, 17, 19, 20, 22, 24, 26, 28, 29, 31, 33, 35)

# amount of money player brings to the roulette table and starts with
cash_money = 500

# normal bet, this is to be doubled every time player loses a roulette spin
bet = 5

# this is the amount of times to simulate the player sitting down with a new bankroll and following the system
trial_range = 1000

# this is the number of times the player sat down with $500 and stopped playing after reaching $1000 ($500 in profit)
num_times_won = 0


# | -------------------------------- MARTINGALE ROULETTE SYSTEM FUNCTION -------------------------------- | #
def play_roulette():
    global bet, cash_money, num_times_won
    bet = 5
    cash_money = 500

    keep_playing = True

    while keep_playing:
        spin = random.randint(1, 38)

        if spin in black:
            cash_money = cash_money + bet
            bet = 5
            if cash_money >= 1000:
                keep_playing = False
                num_times_won += 1
            else:
                pass
        else:
            cash_money -= bet
            if cash_money <= 0:
                keep_playing = False
            else:
                if bet * 2 <= cash_money:
                    bet = bet * 2
                else:
                    bet = cash_money


for trial in range(trial_range):
    play_roulette()


percentage_successful = ((num_times_won / trial_range) * 100)


# | -------------------------------- PRINT RESULTS FOR USER --------------------------------- | #
print(f"Out of {trial_range} trials, you left the roulette table with profits {num_times_won} times.\n")
print(f"With the Martingale Method, you'd be successful about {percentage_successful}% of the time.")
