import tkinter as tk
import tkinter.messagebox
import pymysql
import windows3


def noticeSelect():
    mydb = pymysql.connect(host="localhost", user="root",
                           password="admin", db="sql", port=3306)
    mycursor = mydb.cursor()
    select = 'select * from notice'
    mycursor.execute(select)
    select = mycursor.fetchall()
    mydb.commit()
    windows3.select_windows(select)
    mycursor.close()
    mydb.close()
    return select


def notice_select_id(id):
    mydb = pymysql.connect(host="localhost", user="root",
                           password="admin", db="sql", port=3306)
    mycursor = mydb.cursor()
    mycursor.execute('select * from notice where `sql`.notice.notice_id = %s', id)
    var = mycursor.fetchone()
    mycursor.close()
    mydb.close()
    return var



def noticeAdd(time, date, place, record):
    mydb = pymysql.connect(host="localhost", user="root",
                           password="admin", db="sql", port=3306)
    mycursor = mydb.cursor()
    add = 'insert into notice(notice_time,notice_date,notice_place,notice_record) values (%s, %s, %s, %s)'
    mycursor.execute(add, (time, date, place, record))
    mydb.commit()
    mycursor.close()
    mydb.close()

def noticeUpdate(colunm, var, id):
    mydb = pymysql.connect(host="localhost", user="root",
                           password="admin", db="sql", port=3306)
    mycursor = mydb.cursor()
    if colunm == 'notice_time':
        update = 'update notice set notice_time = %s where `sql`.notice.notice_id = %s'
    elif colunm == 'notice_date':
        update = 'update notice set notice_date = %s where `sql`.notice.notice_id = %s'
    elif colunm == 'notice_place':
        update = 'update notice set notice_place = %s where `sql`.notice.notice_id = %s'
    elif colunm == 'notice_record':
        update = 'update notice set notice_recorde = %s where `sql`.notice.notice_id = %s'
    else:
        return 'error'
    mycursor.execute(update, (var, id))
    mydb.commit()
    mycursor.close()
    mydb.close()

def noticeDelete(id):
    mydb = pymysql.connect(host="localhost", user="root",
                           password="admin", db="sql", port=3306)
    mycursor = mydb.cursor()
    delete = 'delete from notice where `sql`.notice.notice_id = %s'
    mycursor.execute(delete, id)
    mydb.commit()
    mycursor.close()
    mydb.close()
