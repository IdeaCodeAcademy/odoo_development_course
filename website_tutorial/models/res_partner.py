from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def api_testing_execute_method(self, **kwargs):
        return {
            "status": "success", **kwargs}

    def api_testing_execute_method_read(self, **kwargs):
        return {"name": self.name}
