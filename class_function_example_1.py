##
# class_function_example_1.py
# Class example of building with functions
# Author: Rhiannon MacCreadie
# Date: 09.03.2021


def chorus_1():
    """
    Prints out chorus of song
    """
    print("Gucci")
    chorus_2()


def chorus_2():
    """
    Prints second line of chorus
    """
    print("Gang")

# main routine
if __name__ == "__main__":
# calling functions
    for i in range(200):
        chorus_1()
        
