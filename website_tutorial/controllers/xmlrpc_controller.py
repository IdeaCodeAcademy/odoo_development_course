import json

import requests
from odoo import http


class XMLRPCController(http.Controller):
    @http.route('/info', type='http', auth='public')
    def info(self):
        return json.dumps({"message": "Hello World", "current_user": http.request.env.user.name})

    @http.route('/login', type="http", auth='public', csrf=False)
    def login(self, **kwargs):
        db_name = http.request.session.db
        user = kwargs.get('login')
        password = kwargs.get('password')
        http.request.session.authenticate(db_name, user, password)
        return "login success."

    @http.route('/logged_user', type='http', auth='user')
    def logged_user(self,**kwargs):
        return json.dumps({"message": "Hello World", "current_user": http.request.env.user.name})
