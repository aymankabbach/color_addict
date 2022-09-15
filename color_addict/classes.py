import random
class Card:
    def __init__(self,word,colour):
        self.word=word
        self.colour=colour
class Deck:
    def __init__(self):
        self.cards=[]
class Discard_pile:
    def __init__(self):
        self.cards=[]
class Player():
    def __init__(self,number):
        self.number=number
        self.hand_cards=[]
        self.deck_cards=[]
    def draw_card(self):
        self.hand_cards.append(self.deck_cards.pop(0))
    def players_choice(self,ref,valid_cards):
        wrong_input=True
        while wrong_input:
            player_choice=ref.is_card_valid_to_play(self,valid_cards)
            if player_choice!=False:
                wrong_input=False
                return player_choice
    def choose_colour(self,ref,colour,card):
        wrong_input=True
        while wrong_input:
            player_choice=ref.is_colour_valid(colour)
            if player_choice!=False:
                wrong_input=False
                card.colour=colour[player_choice-1]
                return card.colour
class Dealer:
    def __init__(self):
        pass
    def shuffle_deck(self,deck):
        import random
        random.shuffle(deck)
    def put_first_card_in_discrad(self,discard,deck,colour):
        discard.append(deck.pop(0))
        if self.check_joker_case(discard):
            self.active_joker_special_cas(discard,colour)
        else:
            pass
    def check_joker_case(self,discrad):
        if discrad[0].word=="Joker" and discrad[0].colour=="none":
            return True
        else:
            return False
    def active_joker_special_cas(self,discard,colour):
        Cards_colour=random.choice(colour)
        discard[0]=Card("Joker",Cards_colour)
    def distribute_last_card_randomly(self,players,deck):
        randomly_choosen_player=random.choice(players)
        randomly_choosen_player.deck_cards.append(deck.pop(0))
        return randomly_choosen_player.number
    def distribute_cards(self,deck,player_number,players):
        cards_to_distribute=len(deck)/player_number
        for player in players:
            for number in range(int(cards_to_distribute)):
                player.deck_cards.append(deck.pop(0))
        turn=self.distribute_last_card_randomly(players,deck)
        return turn
    def check_turn(self,turn):
        turn+=1
        if turn>4:
            turn=1
        return turn 
    def read_player_choice(self):
        player_choice=input("which card do you want to play ?\n")
        return player_choice
    def is_card_valid_to_play(self,player,valid_cards):
        try:
            player_choice=int(self.read_player_choice())
        except ValueError:
            print("invalid input, try again")
            return False
        else:
            if player_choice>len(player.hand_cards):
                print("invalid input, try again")
                return False
            elif player.hand_cards[player_choice-1] in valid_cards:
                return player.hand_cards[player_choice-1]
            else:
                print("not valid card, chose another one")
                return False
    def is_colour_valid(self,colour):
        try:
            player_choice=int(self.read_player_choice())
        except ValueError:
            print("invalid input, try again")
            return False
        else:
            if player_choice>0 and player_choice<len(colour):
                return player_choice
            else:
                print("invalid input, try again")
                return False
    def check_win(self,player):
        if len(player.hand_cards)==0 and len(player.deck_cards)==0:
            return True
        else:
            return False