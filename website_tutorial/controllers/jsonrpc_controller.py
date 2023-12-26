from odoo import http
from odoo.http import request


class JsonRpcController(http.Controller):
    @http.route('/login', type="json", auth="public")
    def login(self, **kwargs):
        request.session.authenticate(request.session.db, kwargs['login'], kwargs['password'])
        return {"message": "Login Successfully."}

    @http.route(['/model/partner/list', '/model/partner/detail/<model("res.partner"):partner_id>'], type="json",
                auth="user")
    def list_partner(self, partner_id=None, limit=1, offset=0, order=None, **kwargs):
        if partner_id:
            data = partner_id.read(fields=['name', 'email'])
            return {"partner_id": data}
        partner_ids = request.env['res.partner'].search_read([], fields=['name', 'email'], limit=limit, offset=offset,
                                                             order=order)
        return {"partner_ids": partner_ids}

    # @http.route('/model/partner/detail/<model("res.partner"):partner_id>', type="json", auth="user")
    # def get_partner(self, partner_id, **kwargs):
    #     data = partner_id.read(fields=['name', 'email'])
    #     return {"partner_id": data}

    @http.route('/model/partner/create', type="json", auth="user")
    def create_partner(self, **kwargs):
        partner_id = request.env['res.partner'].create(kwargs)
        return {"partner_id": partner_id.read(fields=['name', 'email', 'phone'])}

    @http.route('/model/partner/update/<model("res.partner"):partner_id>', type="json", auth="user")
    def update_partner(self, partner_id, **kwargs):
        partner_id.write(kwargs)
        return {"partner_id": partner_id.read(fields=['name', 'email', 'phone'])}

    # @http.route('/model/partner/testing/<int:partner_id>/<string:name>', type="json", auth="user")
    # def update_partner(self, partner_id, name,**kwargs):
    #     ...
    #     # partner_id.write(kwargs)
    # return {"partner_id": partner_id.read(fields=['name', 'email', 'phone'])}

    @http.route('/model/partner/delete/<model("res.partner"):partner_id>', type="json", auth="user")
    def update_partner(self, partner_id, **kwargs):
        partner_id.unlink()
        return {"success": True}

    @http.route('/model/partner/execute-kw', type="json", auth="user")
    def execute_method(self, **kwargs):
        return request.env['res.partner'].api_testing_execute_method(**kwargs)

    @http.route('/model/partner/execute-kw/<model("res.partner"):partner_id>', type="json", auth="user")
    def api_testing_execute_method_read(self, partner_id, **kwargs):
        return partner_id.api_testing_execute_method_read(**kwargs)
