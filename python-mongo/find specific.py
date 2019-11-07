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
    print(myclinet)
    print(myclinet.list_database_names())
    mydb = myclinet["saidb"]
    print(mydb)
    mycollection = mydb["saicollection"]
    print(mycollection)
    d = {"name" : 'saikumarseshu',
        "age": 23,
        "friendname":'pallavi',
        "momy" : "swetha"}
    x = mycollection.insert(d)
    print(x)
    y = mycollection.find({"name":"seshu"})
    for i in y:
        print(i)
    #mycollection.

if __name__ == '__main__':
    main()
