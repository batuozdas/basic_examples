# In this example, we will find 3-sided or 4-sided shapes. We will get informations from the user about the shape. Then
# we will decide which shape it is.

# Firstly we create a function called geometry. We will send shape value to this function. This shape value will have 3 or 4 values.
def geometry(shape):
    if (len(shape) == 3):  # If length of a shape equal to 3, it is a triangle;
        a = shape[0]  # a side of a triangle.
        b = shape[1]  # b side of a triangle.
        c = shape[2]  # c side of a triangle.
        # There is a condition for triangles. The sum of two sides of a triangle must be bigger than the other side of a triangle.
        if a + b > c and a + c > b and b + c > a:  # If that condition is right. Then we can find the triangle type.
            if a == b == c:  # If all sides length are equal;
                print("It is an equilateral triangle.")
            elif a == b != c or a != b == c or a == c != b:
                print("It is an isosceles triangle.")
            else:
                print("It is a scalene triangle.")
        else:  # If triangle condition is not right;
            print("This cannot be a triangle. Please enter the values again.")
    if (len(shape) == 4):  # If length of a shape equal to 4;
        a = shape[0]  # a side (upside)
        b = shape[1]  # b side (downside)
        c = shape[2]  # c side (leftside)
        d = shape[3]  # d side (rightside)
        if a == b == c == d:  # If all sides are equal;
            print("It is a square.")
        elif a == b and c == d:  # If opposite sides are equal;
            print("It is a rectangular.")
        elif a != b != c != d:  # If sides are not equal;
            print("It is a trapezoid.")
        elif a != b and c == d:  # If up and down sides are not equal, but left and right sides are equal.
            print("It is a isosceles trapezoid.")
        else:
            print('Please enter the values again.')


# We create our function. Now we need to call it.
sides = ['a', 'b', 'c', 'd']
while (True):
    number_of_sides = int(input("Please enter the number of sides (It should be 3 or 4):"))
    if number_of_sides == 3 or number_of_sides == 4:
        sides_length = []  # We are creating empty series to fill later.
        for i in range(number_of_sides):  # If number_of_sides = 3 we will ask the user 3 times side length. If it is 4, then we will ask 4 times.
            print('If it is a 4-sided shape please enter the sides length according to this: a=Upside,b=downside,c=leftside,d=rightside\nbut if it is not 4-sided'
                  ' shape, please ignore this warning.') # Warning for user.
            side_length = int(input('Please enter the {} side length:'.format(sides[i])))
            sides_length.append(side_length)  # We will add the lengths to our sides_length series.
        geometry(sides_length)  # We will send sides_length series to our function called geometry.
    else:  # If number_of_sides value is different than 3 or 4;
        print("Number of sides should be 3 or 4.")