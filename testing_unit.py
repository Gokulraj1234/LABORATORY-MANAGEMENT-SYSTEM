# -*- coding: utf-8 -*-
#############################################################################
#
#
#
#############################################################################

from odoo import models, fields


class TestingUnit(models.Model):
    _name = 'test.unit'
    _rec_name = 'code'
    _description = "Test Unit"

    unit = fields.Char(string="Unit", required=True)
    code = fields.Char(string="code", required=True)
