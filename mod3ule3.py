#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      S533628
#
# Created:     05/11/2019
# Copyright:   (c) S533628 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------


if __name__ == '__main__':
    s = input()
    print(s.isalnum())
    for i in s:
        if i.isalpha():
            print('True')
            break
    for i in s:
        if i.isdigit():
            print('True')
            break
    for i in s:
        if i.islower():
            print('True')
            break
    for i in s:
        if i.isupper():
            print('True')
            break