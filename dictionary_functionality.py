##
# dictionary_functionality.py
# Rhiannon MacCreadie
# 12/5/2021
# Class Demonstration to show modifying a dictionary


country_foods = {"New Zealand":"Pies", "Germany":"Schnitzel", "Australia":"Prawns on the barbie",
                 "Japan":"Sushi", "China":"Dumplings", "USA":"Fast Food"}
# Adding an item to the dictionary
country_foods["Canada"] = "Maple Syrup"
# Modifying an item in the dictionary
country_foods["Japan"] = "Ramen"
# Adding a key in the dictionary with no value
country_foods["Brazil"] = None

# Adding multiple items in a dictionary
country_foods.update({"Turkey":"Turkey", "France":"Frogs", "Scotland":"Haggis"})

print(country_foods)

# Modify multiple items in the dictionary
country_foods.update({"France":"Escargo", "Brazil":"Moqueca"})

##
# Sort the dictionary in alphabetical order of keys
print(sorted(country_foods))
# With key and values
for country, food in sorted(country_foods.items()):
    print(country, ":", food)
    

## DELETING FROM A DICTIONARY
del country_foods["France"]
print(country_foods)

# Deletes whole list
# del country_foods

# Removing and returning values
print(country_foods.pop("Australia"))

# Adding a parameter to pop so it doesnt key error
print(country_foods.pop("Australia",None))

# Remove all contents in dictionary
country_foods.clear()
print(country_foods)




