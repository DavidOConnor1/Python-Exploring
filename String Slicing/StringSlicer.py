#slicing = create a sub string by extrqacting elements from another string
# indexing = extract an individual element from a string
#slicing have three optional arguments start:stop:step

name = "Monkey D. Luffy"

#first_name = name[0:6]
first_name = name[:6] #short cut way of writing the above line

#Last_name = name[7:15]
last_name = name[7:] #short cut way of writing the above line

print(first_name)
print(last_name)


#RandomName = name[0:15:2]
RandomName = name[::2] #short cut way of writing the above line
print(RandomName)

reversed_name = name[::-1]

print(reversed_name)