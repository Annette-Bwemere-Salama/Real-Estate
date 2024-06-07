import datetime

from odoo import api, models, fields, _
from odoo.exceptions import UserError


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate property offers"
    _order = "price DESC"

    price = fields.Float(string="Price")
    status = fields.Selection(selection=[
        ("accepted", "Accepted"),
        ("Refused", "refused"),
    ], copy=False)
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
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

    @api.onchange("price")
    def onchange_price_greater_than_zero(self):
        if self.price < 0:
            return {"warning": {"title": _("Warning"), "message": _("Le montant du prix de doit pas être négative")}}

    def action_accept(self):
        # self.ensure_one()
        if "accepted" in self.property_id.offers_ids.mapped("status"):
            raise UserError(_("Is Accepted"))
        self.status = "accepted"
        self.property_id.selling_price = self.price

    def action_refused(self):
        # self.ensure_one()
        if "refused" in self.property_id.offers_ids.mapped("status"):
            raise UserError(_("We cannot refuse is status is save and accepted"))
        self.status = "refused"
        self.property_id.selling_price = self.price