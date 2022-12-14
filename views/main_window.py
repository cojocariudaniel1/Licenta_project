# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(928, 754)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 145, 781, 551))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.kanban = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.kanban.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.kanban.setContentsMargins(0, 0, 0, 0)
        self.kanban.setObjectName("kanban")
        self.background_color = QtWidgets.QLabel(Form)
        self.background_color.setGeometry(QtCore.QRect(0, 0, 931, 754))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.background_color.sizePolicy().hasHeightForWidth())
        self.background_color.setSizePolicy(sizePolicy)
        self.background_color.setStyleSheet("background-color: rgb(246, 247, 250);")
        self.background_color.setText("")
        self.background_color.setObjectName("background_color")
        self.create_customer = QtWidgets.QPushButton(Form)
        self.create_customer.setGeometry(QtCore.QRect(20, 30, 121, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create_customer.sizePolicy().hasHeightForWidth())
        self.create_customer.setSizePolicy(sizePolicy)
        self.create_customer.setStyleSheet("background-color: rgb(174, 139, 137);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.create_customer.setObjectName("create_customer")
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
        self.antet_color.setGeometry(QtCore.QRect(0, 0, 931, 756))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.antet_color.sizePolicy().hasHeightForWidth())
        self.antet_color.setSizePolicy(sizePolicy)
        self.antet_color.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.antet_color.setText("")
        self.antet_color.setObjectName("antet_color")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(390, 10, 121, 31))
        self.label.setStyleSheet("font: 63 14pt \"Lucida Bright\";")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(590, 70, 51, 31))
        self.label_3.setStyleSheet("font: 63 12pt \"Lucida Bright\";")
        self.label_3.setObjectName("label_3")
        self.list_deselect = QtWidgets.QLabel(Form)
        self.list_deselect.setGeometry(QtCore.QRect(839, 60, 31, 31))
        self.list_deselect.setStyleSheet("font: 63 12pt \"Lucida Bright\";")
        self.list_deselect.setText("")
        self.list_deselect.setPixmap(QtGui.QPixmap("C:/Users/Daniel/Desktop/odoo/icon_lista.png"))
        self.list_deselect.setObjectName("list_deselect")
        self.kanban_deselect = QtWidgets.QLabel(Form)
        self.kanban_deselect.setGeometry(QtCore.QRect(870, 60, 31, 31))
        self.kanban_deselect.setStyleSheet("font: 63 12pt \"Lucida Bright\";")
        self.kanban_deselect.setText("")
        self.kanban_deselect.setPixmap(QtGui.QPixmap("C:/Users/Daniel/Desktop/odoo/kanbank_ne_select.png"))
        self.kanban_deselect.setObjectName("kanban_deselect")
        self.kanban_select = QtWidgets.QLabel(Form)
        self.kanban_select.setGeometry(QtCore.QRect(870, 60, 31, 31))
        self.kanban_select.setStyleSheet("font: 63 12pt \"Lucida Bright\";")
        self.kanban_select.setText("")
        self.kanban_select.setPixmap(QtGui.QPixmap("C:/Users/Daniel/Desktop/odoo/kanban_select.png"))
        self.kanban_select.setObjectName("kanban_select")
        self.list_select = QtWidgets.QLabel(Form)
        self.list_select.setGeometry(QtCore.QRect(839, 60, 31, 31))
        self.list_select.setStyleSheet("font: 63 12pt \"Lucida Bright\";")
        self.list_select.setText("")
        self.list_select.setPixmap(QtGui.QPixmap("C:/Users/Daniel/Desktop/odoo/list_select.png"))
        self.list_select.setObjectName("list_select")
        self.kanban_bg_color_3 = QtWidgets.QLabel(Form)
        self.kanban_bg_color_3.setGeometry(QtCore.QRect(20, 120, 887, 601))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kanban_bg_color_3.sizePolicy().hasHeightForWidth())
        self.kanban_bg_color_3.setSizePolicy(sizePolicy)
        self.kanban_bg_color_3.setSizeIncrement(QtCore.QSize(0, 0))
        self.kanban_bg_color_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.kanban_bg_color_3.setText("")
        self.kanban_bg_color_3.setObjectName("kanban_bg_color_3")
        self.tree_view_widget_client = QtWidgets.QTreeWidget(Form)
        self.tree_view_widget_client.setGeometry(QtCore.QRect(40, 140, 847, 561))
        self.tree_view_widget_client.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tree_view_widget_client.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tree_view_widget_client.setAutoScrollMargin(16)
        self.tree_view_widget_client.setAlternatingRowColors(False)
        self.tree_view_widget_client.setAnimated(True)
        self.tree_view_widget_client.setObjectName("tree_view_widget_client")
        item_0 = QtWidgets.QTreeWidgetItem(self.tree_view_widget_client)
        item_0 = QtWidgets.QTreeWidgetItem(self.tree_view_widget_client)
        self.tree_view_widget_client.header().setVisible(True)
        self.tree_view_widget_client.header().setCascadingSectionResizes(False)
        self.tree_view_widget_client.header().setHighlightSections(False)
        self.tree_view_widget_client.header().setSortIndicatorShown(True)
        self.background_color.raise_()
        self.kanban_bg_color_3.raise_()
        self.antet_color.raise_()
        self.gridLayoutWidget.raise_()
        self.create_customer.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.line_5.raise_()
        self.line_6.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.list_deselect.raise_()
        self.kanban_deselect.raise_()
        self.kanban_select.raise_()
        self.list_select.raise_()
        self.tree_view_widget_client.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.create_customer.setText(_translate("Form", "CREATE"))
        self.label.setText(_translate("Form", "Costumers"))
        self.label_3.setText(_translate("Form", "Filter"))
        self.tree_view_widget_client.setSortingEnabled(True)
        self.tree_view_widget_client.headerItem().setText(0, _translate("Form", "ID"))
        self.tree_view_widget_client.headerItem().setText(1, _translate("Form", "Type_client"))
        self.tree_view_widget_client.headerItem().setText(2, _translate("Form", "Email"))
        self.tree_view_widget_client.headerItem().setText(3, _translate("Form", "Phone"))
        self.tree_view_widget_client.headerItem().setText(4, _translate("Form", "Street"))
        self.tree_view_widget_client.headerItem().setText(5, _translate("Form", "Street Nr"))
        self.tree_view_widget_client.headerItem().setText(6, _translate("Form", "City"))
        self.tree_view_widget_client.headerItem().setText(7, _translate("Form", "District"))
        self.tree_view_widget_client.headerItem().setText(8, _translate("Form", "Country"))
        self.tree_view_widget_client.headerItem().setText(9, _translate("Form", "Web Site"))
        __sortingEnabled = self.tree_view_widget_client.isSortingEnabled()
        self.tree_view_widget_client.setSortingEnabled(False)
        self.tree_view_widget_client.topLevelItem(0).setText(0, _translate("Form", "2"))
        self.tree_view_widget_client.topLevelItem(0).setText(1, _translate("Form", "Juridica"))
        self.tree_view_widget_client.topLevelItem(0).setText(2, _translate("Form", "daniel@gmail.com"))
        self.tree_view_widget_client.topLevelItem(0).setText(3, _translate("Form", "0737462415"))
        self.tree_view_widget_client.topLevelItem(0).setText(4, _translate("Form", "Sfantul Andrei"))
        self.tree_view_widget_client.topLevelItem(0).setText(5, _translate("Form", "74"))
        self.tree_view_widget_client.topLevelItem(0).setText(6, _translate("Form", "Sibiu"))
        self.tree_view_widget_client.topLevelItem(0).setText(7, _translate("Form", "Sibiu"))
        self.tree_view_widget_client.topLevelItem(0).setText(8, _translate("Form", "Romania"))
        self.tree_view_widget_client.topLevelItem(1).setText(0, _translate("Form", "1"))
        self.tree_view_widget_client.topLevelItem(1).setText(1, _translate("Form", "Fizica"))
        self.tree_view_widget_client.topLevelItem(1).setText(2, _translate("Form", "ion@gmail.com"))
        self.tree_view_widget_client.topLevelItem(1).setText(3, _translate("Form", "0734672812"))
        self.tree_view_widget_client.topLevelItem(1).setText(4, _translate("Form", "Lazar"))
        self.tree_view_widget_client.topLevelItem(1).setText(5, _translate("Form", "112"))
        self.tree_view_widget_client.topLevelItem(1).setText(6, _translate("Form", "Iasi"))
        self.tree_view_widget_client.topLevelItem(1).setText(7, _translate("Form", "Iasi"))
        self.tree_view_widget_client.topLevelItem(1).setText(8, _translate("Form", "Romania"))
        self.tree_view_widget_client.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
