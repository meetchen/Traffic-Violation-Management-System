import pymysql
import tkinter
import tkinter.messagebox
import tkwindows

# 查看所有驾驶人信息


def driver():
    mydb = pymysql.connect(host="localhost", user="root",
                           password="8928000cjc", db="sql", port=3306)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM driver")
    var = mycursor.fetchall()  # fetchall() 获取所有记录
    tkwindows.select_windows(var)
    return var


# 添加驾驶人信息
def driver_insert(name, phone, address, post_code):
    mydb = pymysql.connect(host="localhost", user="root", password="8928000cjc", db="sql", port=3306)
    mycursor = mydb.cursor()
    add = 'insert into driver(driver_name,driver_phone,driver_address,driver_post_code) values(%s,%s,%s,%s) '
    add = mycursor.execute(add, (name, phone, address, post_code))
    mydb.commit()

    # 更新驾驶人信息


def diverUpdate(column, varupdate, id):
    mydb = pymysql.connect(host="localhost", user="root", password="8928000cjc", db="sql", port=3306)
    mycuror = mydb.cursor()
    if column == 'driver_name':
        update = 'UPDATE driver set driver_name = %s where driver_id = %s'
        update = mycuror.execute(update, (varupdate, id))
    elif column == 'driver_phone':
        update = 'UPDATE driver set driver_phone = %s where driver_id = %s'
        update = mycuror.execute(update, (varupdate, id))
    elif column == 'driver_post_code':
        update = 'UPDATE driver set driver_post_code = %s where driver_id = %s'
        update = mycuror.execute(update, (varupdate, id))
    else:
        print('error')
    mydb.commit()



# 删除
def diverDelete(id):
    mydb = pymysql.connect(host="localhost", user="root", password="8928000cjc", db="sql", port=3306)
    mycuror = mydb.cursor()
    delete = 'delete from driver where driver_id= %s'
    delete_var = mycuror.execute(delete, id)
    print(delete_var)
    if delete_var is not 0:
        tkinter.messagebox.showinfo(title='Tips', message='Successful deletion')
    else:
        tkinter.messagebox.showinfo(title='Error', message='Driver_id does not exist')
    mydb.commit()

