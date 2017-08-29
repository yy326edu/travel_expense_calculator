# -*- coding:utf-8 -*-
import calendar

from flask import Flask, render_template, request, jsonify, redirect, url_for, json
from flask_bootstrap import Bootstrap

from some_class import get_oa_name_bm, get_no, get_token, varify_token, varify_username, insert_update_tb_md, \
    insert_update_tb_1, insert_update_tb_2, insert_update_tb_3, insert_update_tb_4, insert_update_tb_5, \
    insert_update_tb_6, \
    insert_update_tb_7, insert_update_tb_8, del_row_tb, get_md_data, get_tb_data, dt_tostring, get_sumamry_data, \
    del_md_tb, get_md_data_cw, varify_tb, get_qy_id, get_oa_name, make_arr_current, get_qywx_access_token, \
    get_qywx_userid

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/travel_expense/post/subtable1', methods=['POST'])
def get_tb1_data():
    token = request.args.get('token')
    cno = request.args.get('cno')
    if varify_token(token) == 200:
        data = request.get_json(force=True)
        if insert_update_tb_1(data, cno):
            return jsonify(0)
        else:
            return jsonify(1)
    else:
        return jsonify(2)


@app.route('/travel_expense/post/subtable2', methods=['POST'])
def get_tb2_data():
    token = request.args.get('token')
    cno = request.args.get('cno')
    if varify_token(token) == 200:
        data = request.get_json(force=True)
        if insert_update_tb_2(data, cno):
            return jsonify(0)
        else:
            return jsonify(1)
    else:
        return jsonify(2)


@app.route('/travel_expense/post/subtable3', methods=['POST'])
def get_tb3_data():
    token = request.args.get('token')
    cno = request.args.get('cno')
    if varify_token(token) == 200:
        data = request.get_json(force=True)
        if insert_update_tb_3(data, cno):
            return jsonify(0)
        else:
            return jsonify(1)
    else:
        return jsonify(2)


@app.route('/travel_expense/post/subtable4', methods=['POST'])
def get_tb4_data():
    token = request.args.get('token')
    cno = request.args.get('cno')
    if varify_token(token) == 200:
        data = request.get_json(force=True)
        if insert_update_tb_4(data, cno):
            return jsonify(0)
        else:
            return jsonify(1)
    else:
        return jsonify(2)


@app.route('/travel_expense/post/subtable5', methods=['POST'])
def get_tb5_data():
    token = request.args.get('token')
    cno = request.args.get('cno')
    if varify_token(token) == 200:
        data = request.get_json(force=True)
        if insert_update_tb_5(data, cno):
            return jsonify(0)
        else:
            return jsonify(1)
    else:
        return jsonify(2)


@app.route('/travel_expense/post/subtable6', methods=['POST'])
def get_tb6_data():
    token = request.args.get('token')
    cno = request.args.get('cno')
    if varify_token(token) == 200:
        data = request.get_json(force=True)
        if insert_update_tb_6(data, cno):
            return jsonify(0)
        else:
            return jsonify(1)
    else:
        return jsonify(2)


@app.route('/travel_expense/post/subtable7', methods=['POST'])
def get_tb7_data():
    token = request.args.get('token')
    cno = request.args.get('cno')
    if varify_token(token) == 200:
        data = request.get_json(force=True)
        if insert_update_tb_7(data, cno):
            return jsonify(0)
        else:
            return jsonify(1)
    else:
        return jsonify(2)


@app.route('/travel_expense/post/subtable8', methods=['POST'])
def get_tb8_data():
    token = request.args.get('token')
    cno = request.args.get('cno')
    username = request.args.get('username')
    if varify_token(token) == 200:
        data = request.get_json(force=True)
        if insert_update_tb_8(data, cno, username):
            return jsonify(0)
        else:
            return jsonify(1)
    else:
        return jsonify(2)


@app.route('/travel_expense/geturlformdata', methods=['POST'])
def get_form_val():
    token = request.args.get('token')
    username = request.args.get('username')
    status = request.args.get('status')
    if varify_token(token) == 200:
        data = request.get_json(force=True)
        if insert_update_tb_md(data, username, status):
            return jsonify(0)
        else:
            return jsonify(1)
    else:
        return jsonify(2)


