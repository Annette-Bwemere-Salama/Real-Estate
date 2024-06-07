from odoo import models, fields
from odoo import api


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "estate tag"
    _rec_name = "name"
    _order = "name"

    name = fields.Char(required=True)
    color = fields.Char(string="Color")

    _sql_constraints = [
        ("check_unique_tag_name", "unique(tag_name)", "Property Tag must be unique")
    ]

