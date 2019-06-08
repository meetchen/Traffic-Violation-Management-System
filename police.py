import tkinter as tk
import tkinter.messagebox
import pymysql
import tkwindows


def policeSelect():
    # 查询所有警察信息
    mydb = pymysql.connect(host="localhost", user="root",
                           password="8928000cjc", db="sql", port=3306)
    mycursor = mydb.cursor()
    select = 'select * from police'
    mycursor.execute(select)
    select = mycursor.fetchall()
    mydb.commit()
    tkwindows.select_windows(select)
    return select


def police_select_id(id):
    mydb = pymysql.connect(host="localhost", user="root",
                           password="8928000cjc", db="sql", port=3306)
    mycursor = mydb.cursor()
    mycursor.execute('select * from police where `sql`.police.police_id = %s', id)
    var = mycursor.fetchone()
    return var


def policeAdd(policename):
    # 添加警察信息
    mydb = pymysql.connect(host="localhost", user="root",
                           password="8928000cjc", db="sql", port=3306)
    mycursor = mydb.cursor()
    add = 'insert into police(police_name) values (%s)'
    mycursor.execute(add, policename)
    add = mycursor.fetchall()
    mydb.commit()
    tk.messagebox.showinfo(title='插入成功', message=policename)


def policeUpdate(id, policename):
    # 修改警察信息，只可修改警察名
    mydb = pymysql.connect(host="localhost", user="root",
                           password="8928000cjc", db="sql", port=3306)
    mycursor = mydb.cursor()
    update = 'update police set police_name = %s where police_id = %s'
    mycursor.execute(update, (policename, id))
    mydb.commit()


def policeDelete(id):
    # 通过id删除警员信息
    mydb = pymysql.connect(host="localhost", user="root",
                           password="8928000cjc", db="sql", port=3306)
    mycursor = mydb.cursor()
    delete = 'delete from police where `sql`.police.police_id =%s'
    mycursor.execute(delete, id)
    mydb.commit()

