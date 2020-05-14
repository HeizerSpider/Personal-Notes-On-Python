#!/bin/python3

#This code aims to convert an input number to binary form and then count the max number of consecutive 1's
import math
import os
import random
import re
import sys

def converter(n):
    result=""
    while(n>=1):
        bin = n%2
        n = n//2
        result += str(bin)
    return result

def con(num):
    counter = 0
    largest = 0
    for i in num:
        if(int(i)==1):
            counter += 1
            if(counter>largest):
                largest = counter 
        else:
            counter = 0
    print(largest)

if __name__ == '__main__':
    n = int(input())
    binary = converter(n)
    con(binary)