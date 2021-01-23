import pytest

from PySide2 import QtCore

import main


@pytest.fixture
def app(qtbot):
    test_app = main.Window()
    qtbot.addWidget(test_app)
    return test_app


def test_label(app):
    assert app.fx.text() == "<h2>Function Plotter</h2>"


def test_label_after_click(app, qtbot):
    app.f.setText("x")
    app.xmin.setText("0")
    app.xmax.setText("2")
    qtbot.mouseClick(app.button, QtCore.Qt.LeftButton)
    assert app.fx.text() == "<h2> f (x) = " + app.f.text() + " </h2>"