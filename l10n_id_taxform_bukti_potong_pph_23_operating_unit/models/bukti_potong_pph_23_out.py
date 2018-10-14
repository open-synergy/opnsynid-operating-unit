# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models


class BuktiPotongPPh23Out(models.Model):
    _name = "l10n_id.bukti_potong_pph_23_out"
    _inherit = [
        "l10n_id.bukti_potong_pph_23_out",
        "l10n_id.bukti_potong_pph"
    ]
