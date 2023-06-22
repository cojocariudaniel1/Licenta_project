# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'products_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1201, 694)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.lb_title = QtWidgets.QLabel(Form)
        self.lb_title.setGeometry(QtCore.QRect(520, 25, 206, 56))
        self.lb_title.setStyleSheet("font: 28pt \"Lucida Bright\";")
        self.lb_title.setObjectName("lb_title")
        self.antet_color = QtWidgets.QLabel(Form)
        self.antet_color.setGeometry(QtCore.QRect(-25, -5, 1226, 781))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.antet_color.sizePolicy().hasHeightForWidth())
        self.antet_color.setSizePolicy(sizePolicy)
        self.antet_color.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.antet_color.setText("")
        self.antet_color.setObjectName("antet_color")
        self.product_layout = QtWidgets.QFrame(Form)
        self.product_layout.setGeometry(QtCore.QRect(27, 195, 1146, 481))
        self.product_layout.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.product_layout.setFrameShadow(QtWidgets.QFrame.Raised)
        self.product_layout.setObjectName("product_layout")
        self.btn_close_product = QtWidgets.QPushButton(Form)
        self.btn_close_product.setGeometry(QtCore.QRect(985, 95, 186, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_close_product.sizePolicy().hasHeightForWidth())
        self.btn_close_product.setSizePolicy(sizePolicy)
        self.btn_close_product.setStyleSheet("background-color: rgb(174, 139, 137);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.btn_close_product.setObjectName("btn_close_product")
        self.search_product_cb = QtWidgets.QLineEdit(Form)
        self.search_product_cb.setGeometry(QtCore.QRect(965, 160, 201, 26))
        self.search_product_cb.setStatusTip("")
        self.search_product_cb.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.search_product_cb.setObjectName("search_product_cb")
        self.lb_search_product = QtWidgets.QLabel(Form)
        self.lb_search_product.setGeometry(QtCore.QRect(805, 145, 151, 51))
        self.lb_search_product.setStyleSheet("font: 15pt \"Lucida Bright\";")
        self.lb_search_product.setObjectName("lb_search_product")
        self.btn_save_sale = QtWidgets.QPushButton(Form)
        self.btn_save_sale.setGeometry(QtCore.QRect(15, 95, 186, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save_sale.sizePolicy().hasHeightForWidth())
        self.btn_save_sale.setSizePolicy(sizePolicy)
        self.btn_save_sale.setStyleSheet("background-color: rgb(174, 139, 137);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.btn_save_sale.setObjectName("btn_save_sale")
        self.btn_create_products = QtWidgets.QPushButton(Form)
        self.btn_create_products.setGeometry(QtCore.QRect(15, 95, 186, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_create_products.sizePolicy().hasHeightForWidth())
        self.btn_create_products.setSizePolicy(sizePolicy)
        self.btn_create_products.setStyleSheet("background-color: rgb(174, 139, 137);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.btn_create_products.setObjectName("btn_create_products")
        self.antet_color.raise_()
        self.lb_title.raise_()
        self.product_layout.raise_()
        self.btn_close_product.raise_()
        self.search_product_cb.raise_()
        self.lb_search_product.raise_()
        self.btn_save_sale.raise_()
        self.btn_create_products.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lb_title.setText(_translate("Form", "Products"))
        self.btn_close_product.setText(_translate("Form", "CLOSE"))
        self.lb_search_product.setText(_translate("Form", "Search Product"))
        self.btn_save_sale.setText(_translate("Form", "SAVE"))
        self.btn_create_products.setText(_translate("Form", "CREATE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
