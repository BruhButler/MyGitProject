#connects to the mathFile.py file and uses the functions 
import mathFile

print ("Choose from the list below:")
print ("1. Add")
print ("2. Subtract")
print ("3. Multiply")
print ("4. Divide")

#gets the input for the math functions
choice = int(input("Enter choice(1/2/3): "))

#gets the input for math functions
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

#calls the functions from the mathFile.py file
if choice == 1:
    print (num1,"+",num2,"=", mathFile.add(num1,num2))

elif choice == 2:
    print ()

elif choice == 3:
    print ()



    




