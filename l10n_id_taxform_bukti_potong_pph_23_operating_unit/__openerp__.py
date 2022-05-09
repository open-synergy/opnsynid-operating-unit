# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Indonesia - Bukti Potong PPh 23 " "with Operating Units",
    "version": "8.0.1.0.0",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "website": "https://simetri-sinergi.id",
    "category": "Localization",
    "depends": [
        "l10n_id_taxform_bukti_potong_pph_23",
        "l10n_id_taxform_bukti_potong_pph_common_operating_unit",
    ],
    "data": [
        "security/bukti_potong_pph_23_in_security.xml",
        "security/bukti_potong_pph_23_out_security.xml",
    ],
    "installable": True,
    "auto_install": True,
}
