import numpy as np
path = 'input.txt'
visible = 0

dimensions = [0, 0, 0, 0]

scores = []

with open(path) as fp:
  lines = fp.read().strip().split()
  

createdGrid = [list(map(int, list(line))) for line in lines]

lenX = len(createdGrid)
lenY = len(createdGrid[0])

createdGrid = np.array(createdGrid)  # Y, X

currentScore = 1
distance = 0
for y in range(1, lenY-2):
  for x in range(1, lenX-2):
    
    dimensions = [1, 1, 1, 1] 
    currHeight = createdGrid[y,x]
    
    z = 0
    while True:  # Check Right Direction
      z += 1
      if (x+z >= lenX):
        break
      elif(createdGrid[y,z+x] < currHeight):
        dimensions[0]+=1
      else:
        break

    z = 0
    while True:  # Check Left Direction
      z+=1
      if (x-z <= 0):
        break
      elif(createdGrid[y,x-z] < currHeight):
        dimensions[1]+=1
      else:
        break

    z = 0
    while True:  # Check Up Direction
      z+=1
      if (y+z >= lenY):
        break
      elif(createdGrid[y+z,x] < currHeight):
        dimensions[2]+=1
      else:
        break
        
    z = 0
    while True:
      z+=1
      if (y-z <= 0):
        break
      elif(createdGrid[y-z,x] < currHeight):
        dimensions[3]+=1
      else:
        break

    scores.append(dimensions[0]*dimensions[1]*dimensions[2]*dimensions[3])

scores.sort()
print(max(scores))

    
        
      
      



    