#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    '''
    Prent integer of a list
    Parameters:
    my_list(list): The list containing the elemets to print
    x (int): The number of elements to print
    Returns:
    The actual number of elements printed
    '''
    num = 0
    for i in range(0, x):
        item = my_list[i]
        try:
            print("{:d}".format(item), end="")
            num += 1
        except (ValueError, TypeError):
           continue
    print("")
    return (num)

