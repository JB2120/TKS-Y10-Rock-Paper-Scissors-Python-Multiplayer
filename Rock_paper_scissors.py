#here goes the program goes
player = input('player 1 or player 2:')
if player == '1':
    played = input('enter r p or s:')
    data = open("rps data.txt",'r+')
    data.seek(0,0)
    data.writelines(played)
    data.close()
if player == '2':
    played = input('enter r p or s:')
    data = open("rps data.txt",'r+')
    data.seek(1,0)
    data.writelines(played)
    data.close()
    
