##
# numtranslate.py
# Rhiannon MacCreadie
# 12/5/21
# Asks user for a number (1 - 10) and give te reo translation

def add(dictionary):
    """
    Add to dictionary.
    """
    while True:
        try:
            key = int(input("What is the number: "))
            break
        except:
            print("Not a valid number")
            

    value = input("What is the te reo translation: ")
    dictionary[key] = value

    return dictionary

# Modify from dictionary
def edit(dictionary):
    """
    Check if the key is in the dictionary
    then modify and return
    """
    # Force a valid answer from user
    while True:
        try:
            key = int(input("What is the number to modify: "))
        except:
            print("Not a valid number")
    # check if the key is in dictionary
    if key in dictionary:
        # Change value
        dictionary[key]  = input("Enter translation: ")
    else:
        print("That entry doesnt exist!")

    return dictionary
        


# Delete from dictionary
def delete(dictionary):
    """
    Ask 
    """
    # Force a valid answer from user
    while True:
        try:
            key = int(input("What is the number to modify: "))
        except:
            print("Not a valid number")

    # check if the key is in dictionary
    if key in dictionary:
        # delete value
        del dictionary[key]
    else:
        print("That entry doesnt exist!")

    return dictionary


# Prints all entrys
def print_all(dictionary):
    """
    Print 
"""
    for key, value in sorted(dictionary.items()):
        print(key, ":", value)


# Main
if __name__ == "__main__":
    # Define the dictionary
    translator = {}
    # Loop program till exit
    while True:
    # Print out menu
        print("""
Welcome to the te reo translator program
1. Add to the dictionary
2. Edit an entry to the dictionary
3. Delete an entry in the dictionary
4. Print all entrys in the dictionary
5. Exit Program""")

        choice = input("Enter option: ")

        if choice == "1":
            translator = add(translator)
        elif choice == "2":
            translator = edit(translator)
        elif choice == "3":
            translator = delete(translator)
        elif choice == "4":
            print_all(translator)
        elif choice == "5":
            break
        else:
            print("This option does not exist")

        print(translator)

    print("goodbye")
          
