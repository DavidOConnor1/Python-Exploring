#keyword arguments = arg proceded by an identifer when we pass them to further
# the order of the argu does not matter, unlike positional arg
# Python knows the names of the arguments that our function recently used 

def hello(fn, mn, ln):
    print("Hello "+fn+" "+ mn+ " " + ln)

#Postional arguments    
#hello("Monkey", "D.", "Luffy")

#keyword arg
hello(mn="D.", fn="Monkey", ln="Luffy")