a = int(input("Enter a number: "))
print("Divisors of" ,a, "are:", end=" ")
for i in range(1, a ):
    if a % i == 0:
        print(i,end=" ")