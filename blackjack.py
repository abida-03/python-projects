import random


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Takes a list of cards and returns the sum"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "The game is a draw"
    elif c_score == 0:
        return "You lose... The dealer has a blackjack!"
    elif u_score == 0:
        return "You win with a blackjack!!"
    elif u_score > 21:
        return "You went over. You lose :("
    elif c_score > 21:
        return "The dealer went over. You win!!"
    elif u_score > c_score:
        return "You win!!!"
    else:
        return "You lose :("


def play_game():
    logo = '''
                            _____
                    _____  |K  WW| 
            _____  |Q  ww| | o {)|            
     _____ |J  ww| | o {(| |o o%%| _____
    |10 & || o {)| |o o%%| | |%%%||A _  |
    |& & &||o o% | | |%%%| |_%%%>|| ( ) |
    |& & &|| | % | |_%%%O|        |(_'_)|
    |& & &||__%%[|                |  |  |
    |___0I|                       |____V|
    '''
    title = '''

       ____  _            _     _            _    
      | __ )| | __ _  ___| | __(_) __ _  ___| | __
      |  _ \\| |/ _` |/ __| |/ /| |/ _` |/ __| |/ /
      | |_) | | (_| | (__|   < | | (_| | (__|   < 
      |____/|_|\\__,_|\\___|_|\\_\\|_|\\__,_|\\___|_|\\_\\
                            |__/

    '''
    print(logo)
    print(title)
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score((computer_cards))
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to draw another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score((computer_cards))

    print(f"Your final hand: {user_cards}, and final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, and final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("\n Do you want to play a game of blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()
