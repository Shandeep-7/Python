#Pattern : Right anle triangle
n=int(input("Enter a num :"))
for r in range(0,n,1):
    for c in range(0,n,1):
        if(r>=c):
            print("*", end="")
        else:
            print(" ", end="")
    print()