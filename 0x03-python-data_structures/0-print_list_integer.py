#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in my_list:
        print("{:d}".format(i))


list = [1, 2, 3, 4, 5]
print_list_integer(list)