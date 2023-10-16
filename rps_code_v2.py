# This file was created by: Gregory Gutierrez

# Will pick a random integer that is assigned to a value on list
from random import randint

# List of all options 
rps_choice = ["rock", "paper", "scissors"]

# Player gets to choose what they wish to throw in the game.
player = input("do you choose rock or paper or scissors")

# Computer will pick randomly from the list
CPU = rps_choice[randint(0,2)]

# Feedback on what the player chose
if CPU == "rock":
    print("The computer chose rock...")
if CPU == "paper":
    print("The computer chose paper...")
if CPU == "scissors":
    print("The computer chose scissors...")



    if player == "rock":
        print("The player chose rock...")
    if player == "paper":
        print("The player chose paper...")
    if player == "scissors":
        print("The player chose scissors...")
    else:
        print("Invalid choice")
    


# Outome of what happens depending on what computer and player pick
if player == "rock" and CPU == "scissors":
    print("The player wins")
if player == "rock" and CPU == "rock":
    print("It is a tie")
if player == "rock" and CPU == "paper":
    print("The computer wins")
if player == "scissors" and CPU == "rock":
    print("The Computer wins")
if player == "paper" and CPU == "rock":
    print("The Player wins")
if player == "paper" and CPU == "scissors":
    print("The Computer wins")
if player == "paper" and CPU == "paper":
    print("It is a tie")
if player == "scissors" and CPU == "scissors":
    print("It is a tie")
if player == "scissors" and CPU == "paper":
    print("The Player wins")