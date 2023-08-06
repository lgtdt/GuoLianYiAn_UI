import sqlite3

def CreatDB():

    print("连接数据库中...")
    conn = sqlite3.connect("DataBase.db")
    cur = conn.cursor()

    print("正在创建表...")
    #-------- user_manager 数据表 --------

    cur.execute(''' CREATE TABLE IF NOT EXISTS user_manager(
                    user_name VARCHAR(10) PRIMARY KEY,
                    role_name VARCHAR(15),
                    passwd VARCHAR(40),
                    locked INT,
                    lock_time INT,
                    err_time INT,
                    start_time INT
                );''')
    users_init_data = [
        ("admin", "普通用户", "e10adc3949ba59abbe56e057f20f883e", 0, 0, 0, 0),
        ("sysadmin", "系统管理员", "e10adc3949ba59abbe56e057f20f883e", 0, 0, 0, 0),
        ("secadmin", "安全保密管理员", "e10adc3949ba59abbe56e057f20f883e", 0, 0, 0, 0),
        ("auditadmin", "安全审计员", "e10adc3949ba59abbe56e057f20f883e", 0, 0, 0, 0),
    ]
    cur.executemany(''' INSERT INTO user_manager (user_name, role_name, passwd, locked, lock_time, err_time, start_time)
                                VALUES (?, ?, ?, ?, ?, ?, ?)''', users_init_data)


    conn.commit()
    conn.close()
    print("表创建成功！")


if __name__ == "__main__":
    CreatDB()


