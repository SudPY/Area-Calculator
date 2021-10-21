def areaCalculator():
    _input_ = input("Enter the shape you want to calculate the area of : ")
    area = 0
    pi = 3.14

    if _input_ == "Square":
        side = int(input("Enter the value of side : "))
        area = area + (side ** 2)
    
    elif _input_ == "Circle":
        radius = int(input("Enter the value of radius : "))
        area = area + (pi * radius ** 2)
    
    elif _input_ == "Rectangle":
        length = int(input("Enter the value of length : "))
        breadth = int(input("Enter the value of breadth : "))
        area = area + (length * breadth)

    elif _input_ == "Triangle":
        base = int(input("Enter the base of the triangle : "))
        height = int(input("Enter the height of the triangle : "))
        area = area + (0.5 * base * height)
    
    else:
        print("Enter a valid shape")
    
    print("The area is : ", "%.2f" % area)

areaCalculator()
