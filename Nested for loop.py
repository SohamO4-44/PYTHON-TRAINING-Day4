for i in range(1,4):
    for j in range (1,4):
        for j in range (1,4):
            print("i", end="")
            print()
n=(input("enter the number of rows:"))
for i in range(1,n+1):
   for j in range(1,n+1):
    print(chr(64+i),end="")
print()
