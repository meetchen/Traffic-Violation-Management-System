import tkinter as tk
import tkinter.messagebox
import pymysql


def noticeSelect():
    mydb = pymysql.connect(host="localhost", user="root",
                           password="8928000cjc", db="sql", port=3306)
    mycursor = mydb.cursor()
    select = 'select * from notice'
    mycursor.execute(select)
    select = mycursor.fetchall()
    mydb.commit()
    tk.messagebox.showinfo(title='罚单', message=select)


def noticeAdd(time, date, place, record):
    mydb = pymysql.connect(host="localhost", user="root",
                           password="8928000cjc", db="sql", port=3306)
    mycursor = mydb.cursor()
    add = 'insert into notice(notice_time,notice_date,notice_place,notice_record) values (%s, %s, %s, %s)'
    mycursor.execute(add, (time, date, place, record))
    mydb.commit()


def noticeUpdate(colunm, var, id):
    mydb = pymysql.connect(host="localhost", user="root",
                           password="8928000cjc", db="sql", port=3306)
    mycursor = mydb.cursor()
    if colunm == 'notice_time':
        update = 'update notice set notice_time = %s where `sql`.notice.notice_id = %s'
    elif colunm == 'notice_date':
        update = 'update notice set notice_date = %s where `sql`.notice.notice_date = %s'
    elif colunm == 'notice_place':
        update = 'update notice set notice_place = %s where `sql`.notice.notice_place = %s'
    elif colunm == 'notice_record':
        update = 'update notice set notice_recorde = %s where `sql`.notice.notice_record = %s'
    else:
        return 'error'
    mycursor.execute(update, (var, id))
    mydb.commit()


def noticeDelete(id):
    mydb = pymysql.connect(host="localhost", user="root",
                           password="8928000cjc", db="sql", port=3306)
    mycursor = mydb.cursor()
    delete = 'delete from notice where `sql`.notice.notice_id = %s'
    mycursor.execute(delete, id)
    mydb.commit()
