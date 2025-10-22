# Declare an empty list
empty_list = list()
empty_list = []
print(empty_list)

# Declare a list with more than 5 items
list_with_items = [1,2,3,4,5]

# Find the length of your list
print(len(list_with_items))

# Get the first item, the middle item and the last item of the list
first_item = list_with_items[0]
print(first_item)
middle_item = list_with_items[(len(list_with_items)//2)]
print(middle_item)
last_item = list_with_items[-1]
print(last_item)

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Ralph Christian Gabriel", 21, 5.10, "Relationship", "123 Main St"]
print(mixed_data_types)

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print the list using print()
print(it_companies)

# Print the number of companies in the it_companies list
print(len(it_companies))

# Print the first, middle and last company
print(it_companies[0])
print(it_companies[len(it_companies)//2])
print(it_companies[-1])

# Print the list after modifying one of the companies
it_companies[0] = "Meta"
print(it_companies)

# Add an IT company to it_companies list
it_companies.append("Netflix")
print(it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2, "Tesla")
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print(it_companies)

# Join the it_companies with a string '#;  'separator
joined_companies = '#;  '.join(it_companies)
print(joined_companies)

# Check if a certain company exists in the it_companies list.
print("Apple" in it_companies)

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
print(it_companies[0:3])

# Slice out the last 3 companies from the list
print(it_companies[-3:1])

# Slice out the middle IT company or companies from the list
print(it_companies[len(it_companies)//2:])

# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# Remove the middle IT company or companies from the list
it_companies.pop(len(it_companies)//2)
print(it_companies)

# Remove the last IT company from the list
it_companies.pop(-1)
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
del it_companies

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joining_lists = front_end + back_end
print(joining_lists)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack.
full_stack = joining_lists.copy()
i = full_stack.index('Redux')
full_stack.insert(i+1, 'SQL')
full_stack.insert(i+1, 'Python')
print(full_stack)


# Exercice 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Trier la liste et trouver le min et le max
ages.sort()
print("Ages triés :", ages)
print("Âge minimum :", min(ages))
print("Âge maximum :", max(ages))

# Ajouter min et max à la liste
ages.append(min(ages))
ages.append(max(ages))

# Trouver la médiane
ages_sorted = sorted(ages)
m = len(ages_sorted)
if m % 2 == 0:
    median = (ages_sorted[m//2 - 1] + ages_sorted[m//2]) / 2
else:
    median = ages_sorted[m//2]
print("Médiane :", median)

# Moyenne
average_ages = sum(ages) / len(ages)
print("Moyenne :", average_ages)

# Étendue
age_range = max(ages) - min(ages)
print("Étendue :", age_range)

# Comparaison min/avg et max/avg
min_average = abs(min(ages) - average_ages)
max_average = abs(max(ages) - average_ages)
print("Écart min/moyenne :", min_average)
print("Écart max/moyenne :", max_average)


# Find the miidle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];
middle_index = len(countries) // 2
if len(countries) % 2 == 0:
    middle_countries = countries[middle_index - 1: middle_index + 1]

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
country_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first, second, third, *scandic_countries = country_list
print(first)
print(second)
print(third)
print(scandic_countries)









