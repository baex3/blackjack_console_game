############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import os
from time import sleep
import random

cards = {
  "Ace": [11, 1],
  "One": 1,
  "Two": 2,
  "Three": 3,
  "Four": 4,
  "Five": 5,
  "Six": 6,
  "Seven": 7,
  "Eight": 8,
  "Nine": 9,
  "Ten": 10,
  "Jack": 10,
  "Queen": 10,
  "King": 10
}
##Variable declaration
cards_key_list = list(cards)
my_starting_hand = 2
dealers_starting_hand = 1
card_count = 0
my_hand = []
dealers_hand = []

def blackjack():
  card_count = 0
  my_hand.clear()
  dealers_hand.clear()
  play = ""
  while play not in ["y", "n"]: play = input("Do you want to play a game of Blackjack? Type 'y' or 'n'\n"); continue

  if play == 'n':
    ui = ['.']
    for _ in range(7):
      print(''.join(ui))
      sleep(0.5)
      os.system('cls' if os.name=='nt' else 'clear')
      ui += '.' 
    print(logo)
    print("...Exiting blackjack game interface...")
    exit()
  else:
    os.system('cls' if os.name=='nt' else 'clear')
    print(logo)

  #Get my first hand
  while card_count < my_starting_hand:
    get_hand(hand=my_hand)
    card_count = len(my_hand)

  my_score = sum(my_hand)

  print(f"Your cards: {my_hand}, current score : {my_score}")
  card_count = 0
  #Get Dealer's first hand
  while card_count < dealers_starting_hand:
    get_hand(dealers_hand)
    card_count = len(dealers_hand)

  dealers_score = sum(dealers_hand)
  print(f"Dealer's cards: {dealers_hand}, current score : {dealers_score}")
  # Check for an initial blackjack first
  if my_score == 21:
    show_final_hand(my_hand, dealers_hand, my_score, dealers_score)
    print("You Win with a Blackjack 😎")
  #Determine if the player wants to deal a card until they say no
  y_or_no = draw_or_pass()
  while y_or_no == "y":
    get_hand(my_hand)
    my_score = sum(my_hand)
    print(f"Your cards: {my_hand}, current score : {my_score}")
    print(f"Dealer's cards: {dealers_hand}, current score : {dealers_score}")
    if my_score == 21:
        print("You Win with a Blackjack 😎")
        blackjack()
    if my_score > 21:
      show_final_hand(my_hand, dealers_hand, my_score, dealers_score)
      print("You went over. You lose 😤 ")
      blackjack()
    else:
      y_or_no = draw_or_pass()
  #Once the player says no, determine the final hands, scores, and the winner
  if y_or_no == "n":
    dealers_score = show_final_hand(my_hand, dealers_hand, my_score, dealers_score)
    if my_score == dealers_score:
        print("The game has ended in a Draw!")
        blackjack()
    elif my_score > dealers_score or dealers_score > 21:
        print("You win! 😃")
        blackjack()
    else:
        print("You Lose! ")
        blackjack()

def show_final_hand(player_hand, computer_hand, player_score, computer_score):
    '''Calculate the dealer's last hand, print final and return the dealer's score'''
    #if the dealer's hand is less than 17, they have to draw until it is greater
    while computer_score < 17:
      get_hand(computer_hand)
      computer_score = sum(computer_hand)
    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Dealer's final hand: {computer_hand}, final score: {computer_score}\n")
    return computer_score

def get_card():
  '''Pull a random card from the deck'''
  random_card = random.choice(cards_key_list)
  return random_card

def get_hand(hand):
  '''Add card to player or dealer's hand'''
  card = get_card()
  #An ace is worth 1 or 11, in favor of the one who draws it
  if card == "Ace" and sum(hand) + cards["Ace"][0] < 21:
    my_hand.append(cards["Ace"][0])
  elif card == "Ace" and sum(hand) + cards["Ace"][0] > 21:
    hand.append(cards["Ace"][1])
  else:
    hand.append(cards[card])

def draw_or_pass():
  continuation = ""
  #Verify if the player wants to get another card or pass
  while continuation not in ["y", "n"]: continuation = input("Type 'y' to get another card, type 'n' to pass\n"); continue
  return continuation

blackjack()





