import random
import art

# Defines the deck of cards. 10 is repeated three more times to represent the face cards: Jack, Queen, and King
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Function to simulate drawing a new card from the deck
def hit_me(card_hand, deck):
    card_hand.append(random.choice(deck))  # Adds a random card from the deck to the hand


# Function to calculate the total score of a hand
def calculate_score(card_hand):
    score = sum(card_hand)
    # If the score exceeds 21 and there's an Ace (11), change the Ace from 11 to 1
    if score > 21 and 11 in card_hand:
        card_hand.remove(11)
        card_hand.append(1)
        score = sum(card_hand)
    return score


# Displays the logo at the start of the game
print(art.logo)

play_game = True

# Main game loop
while play_game:
    if input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "n":
        # Exits the loop if the player does not want to play
        play_game = False
        break
    else:
        # Deal two random cards to the player and the computer
        player_hand = [random.choice(cards), random.choice(cards)]
        computer_hand = [random.choice(cards), random.choice(cards)]

        # Calculate the scores for both the player and the computer
        player_score = calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)

        # Check for player's natural blackjack right after initial deal
        if player_score == 21:
            print(f"Your final hand: {player_hand}, final score: {player_score}")
            print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
            print("You win with a Blackjack!")
            break

        # Displays the player's cards and score as well as the computer's first card
        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Computer's first card: {computer_hand[0]}")

        # Player's turn to hit or stand
        hit_or_stand = True
        while hit_or_stand:
            # If ever adding betting, add an IF statement here for Doubling Down
            if input("Type 'y' to Hit, type 'n' to Stand: ").lower() == 'y':
                hit_me(player_hand, cards)
                player_score = calculate_score(player_hand)
                # If the player's score exceeds 21, they lose
                if player_score > 21:
                    print("Bust. You lose!")
                    break

                # Displays an updated hand and score
                print(f"Your cards: {player_hand}, current score: {player_score}")
                print(f"Computer's first card: {computer_hand[0]}")
            else:
                # Player stands, ending their turn
                hit_or_stand = False

        # If player busts, ski[
        if player_score > 21:
            continue

        print(f"Your final hand: {player_hand}, final score: {player_score}")

        # Computer's turn (draw cards until the score is 17 or greater)
        if player_score <= 21:
            while computer_score < 17:
                hit_me(computer_hand, cards)
                computer_score = calculate_score(computer_hand)

        print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")

        # Determine the outcome
        if computer_score > 21:
            print("Dealer busts! You win!")
        elif player_score > computer_score and player_score <= 21:
            print("You win!")
        elif player_score == computer_score:
            print("You tie.")
        else:
            print("You lose!")
