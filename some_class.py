# -*- coding:utf-8 -*-

import hashlib
import json
import datetime
import os
import requests

from db import MSSQL
from itsdangerous import TimestampSigner, SignatureExpired

secret_key = '5UdCQ16osyo7vWSlGkZ4iimja92w5iuL'
max_age = 7200

ms = MSSQL()

api_account = 'bfa03f730e200f453c8c8e15b56b0543'
api_key = 'i1Ty6Bqv48QJEUaV'
# req_time = time.time()  # 获得时间戳

arr = {'account': api_account}


def dt_tostring(dt):
    dt_str = dt.strftime('%Y-%m-%d %H:%M')
    dt_year = dt.strftime('%Y')
    if dt_year == '1900':
        return ''
    else:
        return dt_str


def varify_tb(tbname, clf_no):
    sql = "SELECT COUNT(*)AS count_res FROM  " + tbname + " WHERE  clf_no= ?"
    parameters = clf_no
    resList = ms.exec_one_query(sql, parameters)
    return resList[0]


def user_varify_tb(tbname, ID):
    sql = "SELECT COUNT(*)AS count_res FROM  " + tbname + " WHERE  ID= ?"
    parameters = ID
    resList = ms.exec_one_query(sql, parameters)
    return resList[0]


def varify_sub_tb(tbname, no, tid):
    sql = "SELECT COUNT(*)AS count_res FROM  " + tbname + " WHERE  md_no= ? and tid=?"
    parameters = (no, tid)
    resList = ms.exec_one_query(sql, parameters)
    # print tbname,resList[0]
    return resList[0]


def insert_update_tb_md(data, username, status):
    clf_no = data["clf_no"]
    apply_id = data["apply_id"]
    apply_date = data["apply_date"]
    apply_bm_text = data["apply_bm_text"]
    travel_reason = data["travel_reason"]
    traffic_one = data["traffic_one"]
    hotel_one = data["hotel_one"]
    meals_one = data["meals_one"]
    urban_reimbursement_cost = data["urban_reimbursement_cost"]
    hotel_reimbursement_cost = data["hotel_reimbursement_cost"]
    travel_reimbursement_cost = data["travel_reimbursement_cost"]
    restaurant_reimbursement_cost = data["restaurant_reimbursement_cost"]
    meals_reimbursement_cost = data["meals_reimbursement_cost"]
    other_reimbursement_cost = data["other_reimbursement_cost"]
    total_travel_real_cost = data["total_travel_real_cost"]
    total_travel_standard_cost = data["total_travel_standard_cost"]
    total_hotel_standard_cost = data["total_hotel_standard_cost"]
    total_hotel_real_cost = data["total_hotel_real_cost"]
    total_urban_real_cost = data["total_urban_real_cost"]
    total_urban_standard_cost = data["total_urban_standard_cost"]
    total_meals_real_cost = data["total_meals_real_cost"]
    total_meals_standard__cost = data["total_meals_standard_cost"]
    total_restaurant_real_cost = data["total_restaurant_real_cost"]
    total_other_real_cost = data["total_other_real_cost"]
    if varify_tb('clf_maindata', clf_no) == 0:
        sql = "INSERT INTO clf_maindata(clf_no,apply_name,oa_account,apply_date,apply_bm,apply_reason,traffic_one,hotel_one,meals_one," \
              "urban_reimbursement_cost,hotel_reimbursement_cost,travel_reimbursement_cost,restaurant_reimbursement_cost,meals_reimbursement_cost," \
              "other_reimbursement_cost,total_travel_real_cost,total_travel_standard_cost,total_hotel_standard_cost," \
              "total_hotel_real_cost,total_urban_real_cost,total_urban_standard_cost,total_meals_real_cost,total_meals_standard__cost," \
              "total_restaurant_real_cost,total_other_real_cost,status)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        parameters = (
            clf_no, apply_id, username, apply_date, apply_bm_text, travel_reason, traffic_one, hotel_one, meals_one,
            urban_reimbursement_cost
            , hotel_reimbursement_cost, travel_reimbursement_cost, restaurant_reimbursement_cost,
            meals_reimbursement_cost,
            other_reimbursement_cost, total_travel_real_cost, total_travel_standard_cost,
            total_hotel_standard_cost, total_hotel_real_cost, total_urban_real_cost, total_urban_standard_cost,
            total_meals_real_cost, total_meals_standard__cost, total_restaurant_real_cost, total_other_real_cost,
            status)
        try:
            ms.ExecQuery(sql, parameters)
        except EOFError, e:
            print e
    else:
        sql = "UPDATE clf_maindata SET apply_name=?,apply_reason=?,traffic_one=?,hotel_one=?,meals_one=?," \
              "urban_reimbursement_cost=?,hotel_reimbursement_cost=?,travel_reimbursement_cost=?,restaurant_reimbursement_cost=?,meals_reimbursement_cost=?," \
              "other_reimbursement_cost=?,total_travel_real_cost=?,total_travel_standard_cost=?,total_hotel_standard_cost=?," \
              "total_hotel_real_cost=?,total_urban_real_cost=?,total_urban_standard_cost=?,total_meals_real_cost=?,total_meals_standard__cost=?," \
              "total_restaurant_real_cost=?,total_other_real_cost=?,status=? WHERE clf_no=? AND oa_account=?"
        parameters = (
            apply_id, travel_reason, traffic_one, hotel_one, meals_one,
            urban_reimbursement_cost
            , hotel_reimbursement_cost, travel_reimbursement_cost, restaurant_reimbursement_cost,
            meals_reimbursement_cost,
            other_reimbursement_cost, total_travel_real_cost, total_travel_standard_cost,
            total_hotel_standard_cost, total_hotel_real_cost, total_urban_real_cost, total_urban_standard_cost,
            total_meals_real_cost, total_meals_standard__cost, total_restaurant_real_cost, total_other_real_cost,
            status, clf_no, username)
        try:
            ms.ExecQuery(sql, parameters)
        except EOFError, e:
            print e
    return True


