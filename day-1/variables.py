name = input("Name: ")
age = int(input("Age: "))
Gender = input("Gender: ")
age_limit = 18 - age

if age >= 18:
    print("Eligible to vote\n")
    print("*********** DETAILS ************")
    print(f"NAME : {name}")
    print(f"AGE: {age}")
    print(f"GENDER: {Gender}")
else:
    print("Not qualified to vote !!")
    print(f"Age is less by {age_limit}")