@app.route('/travel_expense/tb_delete/<int:tid>', methods=['POST'])
def travel_table_delete(tid):
    token = request.args.get('token')
    no = request.args.get('no')
    if varify_token(token) == 200:
        data = request.get_json(force=True)
        if tid == 1:
            if del_row_tb(data, no, 'clf_sub_table_1') == 404:
                return jsonify(1)
            else:
                return jsonify(0)
        elif tid == 2:
            if del_row_tb(data, no, 'clf_sub_table_2') == 404:
                return jsonify(1)
            else:
                return jsonify(0)
        elif tid == 3:
            if del_row_tb(data, no, 'clf_sub_table_3') == 404:
                return jsonify(1)
            else:
                return jsonify(0)
        elif tid == 4:
            if del_row_tb(data, no, 'clf_sub_table_4') == 404:
                return jsonify(1)
            else:
                return jsonify(0)
        elif tid == 5:
            if del_row_tb(data, no, 'clf_sub_table_5') == 404:
                return jsonify(1)
            else:
                return jsonify(0)
        elif tid == 6:
            if del_row_tb(data, no, 'clf_sub_table_6') == 404:
                return jsonify(1)
            else:
                return jsonify(0)
        elif tid == 7:
            if del_row_tb(data, no, 'clf_sub_table_7') == 404:
                return jsonify(1)
            else:
                return jsonify(0)
        else:
            return jsonify(0)
    else:
        return jsonify(2)


@app.route('/travel_expense/addForm', methods=['GET'])
def travel_expense_add_form():
    username = request.args.get('username')
    token = request.args.get('token')
    status = 0
    if token and username:
        if varify_token(token) == 200:
            if username:
                resList = get_oa_name_bm(username)
                for (EMPNAME, ORGNAME) in resList:
                    oa_name = EMPNAME
                    oa_orgname = ORGNAME
                    return render_template('addform.html', username=username, oa_name=oa_name, oa_orgname=oa_orgname,
                                           no=get_no(), token=token, status=status)
            else:
                return u"系统显示异常，请尝试调整浏览器为极速模式，仍无法解决请联系管理员"
        else:
            return varify_token(token)
    else:
        return u"系统显示异常，请尝试调整浏览器为极速模式，仍无法解决请联系管理员"


@app.route('/travel_expense/showForm', methods=['GET'])
def travel_expense_show_form():
    username = request.args.get('username')
    token = request.args.get('token')
    no = request.args.get('no')
    if token and username:
        if varify_token(token) == 200:
            resList = get_md_data(username, no)
            for (
                    apply_name, apply_date, apply_bm, apply_reason, traffic_one, hotel_one, meals_one,
                    urban_reimbursement_cost,
                    hotel_reimbursement_cost, travel_reimbursement_cost, restaurant_reimbursement_cost,
                    meals_reimbursement_cost,
                    other_reimbursement_cost, total_travel_real_cost, total_travel_standard_cost, total_hotel_standard_cost,
                    total_hotel_real_cost, total_urban_real_cost, total_urban_standard_cost, total_meals_real_cost,
                    total_meals_standard__cost,
                    total_restaurant_real_cost, total_other_real_cost, status, bz_1, bz_2, bz_3, bz_4, bz_5,
                    bz_6) in resList:
                return render_template('showform.html', apply_name=apply_name, apply_date=apply_date, apply_bm=apply_bm,
                                       apply_reason=apply_reason,
                                       traffic_one=traffic_one, hotel_one=hotel_one, meals_one=meals_one,
                                       urban_reimbursement_cost=urban_reimbursement_cost,
                                       hotel_reimbursement_cost=hotel_reimbursement_cost,
                                       travel_reimbursement_cost=travel_reimbursement_cost,
                                       restaurant_reimbursement_cost=restaurant_reimbursement_cost,
                                       meals_reimbursement_cost=meals_reimbursement_cost,
                                       other_reimbursement_cost=other_reimbursement_cost,
                                       total_travel_real_cost=total_travel_real_cost,
                                       total_travel_standard_cost=total_travel_standard_cost,
                                       total_hotel_standard_cost=total_hotel_standard_cost,
                                       total_hotel_real_cost=total_hotel_real_cost,
                                       total_urban_real_cost=total_urban_real_cost,
                                       total_urban_standard_cost=total_urban_standard_cost,
                                       total_meals_real_cost=total_meals_real_cost,
                                       total_meals_standard_cost=total_meals_standard__cost,
                                       total_restaurant_real_cost=total_restaurant_real_cost,
                                       total_other_real_cost=total_other_real_cost, status=status, final_travel_bz=bz_1,
                                       final_urban_bz=bz_2, final_hotel_bz=bz_3, final_meals_bz=bz_4,
                                       final_restaurant_bz=bz_5, final_other_bz=bz_6, no=no, username=username, token=token)
        else:
            return varify_token(token)
    else:
        return u"系统显示异常，请尝试调整浏览器为极速模式，仍无法解决请联系管理员"


