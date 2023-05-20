import Conversion  as Convert                                               #importing the program file to use their functions or methods.
import ByteAdder as BAdder

def binaryAdder():
    print("------------------------------------Binary Adder------------------------------------")
    Continue = True

    while Continue == True:                                                 # While loop for continuing to sum two binary numbers.
        end = False
        while end == False:                                                 # While Loop for wrong inputs in integer type variable a. 
            try:
                a = int(input(" Enter First Number: "))
                
                if a > 255 or a < 0:
                    print(" Sorry! the entered number must be between 0 & 255.")
                    print("")
                else:
                    end = True
            except:
                print(" Please, type integer number only!")
                print("")

        print("---------------------------")
        end = False
        while end == False:                                                     # While loop for wrong inputs in integer type variable b.
            try:                
                b = int(input(" Enter Second Number: "))
                if b > 255 or b < 0:
                    print(" Sorry! the entered number must be between 0 & 255.")
                    print("")
                else:
                    end = True
            except:                                                             # Exception if string value is entered.
                print(" Please, type integer number only!")
                print("")
        
        if a == 0 and b == 0:                                                   # both 0 input can cause an error when deducting leading 0's
            value = '0'
            binForma = [0]                                                      # values are assigned directly to avoid errors.       
            binFormb = [0]                                
        else:
            binForma = Convert.decimal_Binary(a)                                # Calling decimal_Binary function from Conversion.py passing an argument a.
            binFormb = Convert.decimal_Binary(b)                                # Calling decimal_Binary function from Conversion.py passing an argument b.
            value = BAdder.byteAdder(binForma[1], binFormb[1])                  # Calling byteAdder function from BitAdder.py passing two arguments binForma adn binFormb.
        
        print("---------------------------")  
        print("")      
        print(" The binary form of decimal value %s and %s is %s and %s respectively." %(str(a),str(b),binForma[0],binFormb[0]))
        print("") 
        print(" Their binary sum is " + value + " and the decimal sum is " + str(Convert.binary_Decimal(value))+".")
        print("")
        print("------------------------------------------------------------------------------------")

        Cont = (input(" Do you want to Continue (Y/N)? ")).upper()
        while Cont != "Y" and Cont != "N":                                       # looping when the inputs are rather than "Y" & "N".
            Cont = (input(" only (Y/N)? ")).upper()
        if Cont == "Y":
            Continue = True
            print("------------------------------------------------------------------------------------")
            print("")
        else:
            print("------------------")
            print("  You've Exited!")  
            print("------------------")          
            Continue = False
        
binaryAdder()                                                                     # Calling binaryAdder function with no Arguments.