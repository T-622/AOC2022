filepath = 'rucksacks.txt'
global currline1
global currline2
global currline3
currline1 = []
currline2 = []
currline3 = []
totals = []
matchingChar = 0
number = 0
val = 0
val2 = 0

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

numbers = [0]*52

for x in range (0, 52):
  number += 1
  numbers[x] = number

resDict = dict(map(lambda i,j : (i,j) , letters,numbers))

def IntersecOfSets(arr1, arr2, arr3):
    # Converting the arrays into sets
    s1 = set(arr1)
    s2 = set(arr2)
    s3 = set(arr3)
      
    # Calculates intersection of 
    # sets on s1 and s2
    set1 = s1.intersection(s2)         #[80, 20, 100]
      
    # Calculates intersection of sets
    # on set1 and s3
    result_set = set1.intersection(s3)
      
    # Converts resulting set to list
    final_list = list(result_set)
    return final_list[0]

with open(filepath) as fp:
  
  val += 1

  while val <= 100:
    
    val += 1
    currline1 = []
    currline2 = []
    currline3 = []
    
    for x in range(0, 3):
        
      line = 0
      line = fp.readline()    
      line = line.strip()
      
      if (x == 0):
        currline1 = [*line]
        
      elif (x == 1):
        currline2 = [*line]
        
      elif (x == 2):
        currline3 = [*line]

      val2 += 1
    
    matchingChar = IntersecOfSets(currline1, currline2, currline3)
    
    totals.append(int(resDict[matchingChar]))


  print(totals)
  print(sum(totals)) 