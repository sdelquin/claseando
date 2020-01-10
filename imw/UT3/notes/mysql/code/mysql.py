import pymysql.cursors


class DB():
    def _make_connection(self):
        self.connection = pymysql.connect(
            host='localhost',
            port=3306,
            user=self.username,
            password=self.password,
            db=self.database,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def __init__(self, username, password, database):
        self.username = username
        self.password = password
        self.database = database
        self._make_connection()

    def run(self, sql):
        if not self.connection.open:
            self._make_connection()

        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            if sql.startswith('select'):
                return cursor.fetchall()
