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
    passwd = 'Sainalivela@1',
    database = 'pets'
    )
    mycursor = connobj.cursor()
    try:
        mycursor.execute('CREATE TABLE ANIMAL (NAME VARCHAR(255),PLACE VARCHAR(255) )')
    except:
        print('error in creating the table')
    connobj.close()

if __name__ == '__main__':
    main()
