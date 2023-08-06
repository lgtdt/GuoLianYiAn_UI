#--------User_Manager 用户表 逻辑函数--------------
import sqlite3
import time

#获取密码
def GetPasswd(user_name):
    conn = sqlite3.connect("./db/DataBase.db")
    cur = conn.cursor()

    cur.execute(" SELECT passwd FROM user_manager WHERE user_name= ?", (user_name,))
    result = cur.fetchone()
    conn.close()

    return result[0]

# 输入密码错误执行逻辑
def WrongPassFunc(user_name):
    conn = sqlite3.connect("./db/DataBase.db")
    cur = conn.cursor()

    cur.execute("SELECT err_time FROM user_manager WHERE user_name = ?", (user_name,))
    result = cur.fetchone()[0] + 1
    if result >= 5 :
        cur.execute("UPDATE user_manager SET locked = ? WHERE user_name = ?", (1, user_name))
        cur.execute("UPDATE user_manager SET err_time = ? WHERE user_name = ?", (result, user_name))
        cur.execute("UPDATE user_manager SET lock_time = ? WHERE user_name = ?", (int(time.time()), user_name))
        conn.commit()
        conn.close()
    else:
        cur.execute("UPDATE user_manager SET err_time = ? WHERE user_name = ?", (result, user_name))
        conn.commit()
        conn.close()

#判断用户是否被锁定
def IsUserLocked(user_name):
    # LOCKED_TIME 为锁定周期
    LOCKED_TIME = 1800

    conn = sqlite3.connect("./db/DataBase.db")
    cur = conn.cursor()

    cur.execute("SELECT locked, lock_time FROM user_manager WHERE user_name = ?", (user_name,))
    result = cur.fetchone()
    locked = result[0]
    lock_time = result[1]
    now_time = int(time.time())

    if locked == 1:
        if now_time - lock_time > LOCKED_TIME:
            cur.execute("UPDATE user_manager SET locked = ? WHERE user_name = ?", (0, user_name))
            cur.execute("UPDATE user_manager SET err_time = ? WHERE user_name = ?", (0, user_name))
            cur.execute("UPDATE user_manager SET lock_time = ? WHERE user_name = ?", (0, user_name))
            conn.commit()
            conn.close()
            return False
        else:
            LOCKED_TIME_LEFT = LOCKED_TIME - (now_time - lock_time)
            conn.close()
            return LOCKED_TIME_LEFT
    else:
        conn.close()
        return False



def UnLockUser(user_name):
    conn = sqlite3.connect("./db/DataBase.db")
    cur = conn.cursor()

    cur.execute("UPDATE user_manager SET locked = ? WHERE user_name = ?", (0, user_name))
    cur.execute("UPDATE user_manager SET err_time = ? WHERE user_name = ?", (0, user_name))
    cur.execute("UPDATE user_manager SET lock_time = ? WHERE user_name = ?", (0, user_name))
    conn.commit()
    conn.close()




