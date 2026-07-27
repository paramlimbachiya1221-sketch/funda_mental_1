print("Welcome to the interactive personal data collector!")
print("")

name=input("Please enter your name: ")
age=int(input("Please enter your age: "))
height=float(input("Please enter your height in cm: "))
favourite=int(input("Please enter your favourite number: "))

print("")
print("thank you! Here is the information we collected:")
print("")

print("Name:", name,type(name),"Memory Address : ", id(name))
print("Age:", age,type(age),"Memory Address : ", id(age))
print("Height:", height,type(height),"Memory Address : ", id(height))
print("Favourite Number:", favourite,type(favourite),"Memory Address : ",id(favourite))

print("")

print("your birth year is approximately ", 2026-age," (based on your age of ",age)
print("")

print("Thank you for using the personal data collector! Have a great day!")