# Mini Project: Simple Calculater
# Using Variables, Conditionals and While loop
#------------------------------------‐‐--------‐--‐-------‐---------

while True:
     print("Simple Calculator") # means show the word calculator 
     print("Operations: + - * / ")
     print("-------------------------------")
     num1 = float(input("First number: " )) #variable for the first number.
     sign = input("Enter Operation> ")
     num2 = float(input("Second number: "))
    
     sign == "+":
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
        