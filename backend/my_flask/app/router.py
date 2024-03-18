from app import app
from flask import redirect, render_template, Response

from app.controller.UserController import user

app.register_blueprint(user, url_prefix='/')


@app.errorhandler(404)
def page_not_found(e):
    return Response('404', content_type='application/json')


@app.errorhandler(500)
def internal_server_error(e):
    return Response('500', content_type='application/json')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

