import sys
from DbConf import conf as conf1  # Подключение к БД

sys.path.append('R:\**********************')
import pandas as pd

from datetime import datetime
import time
import os.path


def xl_to_sql(filexl: str, SchemaDB: str, basetable: str, sheetsxl: str = 0, delim: str = ''):
    global df
    extension = os.path.splitext(filexl)[1][1:]
    conf = ('Data Source Name=pymssql;'
            ' Driver=ODBC Driver 17 for SQL Server;'
            ' UID=**********;'
            ' PWD=*******;'
            ' WSID=******;'
            ' APP=Microsoft Office;'
            ' Server=***********;'
            ' Database=******;'
            ' Trusted_connection=no;')
    conx = conf1(conf)
    if extension == 'xlsx' or extension == 'xls' or extension == 'xlsm':
        t1 = time.time()
        df = pd.read_excel(filexl, sheet_name=sheetsxl, )
        print(f'{time.time() - t1:.1f} seconds открытие файла')
    elif extension == 'txt' or extension == 'csv':
        t1 = time.time()
        df = pd.read_csv(filexl, encoding='Windows-1251', delimiter=delim, index_col=False, header=0, low_memory=False)
        print(f'{time.time() - t1:.1f} seconds открытие файла')
    try:
        t2 = time.time()
        # if_exists='replace' - Удаляет таблицу в базе и создает новую.
        # if_exists=‘append’ - Добавляет данные в конец таблицы
        df.to_sql(name=basetable, index=False, con=conx, schema=SchemaDB, if_exists='append')
        print(f'{time.time() - t2:.1f} seconds загрузка данных в базу')
    except ValueError:
        print('Ошибка загрузки данных')
    else:
        print("Данные записаны в таблицу")


if __name__ == '__main__':
    start_time_str = str(datetime.now())
    t0 = time.time()
    # Для запуска укажи Путь к файлу, схему данных таблицы,название таблицы.
    # При необходимости название или номер листа в книге Excel
    # Для списка сотрудников делиметр \t
    # xl_to_sql('Data\\informatica\\*****.xlsx', 'svp_tmp', 'WHS_Phyton_tst', sheetsxl='V_WHS', delim=',')
    xl_to_sql(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]), str(sys.argv[4]), str(sys.argv[5]))
    print(f'{time.time() - t0:.1f} seconds общее время работы программы')
