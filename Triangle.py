def classify_triangle(a, b, c):
#the letters abc represent the three sides of a given triangle
#The goal of this function is to classify that given triangle into its type
#Types are

    triangle = str("Triangle Classification")

    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    if a == b == c:
        triangle = str("Equilateral triangle")
    elif a == b or b == c or a == c:
        triangle = str("Isosceles triangle")
    else:
        triangle = str("Scalene triangle")

    print("Triangle is classified as: " + triangle)


    #these if statements first check to see if all
    #sides are equal, then if two are, then if none are equal

classify_triangle(0,0,0)

