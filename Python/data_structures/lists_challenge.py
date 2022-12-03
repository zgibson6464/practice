import random


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    choice = input('Press enter to pick a card, or type Q and enter to exit: ')
    if choice == 'Q':
        break
    else:
        randomCard = random.randint(0, len(diamonds)-1)
        hand.append(diamonds[randomCard])
        diamonds.pop(randomCard)
        print(diamonds)
        print(hand)
if not diamonds:
    print('There are no more cards to pick')
