#a block of code that only runs when it is called

def hello(fname, lname, age):
    print("Hello "+fname+" "+lname)
    print("Your Age is: "+str(age))
    print("have a nice day")
    
#hello()

#calling the hello function 3 times
#for i in range(3):
 #   hello("davey")

#hello(input("Enter Your Name: ")) #Taking input from the user when using the hello function since input is automatically assigned to string

#These fucntions can take more than one argument for a parameter
hello("Auto", "Bot", 22)