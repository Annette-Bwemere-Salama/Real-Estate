from odoo import models, fields


class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = "estate property type description"
    _order = "name"

    name = fields.Char(string="Name", required=True)
    property_ids = fields.Many2one("estate.property", string="Property Id")
    Sequence = fields.Integer(string="Sequence", default=1, help="Use Sequence")
    _sql_constraints = [
        ("name_uniq", "unique(name)", "Name must be unique"),
    ]