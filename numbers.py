#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      S533628
#
# Created:     11/09/2019
# Copyright:   (c) S533628 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math as m

def main():

    re = fun(8000,[[1,2000],[2,4000],[3,2000]],[[1,2000],[2,4000],[3,3000]])
    print("Final rezult of the : ================" , re)



def fun(value, forlist,returnlist):
    list = []
    list1 = []
    k = 0
    for i in forlist:
        for j in returnlist:
            sum = 0

            print("accessing 2 element in the list:", i[1],j[1])
            sum += i[1] + j[1]
            if sum <= value:
                print("sum :",sum)
                print("i[0]:   ",i[0])
                print("j[0]:   ",j[0])
                print("list",list)
                print("list1",list1)
                list.append(i[0])
                list.append(j[0])
                list1.append(list)
                print("list1",list1)
    return list1
















if __name__ == '__main__':
    main()
