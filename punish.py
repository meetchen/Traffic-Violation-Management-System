import tkinter as tk
import pymysql
import tkinter.messagebox


def punishSelect():
    mydb = pymysql.connect(host="localhost", user="root",
                           password="8928000cjc", db="sql", port=3306)
    mycursor = mydb.cursor()
    select = 'select * from punish'
    mycursor.execute(select)
    select = mycursor.fetchall()
    mydb.commit()

    tk.messagebox.showinfo(title='惩罚表', message=select)


def punishAdd(type):
    mydb = pymysql.connect(host="localhost", user="root",
                           password="8928000cjc", db="sql", port=3306)
    mycursor = mydb.cursor()
    add = 'insert into punish(punish_type) values %s'
    mycursor.execute(add, type)
    mydb.commit()


def punishDelete(id):
    mydb = pymysql.connect(host="localhost", user="root",
                           password="8928000cjc", db="sql", port=3306)
    mycursor = mydb.cursor()
    delete = 'delete from punish where `sql`.punish.punish_id = %s'
    mycursor.execute(delete, id)
    mydb.commit()


def punishUpdate(type):
    mydb = pymysql.connect(host="localhost", user="root",
                           password="8928000cjc", db="sql", port=3306)
    mycursor = mydb.cursor()
    update = 'update punish set punish_type = %s'
    mycursor.execute(update, type)
    mydb.commit()

