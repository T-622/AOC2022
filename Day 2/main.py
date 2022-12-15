'''
  Object + 3 For Tie
  Object + 6 For Win
  Object + 0 For Loss

  Possibilities:

  (U1) : (U2)
  
  A X = (1+3) (1+3) Tie
  A Y = (1+0) (2+6) U2 Win
  A Z = (1+6) (3+0) U1 Win

  B X = (2+6) (1+0) U1 Win
  B Y = (2+3) (2+3) Tie
  B Z = (2+0) (3+6) U2 Win

  C X = (3+0) (1+6) U2 Win
  C Y = (3+6) (2+0) U1 Win
  C Z = (3+3) (3+3) Tie

  U1:
  A = Rock (1) +6 For Win
  B = Paper (2) +6 For Win
  C = Scissors (3) +6 For Win

  U2:
  X = Rock (1) +6 For Win
  Y = Paper (2) +6 For Win
  Z = Scissors (3) +6 For Win

'''
filepath = 'plays.txt'

opponent = ""
you = ""
line = 0

u1total = 0
u2total = 0

with open(filepath) as fp:
  line = fp.readline()
  cnt = 0
  
  while line:
    if (cnt == 0):
      print("Skipping Read For First Line")
    else:
      line = fp.readline()
      line = line.strip()
    
    cnt+=1
    try:
      opponent, you = line.strip().split(' ')
    except ValueError:
      break
    print(opponent, you)
     
    if (opponent in 'aA'):  # If P1 Chooses Rock
      if (you in 'xX'):  # If Users Have Same Input
        u1total += 4  # Tie, Both Get +3,1 Point
        u2total += 4
      elif (you in 'yY'):
        u1total += 1  # U2 Wins, Gets 1+7 Pts, U1 Gets +1,0 For Choosing
        u2total += 8
      elif (you in 'zZ'):
        u1total += 7  # U1 Wins Again, Gets 1+7 Pts, U2 Gets +3,0 For Choosing
        u2total += 3
       
    elif (opponent in 'bB'):
      if (you in 'xX'):  # If Users Have Same Input
        u1total += 8  # U1 Win, Gets +2,6 Pts For Winning
        u2total += 1  # U2 Gets 1
      elif (you in 'yY'):
        u1total += 5  # Tie, Both Get +3,2 Pts For Tying
        u2total += 5
      elif (you in 'zZ'):
        u1total += 2  # U2 Wins, Gets +3,6 Pts For Winning
        u2total += 9

    elif (opponent in 'cC'):
      if (you in 'xX'):  # If Users Have Same Input
        u1total += 3  # U1 Win, Gets +3,6 Pts For Winning
        u2total += 7
      elif (you in 'yY'):
        u1total += 9  # U1 Wins, Gets +3,6 Pts For Winning
        u2total += 2
      elif (you in 'zZ'):
        u1total += 6  # Tie, Both Get +3,3 Pts For Winning
        u2total += 6
      
  
  print(u2total)  
print("Opponent:",u1total)
print("You:",u2total)