filename = 'input.txt'

itemsM0 = []
itemsM1 = []
itemsM2 = []
itemsM3 = []

line1 = []
line2 = []
line3 = []
line4 = []
line5 = []
line6 = []

inspectedItem = [0, 0, 0, 0, 0, 0, 0, 0] #M0, M1, M2, M3
y = 0

monkeys = []  # Call W/ monkeys[id][element]
monkey = {}

with open(filename) as fp:
  for x in range(8):
    line1 = fp.readline().strip('\n').strip(':').split()  # Monkey Number
    line2 = fp.readline().strip().split(': ')[1].split(',')  # Starting Items
    line3 = fp.readline().strip().split()  # Operation
    line4 = fp.readline().strip().split()  # Test
    line5 = fp.readline().strip().split()  # Throw To True
    line6 = fp.readline().strip().split()  # Throw To False
    line7 = fp.readline()
  
    monkey = {
      'ID':line1[1],
      'List':line2,
      'Op':line3[-1],
      'Test':line4[-1],
      'Tm':line5[-1],
      'Fm':line6[-1]
    }
    monkeys.append(monkey)

#print(monkeys)

bigMod = 9699690

for x in range (10000):
  for m in monkeys:
    currId = int(m["ID"])
    
    for z in range (len(monkeys[currId]["List"])):
      old = int(monkeys[currId]["List"][z])
      if (currId == 0):
        newNum = (old * int(m["Op"])) % bigMod
      elif (currId == 1):
        newNum = (old + int(m["Op"])) % bigMod
      elif (currId == 2):
        newNum = (old + int(m["Op"])) % bigMod
      elif (currId == 3):
        newNum = (old + int(m["Op"])) % bigMod
      elif (currId == 4):
        newNum = (old * int(m["List"][z])) % bigMod
      elif (currId == 5):
        newNum = (old + int(m["Op"])) % bigMod
      elif (currId == 6):
        newNum = (old + int(m["Op"])) % bigMod
      elif (currId == 7):
        newNum = (old * int(m["Op"])) % bigMod

      if (newNum % int(m["Test"]) == 0):
        monkeys[int(monkeys[currId]["Tm"])]["List"].append(str(newNum))
        inspectedItem[currId] += 1
        
      else:
        monkeys[int(monkeys[currId]["Fm"])]["List"].append(str(newNum))
        inspectedItem[currId] += 1
    
    m["List"].clear() 

inspectedItem.sort()
print("Part 1:",inspectedItem[-1]*inspectedItem[-2])


    
  