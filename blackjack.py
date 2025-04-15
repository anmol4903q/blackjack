# 🃏 BLACKJACK GAME BY ANMOL
import random  # Importing random to randomly select cards

# Function to calculate the total values of player and bot cards
def capare(fst_card, sec_card, bot_fst_card, bot_sec_card):

    # Nested function to get the value of a single card
    def card_value(card):
        if card == "ace":
            return 11  # By default, ace is treated as 11
        elif card in ["king", "queen", "jack"]:
            return 10
        else:
            return card  # Number cards return their numeric value

    # Creating lists of player's and computer's two cards
    player_cards = [fst_card, sec_card]
    bot_cards = [bot_fst_card, bot_sec_card]

    # Calculating initial totals
    player_tot = sum(card_value(card) for card in player_cards)
    bot_tot = sum(card_value(card) for card in bot_cards)

    # Adjusting ace from 11 to 1 if total exceeds 21
    if "ace" in player_cards and player_tot > 21:
        player_tot -= 10

    if "ace" in bot_cards and bot_tot > 21:
        bot_tot -= 10

    return player_tot, bot_tot

# Function to randomly change the first card
def fst_card_change(fst_card):
    deck = ["ace","king","queen","jack", 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return random.choice(deck)

# Function to randomly change the second card
def sec_card_change(sec_card):
    deck = ["ace","king","queen","jack", 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return random.choice(deck)

# Main game loop
ch = "YES"
while ch == "YES":
    try:
        # Creating full deck
        cards = ["ace","king","queen","jack", 2, 3, 4, 5, 6, 7, 8, 9, 10]

        # Randomly selecting two cards for player
        fst_card = random.choice(cards)
        sec_card = random.choice(cards)
        print(f"\n🎴 Your cards: [{fst_card} and {sec_card}]")

        # Randomly selecting two cards for computer (only first shown)
        bot_fst_card = random.choice(cards)
        bot_sec_card = random.choice(cards)
        print(f"🤖 Computer's first card is [{bot_fst_card}]\n")

        # Asking if player wants to exchange a card
        exc = input("🔁 Do you want to exchange any of your cards? (Y/N): ").upper()
        if exc == "Y":
            wc = int(input("Which card do you want to change? First(1) or Second(2): "))
            if wc == 1:
                fst_card = fst_card_change(fst_card)
                print(f"🔄 Your new first card is: {fst_card}")
            elif wc == 2:
                sec_card = sec_card_change(sec_card)
                print(f"🔄 Your new second card is: {sec_card}")

        # Asking if player wants to reveal the cards
        reveal = input("🔎 Type 'Y' to reveal the cards: ").upper()
        if reveal == "Y":
            # Get the totals for both
            player_total, bot_total = capare(fst_card, sec_card, bot_fst_card, bot_sec_card)
            print(f"\n🎯 Your total: {player_total}")
            print(f"🖥️ Computer's total: {bot_total}")

            # Win/loss logic
            if player_total > 21:
                print("💥 Oh no! You crossed 21\n❌ YOU LOSE!")
            elif bot_total > 21:
                print("🔥 Computer crossed 21\n✅ YOU WON!")
            else:
                if player_total > bot_total:
                    print("🏆 You won!")
                elif player_total < bot_total:
                    print("😢 You lose!")
                else:
                    print("⚖️ It's a tie!")

        # Line break after each game
        print("*" * 90)
        ch = input("🎮 Wanna play one more time? (Yes/No): ").upper()

    except ValueError:
        # Handles invalid number inputs like text instead of 1/2
        print("⚠️ Please enter valid input! Restarting the round...\n")
