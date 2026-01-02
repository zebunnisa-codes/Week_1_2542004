from area_calculations import *
print("Program begins....... ", "\n")

#Circle
print("To calculate area of circle.........")
r = float(input("Enter radius of circle : "))
print("Area of circle is ", area_of_circle(r), "\n")

#Triangle 
print("To calculate area of triangle.........")
b=float(input("Enter base of triangle : "))
h=float(input("Enter height of triangle : "))
print("Area of Triangle is ", area_of_triangle(b, h), "\n")

#Square
print("To calculate area of square.........")
s = float(input("Enter side of square : " ))
print("Area of Square is ", area_of_square(s), "\n")

#Rectangle
print("To calculate area of rectangle.........")
l = float(input("Enter length of rectangle : " ))
w = float(input("Enter width of rectangle : " ))
print("Area of Rectangle is ", area_of_rectangle(l, w), "\n")

print("Program ends....... ", "\n")


