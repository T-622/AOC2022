from collections import defaultdict
input = 'input.txt'
currPath = []
sampleArray = []
pathDict = defaultdict(int)
readData = open(input).read().strip()  # Read Data Into Single String
lines = [x for x in readData.split('\n')]

  
def closest(lst, K):
      
  return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

xy = 0
for line in lines:
  ins = line.strip().split()
  if (ins [1]== 'cd'):  # If we're changing dir
    
    if(ins[2] == '..'):
      currPath.pop()  # Remove Last Directory Entry On 'cd ..'
      
    else:
      
      currPath.append(ins[2])  # Add To Current Directory Entry
      
  elif (ins[1] == 'ls'):
    
    continue
    
  else:  # If No Command Is Being Issued, Directory Values Are Being Provided (ls); Store Them In Currnum, and 
    try:
      
      curNum = int(ins[0]) 
      
      for i in range (len(currPath)+1):
        pathDict['/'.join(currPath[:i])] += curNum  # Add Item To Path Dict As Key, And Attach To Directory Size (Add, To Key (Create It If It Doesn't Exist), and add current value to all leading up directories, as the containing directories grow with their contents!) (Also Grows Path As Progressing Through For Loop, To Add To Correct Dict Keys)
    except:
      pass
      
pt1 = 0
for path, pathSize in pathDict.items():
  if (pathSize <= 100000):
    pt1 += pathSize


totalUsed = pathDict['/']
maxUsable = 70000000 - 30000000
required = totalUsed - maxUsable
print("Current Used (Bytes):",totalUsed)
print("Need To Clear:",required)

pt2 = 0

for path, pathSize in pathDict.items():
  sampleArray.append(pathSize)
sampleArray.sort()
print("Part 1 Is:",pt1)
print("Part 2 Is:",closest(sampleArray, required))