import pymysql
import config

class MySQL:

    @staticmethod
    def connection():
        result = None

        try:
            result = pymysql.connect(
            host = config.HOSTNAME,
            user = config.USER,
            passwd = config.PASSWORD,
            database = config.DATABASE,
            cursorclass= pymysql.cursors.DictCursor)
        except Exception:
            pass
            

        return result