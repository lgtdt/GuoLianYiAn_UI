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

def UpdatePasswd(username, password):
    conn = sqlite3.connect("./db/DataBase.db")
    cur = conn.cursor()

    cur.execute("UPDATE user_manager SET passwd = ? WHERE user_name = ?", (password, username))
    cur.execute("UPDATE user_manager SET err_time = ? WHERE  user_name = ?", (0, username))
    cur.execute("UPDATE user_manager SET lock_time = ? WHERE user_name = ?", (0, username))
    cur.execute("UPDATE user_manager SET start_time = ? WHERE user_name = ?", (int(time.time()), username))
    conn.commit()
    conn.close()

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

def ResetUserPasswd(username):
    conn = sqlite3.connect("./db/DataBase.db")
    cur = conn.cursor()

    cur.execute("UPDATE user_manager SET passwd = ? WHERE user_name = ?",("e10adc3949ba59abbe56e057f20f883e", username))
    cur.execute("UPDATE user_manager SET locked = ? WHERE user_name = ?", (0, username))
    cur.execute("UPDATE user_manager SET err_time = ? WHERE user_name = ?", (0, username))
    cur.execute("UPDATE user_manager SET lock_time = ? WHERE user_name = ?", (0, username))
    conn.commit()
    conn.close()

def UnLockUser(username):
    conn = sqlite3.connect("./db/DataBase.db")
    cur = conn.cursor()

    cur.execute("UPDATE user_manager SET locked = ? WHERE user_name = ?", (0, username))
    cur.execute("UPDATE user_manager SET err_time = ? WHERE user_name = ?", (0, username))
    cur.execute("UPDATE user_manager SET lock_time = ? WHERE user_name = ?", (0, username))
    conn.commit()
    conn.close()

def LoginSuccess(username):
    conn = sqlite3.connect("./db/DataBase.db")
    cur = conn.cursor()
    #登陆成功 添加日志
    cur.execute("SELECT COUNT(*) FROM optr_logs")
    len = cur.fetchone()[0]
    log_id = 100000 + len
    cur.execute("UPDATE user_manager SET locked = ? WHERE user_name = ?", (0, username))
    cur.execute("UPDATE user_manager SET err_time = ? WHERE user_name = ?", (0, username))
    cur.execute("UPDATE user_manager SET lock_time = ? WHERE user_name = ?", (0, username))
    cur.execute("SELECT role_name FROM user_manager WHERE user_name = ?", (username,))
    role_name = cur.fetchone()[0]
    log_data = [
        (log_id, time.time(), 1, username, role_name, "登录", role_name+"成功登录"),
    ]
    cur.executemany(''' INSERT INTO optr_logs (log_id, time_stamp, operate_type, user_name, role_name, operate_value, operate_result)
                                    VALUES (?, ?, ?, ?, ?, ?, ?)''', log_data)
    conn.commit()
    conn.close()





