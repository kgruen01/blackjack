# Katie Gruenhagen, Lilly Liu
# 5C Hackathon Fall 2015
# Friday, November 13, 2015
#
#
import random
DEBUG = True

card_values = { "AH": 11, "AS": 11, "AD": 11, "AC": 11, "KH": 10, "KS": 10, "KD": 10, \
 "KC": 10, "QH": 10, "QS": 10, "QD": 10, "QC": 10, "JH": 10, "JS": 10, "JD": 10, "JC": 10, \
 "10H": 10, "10S": 10, "10D": 10, "10C": 10, "9H": 9, "9S": 9, "9D": 9, "9C": 9, "8H": 8, \
 "8S": 8, "8D": 8, "8C": 8, "7H": 7, "7S": 7, "7D": 7, "7C": 7, "6H": 6, "6S": 6, "6D": 6, \
  "6C": 6, "5H": 5, "5S": 5, "5D": 5, "5C": 5, "4H": 4, "4S": 4, "4D": 4, "4C": 4, "3H": 3, \
  "3S": 3, "3D": 3, "3C": 3, "2H": 2, "2S": 2, "2D": 2, "2C": 2 }

deck_of_cards =["AH", "AS", "AD", "AC", "KH", "KS", "KD", "KC", "QH", "QS", "QD", "QS", "QD",\
 "QC", "QD", "QC", "JH", "JS", "JD", "JC", "10H", "10S", "10D", "10C", "9H", "9S", "9D", "9C", \
 "8H", "8S", "8D", "8C", "7H", "7S", "7D", "7C", "6H", "6S", "6D", "6C", "5H", "5S", "5D", "5C",\
  "4H", "4S", "4D", "4C", "3H", "3S", "3D", "3C", "2H", "2S", "2D", "2C"]

def main():
    print "welcome to blackjack"
    user = createHand()
    print "Your cards are:"
    print printHand(user)
    dealer = createHand()
    if checkBlackjack(dealer) == True:
        print "The dealer's hand is:"
        print printHand(dealer)
        print "Dealer got a blackjack, sorry you lost"
        playagain()
    sum_user_hand = sumHand(user)
    sum_dealer_hand = sumHand(dealer)
    while bustchecker(user) == False:
        choice = userChoice()
        if choice == True:
            print "You drew a card"
            user += [dealCard()]
            if bustchecker(user) == True:
                print "Your cards are"
                print printHand(user)
                print "You busted"
                playagain()
            else:
                dealerPlay(sum_dealer_hand, dealer)
                print printHand(user)
        elif choice == False:
            while sum_dealer_hand < 17:
                dealer= dealerPlay(sum_dealer_hand, dealer)
                sum_dealer_hand = sumHand(dealer)
            if sum_dealer_hand >= 17 and bustchecker(dealer) == False:
                if sum_dealer_hand > sum_user_hand:
                    print "The dealer's cards are:"
                    print printHand(dealer)
                    print "The dealer wins!"
                    playagain()
                if sum_user_hand >= sum_dealer_hand:
                    print "The dealer's cards are:"
                    print printHand(dealer)
                    print "You win!"
                    playagain()

def dealerPlay(sum_dealer_hand, dealer):
    if sum_dealer_hand < 17:
        dealer += [dealCard()]
        if bustchecker(dealer) == True:
            print "The dealer drew a card"
            print "The dealer's cards are: "
            print printHand(dealer)
            print "The dealer busted. You win!"
            playagain()
        else:
            print "The dealer drew a card"
    elif sum_dealer_hand >= 17 and bustchecker(dealer) == False:
        if sum_dealer_hand > sum_user_hand:
            print "The dealer's cards are:"
            print printHand(dealer)
            print "The dealer wins!"
            playagain()
        if sum_user_hand > sum_dealer_hand:
            print "The dealer's cards are:"
            print printHand(dealer)
            print "You win!"
            playagain()
    elif bustchecker(dealer) == True:
        print "You win!"
        playagain()
    return dealer


def playagain():
    play = raw_input("Would you like to play again? yes or no?")
    if play == "no":
        print "Bye!"
        quit()
    elif play == "yes":
        main()
    else:
        print "Please only put yes or no."
        playagaim()

def bustchecker(hand):
    if sumHand(hand) > 21:
        return True
    else:
        return False

def dealCard():
	global deck_of_cards
	cardnum = random.choice(range(len(deck_of_cards)))
	card =  deck_of_cards[cardnum]
	deck_of_cards=  deck_of_cards[:cardnum] + deck_of_cards[cardnum + 1:]
	return card

def createHand():
    hand = []
    num_cards = 0
    for i in range(2):
        hand += [dealCard()]
    return hand

def printHand(hand):
    if len(hand) == 0:
        return ""
    elif len(hand) == 1:
        return hand[-1]
    else:
        return hand[0] + "\n" + printHand(hand[1:])


def checkBlackjack(hand):
    sum_hand = 0
    global card_values
    for card in hand:
        sum_hand += card_values[card]
    if sum_hand == 21:
        return True
    else:
        return False


def sumHand(hand):
    sum_hand = 0
    global card_values
    for card in hand:
        sum_hand += card_values[card]
    return sum_hand

def userChoice():
    user_choice = raw_input("Hit or stand? ")
    if user_choice == 'stand':
        return False
    if user_choice == 'hit':
        return True

    else:
        print "Choose only hit or stand"
        userChoice()
