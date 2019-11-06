#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      S533628
#
# Created:     06/11/2019
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
        SQL = 'INSERT INTO ANIMAL(NAME , PLACE) VALUES (%s,%s)'
        VALUES = [
        ('DOG2','hyd'),
        ('cat','karimnagar'),
        ('tiger','warangal'),
        ('elephant','shivangar'),
        ('leopard','sec')
        ]
        mycursor.executemany(SQL,VALUES)
        connobj.commit()
    except:
        print('error in inserting the table')
    connobj.close()

if __name__ == '__main__':
    main()
