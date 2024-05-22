#nested loops are the inner loops that will finish all of iterations before
#before finishing the outer loops

rows = int(input("how many rows?: "))
columns = int(input("How many columns?: "))
symbol = input(("enter your symbol: "))

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()