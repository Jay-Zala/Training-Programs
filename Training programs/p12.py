n = int(input("Enter the number:"))
a = 1
for i in range (1,n+1):
    print(i,end="")
    if i < n:
        print("*")
    a=a*i

print("\nfactorial=",a)