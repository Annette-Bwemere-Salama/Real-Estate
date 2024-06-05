from odoo import models, fields


class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = "estate property type description"

    name = fields.Char(string="Name", required=True)

