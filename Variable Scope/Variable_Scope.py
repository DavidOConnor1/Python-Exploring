# scope = the region that a variable is recognized
#   A variable that is only available from the region it is created in example : function (local scope) 
#   A global and locally scoped versions of a variable can be created

name = "Davey" #global scope variable (available inside or outside functions)

def display_name():
    name = "Gravy" # local scope variable (only available from within this function)
    print(name)
    
display_name();
print(name)