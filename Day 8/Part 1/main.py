import numpy as np
path = 'input.txt'
visible = 0

with open(path) as fp:
  lines = fp.read().strip().split()
  

createdGrid = [list(map(int, list(line))) for line in lines]

lenX = len(createdGrid)
lenY = len(createdGrid[0])

createdGrid = np.array(createdGrid)

print(createdGrid)
for y in range(lenY):
  for x in range(lenX):
    currHeight = createdGrid[y,x]  # Run Through Each Tree, One Place At A Time
    if (x == 0 or y == 0 or x == lenX-1 or y == lenY - 1):  # If Any Edges Reached
      visible += 1
    elif (np.amax(createdGrid[y, :x]) < currHeight):  # Check If Axis Max Leading Up To Current Position; At Y, Up To Current X (Excl Current), is smaller Than Current Value, Otherwise It Will Be Blocked By A Larger Tree From Left Side
      visible += 1
    elif (np.amax(createdGrid[y, (x+1):]) < currHeight):  # Check If Axis Max Leading From Current Position (Right), Contains A Value Smaller Than Current Height, Otherwise, A Taller Tree From The Right Is Blocking It
      visible += 1
    elif (np.amax(createdGrid[:y, x]) < currHeight):  # Check Downwards Axis Max, To See If Any Trees Leading Up To The Current Could Be Larger, Blocking The Front View
      visible += 1
    elif (np.amax(createdGrid[(y+1):, x]) < currHeight):  # Check Axis Upwards Max, To See If Any Trees In Upwards Direction Will Block Rear View
      visible += 1

print("Day 1, Pt.1 Is:",visible)



    