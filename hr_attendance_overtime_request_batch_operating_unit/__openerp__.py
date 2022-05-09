# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Indonesia - Overtime Request Batches " "with Operating Units",
    "version": "8.0.1.0.0",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "website": "https://simetri-sinergi.id",
    "category": "Localization",
    "depends": ["hr_attendance_overtime_request_batch", "operating_unit"],
    "data": [
        "security/hr_overtime_request_batch_security.xml",
        "views/hr_overtime_request_batch_views.xml",
    ],
    "installable": True,
    "auto_install": True,
}
