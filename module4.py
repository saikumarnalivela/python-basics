#-------------------------------------------------------------------------------
# Name:        module4
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

    print("Please enter the number of parts of boat")
    p = int(input())
    print("Please enter the days ")
    n = int(input())
    for i in range(n):
        l.append(input())
    for i in range(len(l)-1):
        for j in range(i+1,len(l)-1):
            if l[i] == l[j]:
                l.remove(l[j])
    print(l)
    if len(l) >= p:
        print(len(l))
    else:
        print("parabox avoided")








if __name__ == '__main__':
    main()
