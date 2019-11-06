#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      S533628
#
# Created:     05/11/2019
# Copyright:   (c) S533628 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import MySQLdb

def main():

    db = MySQLdb.connect(host='localhost',
                         user='root',
                         passwd='Sainalivela@1',
                         db='testdb')

    cur = db.cursor()

    cur.execute('SELECT * FROM testdb.customers')

    for row in cur.fetchall():
        print(row)

    db.close()

if __name__ == '__main__':
    main()
