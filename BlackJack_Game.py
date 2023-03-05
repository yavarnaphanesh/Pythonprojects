import random


def rand_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    picked_card = random.choice(cards)
    return picked_card


def sum_cards(card_list):
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)


user_cards = []
computer_cards = []
is_game_Over = False

for i in range(2):
    user_cards.append(rand_card())
    computer_cards.append(rand_card())

while not is_game_Over:
    sum_of_user_cards = sum_cards(user_cards)
    sum_of_computer_cards = sum_cards(computer_cards)
    print(f"your card : {user_cards} current_score = {sum_of_user_cards}")
    print(f"computers first  card : {computer_cards[0]}")

    if sum_of_user_cards == 0 or sum_of_computer_cards == 0 or sum_of_user_cards > 21:
        is_game_Over = True
    else:
        user_should_deal = input(" for one more card type Y , type N to pass :")
        if user_should_deal == "Y":
            user_cards.append(rand_card())
        else:
            is_game_Over == True
while sum_of_computer_cards != 0 and sum_of_computer_cards < 17:
    computer_cards.append(rand_card())
    sum_of_computer_cards = sum_cards(computer_cards)

# print(user_cards)
# print(computer_cards)
# print(sum_of_user_cards)
# print(sum_of_computer_cards)
