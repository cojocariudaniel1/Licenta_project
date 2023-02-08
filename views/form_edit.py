# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_edit.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(932, 761)
        self.background_color = QtWidgets.QLabel(Form)
        self.background_color.setGeometry(QtCore.QRect(0, 0, 931, 761))
        self.background_color.setStyleSheet("background-color: rgb(246, 247, 250);")
        self.background_color.setText("")
        self.background_color.setObjectName("background_color")
        self.save_button = QtWidgets.QPushButton(Form)
        self.save_button.setGeometry(QtCore.QRect(20, 30, 121, 41))
        self.save_button.setStyleSheet("background-color: rgb(174, 139, 137);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.save_button.setObjectName("save_button")
        self.kanban_bg_color = QtWidgets.QLabel(Form)
        self.kanban_bg_color.setGeometry(QtCore.QRect(20, 120, 887, 601))
        self.kanban_bg_color.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.kanban_bg_color.setText("")
        self.kanban_bg_color.setObjectName("kanban_bg_color")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(20, 120, 889, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(20, 121, 3, 602))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(20, 722, 889, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(908, 121, 3, 604))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setGeometry(QtCore.QRect(0, 110, 1000, 3))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(Form)
        self.line_6.setGeometry(QtCore.QRect(-30, 731, 1000, 3))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.antet_color = QtWidgets.QLabel(Form)
        self.antet_color.setGeometry(QtCore.QRect(-20, 0, 971, 111))
        self.antet_color.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.antet_color.setText("")
        self.antet_color.setObjectName("antet_color")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(390, 10, 131, 31))
        self.label.setStyleSheet("font: 63 14pt \"Lucida Bright\";")
        self.label.setObjectName("label")
        self.rb_fizica = QtWidgets.QRadioButton(Form)
        self.rb_fizica.setGeometry(QtCore.QRect(260, 145, 101, 31))
        self.rb_fizica.setStyleSheet("font: 63 14pt \"Lucida Bright\";")
        self.rb_fizica.setObjectName("rb_fizica")
        self.rb_juridica = QtWidgets.QRadioButton(Form)
        self.rb_juridica.setGeometry(QtCore.QRect(390, 145, 131, 31))
        self.rb_juridica.setStyleSheet("font: 63 14pt \"Lucida Bright\";")
        self.rb_juridica.setObjectName("rb_juridica")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 145, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.street_label = QtWidgets.QLabel(Form)
        self.street_label.setGeometry(QtCore.QRect(130, 290, 61, 31))
        self.street_label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.street_label.setObjectName("street_label")
        self.judet_label = QtWidgets.QLabel(Form)
        self.judet_label.setGeometry(QtCore.QRect(130, 335, 51, 31))
        self.judet_label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.judet_label.setObjectName("judet_label")
        self.country_label = QtWidgets.QLabel(Form)
        self.country_label.setGeometry(QtCore.QRect(490, 380, 51, 31))
        self.country_label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.country_label.setObjectName("country_label")
        self.nr_street_label = QtWidgets.QLabel(Form)
        self.nr_street_label.setGeometry(QtCore.QRect(490, 290, 41, 31))
        self.nr_street_label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.nr_street_label.setObjectName("nr_street_label")
        self.cod_postal = QtWidgets.QLabel(Form)
        self.cod_postal.setGeometry(QtCore.QRect(490, 335, 111, 31))
        self.cod_postal.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.cod_postal.setObjectName("cod_postal")
        self.oras_label = QtWidgets.QLabel(Form)
        self.oras_label.setGeometry(QtCore.QRect(130, 380, 61, 31))
        self.oras_label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.oras_label.setObjectName("oras_label")
        self.telefon_label = QtWidgets.QLabel(Form)
        self.telefon_label.setGeometry(QtCore.QRect(490, 425, 71, 31))
        self.telefon_label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.telefon_label.setObjectName("telefon_label")
        self.web_site_label = QtWidgets.QLabel(Form)
        self.web_site_label.setGeometry(QtCore.QRect(130, 425, 81, 31))
        self.web_site_label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.web_site_label.setObjectName("web_site_label")
        self.web_site_label_2 = QtWidgets.QLabel(Form)
        self.web_site_label_2.setGeometry(QtCore.QRect(490, 245, 61, 31))
        self.web_site_label_2.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.web_site_label_2.setObjectName("web_site_label_2")
        self.street_input = QtWidgets.QLineEdit(Form)
        self.street_input.setGeometry(QtCore.QRect(210, 295, 241, 20))
        self.street_input.setMinimumSize(QtCore.QSize(100, 0))
        self.street_input.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.street_input.setText("")
        self.street_input.setObjectName("street_input")
        self.judet_input = QtWidgets.QLineEdit(Form)
        self.judet_input.setGeometry(QtCore.QRect(210, 340, 113, 20))
        self.judet_input.setMinimumSize(QtCore.QSize(100, 0))
        self.judet_input.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.judet_input.setText("")
        self.judet_input.setObjectName("judet_input")
        self.country_input = QtWidgets.QLineEdit(Form)
        self.country_input.setGeometry(QtCore.QRect(580, 385, 113, 20))
        self.country_input.setMinimumSize(QtCore.QSize(100, 0))
        self.country_input.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.country_input.setText("")
        self.country_input.setObjectName("country_input")
        self.nr_street_input = QtWidgets.QLineEdit(Form)
        self.nr_street_input.setGeometry(QtCore.QRect(580, 295, 50, 20))
        self.nr_street_input.setMinimumSize(QtCore.QSize(50, 0))
        self.nr_street_input.setMaximumSize(QtCore.QSize(50, 16777215))
        self.nr_street_input.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.nr_street_input.setText("")
        self.nr_street_input.setObjectName("nr_street_input")
        self.zip_code_input = QtWidgets.QLineEdit(Form)
        self.zip_code_input.setGeometry(QtCore.QRect(580, 340, 113, 20))
        self.zip_code_input.setMinimumSize(QtCore.QSize(100, 0))
        self.zip_code_input.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.zip_code_input.setText("")
        self.zip_code_input.setObjectName("zip_code_input")
        self.oras_input = QtWidgets.QLineEdit(Form)
        self.oras_input.setGeometry(QtCore.QRect(210, 385, 113, 20))
        self.oras_input.setMinimumSize(QtCore.QSize(100, 0))
        self.oras_input.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.oras_input.setText("")
        self.oras_input.setObjectName("oras_input")
        self.telefon_input = QtWidgets.QLineEdit(Form)
        self.telefon_input.setGeometry(QtCore.QRect(580, 430, 191, 20))
        self.telefon_input.setMinimumSize(QtCore.QSize(100, 0))
        self.telefon_input.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.telefon_input.setText("")
        self.telefon_input.setObjectName("telefon_input")
        self.name_label = QtWidgets.QLabel(Form)
        self.name_label.setGeometry(QtCore.QRect(130, 245, 61, 31))
        self.name_label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.name_label.setObjectName("name_label")
        self.name_input = QtWidgets.QLineEdit(Form)
        self.name_input.setGeometry(QtCore.QRect(210, 250, 241, 21))
        self.name_input.setMinimumSize(QtCore.QSize(100, 0))
        self.name_input.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.name_input.setInputMask("")
        self.name_input.setText("")
        self.name_input.setPlaceholderText("")
        self.name_input.setObjectName("name_input")
        self.street_label_2 = QtWidgets.QLabel(Form)
        self.street_label_2.setGeometry(QtCore.QRect(130, 195, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.street_label_2.setFont(font)
        self.street_label_2.setMouseTracking(False)
        self.street_label_2.setStyleSheet("")
        self.street_label_2.setObjectName("street_label_2")
        self.email_input = QtWidgets.QLineEdit(Form)
        self.email_input.setGeometry(QtCore.QRect(580, 250, 191, 20))
        self.email_input.setMinimumSize(QtCore.QSize(100, 0))
        self.email_input.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.email_input.setText("")
        self.email_input.setObjectName("email_input")
        self.web_site_input = QtWidgets.QLineEdit(Form)
        self.web_site_input.setGeometry(QtCore.QRect(210, 430, 191, 20))
        self.web_site_input.setMinimumSize(QtCore.QSize(100, 0))
        self.web_site_input.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.web_site_input.setText("")
        self.web_site_input.setObjectName("web_site_input")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(492, 171, 100, 16))
        self.label_9.setMinimumSize(QtCore.QSize(100, 0))
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.close_button = QtWidgets.QPushButton(Form)
        self.close_button.setGeometry(QtCore.QRect(760, 30, 121, 41))
        self.close_button.setStyleSheet("background-color: rgb(174, 139, 137);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.close_button.setObjectName("close_button")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(120, 486, 130, 31))
        self.label_3.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"border-top: 1px solid;\n"
"border-top-color: rgb(174, 139, 137);\n"
"border-left: 1px solid;\n"
"border-left-color: rgb(160,160,160);\n"
"border-right: 1px solid;\n"
"border-right-color: rgb(160,160,160);\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(249, 486, 130, 31))
        self.label_4.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"border-top: 1px solid;\n"
"border-top-color:rgb(160,160,160);\n"
"border-left: 1px solid;\n"
"border-left-color: rgb(160,160,160);\n"
"border-right: 1px solid;\n"
"border-right-color: rgb(160,160,160);\n"
"border-bottom: 1px solid;\n"
"border-bottom-color: rgb(160,160,160);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 486, 101, 31))
        self.label_5.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"border-top: 1px solid white;\n"
"border-bottom: 1px solid;\n"
"border-bottom-color: rgb(160,160,160);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(379, 486, 530, 31))
        self.label_6.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"border-top: 1px solid white;\n"
"border-bottom: 1px solid;\n"
"border-bottom-color: rgb(160,160,160);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.image = QtWidgets.QLabel(Form)
        self.image.setGeometry(QtCore.QRect(795, 130, 100, 100))
        self.image.setText("")
        self.image.setObjectName("image")
        self.btn_upload_image = QtWidgets.QPushButton(Form)
        self.btn_upload_image.setGeometry(QtCore.QRect(630, 150, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(1)
        self.btn_upload_image.setFont(font)
        self.btn_upload_image.setStyleSheet("background-color: rgb(174, 139, 137);\n"
"color: rgb(255, 255, 255);\n"
"font: 50 8 \"MS Shell Dlg 2\";")
        self.btn_upload_image.setObjectName("btn_upload_image")
        self.label_9.raise_()
        self.background_color.raise_()
        self.kanban_bg_color.raise_()
        self.antet_color.raise_()
        self.save_button.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.line_5.raise_()
        self.line_6.raise_()
        self.label.raise_()
        self.rb_fizica.raise_()
        self.rb_juridica.raise_()
        self.label_2.raise_()
        self.street_label.raise_()
        self.judet_label.raise_()
        self.country_label.raise_()
        self.nr_street_label.raise_()
        self.cod_postal.raise_()
        self.oras_label.raise_()
        self.telefon_label.raise_()
        self.web_site_label.raise_()
        self.web_site_label_2.raise_()
        self.street_input.raise_()
        self.judet_input.raise_()
        self.country_input.raise_()
        self.nr_street_input.raise_()
        self.zip_code_input.raise_()
        self.oras_input.raise_()
        self.telefon_input.raise_()
        self.name_label.raise_()
        self.name_input.raise_()
        self.street_label_2.raise_()
        self.email_input.raise_()
        self.web_site_input.raise_()
        self.close_button.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.image.raise_()
        self.btn_upload_image.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.save_button.setText(_translate("Form", "SAVE"))
        self.label.setText(_translate("Form", "Editare client"))
        self.rb_fizica.setText(_translate("Form", "Fizica"))
        self.rb_juridica.setText(_translate("Form", "Juridica"))
        self.label_2.setText(_translate("Form", "Persoana:"))
        self.street_label.setText(_translate("Form", "Strada*"))
        self.judet_label.setText(_translate("Form", "Judet*"))
        self.country_label.setText(_translate("Form", "Tara*"))
        self.nr_street_label.setText(_translate("Form", "Nr*"))
        self.cod_postal.setText(_translate("Form", "Cod postal*"))
        self.oras_label.setText(_translate("Form", "Oras*"))
        self.telefon_label.setText(_translate("Form", "Telefon*"))
        self.web_site_label.setText(_translate("Form", "Web Site"))
        self.web_site_label_2.setText(_translate("Form", "Email"))
        self.name_label.setText(_translate("Form", "Nume*"))
        self.street_label_2.setText(_translate("Form", "Contact"))
        self.close_button.setText(_translate("Form", "ANULEAZA"))
        self.label_3.setText(_translate("Form", "Accounting"))
        self.label_4.setText(_translate("Form", "Internal Notes"))
        self.btn_upload_image.setText(_translate("Form", "Upload Image"))
