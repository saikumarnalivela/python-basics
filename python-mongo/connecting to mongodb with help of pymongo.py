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
import pymongo
def main():
    myclinet = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclinet.list_database_names()
    for i in mydb:
        print(i)

if __name__ == '__main__':
    main()
