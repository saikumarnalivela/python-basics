#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      S533628
#
# Created:     16/10/2019
# Copyright:   (c) S533628 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import time
import calendar
import notebook

def main():
    print(time.clock())
    print(time.time())
    print(calendar.calendar(2008))
    print(calendar.month(2019,11))
    print(time.gmtime())
    print(time.localtime())
    t = time.clock()
    sai()
    t2 = time.clock()
    print('time taken by sunction',t2-t)
    print("time localtime : ",time.localtime())
    print('time asctime',time.asctime())
    print('time gmtimee',time.gmtime())

    print('time of time',time.timezone)


    a = time.localtime()
    print(a[1])
    b = time.asctime()
    print(type(b))

    def alar():
        a = str(input('Please enter the time to set the remainder in the format HH:MM PM/AM'))
        print(type(a))
        b = a.split(':')
        h = b[0]
        c = b[1].split(' ')
        m = c[0]
        m2 = c[1]
        print(h,m,m2)




    print(notebook.__version__)
    print(notebook.DEFAULT_STATIC_FILES_PATH)




def sai():
    i = 0
    j = 2
    print(i + j)
    for i in range(2000000):
        #print(i)
        i = 0


if __name__ == '__main__':
    main()
