from random import randint

card_base = randint(1, 13)
is_playing = True

def play(): # Defines the starting of a new round
    global is_playing
    begin_input = input("Would you like to begin the game? (y) ")
    if begin_input != "y":
        print("Goodbye")
        is_playing = False
    else:
        print("Let's play!")
        game_loop()

def game_loop(): # This is the main game loop
    global is_playing
    cards_value = 0  # Defining the value of all cards added outside the loop
    while is_playing:

        draw_input = input("Press Enter to draw your card") # This is the input for drawing a card
        if draw_input == "": # If the user presses Enter
            card_value = recieve_card() # Calling the function to determine the value of the card (The  function is defined later)
            cards_value += card_value
            print(f"Your card value is {card_value}. Total value: {cards_value}")
            draw_input = 0

            if cards_value > 21:
                print("You're Bust! The value of your cards is over 21.")
                is_playing = False
                play()

def recieve_card():
    card_base = randint(1, 13)
    if 2 <= card_base <= 10:
        return card_base
    elif card_base == 1:
        return 11  # Assuming Ace is 11
    else:
        return 10  # For J, Q, K
    
while True:
    play()