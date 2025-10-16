# Exercice : level 1
first_name = "Ralph Christian"
last_name = "Gabriel"
full_name = first_name +" "+ last_name
country = "Haiti"
city = "Port-au-Prince"
age = 21
year = 2004
is_married = False
is_true = True
is_light_on = is_true
skills, school, address = "Python", "ETS", "123 Street"

# Exercice : level 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(skills))
print(type(school))
print(type(address))
print("The length of my first name is:"+str(len(first_name)))
print("The length of my last name is:"+str(len(last_name)))

# Operations
num_one, num_two = 5,4
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
division = num_one / num_two
reminder = num_one % num_two
exp = num_one ** num_two 
floor_division = num_one // num_two

# Circle calculations
radius = 30
radius = int(input("Give me are radius of a circle: "))
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
full_name = first_name +" "+ last_name
country = input("What country do you live in? ")
age = input("How old are you? ")
pi = 3.14
area_of_circle = pi * radius ** 2
circum_of_circle = 2 * pi * radius
print(f"Hello {full_name}the area of a circle with radius "+str(radius)+" is: "+str(area_of_circle)+" and the circumference is: "+str(circum_of_circle))
