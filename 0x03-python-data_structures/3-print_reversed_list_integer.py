#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        for idx in my_list[::-1]:
            print("{:d}".format(idx))
"""
aletrnative solution:

def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    print(*my_list, sep="\n")"""
