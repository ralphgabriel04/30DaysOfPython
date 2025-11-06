# Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [num for num in numbers if num<=0]
print(negative_and_zero)

# Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flattened_list = [num for sublist_2 in list_of_lists for sublist_1 in sublist_2 for num in sublist_1]

print(flattened_list)
# output
[1, 2, 3, 4, 5, 6, 7, 8, 9]

# Using list comprehension create the following list of tuples:

list_of_tuples = [(i,1,i**2,i**3,i**4,i**5) for i in range(11)]
print(list_of_tuples)

# Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

fomatted_countries = [[country[0].upper(), country[0][:3].upper(), country[1].upper()] for sublist in countries for country in sublist]
# output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
print(fomatted_countries)

# Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_countries = [{'country':country[0].upper(), 'city':country[1].upper()} for sublist in countries for country in sublist]
# output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]
print(dict_countries)

# Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [' '.join(name) for sublist in names for name in sublist]
# output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
print(full_names)

# Write a lambda function which can solve a slope or y-intercept of linear functions.

slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
print(slope(2, 3, 4, 7))  # Output: 2.0

