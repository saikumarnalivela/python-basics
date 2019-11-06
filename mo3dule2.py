#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      S533628
#
# Created:     04/11/2019
# Copyright:   (c) S533628 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def mutate_string(string, position, character):
    s = list(string)
    print(s)
    s[position] = character
    s1 = ''.join(s)
    return str(s1)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
