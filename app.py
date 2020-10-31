import addition.py
import subtraction.py
import multiplication.py
import division.py 

print ("choose an operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

userChoice = input ("Select Operation")
if userChoice in ('1', '2', '3', '4' ):
    num1 = float(input("Enter first number"))
    num2 = float(input("Enter second number"))
    
    
    if(userChoice =="1"):
        addition.add(num1, num2)
    elif(userChoice == "2"):
        subtraction.sub(num1, num2)
    elif(selection == "3"):
        multiplication.multi(num1, num2)
    elif(userChoice == "4"):
        division.div(num1, num2)
        
    else:
        print("error")