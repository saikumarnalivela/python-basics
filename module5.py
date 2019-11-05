#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    genes = input().rstrip().split()

    health = list(map(int, input().rstrip().split()))

    s = int(input())
    l = []

    for s_itr in range(s):
        firstLastd = input().split()

        first = int(firstLastd[0])

        last = int(firstLastd[1])

        d = firstLastd[2]
        sum = 0

        for i in range(first,last+1):
            if genes[i] in d and d.count("genes[i]") <= 1:
                print("matching genes",genes[i] , "health ", health[i])
                sum += health[i]
                print("sum",sum)
            else:
                sum += health[i]* d.count(genes[i])
        l.append(sum)
    print(min(l),max(l))



