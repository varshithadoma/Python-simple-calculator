def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x,y):
    if y!=0:
        return x / y
    else:
      return "Error! Division by Zero."

def calculator():
    print("Simple Calculator")
    print("Choose operation:")
    print("1. Add")
    print("2.substract")
    print("3.Multiply")
    print("4.Divide")
    
    while True:
         choice = input("Enter choice (1/2/3/4): ")
         
         if choice in ('1', '2','3', '4'):
             num1 = float(input("Enter first number: "))
             num2 = float(input("Enter second number: "))
             
             if choice == '1':
                 print(f"The Result is: {add(num1,num2)}")
             elif choice == '2':
                 print(f"The Result is:{substract(num1, num2)}")
             elif choice == '4':
                 print(f"The Result is:{multiply(num1, num2)}")
             
             next_calculation = input("do you want to perform another calculation? (yes/no): ")
             if next_calculation.lower() != 'yes':
                 break
    else:
        print("Invalid Input")
calculator()       
