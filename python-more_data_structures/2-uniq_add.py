#!/usr/bin/python3
def uniq_add(my_list=[]):
    i = set()
    for num in my_list:
        i.add(num)
    return sum(i)