import sys
from pathlib import Path
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import QPropertyAnimation, QPoint, QObject, QEvent
from PyQt5.QtGui import (QFont, QFontDatabase, QColor, QIcon)
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QMessageBox, QComboBox
import sqlite3
from app.assets import res_rc
from app.database.db_connection import Database, database
from app.utils.util import (MyWindow, HoverShadow, load_font, setupComboBox)

class FillupWindow(MyWindow):
    def __init__(self):
        super().__init__()
        self.setup_paths()
        self.setup_ui()
        self.Set_up_comboBox()
        self.setupFontsandICons()
        self.setup_shadows()
        self.submitbtn.clicked.connect(lambda : print(self.college_setup.get_selected_value()))


        #-------------------------------------------- This setups the paths ----------------
    def setup_paths(self):
        current_file_path = Path(__file__).resolve()
        self.project_root = current_file_path.parent.parent
        asset_paths = {
            'ui': self.project_root / 'assets' / 'signupform.ui',
            'isb_font': self.project_root / 'assets' / 'InclusiveSans-Bold.ttf',
            'isr_font': self.project_root / 'assets' / 'InclusiveSans-Regular.ttf'
        }
        for key, path in asset_paths.items():
            if not path.exists():
                raise FileNotFoundError(f"Required file not found: {path}")
            setattr(self, f"{key}_path", path)


        self.password_states = {}

        #-------------------------------------------- This setups the UI -------------------
    def setup_ui(self):
        uic.loadUi(self.ui_path, self)
        self.database = Database()

########################################## STYLE AREA ###############################################
    # -------------------------------------------- This setups the stylized fonts ----------------
    def setupFontsandICons(self):
        self.largelabel_font = load_font(self.isb_font_path, 32, bold=True)
        self.mediumlabel_font = load_font(self.isb_font_path, 14, bold=True)
        self.field_font = load_font(self.isr_font_path, 10, bold=False)

        font_map = {
            self.largelabel_font: [self.Title],
            self.mediumlabel_font: [self.submitbtn],
            self.field_font: [self.firstname, self.lastname, self.mi, self.suffix, self.civilstatus, self.sex,
                              self.birthday, self.age, self.studentID, self.college, self.yearlevel, self.program,
                              self.municipality, self.phoneno]
        }
        for font, widgets in font_map.items():
            for widget in widgets:
                widget.setFont(font)

    # -------------------------------------------- This setups the hover shadows ----------------
    def setup_shadows(self):
        widgets_to_shadow = [
            self.firstname, self.lastname, self.mi, self.suffix, self.civilstatus, self.sex,
            self.birthday, self.age, self.studentID, self.college, self.yearlevel, self.program,
            self.municipality, self.phoneno, self.submitbtn,  self.profilephoto
        ]
        for widget in widgets_to_shadow:
            HoverShadow(widget)

    # -------------------------------------------- This setups the ComboBox ---------------------
    def Set_up_comboBox(self):
        self.civilstatuses = ["Single", "Married", "Divorced/Annulled", "Widowed"]
        self.genders = ["Male", "Female", "Other"]
        self.colleges = ["CICS", "BSN", "CAS", "CABEIHM", "CJE"]
        self.years = ["1st - Year", "2nd - Year", "3rd - Year", "4th - Year"]
        self.municipalities = ["Balayan","Calaca", "Calatagan", "Lemery", "Nasugbu", "Tuy"]

        self.program_data = {
            "CICS": ["BSIT", "COMENG", "COMSCI"],
            "BSN": ["NURSING", "CRIM", "MASSCOM"],
            "CAS": ["PSYCH", "SOCIOLOGY"],
            "CABEIHM": ["BSED", "BEED"],
            "CJE": ["LAW", "POLSCI"]
        }

        self.civil_status_setup = setupComboBox(self.civilstatus, self.civilstatuses, "Civil Status")
        self.sex_setup = setupComboBox(self.sex, self.genders, "Gender")

        self.college_setup = setupComboBox(self.college, self.colleges, "College")
        self.program_setup = setupComboBox(self.program, [], "Program")
        self.yearlevel_setup = setupComboBox(self.yearlevel, self.years, "Year Level")
        self.municipality_setup = setupComboBox(self.municipality, self.municipalities, "Municipality")
        self.college.currentTextChanged.connect(self.updateProgramComboBox)
        self.program.setEnabled(False)
    def updateProgramComboBox(self, selected_college_name: str):

        programs_list = self.program_data.get(selected_college_name)
        self.program.clear()

        if programs_list:
            self.program.setEnabled(True)
            setupComboBox(self.program, programs_list, "Program")
        else:
            self.program.setEnabled(False)
            self.program.addItem("Program")
            self.program.setCurrentIndex(0)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = FillupWindow()
    dialog.show()
    sys.exit(app.exec_())