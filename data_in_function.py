# data_in_functions.py
# Class example of how to put data into functions
# Rhiannon MacCreadie
# 10.03.2021


def print_something(s):
    """
    Setup one input and name it s
    """
    print(s)


def combine_animals(animal_1, animal_2):
    print(animal_1 + animal_2)

    
def call_print():
    print_something("Hello World")


if __name__ == "__main__":
    call_print()
    print_something(True)
    print_something(3.141592654)

    animals = ["Dog", "Horse", "Cat", "Bear", "Moose"]
    reptiles = ["Crocodiles", "Chameleon", "Komodo", "Frog", "Skink"]
    #for animal in animals:
    #    print_something(animal)
    for i in range(len(animals)):
        combine_animals(animals[i], reptiles[i])
