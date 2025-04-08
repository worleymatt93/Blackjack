# Blackjack

A simple command-line interface Blackgack game written in Python. It simulates a game of Blackjack between a single player and the computer acting as the dealer. The game follows traditional Blackjack rules and includes features like hitting, standing, and checking for Blackjack and busts.

# Features

- Simulates drawing cards from a deck.
- Adjusts Ace value (11 to 1) to avoid busts.
- Handles player input to decide game flow.
- Dealer follows standard Blackjack rules.
- Simple win/loss/tie logic.

# Game Rules

- The goal is to get as close to 21 as possible without going over.
- Cards are valued as follows:
  + Number cards (2-10) have face value.
  + Face cards (Jack, Queen, King) are worth 10.
  + Aces can be worth 11 or 1, depending on which is more favoriable to the hand.
- The player and the dealer both start with two cards.
- The dealer reveals only one of their cards initially.
- The place can choose to Hit (draw a card) or Stand (end their turn).
- The dealer must continue drawing until reaching a score of at least 17.
- If either the player or dealer exceeds 21, they bust and lose the game.
