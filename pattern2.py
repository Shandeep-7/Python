#Pattern : Diamond
n=int(input("Enter a num :"))
for r in range(0,2*n,1):
    for c in range(0,2*n,1):
        if(r+c>=n+1 and c-r<=n-1 and r<n):
            print("*", end="")
        elif(r-c<=n-1 and r+c<=2*n+2 and r>=n):
            print("*", end="")
        else:
            print(" ", end="")
    print()