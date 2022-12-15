import numpy as np
import sys

filepath = 'input.txt'

np.set_printoptions(edgeitems=30, linewidth=100000, 
    formatter=dict(float=lambda x: "%.3g" % x))

clkCount = 0
currentValue = 1
lineValue = 0
part2 = 0
values = [1]*241

with open(filepath) as fp:
  line = fp.readline().strip().split()
  while line:
    lines = [*line]
    
    if (lines[0] == 'noop'):  # No Operation
      clkCount += 1           # Increase Clock Edge Count
      values[clkCount] = currentValue # Value At Clk Pos In Values
      
    elif (lines[0] == 'addx'):
      lineValue = int(lines[1])
      values[clkCount + 1] = currentValue
      currentValue += lineValue
      clkCount += 2  # Increase Tick Counter By 2 (For Add OP)
      values[clkCount] = currentValue
      
      
      
    line = fp.readline().strip().split()
    
#print(values)  # Print Out 0-240 Values

dispArr = np.full([6, 40], '*',dtype=str)

cyclePosition = 0

for col in range(6):    # Iterate Through Columns
  for row in range(40): # Iterate Through Rows
    cyclePosition += 1  # Increase counter That Runs From 0-240
    
    if(abs(values[cyclePosition-1] - row) <= 1):
      dispArr[col,row] = "##"
    else:
      dispArr[col,row] = "  "# Put Empty Pixel

print(dispArr)
    

  