import pandas as pd
from DbConf import conf as conf1  # Подключение к БД
from datetime import datetime
import time
from sqlalchemy import *


def sql_to_sql(TableOut: str, SchemaOut: str, TableIn: str, SchemaIn: str, *, DBConfIn: str, DBConfOut: str, where: str):
    conf = ('Data Source Name=pymssql;'
            ' Driver=ODBC Driver 17 for SQL Server;'
            ' WSID=******;'
            ' APP=Microsoft Office;'
            ' Trusted_connection=No;')
    conx = conf1(conf + DBConfIn)
    conx2 = conf1(conf + DBConfOut)

    readsql = conx2.connect()
   
    text_sql = text("SELECT * FROM " + SchemaOut + "." + TableOut + " as a WHERE " + where)

    pd.read_sql(text_sql, readsql, index_col=None).to_sql(name=TableIn, index=False, con=conx, schema=SchemaIn,
                                                          if_exists='append')


if __name__ == '__main__':
    start_time_str = str(datetime.now())
    t0 = time.time()
    sql_to_sql('view_urv', 'urv_rcatp', 'data_skud2_tmp', 'inf_tmp',
               DBConfOut=('Server=nedapreport;'
                          'Database=reports;'
                          'UID=*******;'
                          'PWD=********;'),
               DBConfIn=('Server=**********;'
                         'Database=*******;'
                         'UID=**********;'
                         'PWD=**********;'),
               where="a.[Дата отчета] BETWEEN '20230501' AND '20230531'")


    print(f'{time.time() - t0:.1f} seconds общее время работы программы')
#    input('Нажмите любую клавишу для завершения')
