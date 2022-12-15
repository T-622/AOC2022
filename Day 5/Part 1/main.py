mvfr = 0
mvto = 0
mvnum = 0

row1 = ["R", "S", "L", "F", "Q"]
row2 = ["N","Z","Q","G","P","T"]
row3 = ["S","M","Q","B"]
row4 = ["T","G","Z","J","H","C","B","Q"]
row5 = ["P","H","M","B","N","F","S"]
row6 = ["P","C","Q","N","S","L","V","G"]
row7 = ["W","C","F"]
row8 = ["Q","H","G","Z","W","V","P","M"]
row9 = ["G","Z","D","L","C","N","R"]
stackMap = {1: row1, 2: row2, 3: row3, 4: row4, 5: row5, 6: row6, 7: row7,8: row8, 9: row9}

with open('instructions.txt') as f:
  instructions = f.readlines()

for instruction in instructions:
  
  instruction = instruction.strip()
  instruction = instruction.split(' ')
  print(instruction)
  
  i = 0
  
  while i < int(instruction[1]):
    stackMap[int(instruction[5])].append(stackMap[int(instruction[3])].pop())
    i += 1

print(row1[len(row1)-1], row2[len(row2)-1],row3[len(row3)-1], row4[len(row4)-1], row5[len(row5)-1], row6[len(row6)-1], row7[len(row7)-1], row8[len(row8)-1], row9[len(row9)-1])