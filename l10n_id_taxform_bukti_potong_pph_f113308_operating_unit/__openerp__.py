# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Indonesia - Bukti Potong PPh Pasal 26 (f.1.1.33.08)"
    "with Operating Units",
    "version": "8.0.1.0.0",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "website": "https://simetri-sinergi.id",
    "category": "Localization",
    "depends": [
        "l10n_id_taxform_bukti_potong_pph_f113308",
        "l10n_id_taxform_bukti_potong_pph_common_operating_unit",
    ],
    "data": [
        "security/bukti_potong_pph_f113308_in_security.xml",
        "security/bukti_potong_pph_f113308_out_security.xml",
    ],
    "installable": True,
    "auto_install": True,
}
