import pymysql

def con():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='sys', charset='utf8')
    cursor = conn.cursor()
    return cursor
