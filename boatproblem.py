#-------------------------------------------------------------------------------
# Name:        module5
# Purpose:
#
# Author:      S533628
#
# Created:     17/09/2019
# Copyright:   (c) S533628 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    diff()

def diff():
    l = []
    p,n = input().split()
    c = 0
    for i in range(int(n)):
        r = input()
        if r not in l:
            l.append(r)
        else:
            if len(l) < int(p):
                c += 1
    if len(l) >= int(p):
        print(len(l)+c)
    else:
        print("paradox avoided")






if __name__ == '__main__':
    main()
