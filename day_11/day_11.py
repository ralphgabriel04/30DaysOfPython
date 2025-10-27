import math
from collections import Counter
import keyword
# day_11/day_11.py
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # remonte d'un dossier (le projet)
sys.path.insert(0, str(ROOT))               # rends le root importable

from countries_data import countries_data   # variable définie dans countries_data.py

# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(one_number,two_number):
    return one_number + two_number
print(add_two_numbers(2,3))

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_circle(r):
    pi = 3.14
    return pi*r**2
print(area_circle(5))

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    invalid = [x for x in args
                    if isinstance(x,bool) or not isinstance(x,(int,float))
               ]
    if invalid:
        return f"Tous les arguments doivent être des nombres (int/float), pas des booléens/chaînes. Invalides: {invalid}"
    return sum(args)
print(add_all_nums(4,5,True,False))

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(c):
    f = (c*9/5) + 32
    return f
print(convert_celsius_to_fahrenheit(5))

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month in "september, october, november".lower():
        return "Autumn"
    elif month in "March, April, May".lower():
        return "Spring"
    elif month in "June, July, August".lower():
        return "Summer"
    elif month in "December, January, February".lower():
        return "Winter "
    return "Not a valid month"
print(check_season("August".lower()))

# Write a function called calculate_slope which return the slope of a linear equation
def slope(x1,y1,x2,y2):
    return (y2-y1) / (x2-x1)
print(slope(1,2,3,4))

# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a,b,c):
    d = b**2 - 4*a*c
    if d < 0:
        return()
    if d == 0:
        return (-b/ (2*a),)
    r = math.sqrt(d)
    return ((-b - r)/(2*a), (-b + r)/(2*a))
print(solve_quadratic_eqn(1,6,4))

# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list
def print_list(*args):
    for x in args:
        print(x)
print_list([1,2,3])

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(array):
    reverse_list = []
    for item in range(len(array)-1, -1, -1):
        reverse_list.append(array[item])
    return reverse_list
print(reverse_list([1,2,3]))

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(item):
   return [s.capitalize() for s in item]
print(capitalize_list_items(["allo","christian"]))

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(list_item,item):
    if item not in list_item:
        list_item.append(item)
    return list_item 
    
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))     # [2, 3, 7, 9, 5]

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def  remove_item(list_item,item):
    if item in list_item:
        list_item.remove(item)
    return list_item
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(number):
    total_number = 0
    for i in range(number +1):
        total_number += i
    return total_number
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(number):
    total_number = 0
    for i in range(number + 1):
        if(i % 2 == 1):
            total_number += i
    return total_number
print(sum_of_odds(5))

# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(positif_int):
    total_even_number = 0
    total_odd_number = 0
    if(positif_int >= 0): 
        for i in range (positif_int + 1):
            if(i % 2 == 0 and i >=0):
                total_even_number +=i
            if(i % 2 == 1 and i >=0):
                total_odd_number +=i
    else:
            return "Not a positif integer number"
    return f"The number of odds are {total_odd_number} and the number of evens are {total_even_number}"
print(evens_and_odds(5))
# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(number):
    total = 1
    for k in range(2,number +1):
        total *=k
    return total
print(factorial(0))  # 1
print(factorial(1))  # 1
print(factorial(5))  # 120

# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(value):
    return not bool(value)
print(is_empty([]))        # True
print(is_empty("hello"))   # False
print(is_empty(0))         # True
print(is_empty(None))      # True

# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(data):
    return sum(data) / len(data)
def calculate_median(data):
    data_sorted = sorted(data)
    number_data = len(data)
    middle = number_data // 2
    return data_sorted[middle] if number_data % 2 else (data_sorted[middle - 1] + data_sorted[middle]) / 2
def calculate_mode(data):
    counts = Counter(data)
    max_freq = max(counts.values())
    return [val for val, freq in counts.items() if freq == max_freq]
def calculate_range(data):
    return max(data) - min(data)
def calculate_variance(data, ddof=0):
    number_data = len(data)
    if number_data <=0:
        raise ValueError("ddof must be less than the number of data points.")
    m = calculate_mean(data)
    return sum((x - m) ** 2 for x in data) / (number_data - ddof)
def calculate_std(data, ddof=0):
    return math.sqrt(calculate_variance(data, ddof=ddof))
nums = [1, 2, 2, 3, 4]
print("mean:", calculate_mean(nums))                 # 2.4
print("median:", calculate_median(nums))             # 2
print("mode:", calculate_mode(nums))                 # [2]
print("range:", calculate_range(nums))               # 3
print("variance (pop):", calculate_variance(nums))   # 1.04
print("std (pop):", calculate_std(nums))             # 1.019803902718557

# sample versions
print("variance (sample):", calculate_variance(nums, ddof=1))
print("std (sample):", calculate_std(nums, ddof=1))

# Write a function called is_prime, which checks if a number is prime.
def is_prime(number):
    """
    Return True if n is a prime number, else False.

    Rules:
      - Only integers are allowed.
      - Primes are >= 2.
      - Uses sqrt(n) bound and 6k ± 1 optimization for speed.
    """
    if not isinstance(number, int):
        raise TypeError("is_prime() expects an integer")
    if number < 2:
        return False
    if number in (2, 3):
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    # Check factors of the form 6k ± 1 up to sqrt(n)
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True
# Examples
print(is_prime(1))    # False
print(is_prime(2))    # True
print(is_prime(17))   # True
print(is_prime(100))  # False

# Write a functions which checks if all items are unique in the list.
def all_unique(item):
    seen = []
    for x in item:
        if x in seen:
            return False
        seen.append(x)
    return True
print(all_unique([1, 2, 3]))                # True
print(all_unique([1, 2, 2]))                # False
print(all_unique(["a", "b", "A"]))          # True
print(all_unique([[1,2], [1,2]]))           # False (lists are equal)

# Write a function which checks if all the items of the list are of the same data type.
def all_same_type(item):
    if not item:
        return True
    first_type = type(item[0])
    return all(type(x) == first_type for x in item)
# Examples
print(all_same_type([1, 2, 3]))          # True
print(all_same_type([1, 2.0, 3]))        # False
print(all_same_type(["a", "b"]))         # True
print(all_same_type([]))                 # True

# Write a function which check if provided variable is a valid python variable
def is_valid_variable(name):
    if not isinstance(name, str):
        return False
    return name.isidentifier() and not keyword.iskeyword(name)
print(is_valid_variable("x"))          # True
print(is_valid_variable("_value"))     # True
print(is_valid_variable("café"))       # True
print(is_valid_variable("2cats"))      # False (starts with digit)
print(is_valid_variable("for"))        # False (keyword)
print(is_valid_variable("user-name"))  # False (hyphen not allowed)

# Go to the data folder and access the countries-data.py file.
def most_spoken_languages(data, number=10):
    counter = Counter()
    for country in data:
        for lang in country.get("language",[]):
            counter[lang] +=1
    return [{"language": lang, "count":count}
                for lang, count in counter.most_common(number)
            ]
def most_populated_countries(data, n=10):
    sorted_country = sorted(data, key=lambda c:c.get("population", 0), reverse=True)
    top_value = sorted_country[:n]
    return [{"name" : country.get("name"), "population" : country.get("population",0)} for country in top_value]

# exemples
print(most_spoken_languages(countries_data, 10))
print(most_populated_countries(countries_data, 10))