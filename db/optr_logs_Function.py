import sqlite3

def GetLogs(user_name):
    conn = sqlite3.connect("./db/DataBase.db")
    cur = conn.cursor()

    cur.execute(" SELECT log_id, role_name, time_stamp, operate_value, operate_result  FROM optr_logs WHERE user_name= ?", (user_name,))
    result = cur.fetchall()
    conn.close()
    return result

# if __name__ == '__main__':
#     res = GetLogs("sysadmin")
#     print(res[0])