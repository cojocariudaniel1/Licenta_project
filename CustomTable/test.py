import logging
import random
import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QEvent, QRect, QObject, pyqtSignal, QPoint
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFrame, QLabel, QLineEdit, QPushButton

from base import Session
from model.custom_classes.custom_radio_button import CustomRadioButtonWidget
from views.sales_view import Ui_Form
import qtmodern.styles
import qtmodern.windows

"""
item header =
{
    "name": value -> string,
    "sortable": value -> bool,
    "width": valeu -> int (pixels)
    ""
}

With the widht of value all column values wiill have the same width
                
"""


class HideUserInput(QObject):
    hide_user_input_signal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def eventFilter(self, obj, event):
        try:
            if event.type() == QEvent.MouseButtonPress:
                self.hide_user_input_signal.emit()
                return True
            return False
        except BaseException as e:
            logging.exception(e)


class RowEvent(QObject):
    def __init__(self, row, idx, parent=None):
        super().__init__(parent)
        self.row = row
        self.idx = idx

    def eventFilter(self, obj, event):
        try:
            if event.type() == QEvent.Enter:
                obj.setStyleSheet("#%s {background-color: #f1f1f1; ;border-bottom: 1px solid #e9ecef;}" % self.row)
                return True
            if event.type() == QEvent.Leave:
                if self.idx % 2 == 0:
                    obj.setStyleSheet("#%s {background-color: #fcfcfc ;border-bottom: 1px solid #e9ecef;} " % self.row)
                else:
                    obj.setStyleSheet("#%s {background-color: #ffffff ;border-bottom: 1px solid #e9ecef;} " % self.row)

                return True
            return False
        except BaseException as e:
            logging.exception(e)


class ClickableLabel(QObject):
    click_label_signal = pyqtSignal(str)

    def __init__(self, main_parent=None, parent=None):
        super().__init__(parent)
        self.main_parent = main_parent

    def eventFilter(self, obj, event):
        try:
            if event.type() == QEvent.MouseButtonPress:
                self.signal_edit_label.emit(
                    [obj.text(), [obj.x(), obj.y(), obj.width(), obj.height()], self.main_parent, obj.objectName()])
                return True

            return False
        except BaseException as e:
            logging.exception(e)


class EditableLabel(QObject):
    signal_edit_label = pyqtSignal(list)

    def __init__(self, main_parent=None, parent=None):
        super().__init__(parent)
        self.main_parent = main_parent

    def eventFilter(self, obj, event):
        try:
            if event.type() == QEvent.MouseButtonPress:
                self.signal_edit_label.emit(
                    [obj.text(), [obj.x(), obj.y(), obj.width(), obj.height()], self.main_parent, obj.objectName()])
                return True

            return False
        except BaseException as e:
            logging.exception(e)


class LabelEvent(QObject):
    end_of_line_signal = pyqtSignal(bool, int)

    def __init__(self, column, idx, parent=None):
        super().__init__(parent)
        self.idx = idx
        self.column = column

    def eventFilter(self, obj, event):
        try:
            if event.type() == QEvent.Enter:
                # acțiunea care se va executa la hover
                obj.setStyleSheet("#%s {background-color: #dde0e3;border-bottom: 0.5x solid gray; }" % self.column)
                self.end_of_line_signal.emit(True, self.idx)

                return True
            if event.type() == QEvent.Leave:
                obj.setStyleSheet(
                    "#%s {background-color: #e9ecef; border-bottom: 0.5px solid gray;}" % self.column)
                self.end_of_line_signal.emit(False, self.idx)
                return True
            return False
        except BaseException as e:
            logging.exception(e)