def insert_update_tb_1(data, no):
    for data_list in data:
        city_one_array = ""
        tid = data_list["id"]
        name = data_list["name"]
        job_level = data_list["job_level"]
        sex = data_list["sex"]
        travel_city_one = data_list["travel_city_one"]
        travel_days_one = data_list["travel_days_one"]
        travel_city_other = data_list["travel_city_other"]
        travel_days_other = data_list["travel_days_other"]
        for i in range(len(travel_city_one)):
            city_one_array += travel_city_one[i] + ","
        if varify_sub_tb('clf_sub_table_1', no, tid) == 0:
            sql = "INSERT INTO clf_sub_table_1(tid, name, job_level, sex, travel_city_one, travel_days_one," \
                  " travel_city_other, travel_days_other, md_no)  VALUES (?,?,?,?,?,?,?,?,?)"
            parameters = (
                tid, name, job_level, sex, city_one_array, travel_days_one, travel_city_other, travel_days_other, no)
            try:
                ms.ExecQuery(sql, parameters)
            except EOFError, e:
                print e
        else:
            sql = "UPDATE clf_sub_table_1 SET name=?,job_level=?,sex=?,travel_city_one=?,travel_city_other=?," \
                  "travel_days_one=?,travel_days_other=? WHERE md_no=? AND tid=?"
            parameters = (
                name, job_level, sex, city_one_array, travel_city_other, travel_days_one, travel_days_other, no, tid)
            try:
                ms.ExecQuery(sql, parameters)
            except EOFError, e:
                print e
    return True


