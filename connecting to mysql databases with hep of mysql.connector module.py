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
#Install the mysql.connector modeule into the python path
#Pip install mysql.connector
import mysql.connector
def main():

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Sainalivela@1"
    )

    print(mydb)
    mycursor = mydb.cursor()
    #mycursor.execute("CREATE DATABASE mydatabase")
    mycursor.execute('show databases')
    for i in mycursor:
        print(i)
    mydb.close()

if __name__ == '__main__':
    main()
