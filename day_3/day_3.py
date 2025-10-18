# Variables of different data types
age = 0
height = 0.0
complex_number = 0j
pi = 3.14

# Triangle calculation

# Area of a triangle
base = int(input("Enter base: "))
height = int(input("Enter height: "))
area_triangle = 0.5 * base * height
print("The area of the triangle is: ", area_triangle)

# Perimeter of a triangle
side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
perimeter_triangle = side_a + side_b + side_c
print("The perimeter of the triangle is: ", perimeter_triangle)

# Rectangle calculation

# Area of a rectangle
lenght = int(input("Enter lenght: "))
width = int(input("Enter width: "))
area_rectangle = lenght * width
# Perimeter of a rectangle
perimeter_rectangle = 2 * (lenght + width)
print("The area of the rectangle is: ", area_rectangle , "\nThe perimeter of the rectangle is: ", perimeter_rectangle)

# Circle calculation
# Area of a circle
radius = int(input("Enter radius: "))
area_circle = pi * radius **2
# Circumference of a circle
circumference_circle = 2 * pi * radius

# Calculate slope, x-intercept and y-intercept of y = 2x -2
# formula: y = mx + b

m = 2
b = -2

# 0 = mx+b -> x = -b/m
x_intercept = -b/m
print("Slope is: ",m)
print("The x-intercept is: ", x_intercept)

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1 , y1 = 2,2
x2, y2 = 6,10
m_euclidean = (y2 - y1) / (x2 - x1)
d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print("distance", d)

# Compare the slopes in tasks 8 and 9.
if m == m_euclidean:
    print("The slopes are equal.")
    
else:
    print("The slopes are not equal.")
x_zero = -3
y_zero = x_zero**2+6*x_zero+9
print("The value of y when x is -3: ", y_zero)

len("python") > len("dragon")

if("on" not in "python" and "on" not in "dragon"):
    print("The word 'on' is not found in both 'python' and 'dragon'")
value_py = float(len("python"))
convert_string = str(value_py)

print("Even number"if(int(input("Enter a even number: "))%2==0) else "Odd number")

if (7//3 == int(2.7)):
    print("7//3 is equal to 2.7")

'10' == 10
int('9.8') == 10

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input("Enter hours: "))
rate_hours = float(input("Enter rate per hour: "))
weekly_earnings = hours * rate_hours
print("Your weekly earning is: ", weekly_earnings)

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print("You have lived for ", seconds, " seconds.")

for i in range(1,6):
    print(i, i**2, i**3)
    