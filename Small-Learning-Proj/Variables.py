name = input("Enter your name:")
age = input("Enter your age:")
height = float(input("Enter your height in metres (eg. 1.80):"))
current = ("beginner python developer currently testing variables")

print(f"Your name is {name}, you are {age} years old and {height}m tall. You are a {current}")

is_raining = input("Is it raining? Yes/No?: ")

if is_raining == "Yes": print(str(f"You better get a coat on, {name}")) ; 
else: print("Enjoy the weather!")
