def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2
def calculator(n1,n2,operation):
    if operation == '+':
        return add(n1,n2)
    elif operation == '-':
        return subtract(n1,n2)
    elif operation == '*':
        return multiply(n1,n2)
    elif operation == '/':
        return divide(n1,n2)
    else:
        return "Invalid operation"
def main():
    print("Welcome to the calculator program!")
while True:
    print("Please select an operation:")    
    n1 = float(input("Enter first number: "))
    operation = input("Enter operation (+, -, *, /): ")
    n2 = float(input("Enter second number: "))
    result = calculator(n1,n2,operation)
    print(f"The result is: {result}")
if __name__ == "__main__":
    main()
