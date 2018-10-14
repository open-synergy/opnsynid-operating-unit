# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import fields, models, api


class BuktiPotongPPh(models.Model):
    _inherit = "l10n_id.bukti_potong_pph"

    operating_unit_id = fields.Many2one(
        string="Default Operating Unit",
        comodel_name="operating.unit",
        default=lambda self:
        self.env['res.users'].
        operating_unit_default_get(self._uid)
    )

    @api.onchange(
        "journal_id")
    def onchange_ou_id(self):
        journal = self.journal_id
        ou = journal.operating_unit_id

        if not ou:
            ou_user =\
                self.env['res.users'].operating_unit_default_get(self._uid)
            self.operating_unit_id = ou_user.id
        else:
            self.operating_unit_id = ou.id

    @api.multi
    def _prepare_accounting_entry_data(self):
        res = super(BuktiPotongPPh, self)._prepare_accounting_entry_data()
        res["operating_unit_id"] = self.operating_unit_id.id
        return res
