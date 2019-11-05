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
    s = input()
    if s[-1] == "s" and s[-2] == "s":
        print("hiss")
    else:
        print("no hiss")

if __name__ == '__main__':
    main()
