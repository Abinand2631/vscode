def add():
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the first number: "))
    result=num1+num2
    print(f"The result of {num1}+{num2} is {result}")

def subtract():
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the first number: "))
    result=num1-num2
    print(f"The result of {num1}-{num2} is {result}")

def multiply():
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the first number: "))
    result=num1*num2
    print(f"The result of {num1}*{num2} is {result}")

def divide():
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the first number: "))
    if num2 != 0:
        result = num1 / num2 
        print(f"The result of {num1} / {num2} is {result}") 
    else:
        print("Error! Division by zero is not allowed")
        result=num1/num2
    
def calculator():
    while True:
        print("\n Simple Calculator")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Exit")

        choice=int(input("Enter the operation(1,2,3,4,5) : "))
        if choice==1:
            add()
        elif choice==2:
            subtract()
        elif choice==3:
            multiply()
        elif choice==4:
            divide()
        elif choice == 5: 
            print("Exiting the calculator") 
            break
        else: 
            print("Invalid input! Please choose a valid operation.")
        
calculator()

    

