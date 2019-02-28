# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import models, api


class StockQuant(models.Model):
    _inherit = "stock.quant"

    @api.multi
    def _prepare_fixed_asset_data(self):
        self.ensure_one()
        _super = super(StockQuant, self)
        result = _super._prepare_fixed_asset_data()
        move = self.history_ids[0]  # TODO: Error prone?
        operating_unit_id = \
            move.picking_type_id.warehouse_id.operating_unit_id and \
            move.picking_type_id.warehouse_id.operating_unit_id.id or \
            False
        result.update({
            "operating_unit_id": operating_unit_id,
        })
        return result
