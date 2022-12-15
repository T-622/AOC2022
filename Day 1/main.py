filepath = 'file.txt'
calories = []*1
original = []*1
value = 0
ints = 0

with open(filepath) as f:
    original = f.read()
  
original = original.split('\n')

while True:
  if (value == len(original)):
    break

  print(value)
  if (original[value] in ' '):
    value += 1
    
  elif (int(original[value]) >= 0):
    ints += int(original[value])
    #print(ints)
    if (value == 2248):
      break
    if (original[value+1] in " "):
      value += 1
      calories.append(ints)
      ints = 0
      print("\n")
  value += 1
  
  


calories.sort()
print(len(calories))
print(calories)

    