def insert_update_tb_2(data, no):
    for data_list in data:
        tid = data_list["id"]
        item = data_list["item"]
        datetime = data_list["datetime"]
        travel_departure = data_list["travel_departure"]
        travel_destination = data_list["travel_destination"]
        travel_real_position = data_list["travel_real_position"]
        travel_real_cost = data_list["travel_real_cost"]
        travel_stand_position = data_list["travel_stand_position"]
        travel_stand_cost = data_list["travel_stand_cost"]
        travel_reason = data_list["travel_reason"]
        if varify_sub_tb('clf_sub_table_2', no, tid) == 0:
            sql = "INSERT INTO clf_sub_table_2(tid, item, datetime, travel_departure, travel_destination, " \
                  "travel_real_position, travel_real_cost, travel_stand_position, travel_stand_cost, " \
                  "travel_reason, md_no)  VALUES (?,?,?,?,?,?,?,?,?,?,?)"
            parameters = (tid, item, datetime, travel_departure, travel_destination, travel_real_position,
                          travel_real_cost, travel_stand_position, travel_stand_cost, travel_reason, no)
            try:
                ms.ExecQuery(sql, parameters)
            except EOFError, e:
                print e
        else:
            sql = "UPDATE clf_sub_table_2 SET item=?,datetime=?,travel_departure=?,travel_destination=?," \
                  "travel_real_cost=?,travel_real_position=?,travel_reason=?,travel_stand_cost=?," \
                  "travel_stand_position=?  WHERE md_no=? AND tid=?"
            parameters = (item, datetime, travel_departure, travel_destination, travel_real_cost, travel_real_position,
                          travel_reason, travel_stand_cost, travel_stand_position, no, tid)
            try:
                ms.ExecQuery(sql, parameters)
            except EOFError, e:
                print e
    return True


def insert_update_tb_3(data, no):
    for data_list in data:
        tid = data_list["id"]
        item = data_list["item"]
        datetime = data_list["datetime"]
        urban_transport = data_list["urban_transport"]
        urban_transport_cost = data_list["urban_transport_cost"]
        urban_transport_departure = data_list["urban_transport_departure"]
        urban_transport_destination = data_list["urban_transport_destination"]
        if varify_sub_tb('clf_sub_table_3', no, tid) == 0:
            sql = "INSERT INTO clf_sub_table_3(tid, item,datetime, urban_transport, urban_transport_cost, " \
                  "urban_transport_departure, urban_transport_destination, md_no) VALUES (?,?,?,?,?,?,?,?)"
            parameters = (tid, item, datetime, urban_transport, urban_transport_cost, urban_transport_departure,
                          urban_transport_destination, no)
            try:
                ms.ExecQuery(sql, parameters)
            except EOFError, e:
                print e
        else:
            sql = "UPDATE clf_sub_table_3 SET item=?,datetime=?, urban_transport=?, urban_transport_cost=?, " \
                  "urban_transport_departure=?, urban_transport_destination=? WHERE  md_no=? AND tid=?"
            parameters = (item, datetime, urban_transport, urban_transport_cost, urban_transport_departure,
                          urban_transport_destination, no, tid)
            try:
                ms.ExecQuery(sql, parameters)
            except EOFError, e:
                print e
    return True


def insert_update_tb_4(data, no):
    for data_list in data:
        tid = data_list["id"]
        item = data_list["item"]
        datetime = data_list["datetime"]
        hotel_name = data_list["hotel_name"]
        hotel_days = data_list["hotel_days"]
        hotel_cost = data_list["hotel_cost"]
        if varify_sub_tb('clf_sub_table_4', no, tid) == 0:
            sql = "INSERT INTO clf_sub_table_4(tid, item, datetime, hotel_name, hotel_days, hotel_cost, md_no) VALUES (" \
                  "?,?,?,?,?,?,?) "
            parameters = (tid, item, datetime, hotel_name, hotel_days, hotel_cost, no)
            try:
                ms.ExecQuery(sql, parameters)
            except EOFError, e:
                print e
        else:
            sql = "UPDATE clf_sub_table_4 SET  item=?, datetime=?, hotel_name=?, hotel_days=?, hotel_cost=? WHERE  md_no=? AND tid=?"
            parameters = (item, datetime, hotel_name, hotel_days, hotel_cost, no, tid)
            try:
                ms.ExecQuery(sql, parameters)
            except EOFError, e:
                print e
    return True