class CustomTable(QFrame):

    def __init__(self, x, y, width, height, parent=None):
        super().__init__(parent)
        self.header_columns = []
        self.header_objects = []
        self.data = []
        self.row_frames = []
        self.end_of_label_header = []
        self.edit_label_temp = None
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        self.default_height_row = 37
        # [1,37], [2, 37*2], [3,37*3]
        self.number_of_rows = [[1, self.default_height_row]]

        self.header_frame = QFrame(self)
        self.header_frame.setObjectName("rowframe")
        self.header_frame.setGeometry(QRect(0, 0, self.width(), self.default_height_row))
        self.header_frame.setStyleSheet("background-color: #e9ecef")
        # self.header_frame.installEventFilter(MyEventFilter(self.header_frame))
        self.header_span = 5
        self.setUpHeader()
        self.event_hideInput = HideUserInput()
        self.installEventFilter(self.event_hideInput)
        self.event_hideInput.hide_user_input_signal.connect(self.hide_user_input)
        self.test = False
        self.column_events = []

    def hide_user_input(self):
        if self.edit_label_temp is not None:
            self.edit_label_temp.hide()
            self.edit_label_temp = None

    def change_end_line_style(self, value, idx):
        try:
            if value:
                self.end_of_label_header[idx].setStyleSheet(
                    "background-color: #c1c4c7;border-bottom: 0.5px solid #e9ecef;")
            else:
                self.end_of_label_header[idx].setStyleSheet(
                    "background-color: #e9ecef;border-bottom: 0.5px solid gray;")
        except BaseException as e:
            logging.exception(e)

    """ column [0] idx , [1] name"""

    def header(self, _header: list):
        try:
            countinue = True
            for element in _header:
                if len(element) != 2:
                    logging.exception(msg="Format of the Header is incorect eg: name: value, width: value")
                else:
                    try:
                        k = element["name"]
                        j = element["width"]
                    except BaseException as e:
                        countinue = False
                        logging.exception(e)

            if countinue:
                for idx, item in enumerate(_header):
                    self.header_columns.append([item["name"], item["width"]])
                self.setUpHeader()
        except BaseException as e:
            logging.exception(e)

    def add_item(self):
        pass

    def setUpTable(self):
        # self.data = [[]]
        if len(self.data) > 0:
            for row in self.data:
                if len(row) != len(self.header_columns):
                    logging.exception(msg="Data is not matching the header")
                    sys.exit()

    def redraw_table(self):
        for row in self.row_frames:
            row.deleteLater()

    def QLabelHeader(self, name, x, y, width, height, idx):
        try:
            font = QtGui.QFont("Arial", 11)
            font.setBold(True)

            item = QLabel(f"{name}", self.header_frame)
            item.setObjectName(f"{name}")
            item.setGeometry(QRect(x, y, width, height))

            item.setStyleSheet("#%s {background-color: #e9ecef; border-bottom: 0.5px solid gray;}" % name)

            item.setAlignment(Qt.AlignCenter)
            item.setFont(font)
            # sorting_label = QLabel("\u2191", item)
            # sorting_label.setGeometry(QRect(x+ 30, y, 45, height))
            # sorting_label.setAlignment(QtCore.Qt.AlignCenter)
            # sorting_label.setFont(font)

            label_end_line = QLabel(self.header_frame)
            label_end_line.setObjectName(f"{name}end_line")
            label_end_line.setGeometry(QRect(x + width - 3, y, 3, height, ))
            style1 = "background-color: #e9ecef; border-bottom: 0.5px solid gray;"
            label_end_line.setStyleSheet(style1)
            event = LabelEvent(name, idx, item)
            item.installEventFilter(event)
            event.end_of_line_signal.connect(self.change_end_line_style)
            self.end_of_label_header.append(label_end_line)

            return item
        except BaseException as e:
            logging.exception(e)

    def _QLabelRow(self, name, x, y, width, height, frame_row, idx):
        font = QtGui.QFont("Arial", 11)

        item = QLabel(str(name), frame_row)
        item.setObjectName(f"{name}")
        item.setGeometry(QRect(x, y, width, height))
        # QRect(0,0, 150, 37)
        # item.setStyleSheet(f"background-color: #{random.randint(0, 0xFFFFFF):06x}")
        item.setAlignment(Qt.AlignCenter)
        item.setFont(font)
        for i in self.header_objects:
            if i["idx"] == idx:
                if i["event"] == "editable":
                    event = EditableLabel(frame_row, item)
                    item.installEventFilter(event)
                    event.signal_edit_label.connect(self.edit_label)
                elif i["event"] == "clickable":
                    # event = ClickLabel(frame_row, item)
                    # item.installEventFilter(event)
                    pass

        return item

    def edit_label(self, value: list = None):
        if value:
            label_text = value[0]
            label_name = value[3]
            label_geometry = value[1]
            x, y, width, height = label_geometry
            main_parent = value[2]

            if self.edit_label_temp is not None:
                if self.edit_label_temp.objectName() != label_name:

                    for row in self.data:
                        for column in row:
                            if column.objectName() == self.edit_label_temp.objectName():
                                column.setText(self.edit_label_temp.text())

                self.edit_label_temp.hide()
                self.edit_label_temp = QLineEdit(f"{label_text}", main_parent)
                self.edit_label_temp.setObjectName(label_name)
                self.edit_label_temp.setGeometry(QRect(x, y, width, height))
                self.edit_label_temp.show()
                self.edit_label_temp.setFocus()

            else:
                self.edit_label_temp = QLineEdit(f"{label_text}", main_parent)
                self.edit_label_temp.setObjectName(label_name)
                self.edit_label_temp.setGeometry(QRect(x, y, width, height))
                self.edit_label_temp.show()
                self.edit_label_temp.setFocus()

            print(self.edit_label_temp.objectName(), '323')
        else:
            try:
                if self.edit_label_temp is not None:
                    for row in self.data:
                        for column in row:
                            if column.objectName() == self.edit_label_temp.objectName():
                                column.setText(self.edit_label_temp.text())
                    self.edit_label_temp.hide()
                self.edit_label_temp = None
            except BaseException as e:
                logging.exception(e)

    def _make_row(self, row):
        row_data = []
        last_id_of_row = self.number_of_rows[-1][0]
        current_row = [last_id_of_row + 1, last_id_of_row * self.default_height_row]
        self.number_of_rows.append(current_row)
        row_frame = QFrame(self)
        row_frame.setObjectName(f"{row[0]}")
        row_frame.setGeometry(QRect(0, current_row[1], self.width(), self.default_height_row))
        row_frame.setStyleSheet("background-color: yellow")

        for idx, column in enumerate(row):
            if idx != 0:
                pos_x = 0
                for i in range(int(idx)):
                    pos_x += self.header_columns[i][1]

                k = self._QLabelRow(column, pos_x, 0, self.header_columns[idx][1],
                                    self.default_height_row, row_frame, idx)
                row_data.append(k)
            else:
                k = self._QLabelRow(column, 0, 0, self.header_columns[idx][1], self.default_height_row,
                                    row_frame, idx)
                row_data.append(k)
        self.row_frames.append(row_frame)
        if last_id_of_row % 2 == 0:
            row_frame.setStyleSheet("#%s {background-color: #fcfcfc ;border-bottom: 1px solid #e9ecef;} " % row[0])
        else:
            row_frame.setStyleSheet("#%s {background-color: #ffffff; border-bottom: 1px solid #e9ecef;}" % row[0])
        row_frame.installEventFilter(RowEvent(row[0], last_id_of_row, row_frame))
        self.data.append(row_data)
        self.number_of_rows.append(current_row)

    def add_row(self, row):
        if len(row) != 0:
            if len(row) != len(self.header_columns):

                logging.exception(msg="Data and columns don't match")
                sys.exit()
            else:
                self._make_row(row)
        else:
            logging.exception(msg="Incorect Data : len is 0")
            sys.exit()

    def populate_table(self, data):
        for row in data:
            self.add_row(row)

    def print_data(self):
        pass

    def setUpHeader(self):
        # column[0] -> name of the column, column[1] -> width of the column
        try:
            if len(self.header_columns) > 0:

                for idx, column in enumerate(self.header_columns):
                    if idx != 0:
                        x_pos = 0
                        for i in range(int(idx)):
                            x_pos += self.header_columns[i][1]

                        item = self.QLabelHeader(column[0], x_pos, 0, column[1], self.default_height_row, idx)
                        self.header_objects.append({"idx": idx, "obj": item, "event": None})
                    else:
                        item = self.QLabelHeader(column[0], 0, 0, column[1], self.default_height_row, idx)
                        self.header_objects.append({"idx": idx, "obj": item, "event": None})
            print(self.header_objects)
        except BaseException as e:
            logging.exception(e)


