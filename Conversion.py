def binary_Decimal(binNumber):                                  # Converts binary number to decimal.
    decNumber = 0
    initial = 1

    for i in range(len(binNumber)-1,-1,-1):                     # Iteration from -1 to the lengthof list with -1 step. 
        decNumber = decNumber + initial *int(binNumber[i])
        initial = initial * 2
        
    return decNumber

def decimal_Binary(decNumber):                          # Converts decimal number to binary.
    binList = [] 
    
    while decNumber > 0:

        if decNumber%2 == 0:
            binList.append(0)
        else:
            binList.append(1)
        decNumber = decNumber // 2                       # gives a pure integer number rather than floating numbers.

    # Only for a number string without leading 0's
    if binList != []:                                    #since the list formed on converting 0 to binary number has null elements, so logical operation is performed.
        binList.reverse()
        convertString1 = [str(i) for i in binList]
        joinS1 = "".join(convertString1)
    else:
        joinS1 = str(0)

    # Only for a number string with leading 0's
    binList.reverse() 
    i = len(binList)
    while i < 8:                                         # will add 0 in front, if the length of binary number is less than 8. 
        binList.append(0)                               
        i = i + 1
    binList.reverse()                                    # reverses the list. 
    convertString2 = [str(i) for i in binList]           # Converts each elements of list to String.
    joinS2 = "".join(convertString2)                     # Joins all the String elements from list to a complete single String. 
    
    return [joinS1, joinS2]                              # returns a list of two number-string with or without leading 0's.