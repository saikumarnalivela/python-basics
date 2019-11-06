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
    obj = mysql.connector.connect(host= 'localhost',
    user = 'root',
    passwd = 'Sainalivela@1',
    database = 'testdb'
    )
    mycursor = obj.cursor()
    mycursor.execute('create table animal2s(name varchar(23),age int(2))')





if __name__ == '__main__':
    main()
