# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Module(models.Model):
    _inherit = "ir.module.module"

    @api.multi
    def module_multiple_uninstall(self):
        """ Perform the various steps required to uninstall a module completely
            including the deletion of all database structures created by the module:
            tables, columns, constraints, etc.
        """
        modules = self.browse(self.env.context.get("active_ids"))
        [
            module.button_immediate_uninstall()
            for module in modules
            if module not in ["base", "web"]
        ]
