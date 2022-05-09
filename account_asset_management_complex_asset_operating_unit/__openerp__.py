# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Complex Fixed Assets Management with Operating Units",
    "version": "8.0.1.0.0",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "website": "https://simetri-sinergi.id",
    "category": "Accounting",
    "depends": [
        "account_asset_management_operating_unit",
        "account_asset_management_complex_asset",
    ],
    "data": [
        "security/account_complex_asset_removal_security.xml",
        "security/account_complex_asset_installation_security.xml",
    ],
    "installable": True,
    "auto_install": True,
}
