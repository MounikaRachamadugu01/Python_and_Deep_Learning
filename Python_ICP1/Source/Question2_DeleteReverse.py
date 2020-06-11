# Program to Input the string “Python” as a list of characters from console
# delete at least 2 characters, reverse the resultant string and print it.

# Taking input string
string = input('Enter the string:')
# Deleting 2 characters from the input string
sub = string[0:3] + string[5:]
# Display the resultant string in reverse order
print(sub[::-1])


