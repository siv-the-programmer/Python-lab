# Mini Project: Simple Calculater
# Using Variables, Conditionals and While loop
#------------------------------------‐‐--------‐--‐-------‐---------
while True:
     print("Simple Calculator")
     print("Operations: + - * / ")
     print("-------------------------------")
     num1 = float(input("First number: " ))
     sign = input("Enter Operation> ")
     num2 = float(input("Second number: "))
    
     if sign == "+":
         print(num1 + num2)
     elif sign == "-":
         print(num1 - num2)
     elif sign == "*":
         print(num1 * num2)
     elif sign == "/":
         print(num1 / num2)
         print("invalid operation")
         print("Answer is", sign)
         
     done = input("exit? y/n ")
     if done == "y":
         break
        