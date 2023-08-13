#!/usr/bin/python3
def max_integer(my_list=[]):
    '''
    Find the biggest interger in a list of intergers

    Parameters:
    my_list (list): The list of intergers

    Return:
    maximum integer in the list otherwise None
    '''
    max_num = 0 if len(my_list) == 0 else my_list[0]
    for num in my_list:
        max_num = num if num >= max_num else max_num
    return None if len(my_list) == 0 else max_num
