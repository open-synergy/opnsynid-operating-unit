# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Asset Management Retirement by Scrap with Operating Units",
    "version": "8.0.1.0.0",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "website": "https://opensynergy-indonesia.com",
    "category": "Accounting",
    "depends": [
        "account_asset_management_operating_unit",
        "account_asset_management_retirement_by_scrap"
    ],
    "data": [
        "security/account_asset_retirement_by_scrap_security.xml"
    ],
    "installable": True,
    "auto_install": True
}
