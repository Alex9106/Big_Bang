from random import randint

random_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

computer = random_list[randint(0, 4)]

player = False

while player == False:

    player = input("Rock, Paper, Scissors, Lizard, Spock?: ")
    if player == computer:
        print("Tie!")
    elif player == 'Scissors' and computer == 'Paper':
        print("You win", player, "cuts", computer)
    elif player == 'Scissors' and computer == 'Lizard':
        print("You win", player, "decapitates", computer)
    elif player == 'Paper' and computer == 'Rock':
        print("You win", player, "covers", computer)
    elif player == 'Paper' and computer == 'Spock':
        print("You win", player, "disproves", computer)
    elif player == 'Rock' and computer == 'Lizard':
        print("You win", player, "crushes", computer)
    elif player == 'Rock' and computer == 'Scissors':
        print("You win", player, "crushes", computer)
    elif player == 'Lizard' and computer == 'Spock':
        print("You win", player, "poisons", computer)
    elif player == 'Lizard' and computer == 'Paper':
        print("You win", player, "eats", computer)
    elif player == 'Spock' and computer == 'Scissors':
        print("You win", player, "smashes", computer)
    elif player == 'Spock' and computer == 'Rock':
        print("You win", player, "vaporizes", computer)
    elif computer == 'Scissors' and player == 'Paper':
        print("You lose", computer, "cuts", player)
    elif computer == 'Scissors' and player == 'Lizard':
        print("You lose", computer, "decapitates", player)
    elif computer == 'Paper' and player == 'Rock':
        print("You lose", computer, "covers", player)
    elif computer == 'Paper' and player == 'Spock':
        print("You lose", computer, "disproves", player)
    elif computer == 'Rock' and player == 'Lizard':
        print("You lose", computer, "crushes", player)
    elif computer == 'Rock' and player == 'Scissors':
        print("You lose", computer, "crushes", player)
    elif computer == 'Lizard' and player == 'Spock':
        print("You lose", computer, "poisons", player)
    elif computer == 'Lizard' and player == 'Paper':
        print("You lose", computer, "eats", player)
    elif computer == 'Spock' and player == 'Scissors':
        print("You lose", computer, "smashes", player)
    elif computer == 'Spock' and player == 'Rock':
        print("You lose", computer, "vaporizes", player)

    else:
        print("That's not a valid play. Check your spelling!")

    player = False
    computer = random_list[randint(0, 4)]
