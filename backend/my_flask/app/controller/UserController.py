from flask import Response, Blueprint, request,jsonify

from app import app, db
from app.model.User import User

from app.utils.utils import json_str
from app.form.UserForm import UserForm

user = Blueprint('user', __name__)
# CORS(user, supports_credentials=True)


@app.route('/get_user_list', methods=['POST','GET'])
def get_user_list():
    print(request.args)
    page_index = int(request.args.get('page'))
    page_size = int(request.args.get('itemsPerPage'))
    # page_size = 10
    total = db.session.query(User).count()
    user_list_rs = db.session.query(User).filter().offset((int(page_index) - 1) * int(page_size)).limit(int(page_size)).all()
    # print(dir(User))
    # user_list_rs = User.query.all()

    user_list = []
    for u_data in user_list_rs:
        u = {
            'uid' : u_data.uid,
            'name' : u_data.name,
            'gender' : u_data.gender,
            'edit' : [
                {'slotName': "editBtn", 'uid' : u_data.uid,'name' : u_data.name, 'gender' : u_data.gender}
            ]
        }
        user_list.append(u)

    total_item_count = total;
    total_filtered_item_count = total;

    return {'code': 200, 'msg': 'Ok', 'data' : {'data' : {'items' : user_list, 'total_item_count':total_item_count, 'total_filtered_item_count' : total_filtered_item_count}}}


@app.route('/add_user', methods=['POST'])
def add_user():

    try:
        formData = request.json;
        uf = UserForm(data = formData)
        # print('uf.vali ' + str(uf.validate()))
        if uf.validate():
            if not uf.validate_name_exist(uf.name):
                nu = User(name=uf.name.data, gender=uf.gender.data)
                # print(nu)
                db.session.add(nu)
                db.session.commit()
                resp = {'code': 200, 'msg': 'Save Succ'}
                return resp;
        else:
            resp = {'code': 100, 'msg': uf.errors}
            return resp;
    except Exception as e:
        resp = {'code': 110, 'msg': str(e)}
        return resp;



@app.route('/edit_user', methods=['POST'])
def edit_user():
    try:
        formData = request.json;
        uf = UserForm(data = formData)
        # print('uf.vali ' + str(uf.validate()))
        if uf.validate():
            if not uf.validate_name_exist(uf.name):
                nu = User.query.filter(User.uid == formData['uid'])\
                    .update({'name' : uf.name.data, 'gender' : uf.gender.data})
                db.session.commit()
                resp = {'code': 200, 'msg': 'Save Succ'}
                return resp;
        else:
            resp = {'code': 100, 'msg': uf.errors}
            return resp;
    except Exception as e:
        resp = {'code': 110, 'msg': str(e)}
        return resp;
