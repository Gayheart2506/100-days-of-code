class Person():
    def __init__(self, name, age):
        self.age = age
        self.name = name
    

    def qualified_voter(self):
        if self.age >= 18:
            return True
        else:
            return False

print("*********** Welcome to the Qualified Voters Identifier Program ************\n")

person = Person(input("Enter Name: "), int(input("Qualified to vote ? Enter Age please: ")))

qualified = person.qualified_voter()
if qualified:
    print(f"Hello {person.name}, You are Qualified to vote")
else:
    print(f"Oops, {person.name}, You are not eligible to vote at the age of {person.age}.")