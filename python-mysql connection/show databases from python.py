#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      S533628
#
# Created:     05/11/2019
# Copyright:   (c) S533628 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import mysql.connector
def main():
    connobj = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Sainalivela@1'
    )
    mycursor = connobj.cursor()
    mycursor.execute('show databases')
    for i in mycursor:
        print(i)
    connobj.close()

if __name__ == '__main__':
    main()
