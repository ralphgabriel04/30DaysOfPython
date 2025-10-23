# Create an empty dictionary called dog
dog = {}
print("Empty Dog Dictionary:", dog)

# Add name, color, breed, legs, age to the dog dictionary
dog = {
    'name' : 'Dopman',
    'breed' : 'Bulldog',
    'color' : 'Brown',
}

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name' : 'Ralph Christian',
    'last_name' : 'Gabriel',
    'gender' : 'Male',
    'age' : 22,
    'martial status' : 'Single',
    'skills' : ['HTML', 'CSS', 'JavaScript', 'Python'],
    'country' : 'Haiti',
    'city' : 'Port-au-Prince',
    'address' : 'Delmas 32'
}

# Get the length of the student dictionary
print("Length of student dictionary:", len(student))

# Get the value of skills and check the data type, it should be a list
value_skills = student.values()
print("Skills:", value_skills)
print("Data type of skills:", type(student['skills']))

# Modify the skills values by adding one or two skills
student['skills'].append('Django')

# Get the dictionary keys as a list
student_keys = list(student.keys())
print("Student Dictionary Keys:", student_keys)

# Get the dictionary values as a list
student_values = list(student.values())

# Change the dictionary to a list of tuples using items() method
student_items = list(student.items())

# Delete one of the items in the dictionary
del student['address']
print("After deleting address:", student)

# Delete one of the dictionaries
del dog


