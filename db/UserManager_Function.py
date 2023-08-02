import sqlite3

def GetPasswd(user_name):
    conn = sqlite3.connect("DataBase.db")
    cur = conn.cursor()

    cur.execute(" SELECT passwd FROM user_manager WHERE user_name=?",(user_name,))
    result = cur.fetchone()

    return result