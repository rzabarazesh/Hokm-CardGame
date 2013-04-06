import random
import os
deck = []
# +++++++++++++++++ DEFINING THE CLASSES ++++++++++++++++++++
class card :
    def __init__(self,suit,mark):
        self.suit = suit
        self.value = mark
        self.mark = mark
        self.owner = ''
        if mark == 1 or mark == 'a':
            self.value = 14
        if mark == 'j' :
            self.value = 11
        if mark == 'q' :
            self.value = 12
        if mark == 'k' :
            self.value = 13
    def __str__(self):
        return(str(self.mark) + " of " + self.suit)




#-----------------------------------------------------------#
class player :
    def __init__(self,playername):
        self.name = playername
        self.hand = []
        self.is_hakem = False
        self.points = 0
    def __str__(self):
        return (str(self.name))
    def throw(self,index):
        # function to throw cards to deck from player's hand
        deck.append( self.hand[int(index)-1] )
        self.hand = self.hand[:int(index)-1] + self.hand[int(index):]

    def showhand(self):
        # function to print all the card player has with a number next to each
        counter = 1
        for card in self.hand :
            print str(counter)+"-->",card
            counter +=1
#----------------------------------------------------------#



def showdeck() :
    print "Deck :  ---> " ,
    for card in deck :
        print card ,":",card.owner, "-" ,
    print " "

# ++++++++++++ DEFINING THE IN-GAME VARIABLES +++++++++++++++
deck = []
allcards = []
print "entekhabe team ha ..."
print "lotfan name khod ra vared konid "
print "--------------------------"
print "TEAM 1 ..."

player1 = player(raw_input("nafare aval : "))
player3 = player(raw_input("nafare dovom : "))
print "TEAM 1 = " , player1.name,'+',player3.name
print "--------------------------"
print "TEAM 2 ..."

player2 = player(raw_input("nafare aval : "))
player4 = player(raw_input("nafare dovom : "))
print "TEAM 2 = " , player2.name,'+',player4.name
print "--------------------------"
print "team ha entekhab shodan ."
print "baraye edame kelide Enter ra feshar dahid ..."
raw_input()
os.system('cls')
not_hakem = [player1,player2,player3,player4]


#-----------------------------------------------------------#
# creating a list of all 52 cards in the game for later use #
#-----------------------------------------------------------#
for suit in ["del","khaaj","pik","khesht"]:
    for mark in [2,3,4,5,6,7,8,9,10,'j','q','k','a']:
        newcard = card(suit,mark)
        allcards.append(newcard)


#-----------------------------------------------------------#
#      randomly choosing one of the players as the hakem    #
#-----------------------------------------------------------#
hakem = random.choice(not_hakem)
not_hakem.remove(hakem)
players =[hakem]+not_hakem
hakem.is_hakem=True

#-----------------------------------------------------------#
#      Randomly giving the hakem 5 card so he can hokm      #
#-----------------------------------------------------------#
print hakem , "be tore tasadofi be onvane hakem entekhab shod."
for i in range(5):
    newcard = random.choice(allcards)
    allcards.remove(newcard)
    newcard.owner = hakem.name
    hakem.hand.append(newcard)
print " ================================================="
print hakem.name ,"in daste avale shomast . lotfan hokm konid : "
hakem.showhand()


#-----------------------------------------------------------#
#  as the hakem does hokm , the value of all the hokm cards #
#  are increased by 100 so they will always win in the deck #
#-----------------------------------------------------------#

hokm = raw_input("(type konid 'pik' or 'del'or 'khesht'or'khaaj') ---> ")
for card in hakem.hand:
    if (card.suit == hokm) :
        card.value = int(card.value)+100

for card in allcards:
    if (card.suit == hokm) :
        card.value += int(card.value)+100

for i in range(8):
    newcard = random.choice(allcards)
    allcards.remove(newcard)
    newcard.owner = hakem.name
    hakem.hand.append(newcard)

for player in not_hakem :
    for i in range(13):
        newcard = random.choice(allcards)
        allcards.remove(newcard)
        newcard.owner = player.name
        player.hand.append(newcard)

#-----------------------------------------------------------#
#                   the game's main loop                    #
#-----------------------------------------------------------#

while (player1.points + player3.points <7 and player2.points + player4.points <7) :
    isfirst = True
    while (len(deck)<4):
        # every player throws a card by turn
        for player in players :
            os.system('cls')
            print "       "
            showdeck()
            print "       "
            print "##################################################"
            print player.name , "nobate shoma ast . "
            print "baraye namayeshe kart haye khod Enter ra feshar dahid ..."
            raw_input()
            player.showhand()
            indice = raw_input("lotfan adade karte morede nazar ra vared konid : ")

            player.throw(indice)
            first_suit = deck[0].suit
            print first_suit
            if (isfirst):
                # if it is the first time in the hand that a card is being throwed
                # all of the card with the same suit will gain 50 additional value
                # only for that hand
                deck[0].value += 50
                for player in players :
                    for card in player.hand:
                        if card.suit == first_suit:
                            card.value +=50
            isfirst = False

    #finding the winner card after each hand
    maxval = 0
    for card in deck :
        print card.value
        if card.value > maxval :
            maxval = card.value
            maxcard = card

    #current hand results
    for player in players :
        if maxcard.owner == player.name :
            print " "
            showdeck()
            print " "
            print "-------------------------------------------------"
            print player.name , "in dast ra ba " , maxcard ," bord !!"
            print " "
            print "================================================="
            player.points += 1
            players = players[players.index(player):] + players [:players.index(player)]
            raw_input("baraye edame kelide Enter ra feshar dahid ...")
    deck = []
    for player in players :
        for card in player.hand:
            if card.suit == first_suit:
                card.value -=50
# final results
print " bazi be payan resid "
print " emtiaze bazi konan:"
print "Team1 :" , player1.name , "And",player3.name ,player1.points+player3.points
print "Team2 :" , player2.name , "And",player4.name ,player2.points+player4.points