def insert_update_tb_5(data, no):
    for data_list in data:
        tid = data_list["id"]
        item = data_list["item"]
        datetime = data_list["datetime"]
        restaurant_name = data_list["restaurant_name"]
        restaurant_cost = data_list["restaurant_cost"]
        if varify_sub_tb('clf_sub_table_5', no, tid) == 0:
            sql = "INSERT INTO clf_sub_table_5(tid, datetime, item, restaurant_name, restaurant_cost, md_no) VALUES (?,?,?,?,?,?) "
            parameters = (tid, datetime, item, restaurant_name, restaurant_cost, no)
            try:
                ms.ExecQuery(sql, parameters)
            except EOFError, e:
                print e

        else:
            sql = "UPDATE clf_sub_table_5 SET datetime=?, item=?, restaurant_name=?, restaurant_cost=? WHERE md_no=? AND tid=?"
            parameters = (datetime, item, restaurant_name, restaurant_cost, no, tid)
            try:
                ms.ExecQuery(sql, parameters)
            except EOFError, e:
                print e
    return True


def insert_update_tb_6(data, no):
    for data_list in data:
        tid = data_list["id"]
        item = data_list["item"]
        datetime = data_list["datetime"]
        restaurant_name = data_list["restaurant_name"]
        restaurant_cost = data_list["restaurant_cost"]
        avg_cost = data_list["avg_cost"]
        if varify_sub_tb('clf_sub_table_6', no, tid) == 0:
            sql = "INSERT INTO clf_sub_table_6(tid, datetime, item, restaurant_name, restaurant_cost,avg_cost, md_no) VALUES (?,?,?,?,?,?,?)"
            parameters = (tid, datetime, item, restaurant_name, restaurant_cost, avg_cost, no)
            try:
                ms.ExecQuery(sql, parameters)
            except EOFError, e:
                print e
        else:
            sql = "UPDATE clf_sub_table_6 SET datetime=?, item=?, restaurant_name=?, restaurant_cost=? ,avg_cost=? WHERE md_no=? AND tid=?"
            parameters = (datetime, item, restaurant_name, restaurant_cost, avg_cost, no, tid)
            try:
                ms.ExecQuery(sql, parameters)
            except EOFError, e:
                print e
    return True


def insert_update_tb_7(data, no):
    for data_list in data:
        tid = data_list["id"]
        item = data_list["item"]
        other_context = data_list["other_context"]
        other_cost = data_list["other_cost"]
        other_explain = data_list["other_explain"]
        if varify_sub_tb('clf_sub_table_7', no, tid) == 0:
            sql = "INSERT INTO clf_sub_table_7(tid, item, other_context, other_cost, other_explain, md_no) VALUES (?,?,?,?,?,?) "
            parameters = (tid, item, other_context, other_cost, other_explain, no)
            try:
                ms.ExecQuery(sql, parameters)
            except EOFError, e:
                print e
        else:
            sql = "UPDATE clf_sub_table_7 SET item=?, other_context=?, other_cost=?, other_explain=? WHERE md_no=? AND tid=?"
            parameters = (item, other_context, other_cost, other_explain, no, tid)
            try:
                ms.ExecQuery(sql, parameters)
            except EOFError, e:
                print e
    return True


