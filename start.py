name = input("What's your name? ")

# remove whitespace left and right -- strip = remove all coverings
name = name.strip()

# capitalize all first letter of the world  - write like title 
name = name.title()

fullname = name
firstName, lastName = name.split(" ")

print("Full name: " + fullname)
print("First name: " + firstName)
print("Last name: " + lastName)



