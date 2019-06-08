import pymysql
import tkinter


def UserSelect(user):
    mydb = pymysql.connect(host="localhost", user="root",
                           password="admin", db="sql", port=3306)
    mycursor = mydb.cursor()
    select = 'select user_password,user_identity from usertable where `sql`.usertable.user = %s'
    mycursor.execute(select, user)
    select = mycursor.fetchone()
    if select is not None:
        return select
    else:
        return 'error'


