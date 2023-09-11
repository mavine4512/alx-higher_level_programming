#!/usr/bin/python3
'''A module containing a list subclass
'''



class MyList(list):
    '''A class that inherits from list
    '''
    def print_sorted(self):
        '''Prints this list in a sorted order.
        '''
        sorted_list = sorted(self)
        print(sorted_list)
