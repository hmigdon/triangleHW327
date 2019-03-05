def classify_triangle(side_a, side_b, side_c):
    # the letters abc represent the three sides of a given triangle
    # The goal of this function is to classify that given triangle into its type
    # Types are
    triangle = str("Triangle Classification")
    side_a = int(input("a: "))
    side_b = int(input("b: "))
    side_c = int(input("c: "))
    if side_a == side_b == side_c:
        triangle = str("Equilateral triangle")
    elif side_a == side_b or side_b == side_c or side_a == side_c:
        triangle = str("Isosceles triangle")
    else:
        triangle = str("Scalene triangle")
    print("Triangle is classified as: " + triangle)


classify_triangle(0, 0, 0)