@app.route('/travel_expense/get/subtable1', methods=['get'])
def show_tb1_data():
    token = request.args.get('token')
    no = request.args.get('no')
    if varify_token(token) == 200:
        resList = get_tb_data(1, no)
        tb_arr = []
        for (
                tid, name, job_level, sex, travel_city_one, travel_city_other, travel_days_one,
                travel_days_other) in resList:
            tblist = {'id': tid, 'name': name, 'job_level': job_level, 'sex': sex, 'travel_city_one': travel_city_one,
                      'travel_city_other': travel_city_other, 'travel_days_one': travel_days_one,
                      'travel_days_other': travel_days_other}
            tb_arr.append(tblist)
        return json.dumps(tb_arr)
    else:
        return varify_token(token)


@app.route('/travel_expense/get/subtable2', methods=['get'])
def show_tb2_data():
    token = request.args.get('token')
    no = request.args.get('no')
    if varify_token(token) == 200:
        resList = get_tb_data(2, no)
        # print resList
        tb_arr = []
        for (tid, item, datetime, travel_stand_position, travel_stand_cost, travel_reason, travel_real_position,
             travel_real_cost, travel_destination, travel_departure) in resList:
            tblist = {'id': tid, 'item': item, 'datetime': dt_tostring(datetime),
                      'travel_stand_position': travel_stand_position,
                      'travel_stand_cost': travel_stand_cost, 'travel_reason': travel_reason,
                      'travel_real_position': travel_real_position, 'travel_real_cost': travel_real_cost,
                      'travel_destination': travel_destination, 'travel_departure': travel_departure}
            tb_arr.append(tblist)
        return json.dumps(tb_arr)
    else:
        return varify_token(token)


@app.route('/travel_expense/get/subtable3', methods=['get'])
def show_tb3_data():
    token = request.args.get('token')
    no = request.args.get('no')
    if varify_token(token) == 200:
        resList = get_tb_data(3, no)
        tb_arr = []
        for (tid, item, datetime, urban_transport, urban_transport_cost, urban_transport_departure,
             urban_transport_destination) in resList:
            tblist = {'id': tid, 'item': item, 'datetime': dt_tostring(datetime), 'urban_transport': urban_transport,
                      'urban_transport_cost': urban_transport_cost,
                      'urban_transport_departure': urban_transport_departure,
                      'urban_transport_destination': urban_transport_destination}
            tb_arr.append(tblist)
        return json.dumps(tb_arr)
    else:
        return varify_token(token)


@app.route('/travel_expense/get/subtable4', methods=['get'])
def show_tb4_data():
    token = request.args.get('token')
    no = request.args.get('no')
    if varify_token(token) == 200:
        resList = get_tb_data(4, no)
        tb_arr = []
        for (tid, item, datetime, hotel_cost, hotel_days, hotel_name) in resList:
            tblist = {'id': tid, 'item': item, 'datetime': dt_tostring(datetime), 'hotel_cost': hotel_cost,
                      'hotel_days': hotel_days, 'hotel_name': hotel_name}
            tb_arr.append(tblist)
        return json.dumps(tb_arr)
    else:
        return varify_token(token)


@app.route('/travel_expense/get/subtable5', methods=['get'])
def show_tb5_data():
    token = request.args.get('token')
    no = request.args.get('no')
    if varify_token(token) == 200:
        resList = get_tb_data(5, no)
        tb_arr = []
        for (tid, item, datetime, restaurant_cost, restaurant_name) in resList:
            tblist = {'id': tid, 'item': item, 'datetime': dt_tostring(datetime), 'restaurant_cost': restaurant_cost,
                      'restaurant_name': restaurant_name}
            tb_arr.append(tblist)
        return json.dumps(tb_arr)
    else:
        return varify_token(token)


@app.route('/travel_expense/get/subtable6', methods=['get'])
def show_tb6_data():
    token = request.args.get('token')
    no = request.args.get('no')
    if varify_token(token) == 200:
        resList = get_tb_data(6, no)
        tb_arr = []
        for (tid, item, datetime, restaurant_name, restaurant_cost, avg_cost) in resList:
            tblist = {'id': tid, 'item': item, 'datetime': dt_tostring(datetime), 'restaurant_name': restaurant_name,
                      'restaurant_cost': restaurant_cost, 'avg_cost': avg_cost}
            tb_arr.append(tblist)
        return json.dumps(tb_arr)
    else:
        return varify_token(token)


