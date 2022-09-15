from classes import*
deck=Deck()
words=["Orange","Blue","Green","Red","Grey","Brown","Black","Yellow","Pink","Purple","Joker"]
colours=["Orange","Blue","Green","Red","Grey","Brown","Black","Yellow","Pink","Purple"]
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
def create_cards():
    for word in words:
        for colour in colours:
            if word=="Joker":
                card=Card(word,'none')
            else:
                card=Card(word,colour)
            deck.cards.append(card)