def insert_update_tb_8(data, no, username):
    for data_list in data:
        final_travel_bz = data_list["final_travel_bz"]
        final_urban_bz = data_list["final_urban_bz"]
        final_hotel_bz = data_list["final_hotel_bz"]
        final_meals_bz = data_list["final_meals_bz"]
        final_restaurant_bz = data_list["final_restaurant_bz"]
        final_other_bz = data_list["final_other_bz"]
        if varify_tb('clf_maindata', no) == 0:
            print "备注导入出错"
        else:
            sql = "UPDATE clf_maindata SET bz_1=?, bz_2=?, bz_3=?, bz_4=?, bz_5=?, bz_6=? WHERE clf_no=? AND oa_account=?"
            parameters = (final_travel_bz, final_urban_bz, final_hotel_bz, final_meals_bz, final_restaurant_bz,
                          final_other_bz, no, username)
            try:
                ms.ExecQuery(sql, parameters)
            except EOFError, e:
                print e
    return True


def del_row_tb(data, no, tbname):
    for data_list in data:
        selectedid = data_list["selectedID"]
        if varify_sub_tb(tbname, no, selectedid) == 0:
            print "查无此项"
            return 404
        else:
            sql = "DELETE FROM " + tbname + " WHERE md_no=? AND tid=?"
            parameters = (no, selectedid)
            try:
                ms.ExecQuery(sql, parameters)
                return 200
            except EOFError, e:
                print e


def del_md_tb(data):
    for data_list in data:
        selectedid = data_list["selectedID"]
        print selectedid
        if user_varify_tb('clf_maindata', selectedid) == 0:
            print "查无此项"
            return 404
        else:
            sql = "UPDATE clf_maindata SET user_del = 1 WHERE ID=?"
            parameters = selectedid
            try:
                ms.ExecQuery(sql, parameters)
                return 200
            except EOFError, e:
                print e


def get_md_data(username, no):
    sql = "select apply_name,apply_date,apply_bm,apply_reason,traffic_one,hotel_one,meals_one," \
          "urban_reimbursement_cost,hotel_reimbursement_cost,travel_reimbursement_cost," \
          "restaurant_reimbursement_cost,meals_reimbursement_cost,other_reimbursement_cost," \
          "total_travel_real_cost,total_travel_standard_cost,total_hotel_standard_cost," \
          "total_hotel_real_cost,total_urban_real_cost,total_urban_standard_cost,total_meals_real_cost," \
          "total_meals_standard__cost,total_restaurant_real_cost,total_other_real_cost," \
          "status,bz_1,bz_2,bz_3,bz_4,bz_5,bz_6 from clf_maindata WHERE  oa_account=? AND clf_no = ?"
    parameters = (username, no)
    resList = ms.exec_select_query(sql, parameters)
    return resList


def get_md_data_cw(no):
    sql = "select apply_name,apply_date,apply_bm,apply_reason,traffic_one,hotel_one,meals_one," \
          "urban_reimbursement_cost,hotel_reimbursement_cost,travel_reimbursement_cost," \
          "restaurant_reimbursement_cost,meals_reimbursement_cost,other_reimbursement_cost," \
          "total_travel_real_cost,total_travel_standard_cost,total_hotel_standard_cost," \
          "total_hotel_real_cost,total_urban_real_cost,total_urban_standard_cost,total_meals_real_cost," \
          "total_meals_standard__cost,total_restaurant_real_cost,total_other_real_cost," \
          "status,bz_1,bz_2,bz_3,bz_4,bz_5,bz_6 from clf_maindata WHERE  clf_no = ?"
    parameters = no
    resList = ms.exec_select_query(sql, parameters)
    return resList