@app.route('/travel_expense/get/subtable7', methods=['get'])
def show_tb7_data():
    token = request.args.get('token')
    no = request.args.get('no')
    if varify_token(token) == 200:
        resList = get_tb_data(7, no)
        tb_arr = []
        for (tid, item, other_context, other_cost, other_explain) in resList:
            tblist = {'id': tid, 'item': item, 'other_context': other_context, 'other_cost': other_cost,
                      'other_explain': other_explain}
            tb_arr.append(tblist)
        return json.dumps(tb_arr)
    else:
        return varify_token(token)


@app.route('/travel_expense/get/rc_table', methods=['GET'])
def travel_expense_rc_table():
    username = request.args.get('username')
    token = request.args.get('token')
    if varify_token(token) == 200:
        if username:
            tb_arr = get_sumamry_data(username)
            return json.dumps(tb_arr)
        else:
            return json.dumps(None)
    else:
        return varify_token(token)


@app.route('/travel_expense/user_rc_delete', methods=['POST'])
def user_rc_delete():
    # username = request.args.get('username')
    token = request.args.get('token')
    if varify_token(token) == 200:
        data = request.get_json(force=True)
        if del_md_tb(data) == 404:
            return jsonify(1)
        else:
            return jsonify(0)
    else:
        return varify_token(token)


@app.route('/travel_expense/user_record_list', methods=['GET'])
def user_record_list():
    username = request.args.get('username')
    token = request.args.get('token')
    if username and token:
        if varify_token(token) == 200:
            return render_template('userecordlist.html', username=username, token=token)
        else:
            return varify_token(token)
    else:
        return u"系统显示异常，请尝试调整浏览器为极速模式，仍无法解决请联系管理员"


@app.route('/travel_expense/post/varifyinput', methods=['POST'])
def varifyinput():
    token = request.args.get('token')
    no = request.args.get('no')
    if varify_token(token) == 200:
        if varify_tb('clf_maindata', no) == 0:
            return jsonify(404)
        else:
            return jsonify(200)
    else:
        return jsonify(2)


@app.route('/travel_expense/cw_user_index', methods=['GET'])
def cw_user_index():
    username = request.args.get('username')
    token = request.args.get('token')
    if varify_token(token) == 200:
        return render_template('cw_researh.html', username=username, token=token)
    else:
        return varify_token(token)


@app.route('/travel_expense/showForm_cw', methods=['GET'])
def travel_expense_show_form_cw():
    username = request.args.get('username')
    token = request.args.get('token')
    no = request.args.get('no')
    if varify_token(token) == 200:
        resList = get_md_data_cw(no)
        for (
                apply_name, apply_date, apply_bm, apply_reason, traffic_one, hotel_one, meals_one,
                urban_reimbursement_cost,
                hotel_reimbursement_cost, travel_reimbursement_cost, restaurant_reimbursement_cost,
                meals_reimbursement_cost,
                other_reimbursement_cost, total_travel_real_cost, total_travel_standard_cost, total_hotel_standard_cost,
                total_hotel_real_cost, total_urban_real_cost, total_urban_standard_cost, total_meals_real_cost,
                total_meals_standard__cost,
                total_restaurant_real_cost, total_other_real_cost, status, bz_1, bz_2, bz_3, bz_4, bz_5,
                bz_6) in resList:
            return render_template('showform_cw.html', apply_name=apply_name, apply_date=apply_date, apply_bm=apply_bm,
                                   apply_reason=apply_reason,
                                   traffic_one=traffic_one, hotel_one=hotel_one, meals_one=meals_one,
                                   urban_reimbursement_cost=urban_reimbursement_cost,
                                   hotel_reimbursement_cost=hotel_reimbursement_cost,
                                   travel_reimbursement_cost=travel_reimbursement_cost,
                                   restaurant_reimbursement_cost=restaurant_reimbursement_cost,
                                   meals_reimbursement_cost=meals_reimbursement_cost,
                                   other_reimbursement_cost=other_reimbursement_cost,
                                   total_travel_real_cost=total_travel_real_cost,
                                   total_travel_standard_cost=total_travel_standard_cost,
                                   total_hotel_standard_cost=total_hotel_standard_cost,
                                   total_hotel_real_cost=total_hotel_real_cost,
                                   total_urban_real_cost=total_urban_real_cost,
                                   total_urban_standard_cost=total_urban_standard_cost,
                                   total_meals_real_cost=total_meals_real_cost,
                                   total_meals_standard_cost=total_meals_standard__cost,
                                   total_restaurant_real_cost=total_restaurant_real_cost,
                                   total_other_real_cost=total_other_real_cost, status=status, final_travel_bz=bz_1,
                                   final_urban_bz=bz_2, final_hotel_bz=bz_3, final_meals_bz=bz_4,
                                   final_restaurant_bz=bz_5, final_other_bz=bz_6, no=no, username=username, token=token)
    else:
        return varify_token(token)


