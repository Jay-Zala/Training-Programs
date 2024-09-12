year = int(input("Enter a year after 2000: "))
if year > 2000:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
else:
    print("Please enter a year after 2000")
