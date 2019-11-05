#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      S533628
#
# Created:     15/09/2019
# Copyright:   (c) S533628 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    list = [1,2,4,5]
    print("list: ",list)
    list1 = ['sai','seshu']
    print("list1 : ",list1)

    list1.append(list)
    print("list1: ",list1)
    list.append(6)
    print("list1: ",list1)
    list.append(7)
    print("list1: ",list1)



if __name__ == '__main__':
    main()
