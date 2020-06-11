# Program to take two numbers as input from user and perform arithmetic operations on them.

print("***Performing Arithmetic Operations on two numbers***\n")
# Taking two numbers as input from the user
number1String = input('Enter the first number:')
number2String = input('Enter the second number:')

# converting the two numbers into integer data type
n1 = int(number1String)
n2 = int(number2String)

# Display the resultant arithmetic operations on two numbers
print("Addition of two numbers:", n1, '+', n2, '=', n1+n2)
print("Subtraction of two numbers:", n1, '-', n2, '=', n1-n2)
print("Multiplication of two numbers:", n1, '*', n2, '=', n1*n2)
print("Division of two numbers:", n1, '/', n2, '=', n1/n2)
print("Modulus of two numbers:", n1, '%', n2, '=', n1 % n2)
print("Exponent of two numbers:", n1, '**', n2, '=', n1**n2)