class SalesForm(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.new_window = None
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.tableView = CustomTable(self.ui.sales_view_layout.x, self.ui.sales_view_layout.y,
                                     self.ui.sales_view_layout.width, self.ui.sales_view_layout.width,
                                     self.ui.sales_view_layout)
        self.tableView.setObjectName("tableView")
        header_list = [
            {"name": "Number", "width": 100},
            {"name": "Customer", "width": 500},
            {"name": "Customer", "width": 100},
            {"name": "Customer", "width": 200},

        ]
        self.tableView.header(header_list)
        self.tableView.header_objects[2]["event"] = "editable"

        data = [["tes5", "test6", "test7", "test8"], ["test1", "test2", "test3", "test4"],
                ["tes5", "test6", "test7", "test8"], ["tes5", "test6", "test7", "test8"]]
        self.tableView.populate_table(data)

        self.event_userinput = HideUserInput()
        self.installEventFilter(self.event_userinput)
        self.event_userinput.hide_user_input_signal.connect(self.hide_user_input)
        self.ui.print_btn.clicked.connect(self.tableView.print_data)

    def hide_user_input(self):
        self.tableView.edit_label(None)


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        qtmodern.styles.light(app)
        widget = SalesForm()
        widget.show()
    except BaseException as e:
        logging.exception(e)

    # add the frame to a scroll area

    sys.exit(app.exec_())
