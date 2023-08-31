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
    # -------- optr_logs 数据表 --------
    cur.execute(''' CREATE TABLE IF NOT EXISTS optr_logs(
                        log_id INT PRIMARY KEY,
                        time_stamp INT,
                        operate_type INT,
                        user_name VARCHAR(10),
                        role_name VARCHAR(15),
                        operate_value VARCHAR(15),
                        operate_result VARCHAR(15)
                    );''')
    logs_init_data = [
        (100000, 100000, 1, "admin", "普通用户", "扫描", "成功"),
        (100001, 100001, 2, "sysadmin", "系统管理员", "登录", "成功"),

    ]
    cur.executemany(''' INSERT INTO optr_logs (log_id, time_stamp, operate_type, user_name, role_name, operate_value, operate_result)
                                    VALUES (?, ?, ?, ?, ?, ?, ?)''', logs_init_data)

    # -------- password_policy 数据表 --------
    cur.execute(''' CREATE TABLE IF NOT EXISTS password_policy(
                            pp_id INT PRIMARY KEY,
                            upper_num INT,
                            lower_num INT,
                            symbol_num INT,
                            digit_num INT,
                            min_len_num INT,
                            passwd_limit INT,
                            err_num INT,
                            lock_time INT
                        );''')
    pass_init_data = [
        (1, 1, 1, 1, 1, 8, 30, 5, 30),
    ]
    cur.executemany(''' INSERT INTO password_policy (pp_id, upper_num, lower_num, symbol_num, digit_num, min_len_num, passwd_limit, err_num, lock_time)
                                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', pass_init_data)


    conn.commit()
    conn.close()
    print("表创建成功！")


if __name__ == "__main__":
    CreatDB()


