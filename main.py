
import mathFile

print ("Choose from the list below:")
print ("1. Add")
print ("2. Subtract")
print ("3. Multiply")
print ("4. Divide")

choice = int(input("Enter choice(1/2/3): "))


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == 1:
    print (num1,"+",num2,"=", mathFile.add(num1,num2))

elif choice == 2:
    print ()

elif choice == 3:
    print ()



    




