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
    currPath = [0]*4      # Initialize Blank Array For 4 Current Charecters
    
    print("StartPos:",i)   # Print Out Start Position (0 Default)
    for x in range (i, i+4):   # Run For 4 Iterations, Filling Our Blank Array With 4 Chars, Starting At i, going to i+4
      
      currPath[y] = tempArr[x]  # Current Index Y Used To Select Where To Fill 4 Chars From tempArr (That Uses Index Between i,to i+4)
      y +=1
      
    print(currPath)             # Print Charecters Currently In Array
      
    if (find_dup_char(currPath) == True):  # If Duplicates Found In Array, Increase Next Position For Starting 4 Chars
      print("Found Duplicate")
      
    else:
      print("After Char",i+4)  # No Duplicate Found, Print Out Where To Find First DIfferent Char
      break

    i += 1  # Increase i (current index in tempArr) If A Duplicate Found
    

  
