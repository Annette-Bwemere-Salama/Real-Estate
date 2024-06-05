from odoo import models, fields
from odoo import api


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "estate tag"

    name = fields.Char(required=True)
    description = fields.Text(string="Description")