@app.route('/sso_login/travel_expense/cw_user', methods=['GET'])
def get_cw_user_login_redirect():
    username = request.args.get('username')
    varify_data = varify_username(username)
    if username:
        if 1 == varify_data:
            token = get_token(username)
            return redirect(url_for('cw_user_index', username=username, token=token))
        else:
            return u"账号异常，请联系管理员"
    else:
        return u"系统显示异常，请尝试调整浏览器为极速模式，仍无法解决请联系管理员"


@app.route('/sso_login/travel_expense', methods=['GET'])
def get_login_redirect():
    username = request.args.get('username')
    varify_data = varify_username(username)
    if username:
        if 1 == varify_data:
            token = get_token(username)
            return redirect(url_for('user_record_list', username=username, token=token))
        else:
            return u"账号异常，请联系管理员"
    else:
        return u"系统显示异常，请尝试调整浏览器为极速模式，仍无法解决请联系管理员"


# @app.route('/mainframe/getlastkq', methods=['GET'])
# def get_last_month():
#     qyid = request.args.get('qyid')
#     # day_now = time.localtime()
#
#     if day_now.tm_mon == 1:
#         current_str_date = "%d-%d-01" % (day_now.tm_year - 1, day_now.tm_mon - 1)  # 月初肯定是1号
#         current_end_date = "%d-%d-31" % (day_now.tm_year - 1, day_now.tm_mon - 1,)  # 当前月份减1
#     elif 1 < day_now.tm_mon < 10:
#         current_str_date = "%d-0%d-01" % (day_now.tm_year, day_now.tm_mon - 1)  # 月初肯定是1号
#         monthRange = calendar.monthrange(day_now.tm_year - 1,
#                                          day_now.tm_mon - 1)  # 得到本月的天数 第一返回为月第一日为星期几（0-6）, 第二返回为此月天数
#         current_end_date = "%d-0%d-%d" % (day_now.tm_year, day_now.tm_mon - 1, monthRange[1])  # 当前月份减1
#     else:
#         current_str_date = "%d-%d-01" % (day_now.tm_year, day_now.tm_mon - 1)  # 月初肯定是1号
#         monthRange = calendar.monthrange(day_now.tm_year - 1,
#                                          day_now.tm_mon - 1)  # 得到本月的天数 第一返回为月第一日为星期几（0-6）, 第二返回为此月天数
#         current_end_date = "%d-%d-%d" % (day_now.tm_year, day_now.tm_mon - 1, monthRange[1])  # 当前月份减1
#     result = make_arr_current(qyid, current_str_date, current_end_date)
#     return result


@app.route('/sso_login/getkq', methods=['GET'])
def get_login():
    username = request.args.get('username')
    # bm = request.args.get('org')
    qyid = get_qy_id(username)
    oa_name = get_oa_name(username)
    # print qyid
    if qyid:
        return redirect(url_for('mainframe', qyid=qyid, oa_name=oa_name))
    else:
        return u"系统显示异常，请尝试调整浏览器为极速模式，仍无法解决请联系管理员"


@app.route('/', methods=['GET'])
def qywx_login():
    code = request.args.get('code')
    state = request.args.get('state')
    origin_state = 'DGLkLw.Z6Gxf67jIlhBAuJe6ermAVLjXAY'
    if state == origin_state:
        if code:
            if get_qywx_access_token():
                access_toke = get_qywx_access_token()
                username = get_qywx_userid(code, access_toke)
                return redirect(url_for('get_login_redirect', username=username))
            else:
                return u"access_token获取异常"
        else:
            return u"code获取异常"
    else:
        return u"系统异常"


if __name__ == '__main__':
    app.run(debug=True)
