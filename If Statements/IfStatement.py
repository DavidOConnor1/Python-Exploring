# if statemnt is a block of code that will perform if the conditoon is true

age = int(input("How old are you?: "))

if age == 100:
    print("You are ancient")
elif age >= 18:
    print("you are an adult")
elif age <0:
    print("You do not exist")
else:
    print("You are a child!")