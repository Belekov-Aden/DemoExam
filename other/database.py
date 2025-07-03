import pymysql.cursors


class Database:
    def __init__(self, host='localhost', user='root', password='password', database='main'):
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True  # не забудь, если нужно автосохранение
        )

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
            return cursor.lastrowid  # можно возвращать ID вставки

    def close(self):
        self.connection.close()


if __name__ == '__main__':
    db = Database()

    products = db.fetch_all("""
                            SELECT products.id, products.name, categories.name AS category_name, products.price
                            FROM products
                                     JOIN categories ON products.categories = categories.id
                            """)

    for product in products:
        print(product)

    db.close()
