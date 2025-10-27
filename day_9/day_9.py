# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
user_input = int(input("Enter your age: "))
if user_input >= 18:
    print("You are old enough to drive.")
else:
    years_to_wait = 18 - user_input
    print(f"You need to wait for {years_to_wait} more years to drive.")
    
# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

my_age = 22
your_age = int(input("Enter your age: "))
if my_age > your_age:
    age_diff = my_age - your_age
    if age_diff == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {age_diff} years older than you.")
elif your_age > my_age:
    age_diff = your_age - my_age
    if age_diff == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {age_diff} years older than me.")
else:
    print("We are the same age.")
    
# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
if a > b:
    print("a is greater than b.")
elif a < b:
    print("a is smaller than b.")
else:
    print("a is equal to b.")
    
# Write a code which gives grade to students according to theirs scores
score = int(input("Enter your score (0-100): "))
if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
elif 50 <= score < 60:
    grade = 'E'
elif 0 <= score < 50:
    grade = 'F'
else:
    grade = 'Invalid score'
    
print(f"Your grade is: {grade}")

# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

month = input("Enter the month: ").strip().lower()
if month in ['september', 'october', 'november']:
    season = 'Autumn'
elif month in ['december', 'january', 'february']:
    season = 'Winter'
elif month in ['march', 'april', 'may']:
    season = 'Spring'
elif month in ['june', 'july', 'august']:
    season = 'Summer'
else:
    season = 'Invalid month'
print(f"The season is: {season}")

# The following list contains some fruits: If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_to_check = input("Enter a fruit name: ").strip().lower()
if fruit_to_check in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(fruit_to_check)
    print("Modified fruit list:", fruits)

# Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

"""
 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:
"""
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print("Middle skill:", skills[middle_index])
    
    has_python = 'Python' in skills
    print("Has Python skill:", has_python)
    
    if set(skills) == {'JavaScript', 'React'}:
        print("He is a front end developer")
    elif set(['Node', 'Python', 'MongoDB']).issubset(skills):
        print("He is a backend developer")
    elif set(['React', 'Node', 'MongoDB']).issubset(skills):
        print("He is a fullstack developer")
    else:
        print("Unknown title")
if person.get('is_marred') and person.get('country') == 'Finland':
    full_name = f"{person.get('first_name')} {person.get('last_name')}"
    print(f"{full_name} lives in {person.get('country')}.")