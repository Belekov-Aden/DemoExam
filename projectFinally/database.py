import pymysql.cursors


class Database:

    def __init__(self,
                 host='localhost',
                 user='root',
                 password='password',
                 database='demo',
                 charset='utf8',
                 cursorclass=pymysql.cursors.DictCursor,
                 autocommit=True,
                 ):
        self.connection = pymysql.connect(host=host, user=user, password=password, db=database, charset=charset,
                                          cursorclass=cursorclass, autocommit=autocommit)

    def fetch_all(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params or ())
            return cursor.fetchall()

    def fetch_one(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params or ())
            return cursor.fetchone()

    def execute(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params or ())
            return
            # return cursor.lastrowid

    def close(self):
        self.connection.close()


if __name__ == "__main__":
    db = Database()

    # data = db.fetch_all('SELECT * FROM categories')

    # db.execute(f'-- UPDATE categories SET name=%s WHERE id=%s', ('Для дома', 3))

    # db.execute('DELETE FROM categories WHERE id=%s', 3)

    dd = db.fetch_all('SELECT * FROM products order by id')

    print(dd)
