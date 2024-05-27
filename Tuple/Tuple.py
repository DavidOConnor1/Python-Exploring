# collection of which is ordered and unchangeable
# used to group together related data

student = ("Davey", 22,"male")
print(student.count("Davey"))
print(student.index("male"))

for z in student:
    print(z)
    
if "Davey" in student:
    print("Student Exists")