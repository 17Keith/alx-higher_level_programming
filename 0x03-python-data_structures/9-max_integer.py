#!/usr/bin/python3

def max_integer(my_list=[]):

    return (sorted(my_list)[-1] if (my_list and len(my_list)) else None)
