import re
from PySide2.QtWidgets import QMessageBox


def validate_func(string):
    # accept only numbers, x, brackets () or the mathematical operators +, -, *, /

    regex = "(?:[0-9-+ * / ^ () x X])+"
    return bool(re.findall(regex, string))


def validate_x(string):
    # accept only numbers, x, brackets () or the mathematical operators +, -, *, /
    regex = "(?:[0-9-])+"
    return bool(re.match(regex, string))


def make_message(title, text):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setIcon(QMessageBox.Warning)
    msg.setText(title)
    msg.setInformativeText(text)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.show()
    msg.exec_()