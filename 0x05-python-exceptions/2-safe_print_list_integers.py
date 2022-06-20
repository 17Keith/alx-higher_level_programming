#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    
    i = 0
    count = 0
    while i < 0:
            try:
                print("{:d}".format(my_list[i]), end='')
                print()
                return count
            except (IndexError):
                pass
            else:
                count += 1
            finally:
                i += 1
            print()
            return count
