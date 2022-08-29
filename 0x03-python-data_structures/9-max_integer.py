#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max_num = my_list[0]
        for a in my_list:
            if a > max_num:
                max_num = a
        return max_num
    else:
        return None
