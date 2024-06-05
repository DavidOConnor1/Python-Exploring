#   nested function calls = function calls inside other function calls
#   innermost function calls are resolved first
#   returned value is used as argument for the next outer function

#   Without using A nested function call
#   num = input("Enter A whole number: ")
#   num = float(num)
#   num = abs(num)
#   num = round(num)
#   print(num)

#   Using a nested function call

print(round(abs(float(input("Enter A whole number:")))))