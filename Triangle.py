def classify_triangle(a,b,c):
#the letters abc represent the three sides of a given triangle
#The goal of this function is to classify that given triangle into its type
#Types are

    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")


    #these if statements first check to see if all
    #sides are equal, then if two are, then if none are equal

def main():
    classify_triangle(3,3,3)


if __name__ == "__main__":
    main()

