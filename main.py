import sys
from PySide2.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QLineEdit, QLabel
from PySide2 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

import validate
import compute


class Window(QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.setWindowTitle("Function Plotter")
        self.setMinimumWidth(600)
        self.setMinimumHeight(400)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        self.toolbar = NavigationToolbar(self.canvas, self)

        self.button = QPushButton('Plot')

        self.fx = QLabel("<h2>Function Plotter</h2>")
        self.fx.setAlignment(QtCore.Qt.AlignCenter)

        self.f = QLineEdit()
        self.f.setPlaceholderText('Enter the Function')
        self.f.setAlignment(QtCore.Qt.AlignCenter)

        self.xmin = QLineEdit()
        self.xmin.setPlaceholderText('Enter Lower Limit')
        self.xmin.setAlignment(QtCore.Qt.AlignCenter)


        self.xmax = QLineEdit()
        self.xmax.setPlaceholderText('Enter Upper Limit')
        self.xmax.setAlignment(QtCore.Qt.AlignCenter)

        self.button.clicked.connect(self.plot)
        layout = QVBoxLayout()

        layout.addWidget(self.fx)

        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        layout.addWidget(self.f)
        layout.addWidget(self.xmin)
        layout.addWidget(self.xmax)

        layout.addWidget(self.button)

        self.setLayout(layout)

    # this function is called whenever the button is clicked
    def plot(self):
        # get data from textboxes and send to compute.py
        if not validate.validate_func(self.f.text()):
            validate.make_message("Invalid function", "Only numbers (0-9), operators (+, -, *, /) "
                                                      "and the variable X are allowed")
        elif not validate.validate_x(self.xmin.text()):
            validate.make_message("Error", "Please Enter a valid value for lower limit")
        elif not validate.validate_x(self.xmax.text()):
            validate.make_message("Error", "Please Enter a valid value for upper limit")
        else:
            self.fx.setText("<h2> f (x) = " + self.f.text() + " </h2>")
            x, func = compute.comp(self.f.text(), int(self.xmin.text()), int(self.xmax.text()))
            # clear old figure
            self.figure.clear()

            # create an axis
            ax = self.figure.add_subplot(111)

            # plot data
            ax.plot(x, func)

            # refresh canvas
            self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
