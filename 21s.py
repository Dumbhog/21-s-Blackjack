from random import randint

card_base = randint(1, 13)
is_playing = 0 # This is the variable that determines if the game is being played or not
chips = 20 # This is the amount of chips the player has
bet_amount = 0  # This is the amount of chips the player is betting at a given time

def play():  # Defines the starting of a new round
    global is_playing
    begin_input = input(f"Chips: {chips}. Would you like to begin a round? (y) ")
    if begin_input != "y":
        print("You didn't agree. Goodbye!")
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
        return 1  # Assuming Ace is 1
    else:
        return 10  # For J, Q, K

def game_loop():  # This is the main game loop
    global is_playing
    global chips
    global bet_amount
    cards_value = 0  # Defining the value of all cards added outside the loop

    bet_amount = int(input("How much would you like to bet? " ))  # This is the input for the bet amount
    if isinstance(bet_amount, int) == False:
        print("Please enter a valid number.")
        is_playing = False
    if bet_amount > chips:
        print("You don't have enough chips to bet that amount.")
        is_playing = False
    else: 
        chips -= bet_amount
        
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
                chips -= bet_amount
                print(f"You're Bust! The value of your cards is over 21. chips: {chips}")
                is_playing = False


        elif draw_input == "e":  # If the player types E
            print(f"Your final value is {cards_value}") # Prints the final value of the cards
            dealer_cards = 0
            while dealer_cards < 17:
                dealer_card_value = (recieve_card())
                dealer_cards += dealer_card_value
                print(f"The dealer drew a card worth {dealer_card_value}. Total value: {dealer_cards}")
            print(f"The dealer's final value is {dealer_cards}")
            if dealer_cards > 21:
                chips += (bet_amount * 2)
                print(f"The dealer is bust! You win! chips: {chips}")
                is_playing = False
            elif dealer_cards > cards_value:
                print(f"The dealer wins! chips: {chips}")
                is_playing = False
            elif cards_value > dealer_cards:
                chips += (bet_amount * 2)
                print(f"You scored higher than the dealer! You win! chips: {chips}")
                is_playing = False
            elif dealer_cards == cards_value:
                chips += bet_amount
                print(f"Push! You both get your bet back. chips: {chips}")
                is_playing = False
while True:
    play()
