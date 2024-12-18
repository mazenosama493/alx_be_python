number=int(input("Enter the size of the pattern:"))
i= 1
while i<=number:
    for x in range(1,number+1):
        print("*", end="")
    print("\n")
    i+=1
