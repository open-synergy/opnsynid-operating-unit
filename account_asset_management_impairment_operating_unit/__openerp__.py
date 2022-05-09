# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Asset Management Impairment with Operating Units",
    "version": "8.0.1.0.0",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "website": "https://simetri-sinergi.id",
    "category": "Accounting",
    "depends": [
        "account_asset_management_operating_unit",
        "account_asset_management_impairment",
    ],
    "data": [
        "security/account_asset_impairment_security.xml",
        "security/account_asset_impairment_reversal_security.xml",
    ],
    "installable": True,
    "auto_install": True,
}
