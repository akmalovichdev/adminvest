import datetime
import mysql.connector
from aiogram.types import User
import requests
import os

mysqlHost = os.getenv("mysqlHost")
mysqlUser = os.getenv("mysqlUser")
mysqlPassword = os.getenv("mysqlPassword")
mysqlDatabase = os.getenv("mysqlDatabase")

def connect():
    try:
        conn = mysql.connector.connect(
            host=mysqlHost,
            user=mysqlUser,
            password=mysqlPassword,
            database=mysqlDatabase
        )
        return conn
    except Exception as error:
        print("Ошибка подключения к базе данных: {}".format(error))
        return None

#########################################################################################################################################################################

def getNowDate():
    date = datetime.datetime.today().strftime("%d.%m.%Y")
    return date

def getNowDateTime():
    date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    return date

def getUsersExist(user_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(f"SELECT userId FROM users WHERE userId = '{user_id}'")
    if cursor.fetchone() is None:
        return False
    else:
        return True
    
def getAllUsers():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(f"""SELECT userId FROM users""")
    row = cursor.fetchall()
    return row

#########################################################################################################################################################################

def adduser(userId, userName, userPhone):
    conn = connect()
    cursor = conn.cursor(buffered=True)
    user = [userId, userName, userPhone, getNowDateTime()]
    cursor.execute(f'''INSERT INTO users(userId, userName, userPhone, joinDate) VALUES(%s,%s,%s,%s)''', user)
    conn.commit()

#########################################################################################################################################################################

def select(fields, fields2, table, select):
    try:
        conn = connect()
        cursor = conn.cursor(buffered=True)
        cursor.execute(f"""SELECT {select} FROM {table} WHERE {fields} = '{fields2}'""")
        result = cursor.fetchone()
        row = str(result[0])
        return row
    except:
        return False
    
def selectConf(conf):
    conn = connect()
    cursor = conn.cursor(buffered=True)

    cursor.execute(f"""SELECT meaning FROM config WHERE name = '{conf}'""")
    result = cursor.fetchone()
    row = str(result[0])
    return row

#########################################################################################################################################################################
