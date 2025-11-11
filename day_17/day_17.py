names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
# Unpack the first five countries and store them in a variable nordic_countries | Store Estonia and Russia in es, and ru respectively
*nordic_countries, ic,es, ru = names
print("Nordic Countries:", nordic_countries)
print("Iceland:", ic)
print("Estonia:", es)
print("Russia:", ru)