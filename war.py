from random import shuffle

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split() 

class Deck:
    def __init__(self):
        print("Creating New Orderes Deck!")
        self.allcards = [(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("SHUFFLING DECK")
        shuffle(self.allcards) 

    def split_in_half(self):
        return (self.allcards[:26],self.allcards[26:])
    
class Hand:

    def __init__(self,cards):
        self.cards = cards 

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))   

    def add(self,added_cards):
        self.cards.extend(added_cards)

    def remove_cards(self):
        return self.cards.pop()

class Player:

    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_cards = self.hand.remove_cards()    
        print("{} has placed: {}".format(self.name,drawn_cards))
        print('\n')
        return drawn_cards
    
    def remove_war_card(self):
        war_cards = []
        if len(self.hand.cards)< 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):
        return len(self.hand.cards) != 0     
    
print("Welcome to war , let's begin...")

#create new deck and split in half
d = Deck()
d.shuffle()
half1,half2 = d.split_in_half()

#create both players!

comp = Player("Computer", Hand(half1))

name = input("What is your name:")
user = Player(name,Hand(half2))

total_round = 0 
war_count = 0

while user.still_has_cards() and comp.still_has_cards():
    total_round += 1
    print("Time for a new round!")
    print("Here are new current standings")
    print(user.name+"has the count:"+str(len(user.hand.cards)))
    print(comp.name+"has the count:"+str(len(comp.hand.cards)))
    print("Play a card!")
    print('\n')

    table_cards = []

    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        war_count += 1

        print("War!")

        table_cards.extend(user.remove_war_card())
        table_cards.extend(comp.remove_war_card())

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)    

    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)  

print("Game over,number of rounds:" + str(total_round))
print("A war happened " +str(war_count)+ "times")                  
print("Does the computer still have cards?")
print(str(comp.still_has_cards()))
print("Does the human still have cards?")
print(str(user.still_has_cards()))