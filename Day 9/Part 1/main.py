import numpy as np
import os
import time
filepath = 'input.txt'

global lastPos
global headpos
global tailPos 

prevPositions = []

counter = 0

headPos = [0,0]
tailPos = [0,0]
diff = [0,0]


sets = {""}

def updateList(value):
  prevPositions.append([value[0], value[1]])

def calculateDiff(x1, x2, y1, y2):
  return (x1-x2), (y1-y2)

def updateHead(dir):
  if (dir == 'U'):
    headPos[1] = headPos[1] + 1
  elif (dir == 'D'):
    headPos[1] = headPos[1] - 1
  elif (dir == 'L'):
    headPos[0] = headPos[0] - 1
  elif (dir == 'R'):
    headPos[0] = headPos[0] + 1

def moveTail(dx, dy):
  count = 0
  if (abs(dx) == 2 and abs(dy) == 0):
    if (dx > 0):
      tailPos[0] += 1
    else:
      tailPos[0] -= 1
    count += 1
  elif (abs(dx) == 0 and abs(dy) == 2):
    if (dy > 0):
      tailPos[1] += 1
    else:
      tailPos[1] -= 1
    count += 1
  else:
    if (dx == -1 and dy == 2):
      tailPos[0] -= 1
      tailPos[1] += 1
      count += 1
    elif (dx == 1 and dy == 2):
      tailPos[0] += 1
      tailPos[1] += 1
      count += 1
    elif (dx == 1 and dy == -2):
      tailPos[0] += 1
      tailPos[1] -= 1
      count += 1
    elif (dx == -1 and dy == -2):
      tailPos[0] -= 1
      tailPos[1] -= 1
      count += 1

    elif (dx == -2 and dy == 1):
      tailPos[0] -= 1
      tailPos[1] += 1
      count += 1
    elif (dx == 2 and dy  == -1):
      tailPos[0] += 1
      tailPos[1] -= 1
      count += 1
    elif (dx == 2 and dy == 1):
      tailPos[0] += 1
      tailPos[1] += 1
      count += 1
    elif (dx == -2 and dy == -1):
      tailPos[0] -= 1
      tailPos[1] -= 1
      count += 1
  return count
with open(filepath) as fp:
  line = fp.readline().strip().split()
  while line:
    lines = [*line]
    print(lines)
    for x in range(int(lines[1])):
      diff = [0,0]
      updateHead(lines[0])
      diff[0], diff[1] = calculateDiff(headPos[0], tailPos[0], headPos[1], tailPos[1])
      counter += moveTail(diff[0], diff[1])
      updateList(tailPos)
      print(tailPos)
      
      
    line = fp.readline().strip().split()

  se = set(tuple(x) for x in prevPositions)
  print(len(se))  # Len Of Places Traversed Converted Into Set Rids Of Duplicates
      