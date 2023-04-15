from PySide2.QtWidgets import (QDialog, QLineEdit, QPushButton, QSizePolicy,
                               QGroupBox, QSlider, QHBoxLayout, QScrollArea)
from PySide2.QtCore import (QSize, Qt, Slot)
import numpy as np
import personapercentwindow


class PersonaPerPage(QDialog, personapercentwindow.Ui_PersonaPerWindow):
    def __init__(self):
        super(PersonaPerPage, self).__init__()
        self.setupUi(self)
        self.button = np.empty(4, dtype=QPushButton)
        for i in range(4):
            self.button[i] = QPushButton(self)
            self.button[i].setText("Onayla")
            self.button[i].clicked.connect(self.pushed)
            self.button[i].setDefault(False)
            self.button[i].setAutoDefault(False)
            self.tabWidget.widget(i).findChild(QScrollArea).widget().layout().insertWidget(-1, self.button[i])
        self.active = True

    @Slot()
    def updatePerPerWin(self, persona):
        max_num_per = max(map(len, persona))
        self.groupBox = np.empty((4, max_num_per), dtype=QGroupBox)
        self.horizontalSlider = np.empty((4, max_num_per), dtype=QSlider)
        self.line = np.empty((4, max_num_per), dtype=QLineEdit)
        self.hor_layout = np.empty((4, max_num_per), dtype=QHBoxLayout)
        for tab in range(4):
            index = 0
            self.active = True
            for n in persona[tab].keys():
                self.groupBox[tab, index] = QGroupBox(self)
                self.horizontalSlider[tab, index] = QSlider(self.groupBox[tab, index])
                self.line[tab, index] = QLineEdit(self.groupBox[tab, index])
                self.hor_layout[tab, index] = QHBoxLayout(self.groupBox[tab, index])
                self.upLine_ss(tab, index)
                self.upBar_ss(tab, index)
                self.groupBox[tab, index].setTitle(n)
                sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
                self.horizontalSlider[tab, index].setSizePolicy(sizePolicy)
                self.horizontalSlider[tab, index].setMaximum(100)
                self.horizontalSlider[tab, index].setMinimumSize(QSize(300, 0))
                self.horizontalSlider[tab, index].setOrientation(Qt.Horizontal)
                self.horizontalSlider[tab, index].setTickPosition(QSlider.TicksBothSides)
                self.horizontalSlider[tab, index].setTickInterval(10)
                self.line[tab, index].setFixedWidth(50)
                self.hor_layout[tab, index].addWidget(self.horizontalSlider[tab, index])
                self.hor_layout[tab, index].addWidget(self.line[tab, index])
                self.tabWidget.widget(tab).findChild(QScrollArea).widget().layout().addWidget(self.groupBox[tab, index])
                self.tabWidget.widget(tab).findChild(QScrollArea).widget().layout().addWidget(self.button[tab])
                self.horizontalSlider[tab, index].setValue(round(self.personaPer[tab][index]))
                self.line[tab, index].setText(str(round(self.personaPer[tab][index])))
                index = index + 1
            self.active = False

    def upLine_ss(self, tab, index):
        self.horizontalSlider[tab, index].valueChanged.connect(lambda x: self.upLine(tab, index, x))

    def upBar_ss(self, tab, index):
        self.line[tab, index].editingFinished.connect(lambda: self.upBar(tab, index))

    @Slot(int)
    def upLine(self, tab, index, value):
        self.line[tab, index].setText(str(value))
        if not self.active:
            self.active = True
            self.updateOthers(tab, index, value)

    @Slot(str)
    def upBar(self, tab, index):
        self.horizontalSlider[tab, index].setValue(int(self.line[tab, index].text()))
        if not self.active:
            self.active = True
            self.updateOthers(tab, index, int(self.line[tab, index].text()))

    @Slot()
    def updateOthers(self, tab, index, value):
        last = len(self.personaPer[tab]) - 1
        sum = 0.0
        for i, v in enumerate(self.personaPer[tab]):
            if i != index:
                if index == last and i == (last - 1):
                    new_val = 100 - sum - value
                elif index == last:
                    if self.personaPer[tab][index] == 100:
                        new_val = (100-value) / last
                    else:
                        new_val = (100-value) * v / (100 - self.personaPer[tab][index])
                    sum = sum + round(new_val)
                elif i != last:
                    if self.personaPer[tab][index] == 100:
                        new_val = (100-value) / last
                    else:
                        new_val = (100-value) * v / (100 - self.personaPer[tab][index])
                    sum = sum + round(new_val)
                elif i == last:
                    new_val = 100 - sum - value
                self.personaPer[tab][i] = new_val
                self.horizontalSlider[tab, i].setValue(round(new_val))
        self.personaPer[tab][index] = value
        self.active = False

    @Slot()
    def pushed(self):
        self.close()

    @Slot()
    def closeEvent(self, event):
        for tab in range(4):
            for i in reversed(range(self.tabWidget.widget(tab).findChild(QScrollArea).widget().layout().count())):
                self.tabWidget.widget(tab).findChild(QScrollArea).widget().layout().itemAt(i).widget().setParent(None)
            self.tabWidget.widget(tab).findChild(QScrollArea).widget().layout().insertWidget(-1, self.button[tab])
