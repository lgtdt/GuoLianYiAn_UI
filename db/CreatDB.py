import sqlite3

def CreatDB():

    conn = sqlite3.connect("DataBase.db")
    cur = conn.cursor()

    #-------- user_manager 数据表 --------

    cur.execute(''' CREATE TABLE IF NOT EXISTS user_manager(
                    user_name VARCHAR(10) PRIMARY KEY,
                    role_name VARCHAR(15),
                    passwd VARCHAR(40),
                    locked INTEGER,
                    lock_time INTEGER,
                    err_time INTEGER,
                    start_time INTEGER
                )''')
    users_init_data = [
        ("Admin", "普通用户", "e10adc3949ba59abbe56e057f20f883e", 0, 0, 0, 0),
        ("SysAdmin", "系统管理员", "e10adc3949ba59abbe56e057f20f883e", 0, 0, 0, 0),
        ("SecAdmin", "安全保密管理员", "e10adc3949ba59abbe56e057f20f883e", 0, 0, 0, 0),
        ("AuditAdmin", "安全审计员", "e10adc3949ba59abbe56e057f20f883e", 0, 0, 0, 0),
    ]
    cur.executemany(''' INSERT INTO user_manager (user_name, role_name, passwd, locked, lock_time, err_time, start_time)
                        VALUES (?, ?, ?, ?, ?, ?, ?)''', users_init_data)

    conn.commit()
    conn.close()

CreatDB()

