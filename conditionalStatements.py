#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    if(N % 2 != 0):
        print('Weird');
    elif(N % 2 == 0 and N in range(2, 5)):
        print('Not Weird');
    elif(N % 20 != 0 and N in range(6, 20)):
        print('Weird');
    elif(N % 2 == 0 and N > 20):
        print('Not Weird');
    else:
        print('Weird')
