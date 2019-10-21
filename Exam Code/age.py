age = int(input("Enter your age: "))
if age > 0 and age <= 34:
    print("Young")
elif age > 34 and age <= 50:
    print("Mature")
elif age > 50 and age <= 69:
    print("Middle-aged")
elif age > 69:
    print("Old")
else:
    print("Invalid age")