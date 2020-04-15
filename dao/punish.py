import tkinter as tk
import pymysql
import tkinter.messagebox
import windows3


def punishSelect():
    mydb = pymysql.connect(host="localhost", user="root",
                           password="admin", db="sql", port=3306)
    mycursor = mydb.cursor()
    select = 'select * from punish'
    mycursor.execute(select)
    select = mycursor.fetchall()
    mydb.commit()
    mycursor.close()
    mydb.close()
    windows3.select_windows(select)
    return select


def punish_select_id(id):
    mydb = pymysql.connect(host="localhost", user="root",
                           password="admin", db="sql", port=3306)
    mycursor = mydb.cursor()
    mycursor.execute('select * from punish where `sql`.punish.punish_id = %s', id)
    var = mycursor.fetchone()
    mycursor.close()
    mydb.close()
    return var


def punishAdd(type):
    mydb = pymysql.connect(host="localhost", user="root",
                           password="admin", db="sql", port=3306)
    mycursor = mydb.cursor()
    add = 'insert into punish(punish_type) values (%s)'
    mycursor.execute(add, type)
    mydb.commit()
    mycursor.close()
    mydb.close()


def punishDelete(id):
    mydb = pymysql.connect(host="localhost", user="root",
                           password="admin", db="sql", port=3306)
    mycursor = mydb.cursor()
    delete = 'delete from punish where `sql`.punish.punish_id = %s'
    mycursor.execute(delete, id)
    mydb.commit()
    mycursor.close()
    mydb.close()


def punishUpdate(id, type):
    mydb = pymysql.connect(host="localhost", user="root",
                           password="admin", db="sql", port=3306)
    mycursor = mydb.cursor()
    update = 'update punish set punish_type = %s where `sql`.punish.punish_id = %s'
    mycursor.execute(update, (id ,type))
    mydb.commit()
    mycursor.close()
    mydb.close()
