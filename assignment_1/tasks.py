#TASK-1

n1=float(input("Enter first number:"))
n2=float(input("Enter second number:"))
addition=n1+n2
subtraction=n1-n2
multiplication=n1*n2
if(n2==0):
    print("not defined")
else:
    division=n1/n2
print("Addition:",addition)
print("Subtraction:",subtraction)
print("Multiplication:",multiplication)
print("Division:",division)


#TASK-2

a=str(input("Enter your first name:"))
b=str(input("Enter your last name:"))
print("Hello! "+ a +" "+ b + " , Welcome to python class")