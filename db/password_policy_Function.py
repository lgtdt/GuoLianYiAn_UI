import sqlite3


def Save_Password_Policy(policy_dict):
    upper_num = policy_dict['upper_num']
    lower_num = policy_dict['lower_num']
    symbol_num = policy_dict['symbol_num']
    digit_num = policy_dict['digit_num']
    min_len_num = policy_dict['min_len_num']
    passwd_limit = policy_dict['passwd_limit']
    err_num = policy_dict['err_num']
    conn = sqlite3.connect("./db/DataBase.db")
    cur = conn.cursor()
    try:
        cur.execute("UPDATE password_policy SET upper_num=?, lower_num=?, symbol_num=?, digit_num=?, min_len_num=?, passwd_limit=?, err_num=? WHERE pp_id=?",
                    (upper_num, lower_num, symbol_num, digit_num, min_len_num, passwd_limit, err_num, 1))
        conn.commit()
        conn.close()
        return "success"
    except sqlite3.Error as e:
        conn.rollback()
        conn.close()
        return e

def Get_Password_Policy():
    conn = sqlite3.connect("./db/DataBase.db")
    cur = conn.cursor()
    cur.execute("SELECT upper_num, lower_num, symbol_num, digit_num, min_len_num, passwd_limit, err_num FROM password_policy WHERE pp_id=?",(1,))
    result = cur.fetchall()[0]
    conn.close()
    return result