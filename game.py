#Developed By Aman Gupta
import utils
# import the random module
import random

print("________________________________________________________")
print('Starting the Rock Paper Scissors game!')
player_name = input('Please enter your name: ')

print("________________________________________________________")

print('Pick a hand: (0: Rock, 1: Paper, 2: Scissors)')
player_hand = int(input('Please enter a number (0-2): '))

print("________________________________________________________")
if utils.validate(player_hand):
    # Assign a random number between 0 and 2 to computer_hand using randint
    computer_hand = random.randint(0,2)
    
    utils.print_hand(player_hand, player_name)
    utils.print_hand(computer_hand, 'Computer')
    
    print("________________________________________________________")
    
    result = utils.judge(player_hand, computer_hand)
    print('Result: You ' + result)
    print("________________________________________________________")
else:
    print('Please enter a valid number')
    print("________________________________________________________")

print("Developed By Aman Gupta")
