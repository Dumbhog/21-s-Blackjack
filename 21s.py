from random import randint

card_base = randint(1, 13)
is_playing = 0 # This is the variable that determines if the game is being played or not

def play():  # Defines the starting of a new round
    global is_playing
    begin_input = input("Would you like to begin a round? (y) ")
    if begin_input != "y":
        print("Goodbye")
        is_playing = False
    else:
        is_playing = True
        print("Let's play!")
        game_loop()
    
def recieve_card():
    card_base = randint(1, 13)
    if 2 <= card_base <= 10:
        return card_base
    elif card_base == 1:
        return 1  # Assuming Ace is 11
    else:
        return 10  # For J, Q, K

def game_loop():  # This is the main game loop
    global is_playing
    cards_value = 0  # Defining the value of all cards added outside the loop
    while is_playing:

        draw_input = input("Press Enter to draw a card, press (e) to stand " )  # This is the input for drawing a card
        if draw_input == "":  # If the user presses Enter
            card_value = (recieve_card())  # Calling the function to determine the value of the card (The  function is defined later)
            cards_value += card_value
            if 2 <= card_value <= 10:
                print(f"Your card is a {card_value}. Total value: {cards_value}")
            elif card_value == 1:
                print(f"Your card is an Ace. Total value: {cards_value}")
            elif card_value == 11:
                print(f"Your card is a King. Total value: {cards_value}")
            elif card_value == 12: 
                print(f"Your card is a Queen. Total value: {cards_value}")
            elif card_value == 13:
                print(f"Your card is a Jack. Total value: {cards_value}")

            draw_input = 0

            if cards_value > 21:
                print("You're Bust! The value of your cards is over 21.")
                is_playing = False


        elif draw_input == "e":  # If the player types E
            print(f"Your final value is {cards_value}") # Prints the final value of the cards
            dealer_cards = 0
            while dealer_cards < 17:
                dealer_card_value = (recieve_card())
                dealer_cards += dealer_card_value
                print(f"The dealer's card value is {dealer_card_value}. Total value: {dealer_cards}")
            print(f"The dealer's final value is {dealer_cards}")
            if dealer_cards > 21:
                print("The dealer is bust! You win!")
                is_playing = False
            elif dealer_cards > cards_value:
                print("The dealer wins!")
                is_playing = False
            elif cards_value > dealer_cards:
                print("You scored higher than the dealer! You win!")
                is_playing = False
            elif dealer_cards == cards_value:
                print("Push! You both get your bet back.")
                is_playing = False
                
while True:
    play()
