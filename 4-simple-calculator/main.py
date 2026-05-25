def add(a,b):
    return a+b
def minus(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        print("Error! Can't divide by zero")
    return a/b
operations = {
    "+": add,
    "-": minus,
    "*": multiply,
    "/": divide
}
    
print("===== Welcome to Calculator =====");

run_app = True;
while run_app:
    a = float(input("Enter First Number: "))
    operator = input("Enter operator ( +, -, *, / ): ")
    b = float(input("Enter First Number: "))
    
    
    if operator not in operations:
        print("invalid operation choose one from : +, -, *, /")
    
    else:
        func = operations[operator]
        result = func(a, b)
        print(f"{a} {operator} {b} = {result}")
    repeat = input("\nWould you like to do another math? [y/n]: ").lower()
    if repeat == 'n':
        run_app = False
        print("Goodbye!")
