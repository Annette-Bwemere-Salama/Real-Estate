from odoo import api

from odoo import models, fields, _


class EstateProperty(models.Model):
    # _inherit = 'estate.property'
    _name = "estate.property"
    _description = "estate Modul For Annette"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()

    date_availability = fields.Date(string="Date Availability"
                                    # , default=lambda self: fields.date.today() + timedelta(month=3)
                                    )
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
    salesperson_id = fields.Many2one("res.users", string="Salesperson", index=True)
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    offers_ids = fields.One2many("estate.property.offer", "property_id", string="offers id")
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")

    @api.model
    def tags_view_mapping(self):
        if self.tag_ids:
            tags_names = ", ".join(tag.name for tag in self.tag_ids)
            return _("Tags exists: %s") % tags_names
        else:
            return _("No tags are defined")



