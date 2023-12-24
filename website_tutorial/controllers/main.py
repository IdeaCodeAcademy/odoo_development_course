from odoo import http

class MainController(http.Controller):
    @http.route('/home',type="http",auth="public",website=True)
    def home(self,**kwargs):
        values = {}
        return http.request.render("website_tutorial.Home", values)
