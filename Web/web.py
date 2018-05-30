from flask import Flask, request, render_template
import pygal
import sys
import cx_Oracle

db = cx_Oracle.connect('UTS12118776', '12345678', '52.63.159.155:1521/ORCL')
cursor = db.cursor()

co2_time_list = []
pm25_time_list = []
pm10_time_list = []



#######################################


app = Flask(__name__)
sys.stdout = sys.stderr = open('log.txt','wt')

@app.route("/")
def index():
     return render_template("index.html" ,co=get_co(),co2=get_co2(),pm10=get_pm10(),pm25=get_pm25(),temp=get_temp(),humi=get_humi(), aqi_list=get_aqi() ,aqi_data=aqi(), tmp=temperature(), humi_data=humidity(),co2_data=co2(),co_data=co(),pm25_data=pm25(),pm10_data=pm10())

@app.route('/AQI')
def aqi_data():

    return render_template("aqi.html", aqi_data=aqi(),co2_data=co2(),co_data=co(),humi_data=humidity(),pm25_data=pm25(),pm10_data=pm10())

@app.route('/temperature')
def temperature_data():
    return render_template("temperature.html", graph_data=temperature())

@app.route('/security')
def security():
    try:
        line_chart = pygal.Line()
        line_chart.title = 'Security History'
        line_chart.x_labels = map(str, range(2002, 2013))

        line_chart.add('Humidity', [10,20,30,40,50,60])
        graph_data = line_chart.render_data_uri()
        return render_template("security.html" , graph_data=graph_data)

    except Exception as e:
        return (str(e))



@app.route('/table_data')
def table():
    type = request.args.get('type')

    #aqi_dic = {k: v for k, v in zip(get_aqi(), aqi_time_list)}
    #aqi_dic = list(zip(get_aqi(), aqi_time_list))
    return render_template("table_data.html" ,type=type, aqi=aqi_new_dic(),humi=humi_new_dic(),temp=temp_new_dic(),pm25=pm25_new_dic(),pm10=pm10_new_dic(),co=co_new_dic(),co2=co2_new_dic())

@app.route('/history')
def history():
    day = request.args.get('tempday')
    #sql="select e.t_data, to_char(e.s_date, 'mm-dd HH24:MI') day from (select * from temp e order by e.s_date desc) e and day=%s"
    return render_template("historyTable.html",day=day)








#To generate line chart

def update_time():
    aqi_zip = list(zip(get_aqi(), aqi_time_list))
    return aqi_zip


def temperature():

    try:
        line_chart = pygal.Line()
        line_chart.title = 'Temperature History'
        line_chart.x_labels = get_temp_time()[::-1]

        line_chart.add('Temperature', get_temp()[::-1])
        graph_data = line_chart.render_data_uri()
        return graph_data

    except Exception as e:
        return (str(e))


def co2():
    try:
        line_chart = pygal.Line()
        line_chart.title = 'Carbon Dioxide'
        line_chart.x_labels = get_co2_time()[::-1]
        line_chart.add('Co2', get_co2()[::-1])
        graph_data = line_chart.render_data_uri()
        return graph_data

    except Exception as e:
        return (str(e))

def co():
    try:
        line_chart = pygal.Line()
        line_chart.title = 'Carbonic Oxide'
        line_chart.x_labels = get_co_time()[::-1]
        line_chart.add('Co',  get_co()[::-1])
        graph_data = line_chart.render_data_uri()
        return graph_data

    except Exception as e:
        return (str(e))


def humidity():
    try:
        line_chart = pygal.Line()
        line_chart.title = 'Humidity History'
        line_chart.x_labels = get_humi_time()[::-1]
        line_chart.add('Humidity %', get_humi()[::-1])
        graph_data = line_chart.render_data_uri()
        return graph_data

    except Exception as e:
        return (str(e))

def pm25():
    try:
        line_chart = pygal.Line()
        line_chart.title = 'PM2.5 History'
        line_chart.x_labels = get_pm25_time()[::-1]

        line_chart.add('PM2.5',  get_pm25()[::-1])
        graph_data = line_chart.render_data_uri()
        return graph_data
    except Exception as e:
        return (str(e))

def aqi():
    try:
        line_chart = pygal.Line()
        line_chart.title = 'AQI History'
        line_chart.x_labels = get_aqi_time()[::-1]
        line_chart.add('AQI', get_aqi()[::-1])
        graph_data = line_chart.render_data_uri()

        return graph_data

    except Exception as e:
        return (str(e))


def pm10():
    try:
        line_chart = pygal.Line()
        line_chart.title = 'PM10 History'
        line_chart.x_labels = get_pm10_time()[::-1]
        line_chart.add('PM10', get_pm10()[::-1])
        graph_data = line_chart.render_data_uri()
        return graph_data

    except Exception as e:
        return (str(e))





