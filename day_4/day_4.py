# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
first_word = "Thristy"
second_word = "Days"
third_word = "Of"
fourth_word = "Python"
full_sentence = first_word + " " + second_word + " " + third_word + " " + fourth_word
print(full_sentence)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
first_part = "Coding"
second_part = "For"
third_part = "All"
full_phrase = first_part + " " + second_part + " " + third_part
print(full_phrase)

# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# Print the variable company using print().
print(company)

# Print the length of the company string using len() method and print().
print(len(company))

# Change all the characters to uppercase letters using upper() method.
print(company.upper())

# Change all the characters to lowercase letters using lower() method.
print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Cut(slice) out the first word of Coding For All string.
print(company[0:6])

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index("Coding"))

# Replace the word coding in the string 'Coding For All' to Python.
new_copany = "Python For Everyone"
new_word = new_copany.replace("Everyone", "All")

# Split the string 'Coding For All' using space as the separator (split()) .
split_company = company.split(" ")

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", ")

# What is the character at index 0 in the string Coding For All.
print(company[0])

# What is the last index of the string Coding For All.
print(company[-1])

# What character is at index 10 in "Coding For All" string.
print(company[10])

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
phrase = 'Python For Everyone'.split()
acronym = ''.join(word[0] for word in phrase)

# Create an acronym or an abbreviation for the name 'Coding For All'.
phrase2 = 'Coding For All'.split()
acronym2 = ''.join(word[0] for word in phrase2)

# Use index to determine the position of the first occurrence of C in Coding For All.
index_c = company.index("C")
print(index_c)

# Use index to determine the position of the first occurrence of F in Coding For All.
index_f = company.index("F")
print(index_f)

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
last_index_l = "Coding For All People".rfind("l")
print(last_index_l)

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
index_because = sentence.index("because")
print(index_because)

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction
slicde_phrase_because = sentence[31:54]
print(slicde_phrase_because)

# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
first_occurence_because = sentence.find("because")
print(first_occurence_because)

# Does ''Coding For All' start with a substring Coding?
print("Coding For All".startswith("Coding"))

# Does 'Coding For All' end with a substring coding?
print("Coding For All".endswith("coding"))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print('   Coding For All      '.strip)

# Which one of the following variables return True when we use the method isidentifier():
print("30DaysOfPython".isidentifier(), "thirty_days_of_python".isidentifier())

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_librairies = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = ' # '.join(python_librairies)

# Use the new line escape sequence to separate the following sentences.
print("I am enjoying this challenge.\nI just wonder what is next.")

# Use a tab escape sequence to write the following lines.
print(f"{"Name":<10}{"Age":<5}{"Country":<10}{"City":<10}\n{'Asabeneh':<10}{250:<5}{'Finland':<10}{'Helsinki':<10}")

# Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square".format(radius,area))

# Make the following using string formatting methods:
print("{} + {} = {}".format(8,6,8+6))
print("{} + {} = {}".format(8,6,8-6))
print("{} + {} = {}".format(8,6,8*6))
print("{} + {} = {}".format(8,6,8/6))
print("{} + {} = {}".format(8,6,8%6))
print("{} + {} = {}".format(8,6,8//6))
print("{} + {} = {}".format(8,6,8**6))
