##
# dictionaries_intro.py
# Rhiannon MacCreadie
# 05/05/21
# Class Notes on creating a dictionary


# Creating
country_foods = {"Japan" : "Sushi", "France":"Croissants", "New Zealand":"Mince Pies",
                 "Australia":"Kangaroo", "USA":"Fast Food"}

country_population = {"Italy":60674003, "China":1398000000, "India":1366000000,
                      "New Zealand":4971000}

# Zipping (Mapping)two parrallel lists a dictionary
burgers = ["Whopper", "Bk Chicken", "Hawaiian Chicken", "Rodeo", "Boss"]
prices = [5.95, 5.84, 6.84, 7.75, 9.95]
burgers_price = dict(zip(burgers,prices))
print(burgers_price)

# Acessing a key that doesn't exist
# Adding a try and except to catch an error
try:
    print(country_foods["Germany"])
except KeyError:
    print("This country does not exist!")
# Using get
print(burgers_price.get("Boss"))
print(burgers_price.get("whopper", "Does not exist."))

##
# Traversing a dictionary using For each
# Print the key of each item in dictionary
for country in country_foods:
    print(country)
    print(country_foods[country]) # prints value

# Using items() method
for key, value in country_population.items():
    print(key, ":", value)

