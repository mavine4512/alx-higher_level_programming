#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    '''
    Print x element of a list.
    Parameters:
    my_list: the array of elemets
    x: number of elemets
    Returns
    Number of elemets
    '''
    try:
        k = 0
        for i in range(x):
            print("{}".format(my_list=[i]), end="")
            k += 1
    except IndexError:
        pass
    finally:
        print("")
        return k
