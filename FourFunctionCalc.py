# PROJECT-1 (FOUR FUNCTION CALCULATOR)

#For input (Left-hand operand and Right-hand operand)
x = int(input("Enter the Number x: "))  #Taking operand for first operand.
y = int(input("Enter the Number y: "))  #Taking operand for second operand.

#Printing the available operations
print("What is the desired operation?")
print("1 Addition")
print("2 Subtraction")
print("3 Multiplication")
print("4 Division")

#Pompt for operation selection.
operation = input("Enter your choice: ") 

#Implementation of Match Cases
match int(operation):
    case 1:  # Print the result of x+y.
        print("Result:", x + y)
    case 2:  # Print the result of x-y. 
        print("Result:", x - y)
    case 3:  # Print the result of x*y. 
        print("Result:", x * y)
    case 4 if y!=0: #If y is zero, print an error. Otherwise, print the value of x/y. 
        print("Result:", x / y)
    case 4 if y==0:
        print("Result:", "Error!")

