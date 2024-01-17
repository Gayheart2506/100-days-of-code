# Example of a type Error code 

'''In python we cannot concatenate int variables, we can only
concatenate strings, so if the code below is runed without converting the name
variable to a string it will produce a TypeError bug.
You can try remove the str coverter from the name variable and run the code to 
see the output.
'''

name = len(input("what is your name?: "))
print("Your name contains " + str(name) + " characters.")