def get_tb_data(tbn, no):
    if tbn == 1:
        sql = "SELECT tid ,name,job_level,sex,travel_city_one,travel_city_other,travel_days_one,travel_days_other FROM clf_sub_table_1 WHERE md_no=? ORDER BY ID"
        parameters = no
        resList = ms.exec_select_query(sql, parameters)
        return resList
    elif tbn == 2:
        sql = "SELECT tid,item,datetime,travel_stand_position,travel_stand_cost,travel_reason,travel_real_position,travel_real_cost,travel_destination,travel_departure  FROM clf_sub_table_2 WHERE md_no=? ORDER BY ID"
        parameters = no
        resList = ms.exec_select_query(sql, parameters)
        return resList
    elif tbn == 3:
        sql = "SELECT tid,item,datetime,urban_transport,urban_transport_cost,urban_transport_departure,urban_transport_destination  FROM clf_sub_table_3 WHERE md_no=? ORDER BY ID"
        parameters = no
        resList = ms.exec_select_query(sql, parameters)
        return resList
    elif tbn == 4:
        sql = "SELECT tid,item,datetime,hotel_cost,hotel_days,hotel_name  FROM clf_sub_table_4 WHERE md_no=? ORDER BY ID"
        parameters = no
        resList = ms.exec_select_query(sql, parameters)
        return resList
    elif tbn == 5:
        sql = "SELECT tid,item,datetime,restaurant_cost,restaurant_name  FROM clf_sub_table_5 WHERE md_no=? ORDER BY ID"
        parameters = no
        resList = ms.exec_select_query(sql, parameters)
        return resList
    elif tbn == 6:
        sql = "SELECT tid,item,datetime,restaurant_name,restaurant_cost,avg_cost  FROM clf_sub_table_6 WHERE md_no=? ORDER BY ID"
        parameters = no
        resList = ms.exec_select_query(sql, parameters)
        return resList
    elif tbn == 7:
        sql = "SELECT tid,item,other_context,other_cost,other_explain  FROM clf_sub_table_7 WHERE md_no=? ORDER BY ID"
        parameters = no
        resList = ms.exec_select_query(sql, parameters)
        return resList
    else:
        return []


def get_sumamry_data(username):
    sql = "select ID,clf_no,apply_name,apply_date,apply_bm,apply_reason,status from clf_maindata WHERE  oa_account=? AND user_del is NULL ORDER BY ID DESC "
    parameters = username
    resList = ms.exec_select_query(sql, parameters)
    all_tb_arr = []
    for (ID, clf_no, apply_name, apply_date, apply_bm, apply_reason, status) in resList:
        arr_list = {"ID": ID, "clf_no": clf_no, "apply_name": apply_name, "apply_date": apply_date,
                    "apply_bm": apply_bm,
                    "apply_reason": apply_reason, "travel_name": get_all_travel_name(clf_no),
                    "travel_city": get_all_travel_city(clf_no), "status": read_status(status)}
        all_tb_arr.append(arr_list)
    return all_tb_arr


def read_status(status):
    if status == 1:
        return u"暂存"
    elif status == 2:
        return u"已提交"
    else:
        return ""


def get_all_travel_city(no):
    sql = "select travel_city_one,travel_city_other from clf_sub_table_1 WHERE  md_no=?"
    parameters = no
    resList = ms.exec_select_query(sql, parameters)
    city_one_arr = []
    city_oth_arr = []
    arr_to_str = ""
    for travel_city_one, travel_city_other in resList:
        if travel_city_one != "":
            city_one_arr += compare_city_json(travel_city_one[0])
        if travel_city_other != "":
            city_oth_arr.append(travel_city_other)
    all_city = city_one_arr + city_oth_arr
    for i in all_city:
        arr_to_str += i + ","
    return arr_to_str


def get_all_travel_name(no):
    sql = "select name from clf_sub_table_1 WHERE  md_no=?"
    parameters = no
    resList = ms.exec_select_query(sql, parameters)
    name_arr = []
    arr_to_str = ""
    for list in resList:
        name_arr.append(list[0])
    for i in name_arr:
        arr_to_str += i + ","
    return arr_to_str


def compare_city_json(travel_city_one):
    city_arr = []
    with open(os.path.split(os.path.realpath(__file__))[0] + "/static/one_city.json") as f:
        temp = json.loads(f.read())
        for list in temp:
            if travel_city_one == list["value"]:
                city_arr.append(list["text"])
        return city_arr


