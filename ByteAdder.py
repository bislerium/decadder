def orGate(x,y):                                        # OR Gate Function.
    if x == 0 and y == 0:
        return 0 
    else:
        return 1


def xorGate(x,y):                                       # XOR Gate Function
    if (x==1 and y==1) or (x == 0 and y == 0):
        return 0
    else:
        return 1

def andGate(x,y):                                       # AND Gate Function.
    if x == 1 and y == 1:
        return 1
    else:
        return 0

def byteAdder(x,y):                                     # Function for adding two different bytes of binary numbers.
    fOutput = []     

    # Half Bit adder for adding the corresponding last digit of two binary number.
    st_1 = xorGate(int(x[-1]), int(y[-1]))              # Gives Sum
    c_out = andGate(int(x[-1]), int(y[-1]))             # Carry Out

    # Full Bit Adder for adding the corresponding remaining digit of two binary number.
    for i in range(len(y)-2,-1,-1):
        step_1 = xorGate(int(x[i]) , int(y[i]))
        step_2 = andGate(int(x[i]), int(y[i]))
        step_3 = andGate(step_1, c_out)
        step_4 = xorGate(step_1, c_out)                 # Gives Sum
        step_5 = orGate(step_2, step_3)                 # Carry Out
        c_out = step_5
        fOutput.append(step_4)

    if c_out == 1:                                      # Adding the final Carry bit to the output string
        fOutput.append(c_out)
    fOutput.reverse()                                   # Reverses the String 
    fOutput.append(st_1)                                # Adds Carry-Bit from the Half-Bit Adder
    
    while fOutput[0] == 0:                              # deleting the front-leading 0's from the list 
        del fOutput[0]
    convertString = [str(i) for i in fOutput]           # Converts each elements of list to String.
    joinS = "".join(convertString)                      # Joining each elements from the list to form a single string.

    return joinS                                        #Returns a number string without leading 0's.