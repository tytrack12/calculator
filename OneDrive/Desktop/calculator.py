# calculator.py

def sum(a, b):
    return a + b

def real_division(a, b):
    if b == 0:
        return "Error: Division by zero"
    else:
        return a / b

def sub(a, b):
    return a - b

def power(a, b):
    return a ** b

def main():
    print("Welcome to Calculator!")
    print("1. Sum")
    print("2. Real Division")
    print("3. Subtraction")
    print("4. Power")
    choice = int(input("Enter your choice: "))
    
    if choice in [1, 2, 3, 4]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == 1:
            print("Result:", sum(num1, num2))
        elif choice == 2:
            print("Result:", real_division(num1, num2))
        elif choice == 3:
            print("Result:", sub(num1, num2))
        elif choice == 4:
            print("Result:", power(num1, num2))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