def get_oa_name(oa_name):
    sql = "select EMPNAME from v_oa_bm WHERE  USERISACTIVE=1 AND USERISDELETED = 0 AND USERACCOUNTS= ?"
    parameters = (oa_name)
    resList = ms.exec_select_query(sql, parameters)  # 通过oa账号查找用户姓名
    for EMPNAME in resList:
        # print EMPNAME[0]
        return EMPNAME[0]


def get_oa_name_bm(oa_name):
    sql = "select EMPNAME,ORGNAME from v_oa_bm WHERE  USERISACTIVE=1 AND USERISDELETED = 0 AND USERACCOUNTS= ?"
    parameters = (oa_name)
    resList = ms.exec_select_query(sql, parameters)  # 通过oa账号查找用户姓名
    return resList


def get_qy_id(username):
    oa_username = username
    nb_result = get_oa_name_bm(oa_username)
    for (EMPNAME, ORGNAME) in nb_result:
        sql = "select account from qy_account WHERE  departname = ? AND realname= ?"
        parameters = (ORGNAME, EMPNAME)
        resList = ms.exec_select_query(sql, parameters)
        for account in resList:
            return account[0]


def varify_username(username):
    sql = "SELECT COUNT(*)AS count_res FROM  v_oa_bm WHERE  USERISACTIVE=1 AND USERISDELETED = 0 AND USERACCOUNTS= ?"
    parameters = (username)
    resList = ms.exec_one_query(sql, parameters)
    return resList[0]


def get_no():
    d1 = datetime.datetime.now().microsecond
    d2 = datetime.datetime.now()
    d3 = d2.strftime('%Y%m%d%H%M%S')
    d4 = d3 + str(d1)
    return d4


def get_token(username):
    s = TimestampSigner(secret_key)
    token = s.sign(username)
    return token


def varify_token(token):
    s = TimestampSigner(secret_key)
    try:
        s.unsign(token, max_age=max_age)
        return 200
    except SignatureExpired:
        return '登陆信息已过期，请重新登录'


def jnfy_result(result):
    data = json.loads(result)
    # print data['status']
    if data['status'] == 1:
        return json.dumps(data['data'])
    else:
        return 0


def make_arr_current(qyid, current_str_date, current_end_date):
    arr['useraccount'] = qyid
    arr['start'] = current_str_date
    arr['end'] = current_end_date
    # arr['requesttime'] = time.time()
    sort_arr = sorted(arr.iteritems(), key=lambda d: d[0])
    a = ''
    for key, value in sort_arr:
        # a += "\'%s\'=\'%s\'" % (key, value)
        a += str(value)
    api_sign = a + api_key
    m = hashlib.md5()  # 获取md5对象
    m.update(api_sign)
    sign = m.hexdigest()
    arr['sign'] = sign  # print arr
    skurl = 'http://kq.qycn.com/index.php/Api/Api/dayReport?'
    re = requests.get(skurl, arr)
    del arr['sign']
    del arr['useraccount']
    del arr['start']
    del arr['end']
    del arr['requesttime']
    data = re.text
    return jnfy_result(data)


def get_qywx_access_token():
    corpid = 'ww76141bcb2955ed0a'  # 企业微信企业ID
    corpsecret = 'QT9RsU0i5WefJ6H5eZeYgxE21c-D7Jpuj_-TJYdtOvc'
    req_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corpid + '&corpsecret=' + corpsecret
    req_fb = requests.get(req_url)
    vaild_data = req_fb.text
    if vaild_data:
        data = json.loads(vaild_data)
        errcode = data['errcode']
        if errcode == 0:
            access_token = data['access_token']
            return access_token
    else:
        return None


def get_qywx_userid(code,token):
    req_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/getuserinfo?access_token='+token+'&code='+code
    req_fb = requests.get(req_url)
    vaild_data = req_fb.text
    if vaild_data:
        data = json.loads(vaild_data)
        errcode = data['errcode']
        if errcode == 0:
            UserId = data['UserId']
            return UserId




