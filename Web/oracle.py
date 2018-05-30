import cx_Oracle
co_sql = "select d.aqi_data,d.s_date from(select * from aqi d order by d.s_date desc)d where rownum<=9"
db = cx_Oracle.connect('UTS12118776', '12345678', '52.63.159.155:1521/ORCL')
cursor = db.cursor()
def get_co_oracle():

    data_list = []
    time_list = []
    cursor.execute(co_sql)
    data = cursor.fetchall()

    for i in data:
        data_list.append(i[0])
        time_list.append(i[1])
        print(i[0])
        print(i[1])


get_co_oracle()