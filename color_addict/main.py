from classes import*
deck=Deck()
dealer=Dealer()
discard_pile=Discard_pile()
words=["Orange","Blue","Green","Red","Grey","Brown","Black","Yellow","Pink","Purple","Joker"]
colours=["Orange","Blue","Green","Red","Grey","Brown","Black","Yellow","Pink","Purple"]
winner=False
def read_user_input():
    user_input=input("how many players ?\n")
    return user_input
def check_input():
    try:
        user_input=int(read_user_input())
    except ValueError:
        return False
    else:
        if user_input in [2,3,4]:
            return user_input
        else:
            return False
def determine_players_number():
    wrong_input=True
    while wrong_input:
        user_input=check_input()
        if user_input!=False:
            wrong_input=False
            return user_input
def create_cards():
    for word in words:
        for colour in colours:
            if word=="Joker":
                card=Card(word,"none")
            else:
                card=Card(word,colour)
            deck.cards.append(card)
def create_players(players_number):
    players_list=[]
    for number in range(1,players_number+1):
        player=Player(number)
        players_list.append(player)
    return players_list
def draw_first_cards(players):
    for player in players:
        for _ in range(3):
            player.draw_card()
def fisrt_message(turn):
    print(f"it's player {turn} turn")
    print(f"the last card is {[discard_pile.cards[-1].word,discard_pile.cards[-1].colour]}")
def check_valid_cards(turn,players,discard_pile):
    valid_cards=[]
    for card in (players[turn-1].hand_cards):
        if discard_pile[-1].word==card.word or discard_pile[-1].word==card.colour or discard_pile[-1].colour==card.word or  discard_pile[-1].colour==card.colour or card.word=="Joker" or discard_pile[-1].word==card.word==card.colour or discard_pile[-1].colour==card.word==card.colour or card.word==discard_pile[-1].word==discard_pile[-1].colour or discard_pile[-1].colour==card.word==card.colour:
            valid_cards.append(card)
    return valid_cards
def showing_card_to_player(turn,players):
    x=1
    for card in players[turn-1].hand_cards:
        print(x,[card.word,card.colour])
        x+=1
def showing_choices_to_player(colours):
    x=1
    for colour in colours:
        print(x,colour)
        x+=1
def start_game():
    global winner
    players_number=determine_players_number()
    players=create_players(players_number)
    create_cards()
    dealer.shuffle_deck(deck.cards)
    dealer.put_first_card_in_discrad(discard_pile.cards,deck.cards,colours)
    turn=dealer.distribute_cards(deck.cards,players_number,players)
    draw_first_cards(players)
    while winner==False:
        print("------")
        fisrt_message(turn)
        valid_cards=check_valid_cards(turn,players,discard_pile.cards)
        if len(valid_cards)==0:
            print("you have no valid card to play")
            if len(players[turn-1].deck_cards)>0 and len(players[turn-1].hand_cards)<4:
                print("you have to draw a card and pass your turn")
                players[turn-1].draw_card()
            else:
                print("you can't draw, you have to pass your turn")
        elif len(valid_cards)>0:
            showing_card_to_player(turn,players)
            player_card=players[turn-1].players_choice(dealer,valid_cards)
            if player_card.word=="Joker":
                showing_choices_to_player(colours)
                player_card.colour=players[turn-1].choose_colour(dealer,colours,player_card)
            players[turn-1].hand_cards.remove(player_card)
            discard_pile.cards.append(player_card)
            players[turn-1].draw_card()
        winner=dealer.check_win(players[turn-1])
        if winner==False:
            turn=dealer.check_turn(turn)
    print(f"player {turn} wins")
start_game()