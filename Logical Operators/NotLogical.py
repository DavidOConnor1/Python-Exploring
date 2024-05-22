temp = int(input("How hot is it outside?: "))

if not(temp>= 0 and temp<=30):
    print("The Weather Sucks Today")
    print("Play Gamez")
elif not( temp<0 or temp> 30):
    print("The Weather is great")
    print("Touch Grass")