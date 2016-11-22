x = int(input("Give me the X coordinate: "))
y = int(input("Give me the Y coordinate: "))

if (x >= 0):
    if (y >= 0):
        print("1st Quadrant")
    else:
        print("4th Quadrant")
elif (y >= 0):
    print("2nd Quadrant")
else:
    print("3rd Quadrant")
