tempArr = []
filepath = 'datastream.txt'
i = 0

def find_dup_char(input):
 
    if len(input) == len(set(input)): # Check For Len Of Input == To Set; Indicating No Replicated Chars
      return False
    else:  # If Repeated Chars Are Detected, Set Will Remove Duplicate, Making Len Smaller
      return True

with open(filepath) as f:  # Open File
  
  line = f.read()          # Read File Back Into String
  tempArr = [*line]        # Split String Into Charecter Array
  
  i = 0                    # Set I Counter To 0 (Later Use)
  
  while True:
    
    y = 0                  # Y Counter (0 - 13) Set 0 Flush
    currPath = [0]*14      # Initialize Blank Array For 14 Current Charecters
    
    print("StartPos:",i)   # Print Out Start Position (0 Default)
    for x in range (i, i+14):   # Run For 14 Iterations, Filling Our Blank Array With 14 Chars, Starting At i, going to i+14
      
      currPath[y] = tempArr[x]  # Current Index Y Used To Select Where To Fill 14 Chars From tempArr (That Uses Index Between i,to i+14)
      y +=1
      
    print(currPath)             # Print Charecters Currently In Array
      
    if (find_dup_char(currPath) == True):  # If Duplicates Found In Array, Increase Next Position For Starting 14 Chars
      print("Found Duplicate")
      
    else:
      print("After Char",i+14)  # No Duplicate Found, Print Out Where To Find First DIfferent Char
      break

    i += 1  # Increase i (current index in tempArr) If A Duplicate Found
    

  
