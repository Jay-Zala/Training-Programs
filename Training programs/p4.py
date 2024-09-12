x = int(input("Enter x-coordinate: "))
y = int(input("Enter y-coordinate: "))

if x > 0 and y > 0:
    print("The point is in the first quadrant")
elif x < 0 and y > 0:
    print("The point is in the second quadrant")
elif x < 0 and y < 0:
    print("The point is in the third quadrant")
elif x > 0 and y < 0:
    print("The point is in the fourth quadrant")
else:
    print("The point is on the axis")