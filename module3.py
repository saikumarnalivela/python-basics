#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      S533628
#
# Created:     16/09/2019
# Copyright:   (c) S533628 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    print(timeConversion("12:45:54PM"))
    s = "aasdasdasdasd"
    for i in range(len(s)-1):
        if s[i]
    print(s)

def timeConversion(s):
    r = s.split(":")
    if r[2][2] == "P":
        r1 =  12 + int(r[0])
    elif r[2][2] == "A":
        if int(r[0]) == 12:
            r1 = "00"
        else:
            r1 = r[0]

    t = r[2]

    return str(r1)+":"+r[1]+":"+t[0:2]




if __name__ == '__main__':
    main()
