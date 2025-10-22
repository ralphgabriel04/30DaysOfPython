# Create a empty tuple
empty_tuple = ()
empty_tuple_other_way = tuple()
print("Empty Tuple:", empty_tuple,"Other way: ", empty_tuple_other_way)

# Join brothers and sisters tuples -> siblings tuple
brothers_tuple = ("Shawnley","Matis","Aiman")
sisters_tuple = ("Melissa","Mahemie","Analie")
siblings_tuple = brothers_tuple + sisters_tuple
print("Siblings Tuple:", siblings_tuple)

# How many siblings do you have ?
siblings_tuple_length = len(sisters_tuple)
print("Number of sisters:", siblings_tuple_length)

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
father_name = ("Mario")
mother_name = ("Mirelene")
family_members_tuples = siblings_tuple + (father_name, mother_name)
print("Family Members Tuple:", family_members_tuples)

# Unpack siblings and parents from family_members
bro1, bro2, bro3, sis1, sis2, sis3, father, mother = family_members_tuples

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp
fruits_tuple = ("banana","orange", "mangue", "kiwi")
vegetables_tuple = ("carrot","broccoli","spinach","cauliflower")
animal_products_tuple = ("milk","meat","eggs","cheese")
food_stuff_tp = fruits_tuple + vegetables_tuple + animal_products_tuple
print("Food Stuff Tuple:", food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print("Food Stuff List:", food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list
middle_index = (len(food_stuff_tp) // 2)

# Slice out the first three items and the last three items from food_staff_lt list
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]
print("First three items:", first_three_items)
print("Last three items:", last_three_items)

# Delete the food_staff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Is Estonia' is a nordic country ?", 'Estonia' in nordic_countries, "Is 'Iceland' a nordic country ?", 'Iceland' in nordic_countries)






