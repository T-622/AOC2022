filepath = 'input.txt'
count = 0
count1 = 0
first = [0]*2
second = [0]*2
array = []

def isOverlappingFully(x1,x2,y1,y2):
  '''
    Func:
      Test If 2 Ranges Fully Overlap
    Args:
      X1 = Lower Range1
      X2 = Upper Range2

      Y1 = Lower Range2
      Y2 = Upper Range2
    Returns:
      True => Ranges Fully Overlap
      False => Ranges Don't Fully Overlap
  '''
  
  if (y1 >= x1 and y2 <= x2): 
    return True
  elif (x1 >= y1 and x2 <= y2):
    return True
  else:
    return False

with open(filepath) as fp:
  count1 += 1 
  while True:
    for x in range (0, 1000):
      line = 0
      array = []
      line = fp.readline()
      line = line.strip()
      line = line.replace('-', ',')
      array = line.split(',')
      print(array)
      if (isOverlappingFully(int(array[0]), int(array[1]), int(array[2]), int(array[3])) == True):
        count += 1

    print(count)
    break
    
  
  