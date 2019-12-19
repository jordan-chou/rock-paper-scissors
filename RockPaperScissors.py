#   Jordan Chou
#   Dec. 18, 2019
#   Play Rock, Paper, Scissors

from random import randint

def compRandomPlay():
    play = randint(1, 3)
    if play == 1:
        return "Rock"
    elif play == 2:
        return "Paper"
    else:
        return "Scissors"

print("\nRock Paper Scissors!")
print("Best out of 5")

userScore, compScore = 0, 0
rounds = 0

# Ask user for "rock", "paper", or "scissors"
while userScore < 3 and compScore < 3:
    rounds += 1
    print("\nRound " + str(rounds))
    print("You: " + str(userScore) + "\tComputer: " + str(compScore))
    while True:
        userInput = input("Rock, Paper, or Scissors? ").lower()
        if userInput == "rock" or userInput == "paper" or userInput == "scissors":
            break
        else:
            print("Invalid input. Please try again")

    userInput = userInput.capitalize()   # Capitalize user input
    compPlay = compRandomPlay()             # Generate random play for computer

    if userInput == compPlay:
        print("\n\tComputer plays " + compPlay)
        print("\tTie!")
    elif (userInput[0] == "R" and compPlay[0] == "S") or (userInput[0] == "P" and userInput[0] == "R") or (userInput[0] == "S" and compPlay[0] == "P"):
        print("\n\tComputer plays " + compPlay)
        print("\tYou win!")
        userScore += 1
    else:
        print("\n\tComputer plays " + compPlay)
        print("\tYou lose.")
        compScore += 1

print("\nFinal Score")
print("-----------")
print("You: " + str(userScore) + "\tComputer: " + str(compScore))
print("You played " + str(rounds) + " rounds")
if userScore >= 3:
    print("\nYou win!")
else:
    print("\nYou lose.")
