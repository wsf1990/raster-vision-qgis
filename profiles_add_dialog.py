# -*- coding: utf-8 -*-
"""
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt5 import uic
from PyQt5 import QtWidgets

from .settings import Settings

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'profiles_add_dialog_base.ui'))


class ProfilesAddDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        super(ProfilesAddDialog, self).__init__(parent)
        self.setupUi(self)
