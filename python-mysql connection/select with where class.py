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
        sql = "select * from animal where place = 'warangal' "
        mycursor.execute(sql)
    except:
        print('error in creating the table')
    print("displaying the records of the table")
    #print(mycursor.fetchall())


    for i in mycursor:
        print(i)
    #print(mycursor.fetchall())
    #print(mycursor)
    connobj.close()

if __name__ == '__main__':
    main()
