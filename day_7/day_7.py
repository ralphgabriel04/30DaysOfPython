# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
print("Length of it_companies:", len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("After adding Twitter:", it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update(['LinkedIn', 'Snapchat', 'Reddit'])
print("After adding multiple companies:", it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove('IBM')
print("After removing IBM:", it_companies)

# What is the difference between remove and discard
# remove() will raise a KeyError if the element is not found in the set
# discard() will not raise an error if the element is not found in the set
it_companies.discard('NonExistentCompany')

# Join A and B
print("Union of A and B:", A.union(B))

# Find A intersection B
print("Intersection of A and B:", A.intersection(B))

# Is A subset of B
print("Is A subset of B?", A.issubset(B))

# Are A and B disjoint sets
print("Are A and B disjoint?", A.isdisjoint(B))

# Join A with B and B with A
print("A union B:", A.union(B), "B union A:", B.union(A))

# What is the symmetric difference between A and B
print("Symmetric difference between A and B:", A.symmetric_difference(B))

# Delete the sets completely
del A
del B
del it_companies

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print("Length of age list:", len(age), "Length of age set:", len(age_set))

# Explain the difference between the following data types: string, list, tuple and set

# A string is a sequence of characters enclosed in quotes. It is immutable.
# A list is an ordered collection of items that can be of different types. It is mutable
# A tuple is similar to a list but is immutable, meaning its contents cannot be changed after creation.
# A set is an unordered collection of unique items. It is mutable but does not allow duplicate values.

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)
print("Number of unique words:", len(unique_words), "Unique words:", unique_words)

