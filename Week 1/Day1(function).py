# In First week we cover the Python basics 

#  Topic no 01  (Functions)

# Create a simple function which add two numbers and return result.

def add(a,b):
    return a+b

result = add(5,10)

print(result)

# # Create a lambda function which multiply two numbers 

multiply = lambda num1, num2: num1 * num2
num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

result = multiply(num1, num2)

print(result)

# Global variable  (global variable is variable which is delared from outside the function)

global_var = " I am Nouman sajid "

def Functin1 ():
 print("Hellow" , global_var)

def Funation2 ():
   print("hi", global_var)

Functin1()
Funation2()

# Exercise (Solve problems using funactions)

# Problem no 1 :
# Write a recursive function to calculate the factorial of a non-negative integer.
# Exercise Purpose: Factorials (5! = 5 * 4 * 3 * 2 * 1) are the textbook example of recursion. This exercise reinforces the concept of a “Base Case” (stopping at 1) to prevent the function from running forever and crashing the memory stack.
# Given Input: number = 5
# Expected Output: The factorial of 5 is 120

def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)

num = 5
print ("The factorial of num is ", recursive_factorial(num))

# Problem no 02 :
# Sorted list of students according to their marks using lambda function.

students = [("Alice", 88), ("Bob", 75), ("Charlie", 92)]

lambda_sorted_students = sorted(students, key=lambda student: student[1], reverse=True)

print(lambda_sorted_students)