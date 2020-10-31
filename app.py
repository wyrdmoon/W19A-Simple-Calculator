import addition
import subtraction
import multiplication
import division 

print ("choose an operation")
print ("1. addition")
print ("2. subtraction")
print ("3. multiplication")
print ("4. division")

userChoice = input ("Select Operation")
if userChoice in ('1', '2', '3', '4' ):
    num1 = float(input("Enter first number"))
    num2 = float(input("Enter second number"))
    
    
    if(userChoice =="1"):
        addition.addNum(num1, num2)
    elif(userChoice == "2"):
        subtraction.subNum(num1, num2)
    elif(selection == "3"):
        multiplication.multiNum(num1, num2)
    elif(userChoice == "4"):
        division.divNum(num1, num2)
        
    else:
        print("error")