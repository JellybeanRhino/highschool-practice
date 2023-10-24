##
# multidimensional_list.py
# Class demonstration of multidimensional lists
# Rhiannon MacCreadie
# 31/03/21

def maccas():
    """
    """
    list_of_stuff =[["Big Mac", 3.50], ["Fries", 1.50, 2.00, 2.50], ["Chicken Nuggets", .50, 3]]

    # loop through outer list
    for i in range(len(list_of_stuff)):
        for j in range(len(list_of_stuff[i])):
            print(list_of_stuff[i][j])

    # printing the list of stuff using an enhanced for loop
    for thing in list_of_stuff:
        for item in thing:
            print(item)


def two_d_list():
    """
    Fills in 2d list using counter
    """
    # Populating 2d list
    x_list = []
    count = 0
    for i in range(2):
        y_list = []
        x_list.append(y_list)
        for j in range(2):
            y_list.append(count)
            count += 1
    # Call the pretty_print() with the list
   
    return x_list

def pretty_print(list_of_things):
    """
    Prints out a list of things nicely
    """
            
    for thing in list_of_things:
        print(thing)

def pretty_print_trans(list_of_things):
    """
    Prints out the list transposed
    """
    for i in range(len(list_of_things)):
        for j in range(len(list_of_things[i])):
            print(list_of_things[j][i], end = " ")
        print()

# Main routine

if __name__ == "__main__":
    # Fill the list
    list_1 = two_d_list()

    #Call the pretty function with list
    pretty_print(list_1)
    pretty_print_trans(list_1)
