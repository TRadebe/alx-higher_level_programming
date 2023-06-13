#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mul_2 = [True if (i % 2) == 0 else False for i in my_list]
    return mul_2
