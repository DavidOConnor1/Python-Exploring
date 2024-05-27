# index operator [] gives access to the sequence of the element include but not limited to (str, list, tuples)

name = "monkey d. luffy@"

#if(name[0].islower()):
 #   name = name.capitalize()
    
first_name = name[:6].upper()
last_name = name[7:]
last_character = name

#I was trying to captialize both indexes that I have had listed but it only captializes the first index
if(last_name[0].islower() and last_name[3].islower()):
    last_name = last_name.capitalize()

#print(name)
#print(first_name)
print(last_name)