co_sql = "select a.co_data,to_char(a.s_date,'mm-dd HH24:MI') from (select * from co a order by a.s_date desc)a where rownum<=9"

def get_co():
    data_list = []
    cursor.execute(co_sql)
    data = cursor.fetchall()
    for i in data:
        data_list.append(i[0])

    return data_list


def get_co_time():
    while True:
        co_time_list = []
        cursor.execute(co_sql)
        data = cursor.fetchall()
        for i in data:
            co_time_list.append(i[1])
        return co_time_list




co2_sql = "select b.co2_data,to_char(b.s_date,'mm-dd HH24:MI') from(select * from co2 b order by b.s_date desc)b where rownum<=9"

def get_co2():
    data_list = []
    # time_list = []
    cursor.execute(co2_sql)
    data = cursor.fetchall()
    for i in data:
        data_list.append(i[0])
        co2_time_list.append(i[1])
    return data_list

def get_co2_time():
    while True:
        co2_time_list = []
        cursor.execute(co2_sql)
        data = cursor.fetchall()
        for i in data:
            co2_time_list.append(i[1])
        return co2_time_list






pm10_sql = "select g.pm10_data,to_char(g.s_date,'mm-dd HH24:MI') from(select * from pm10 g order by g.s_date desc)g where rownum<=9"

def get_pm10():
    data_list = []

    cursor.execute(pm10_sql)
    data = cursor.fetchall()
    for i in data:
        data_list.append(i[0])
        pm10_time_list.append(i[1])
    return data_list

def get_pm10_time():
    while True:
        pm10_time_list = []
        cursor.execute(pm10_sql)
        data = cursor.fetchall()
        for i in data:
            pm10_time_list.append(i[1])
        return pm10_time_list






pm25_sql = "select f.pm25_data,to_char(f.s_date,'mm-dd HH24:MI') from(select * from pm25 f order by f.s_date desc)f where rownum<=9"

def get_pm25():
    data_list = []
    cursor.execute(pm25_sql)
    data = cursor.fetchall()
    for i in data:
        data_list.append(i[0])
        #pm25_time_list.append(i[1])
    return data_list

def get_pm25_time():
    while True:
        pm25_time_list = []
        cursor.execute(pm25_sql)
        data = cursor.fetchall()
        for i in data:
            pm25_time_list.append(i[1])
        return pm25_time_list




humi_sql="select c.h_data,to_char(c.s_date,'mm-dd HH24:MI') from(select * from humi c order by c.s_date desc)c where rownum<=9"

def get_humi():
    data_list = []
    cursor.execute(humi_sql)
    data = cursor.fetchall()
    for i in data:
        data_list.append(i[0])
        #humi_time_list.append(i[1])
    return data_list

def get_humi_time():
    while True:
        humi_time_list = []
        cursor.execute(humi_sql)
        data = cursor.fetchall()
        for i in data:
            humi_time_list.append(i[1])
        return humi_time_list

temp_sql = "select e.t_data,to_char(e.s_date,'mm-dd HH24:MI') from(select * from temp e order by e.s_date desc)e where rownum<=9"

def get_temp():
    data_list = []
    cursor.execute(temp_sql)
    data = cursor.fetchall()
    for i in data:
        data_list.append(i[0])

    return data_list

def get_temp_time():
    while True:
        temp_time_list = []
        cursor.execute(temp_sql)
        data = cursor.fetchall()
        for i in data:
            temp_time_list.append(i[1])
        return temp_time_list





aqi_sql="select d.aqi_data,to_char(d.s_date,'MM-DD HH24:MI') from(select * from aqi d order by d.s_date desc)d where rownum<=9"

def get_aqi():
    data_list = []
    cursor.execute(aqi_sql)
    data = cursor.fetchall()
    for i in data:
        data_list.append(i[0])
        #
    return data_list

############################################################TIME POINT#######################

def get_aqi_time():

    while True:
        aqi_time_list = []
        cursor.execute(aqi_sql)
        data = cursor.fetchall()
        for i in data:
            aqi_time_list.append(i[1])
        return aqi_time_list



def aqi_new_dic():
    return list(zip(get_aqi(), get_aqi_time()))

def humi_new_dic():
    return list(zip(get_humi(),get_humi_time() ))
def temp_new_dic():
    return list(zip(get_temp(), get_temp_time()))
def pm25_new_dic():
    return list(zip(get_pm25(), get_pm25_time()))
def pm10_new_dic():
    return list(zip(get_pm10(), get_pm10_time()))
def co_new_dic():
    return list(zip(get_co(), get_co_time()))

def co2_new_dic():
    return list(zip(get_co2(), get_co2_time()))


if __name__== "__main__":

    app.run(host='0.0.0.0',port=80, debug=True,threaded=True)

