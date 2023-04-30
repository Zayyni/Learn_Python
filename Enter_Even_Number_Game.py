print("Enter Even number in 3 times to Win Game")
i=1
while i<=3:
    a=int(input("Enter an Even number"))
    if a%2==0:
        break
    i +=1;
if i==4:
    print("Game Over")
else:
    print("You are winner")
print()    