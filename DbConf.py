# Нужно подключить библиотеку sqlalchemy
# Для этого в терминале введите:
# pip install sqlalchemy
import sys
sys.path.append('***')
from sqlalchemy import create_engine
import urllib


def conf(config):
    conn = urllib.parse.quote_plus(config)
    try:
        conx = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(conn), fast_executemany=False)
        return conx
    except ValueError:
        print("Ошибка подключения к базе")
