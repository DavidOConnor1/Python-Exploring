name = "bro"

print(len(name)) #this show string length

print(name.find("r"))# this shows the index of where the character is located

print(name.capitalize()) #will capitalize the first letter of the string

print(name.upper())#will make the string all uppercase

name_second="BRO"

print(name_second.lower())#will make the string all lowercase

print(name.isdigit())#will return a true or faLse text based on if the string is a digit

age = "500"
print(age.isdigit())

print(name.isalpha()) #Will return if the string is a letter or not
print(age.isalpha())
print(name.count("o"))#will count how many of the assigned character is in the string

print(name.replace("b", "p"))# will replace the delcared character with the new character

print(name*4) #We can print a string multiple times by multiplying it by a number