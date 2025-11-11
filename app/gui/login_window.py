import sys
import os
from tkinter.messagebox import showerror

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi
from app.database.db_connection import Database

class LoginWindow(QtWidgets.QStackedWidget):
    def __init__(self):
        super(LoginWindow, self).__init__()
        ui_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "login_window.ui")
        loadUi(ui_path, self)

# -----------------------------------------------Add Shadows-------------------------------------------------------------
        self.shadows(self.username_entry, blur_radius=15, x_offset=0, y_offset=0, color=(0, 0, 0, 100))
        self.shadows(self.password_entry, blur_radius=15, x_offset=0, y_offset=0, color=(0, 0, 0, 100))
        self.shadows(self.label_2, blur_radius=50, x_offset=0, y_offset=0, color=(0, 0, 0, 250))
        self.shadows(self.log_in, blur_radius=5, x_offset=0, y_offset=0, color=(0, 0, 0, 100))

    def shadows(self, widget, blur_radius=15, x_offset=0, y_offset=0, color=(0,0,0,150)):
        shadow = QtWidgets.QGraphicsDropShadowEffect(widget)
        shadow.setBlurRadius(blur_radius)
        shadow.setXOffset(x_offset)
        shadow.setYOffset(y_offset)
        shadow.setColor(QtGui.QColor(*color))
        widget.setGraphicsEffect(shadow)

class SignUpWindow(QtWidgets.QStackedWidget):
    def __init__(self):
        super(SignUpWindow, self).__init__()
        ui_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "signup_window.ui")
        loadUi(ui_path, self)

# -----------------------------------------------Add Shadows and Styles-------------------------------------------------
        self.setStyleSheet("""
            QLineEdit#signUsername::placeholder,
            QLineEdit#signPassword::placeholder,
            QLineEdit#confirmPass::placeholder {
                color: rgba(255, 255, 255, 150);
                font: 8pt "MS Shell Dlg 2";
            }
        """)
        self.shadows(self.signupButton, blur_radius=15, x_offset=0, y_offset=0, color=(0,0,0,150))
        self.shadows(self.signUsername, blur_radius=15, x_offset=0, y_offset=0, color=(0,0,0,250))
        self.shadows(self.signPassword, blur_radius=15, x_offset=0, y_offset=0, color=(0,0,0,100))
        self.shadows(self.confirmPass, blur_radius=15, x_offset=0, y_offset=0, color=(0,0,0,250))
        self.shadows(self.signTable, blur_radius=50, x_offset=0, y_offset=0, color=(0,0,0,250))

        self.signupButton.clicked.connect(self.Sign_Up)

    def shadows(self, widget, blur_radius=15, x_offset=0, y_offset=0, color=(0, 0, 0, 150)):
        shadow = QtWidgets.QGraphicsDropShadowEffect(widget)
        shadow.setBlurRadius(blur_radius)
        shadow.setXOffset(x_offset)
        shadow.setYOffset(y_offset)
        shadow.setColor(QtGui.QColor(*color))
        widget.setGraphicsEffect(shadow)

    def get_account(self):
        username = self.signUsername.text()
        password = self.signPassword.text()
        return username, password

    def Sign_Up(self):
        if len(self.signUsername.text()) == 0 or len(self.signPassword.text()) == 0:
            QMessageBox.showMessage("Please enter your username and password.", QMessageBox.Yes)
        elif self.signPassword.text() != self.confirmPass.text():
            print("Password and Confirm Password don't match")
        else:
            username, password = self.get_account()
            print(username, password)