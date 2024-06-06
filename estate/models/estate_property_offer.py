import datetime

from odoo import api, models, fields


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate property offers"

    price = fields.Float()
    status = fields.Selection(selection=[
        ("accepted", "Accepted"),
        ("Refused", "refused"),
    ], copy=False)
    partner_id = fields.Many2one("res.partner", string="partner", required=True)
    property_id = fields.Many2one("estate.property", required=True, string="Property Id")
    create_date = fields.Datetime(string="Create Date", readonly=True)
    validity = fields.Integer(default="7", string="Validity Day()")
    date_deadline = fields.Datetime(string="Date Deadline", compute="_compute_date_deadline",
                                    inverse="_inverse_date_deadline", store=True)
    # property_type_id = fields.

    @api.depends("create_date", "validity")
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date and record.validity:
                record.date_deadline = record.create_date + datetime.timedelta(days=record.validity)
            else:
                record.date_deadline = False

    def _inverse_date_deadline(self):
        for r in self:
            if r.create_date and r.date_deadline:
                r.validity = r.create_date - r.create_date
