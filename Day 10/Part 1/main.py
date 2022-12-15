from collections import defaultdict

filepath = 'input.txt'

commands = {'addx': 2, 'noop': 1}
clkCount = 1
currentValue = 1
cycles = defaultdict(int)
values = []
sum = 0
usedCycles = [20, 60, 100, 140, 180, 220]

with open(filepath) as fp:
  line = fp.readline().strip().split()

  
  while line:
    lines = [*line]
    cycles[clkCount] = currentValue
    if (lines[0] == 'noop'):
      clkCount += 1
      cycles[clkCount] = currentValue
      
    elif (lines[0] == 'addx'):
      for x in range(2):
        clkCount += 1
        cycles[clkCount] = currentValue
      currentValue += int(lines[1])
      cycles[clkCount] = currentValue
      
      
    line = fp.readline().strip().split()

  for interested_Clks in usedCycles:
    values.append(cycles[interested_Clks]*interested_Clks)
  print(values)
  for x in range(len(values)):
    sum += values[x]
  print(sum)
    
      

  