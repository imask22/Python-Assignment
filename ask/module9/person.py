import card_game1player as dp
nm=input('Enter Your name')
obj=dp.Player(nm)

while(obj.play()):
    obj.show_hand()
    

