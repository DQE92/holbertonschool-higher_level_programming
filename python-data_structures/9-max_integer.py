#!/usr/bin/python3
"""_summary_ : function to get the biggest number 
"""
def max_integer(my_list=[]):
    if my_list == 0:
        return None
    else :
        my_list.sort(reverse=True)
        return my_list[0]
