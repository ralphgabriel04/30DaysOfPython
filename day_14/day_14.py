# Explain the difference between map, filter, and reduce.
# Map, filter, and reduce are three fundamental functions in functional programming that operate on collections of data, such as lists or arrays.
# 1. Map:
#    - Purpose: The map function is used to apply a specific function to each item in a collection and return a new collection containing the results.
#    - Example: If you have a list of numbers and you want to square each number, you would use map.
#    - Syntax: map(function, iterable)  
# 2. Filter:
#    - Purpose: The filter function is used to create a new collection containing only the items that meet a certain condition defined by a function.
#    - Example: If you have a list of numbers and you want to keep only the even numbers, you would use filter.
#    - Syntax: filter(function, iterable)
# 3. Reduce:
#    - Purpose: The reduce function is used to apply a binary function cumulatively to the items of a collection, reducing the collection to a single value.
#    - Example: If you have a list of numbers and you want to calculate the sum of all the numbers, you would use reduce.
#    - Syntax: reduce(function, iterable) (Note: In Python, reduce is available in the functools module: from functools import reduce)


# Explain the difference between higher order function, closure and decorator
# Higher Order Function:
# A higher-order function is a function that either takes one or more functions as arguments or returns a function as its result. Higher-order functions allow for functional programming techniques, enabling functions to be treated as first-class citizens.
# Closure:
# A closure is a nested function that captures the lexical scope in which it was created. This means that the inner function has access to variables from the outer function even after the outer function has finished executing. Closures are often used to create function factories or to maintain state.
# Decorator:
# A decorator is a special type of higher-order function that takes another function as an argument, extends or modifies its behavior, and returns a new function. Decorators are commonly used for logging, access control, memoization, and other cross-cutting concerns in code.

# Define a call function before map, filter or reduce, see examples.
from functools import reduce
def square(x):
    return x*x;
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square,numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

def is_even(x):
    if x % 2 == 0:
        return True
    return False
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4]
def add(x,y):
    return x + y
sum = reduce(add,numbers)
print(sum)  # Output: 15

# Use for loop to print each country in the countries list.
countries = ['Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
for country in countries:
    print(country)
# Use for to print each name in the names list.
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
for name in names:
    print(name)
# Use for to print each number in the numbers list.
for number in numbers:
    print(number)
# Use map to create a new list by changing each country to uppercase in the countries list
uppercased_countries = list(map(lambda country: country.upper(), countries))

# Use map to create a new list by changing each number to its square in the numbers list
squared_numbers_map = list(map(lambda number : square(number), numbers))

# Use map to change each name to uppercase in the names list
uppercased_named = list(map(lambda name: name.upper(), names))

# Use filter to filter out countries containing 'land'.

countries_with_land = list(filter(lambda country : "land" in country, countries))
# Use filter to filter out countries having exactly six characters.
six_char_countries = list(filter(lambda country: len(country) == 6, countries))
# Use filter to filter out countries containing six letters and more in the country list.
six_letters_more_countries = list(filter(lambda country: len(country) >= 6, countries))
# Use filter to filter out countries starting with 'E';
e_countries = list(filter(lambda country: country.startswith('E'), countries))

# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
result = reduce(lambda acc, country: acc + len(country),
                filter(lambda country: len(country) >= 6,
                       map(lambda country: country.upper(), countries)), 0)
# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(input_list):
    return list(filter(lambda item: isinstance(item, str), input_list))

# Use reduce to sum all the numbers in the numbers list.
total_sum = reduce(lambda acc, number: acc + number, numbers, 0)

# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
sentence = reduce(lambda acc, country: acc + ", " + country, countries[:-1], "") + ", and " + countries[-1] + " are north European countries"

# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
def categorize_countries(pattern):
    return list(filter(lambda country: pattern in country, countries))

# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter
def country_starting_letter_count():
    starting_letter_count = {}
    for country in countries:
        first_letter = country[0]
        if first_letter in starting_letter_count:
            starting_letter_count[first_letter] += 1
        else:
            starting_letter_count[first_letter] = 1
    return starting_letter_count
# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries():
    return countries[:10]

# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries():
    return countries[-10:]

# Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
# Sort countries by name, by capital, by population
# Sort out the ten most spoken languages by location.
# Sort out the ten most populated countries.
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from countries_data import countries_data

# Sort countries by name
sorted_by_name = sorted(countries_data, key=lambda country: country['name'])
# Sort countries by capital
sorted_by_capital = sorted(countries_data, key=lambda country: country['capital'])
# Sort countries by population
sorted_by_population = sorted(countries_data, key=lambda country: country['population'], reverse=True)