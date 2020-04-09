first_name = input("What is your first name?   ")
print("Hello", first_name)
if first_name == "Chris":
    print(first_name, "is learning Python")
elif first_name == "Seth":
    print("You should learn Python, {}!".format(first_name))
else:
    age = int(input("How old are you?   "))
    if age <=6:
        print("Wow! You're {}! If you are a strong reader...".format(age))
    print("You should learn Python, {}!".format(first_name))
print("Have a great day {}!".format(first_name))