import pandas as pd
from DbConf import conf as conf1  # Подключение к БД
from datetime import datetime
import time
from sqlalchemy import *


def sql_to_sql(TableOut: str, SchemaOut: str, TableIn: str, SchemaIn: str, *, DBConfIn: str, DBConfOut: str, where: str):
    conf = ('Data Source Name=pymssql;'
            ' Driver=ODBC Driver 17 for SQL Server;'
            ' WSID=OFFICE10469;'
            ' APP=Microsoft Office;'
            ' Trusted_connection=No;')
    conx = conf1(conf + DBConfIn)
    conx2 = conf1(conf + DBConfOut)

    readsql = conx2.connect()
    # sql = sql_query.urv_rcatp_view_urv + "'20230501'" + " AND " + "'20230531'"
    # text_sql = text(sql)
    # text_sql = text("SELECT   CAST(a.[Тип пользователя] 	as nvarchar) as [UserType]"
    #                 ",CAST(a.[Подразделение] 		as nvarchar) as [Division]"
    #                 ",CAST(a.[GUID]                 as nvarchar)as [GUID]"
    #                 ",IIF(ISDATE(a.[Дата отчета])=1, CAST(a.[Дата отчета] as date),NULL) as [report_date]"
    #                 ",IIF(ISDATE(a.[Дата и время входа])=1, CAST(a.[Дата и время входа] 	as datetime2),"
    #                 "NULL) as [DateIn] "
    #                 ",IIF(ISDATE(a.[Дата и время выхода])=1, CAST(a.[Дата и время выхода] 	as datetime2),"
    #                 "NULL) as [DateOut] "
    #                 ",IIF(ISDATE(a.[Отработанное время])=1, CAST(a.[Отработанное время]	as time),NULL) as ["
    #                 "working_hours] "
    #                 ",CAST(a.[Дирекция] 			as nvarchar)as [Directorate]"
    #                 ",CAST(a.[Департамент] 			as nvarchar)as [Department]"
    #                 ",CAST(a.[Функция] 				as nvarchar)as [Function]"
    #                 ",CAST(a.[Служба] 				as nvarchar)as [Service]"
    #                 ",CAST(a.[Отдел] 				as nvarchar)as [Otdel]"
    #                 ",CAST(a.[Сектор] 				as nvarchar)as [Sector]"
    #                 ",CAST(a.[Должность] 			as nvarchar)as [JobTitle]"
    #                 "FROM " + SchemaOut + "." + TableOut + " as a "
    #                 "WHERE a.[Дата отчета] BETWEEN '20230501' AND '20230531'")
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