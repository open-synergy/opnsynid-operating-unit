# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Account Asset Management with Operating Units",
    "version": "8.0.1.0.0",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "website": "https://opensynergy-indonesia.com",
    "category": "Accounting",
    "depends": [
        "account_operating_unit",
        "account_asset_management_extend"
    ],
    "data": [
        "security/account_asset_asset_security.xml",
        "views/account_asset_asset_views.xml"
    ],
    "installable": True,
    "auto_install": True
}
