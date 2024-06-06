from odoo import api, models, fields, _
from odoo.exceptions import ValidationError

GARDEN_ORIENTATION_SELECTION = [
    ("north", "North"),
    ("south", "South"),
    ("east", "East"),
    ("west", "West"),
]

STATE_ESTATE_PROPERTY = [
    ("new", "New"),
    ("offer received", "Offer Received"),
    ("offer accepted", "Offer Accepted"),
    ("sold", "Sold"),
    ("canceled", "Canceled"),
]


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
    garden_orientation = fields.Selection(selection=GARDEN_ORIENTATION_SELECTION)
    # price = fields.Float()
    active = fields.Boolean(default=True)
    state = fields.Selection(selection=STATE_ESTATE_PROPERTY, required=True, default="new", copy=False)
    buyer_id = fields.Many2one("res.partner", string="Bayer", copy=False)
    salesperson_id = fields.Many2one("res.users", string="Salesperson", index=True)
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    offers_ids = fields.One2many("estate.property.offer", "property_id", string="offers id")
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    total_area = fields.Float(compute="_compute_total_area")
    best_price = fields.Float(compute="_compute_best_price", string="Best Offer")

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offers_ids.price")
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.offers_ids.mapped("price") or [0.0])

    @api.onchange("garden")
    def onchange_garden_area_garden_orientation(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = "north"
        else:
            self.garden_area = 0
            self.garden_orientation = ""

    # def action_cancelled(self):
    #     for record in self:
    #         if record in self:
    #             if record.state == "sold":
    #                 raise ValidationError(_("Can't Change states for cancel..........."))
    #             record.state = ["cancel"]
    #             record.offers_ids.status = "cancel"
    #
    # def action_sold(self):
    #     for record in self:
    #         if record.state == "cancel":
    #             raise ValidationError(_("Can't change States for Sold....."))
    #         record.state = "sold"
    #         record.offers_ids.states = "accepted"
    #
    # @api.onchange("state")
    # def onchange_state_cancel_sold(self):
    #     for record in "state":
    #         if self.state == "sold":
    #             raise ValidationError(
    #                 _("Can't change States for Sold.....")
    #             )
    #         record.state = "cancel"
    #         record.offers_ids.status = "cancelled"

