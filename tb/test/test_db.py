import pymysql


from tb.settings import MYSQL_HOST, MYSQL_DB, MYSQL_USER, MYSQL_CHARSET, MYSQL_PASS, MYSQL_PORT


if __name__ == '__main__':
    try:
        conn = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASS, db=MYSQL_DB, charset=MYSQL_CHARSET, port=MYSQL_PORT)
        print(conn.get_server_info())
    except Exception as e:
        print(e)
