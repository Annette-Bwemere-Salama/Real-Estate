from odoo import models, fields


class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = "estate property type description"

    name = fields.Char(string="Name", required=True)
    # property_ids = fields.One2many("estate.property", "property_type_id", string="Property Id")

    _sql_constraints = [
        ("name_uniq", "unique(name)", "Name must be unique"),
    ]