from odoo import models, fields


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate Modul For Annette"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()

    date_availability = fields.Date.today()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default="2")
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(selection=[
        ("north", "North"),
        ("south", "South"),
        ("east", "East"),
        ("west", "West"),
    ])
    price = fields.Float()
    active = fields.Boolean(default=True)
    state = fields.Selection(selection=[
        ("new", "New"),
        ("offer received", "Offer Received"),
        ("offer accepted", "Offer Accepted"),
        ("sold", "Sold"),
        ("canceled", "Canceled"),

    ], required=True, default="New", copy=False)
    buyer_id = fields.Many2one("res.partner", string="Bayer", copy=False)
    salesperson_id = fields.Many2one("res.users", string="Salesperson", index=True, tracking=True, default=lambda self: self.env.user)
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")