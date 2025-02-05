import random
'''
Scissors cuts Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
(and as it always has) Rock crushes Scissors

Write a Python program where a human player plays against the computer. The computer’s
move should be randomized. Play the game for 5 rounds keeping score, and then output
who the winner is (Player or Computer) for the best of 5.
'''

print("best out of 5")
playerchoice = input("rock, paper, scissors, lizard, or spock?: ")
def choicecheck():
    global playerchoice
    invalid = True
    while invalid == True: # check to make sure that user gives correct input
        if playerchoice == "rock":
            playerchoice = "rock"
            invalid = False
        elif playerchoice == "paper":
            playerchoice = "paper"
            invalid = False
        elif playerchoice == "scissors":
            playerchoice = "scissors"
            invalid = False
        elif playerchoice == "lizard":
            playerchoice = "lizard"
            invalid = False
        elif playerchoice == "spock":
            playerchoice = "spock"
            invalid = False
        else:
            print("invalid choice(check spelling?)")
            invalid = True
            playerchoice = input("rock, paper, scissors, lizard, or spock?: ")

computerchoice = random.randint(1, 5)

# tells the player what the computer picked
def computerchoiceis():
    if computerchoice == 1: 
        print("computer: rock")
    elif computerchoice == 2:
        print("computer: paper")
    elif computerchoice == 3:
        print("computer: scissors")
    elif computerchoice == 4:
        print("computer: lizard")
    elif computerchoice == 5:
        print("computer: spock")
computerchoiceis()

playerscore = 0
computerscore = 0

def playerwin():
    global playerscore
    global playerchoice
    global computerchoice
    print("player wins!")
    playerscore = playerscore + 1
    print("player: " + str(playerscore) + " computer: " + str(computerscore))
    computerchoice = random.randint(1, 5)
    playerchoice = input("rock, paper, scissors, lizard, or spock?: ")
    choicecheck()
    computerchoiceis()
    
def computerwin():
    global computerscore
    global playerchoice
    global computerchoice
    print("computer wins!")
    computerscore = computerscore + 1
    print("player: " + str(playerscore) + " computer: " + str(computerscore))
    computerchoice = random.randint(1, 5)
    playerchoice = input("rock, paper, scissors, lizard, or spock?: ")
    choicecheck()
    computerchoiceis()
    
    
    

while computerscore < 5 and playerscore < 5:
    if playerchoice == "rock" and computerchoice == 1:
        print("its a draw, play again.")
        print("player: " + str(playerscore) + " computer: " + str(computerscore))
        computerchoice = random.randint(1, 5)
        playerchoice = input("rock, paper, scissors, lizard, or spock?: ")
        choicecheck()
        computerchoiceis()
    elif playerchoice == "paper" and computerchoice == 2:
        print("its a draw, play again.")
        print("player: " + str(playerscore) + " computer: " + str(computerscore))
        computerchoice = random.randint(1, 5)
        playerchoice = input("rock, paper, scissors, lizard, or spock?: ")
        choicecheck()
        computerchoiceis()
    elif playerchoice == "scissors" and computerchoice == 3:
        print("its a draw, play again.")
        print("player: " + str(playerscore) + " computer: " + str(computerscore))
        computerchoice = random.randint(1, 5)
        playerchoice = input("rock, paper, scissors, lizard, or spock?: ")
        choicecheck()
        computerchoiceis()
    elif playerchoice == "lizard" and computerchoice == 4:
        print("its a draw, play again.")
        print("player: " + str(playerscore) + " computer: " + str(computerscore))
        computerchoice = random.randint(1, 5)
        playerchoice = input("rock, paper, scissors, lizard, or spock?: ")
        choicecheck()
        computerchoiceis()
    elif playerchoice == "spock" and computerchoice == 5:
        print("its a draw, play again.")
        print("player: " + str(playerscore) + " computer: " + str(computerscore))
        computerchoice = random.randint(1, 5)
        playerchoice = input("rock, paper, scissors, lizard, or spock?: ")
        choicecheck()
        computerchoiceis()
    elif playerchoice == "rock" and computerchoice == 2:
        computerwin()
    elif playerchoice == "paper" and computerchoice == 1:
        playerwin()
    elif playerchoice == "scissors" and computerchoice == 1:
        computerwin()
    elif playerchoice == "lizard" and computerchoice == 1:
        computerwin()
    elif playerchoice == "spock" and computerchoice == 1:
        playerwin()
    elif playerchoice == "rock" and computerchoice == 3:
        playerwin()
    elif playerchoice == "scissors" and computerchoice == 2:
        playerwin()
    elif playerchoice == "lizard" and computerchoice == 2:
        playerwin()
    elif playerchoice == "spock" and computerchoice == 2:
        computerwin()
    elif playerchoice == "rock" and computerchoice == 4:
        playerwin()
    elif playerchoice == "paper" and computerchoice == 3:
        computerwin()
    elif playerchoice == "lizard" and computerchoice == 3:
        computerwin()
    elif playerchoice == "spock" and computerchoice == 3:
        playerwin()
    elif playerchoice == "rock" and computerchoice == 5:
        computerwin()
    elif playerchoice == "paper" and computerchoice == 4:
        computerwin()
    elif playerchoice == "scissors" and computerchoice == 4:
        playerwin()
    elif playerchoice == "spock" and computerchoice == 4:
        computerwin()
    elif playerchoice == "paper" and computerchoice == 5:
        playerwin()
    elif playerchoice == "scissors" and computerchoice == 5:
        computerwin()
    elif playerchoice == "lizard" and computerchoice == 5:
        playerwin()

if playerscore == 5:
    print("player wins the game!")
elif computerscore == 5:
    print("computer wins the game!")