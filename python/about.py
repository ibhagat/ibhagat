# Create a variable called name and set it equal to your name
name=input("What is your Name?:")
print(type(name))

# Create a variable called age and set it to your age in years 
# Note: This must be an int, not a string!
age=int(input("What is your age?:"))
print(type(age))

# Create a variable called place and set it equal to where you live
place=input("Where you live?:")
print(type(place))
# Create a variable called output, and use string formatting to 
# make it like the example text in the description
string="Hello my name is {} and I am {} years old. I live in {} and I love Python!"
output=string.format(name,age,place)

# Finally, use the print() function to print the output.
print(output)


#OR THIS COULD BE DONE IN BELOW MANNER ALSO
# Create a variable called name and set it equal to your name
#name = "Indrajit Bhagat"
#print(type(name))

# Create a variable called age and set it to your age in years 
# Note: This must be an int, not a string!
#age = 35
#print(type(age))

# Create a variable called place and set it equal to where you live
#place = "Vadodara"
#print(type(place))

# Create a variable called output, and use string formatting to 
# make it like the example text in the description
#string = "Hello my name is {} and I am {} years old. I live in {} and I love Python!"
#output = string.format(name, age, place)

# Finally, use the print() function to print the output.
#print(output)
