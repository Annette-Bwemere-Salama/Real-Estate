from odoo import models, fields
from odoo import api, _


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "estate tag"
    _rec_name = "name"
    _order = "name"

    name = fields.Char(required=True)
    color = fields.Char(string="Color")

    _sql_constraints = [
        ("check_unique_name", "unique(name)", "Property Tag must be unique")
    ]

    # @api.model
    # def create(self, vals):
    #     if vals.get('name', _('New')) == _('New'):
    #         vals['name'] = self.env['ir.sequence'].next_by_code('estate.property.tag.sequence') or _('New')
    #     return super(EstatePropertyTag, self).create(vals)