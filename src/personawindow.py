# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'personawindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_PersonaWindow(object):
    def setupUi(self, PersonaWindow):
        if not PersonaWindow.objectName():
            PersonaWindow.setObjectName(u"PersonaWindow")
        PersonaWindow.resize(580, 612)
        PersonaWindow.setModal(False)
        self.verticalLayout = QVBoxLayout(PersonaWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gradeTab = QTabWidget(PersonaWindow)
        self.gradeTab.setObjectName(u"gradeTab")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gradeTab.sizePolicy().hasHeightForWidth())
        self.gradeTab.setSizePolicy(sizePolicy)
        self.gradeTab.setMinimumSize(QSize(0, 500))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 1)
        self.scrollArea = QScrollArea(self.tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 556, 466))
        self.horizontalLayout_3 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_2 = QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.widget_2.setMinimumSize(QSize(200, 0))
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 150, -1, 150)
        self.selectBtn = QPushButton(self.widget_2)
        self.selectBtn.setObjectName(u"selectBtn")

        self.verticalLayout_2.addWidget(self.selectBtn)

        self.dropLst = QComboBox(self.widget_2)
        self.dropLst.setObjectName(u"dropLst")

        self.verticalLayout_2.addWidget(self.dropLst)


        self.horizontalLayout_3.addWidget(self.widget_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.gradeTab.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 1)
        self.scrollArea_2 = QScrollArea(self.tab_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 556, 466))
        self.horizontalLayout_4 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_3 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.widget_3.setMinimumSize(QSize(200, 0))
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 150, -1, 150)
        self.selectBtn_2 = QPushButton(self.widget_3)
        self.selectBtn_2.setObjectName(u"selectBtn_2")

        self.verticalLayout_3.addWidget(self.selectBtn_2)

        self.dropLst_2 = QComboBox(self.widget_3)
        self.dropLst_2.setObjectName(u"dropLst_2")

        self.verticalLayout_3.addWidget(self.dropLst_2)


        self.horizontalLayout_4.addWidget(self.widget_3)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_3.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.gradeTab.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_4 = QGridLayout(self.tab_3)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 1)
        self.scrollArea_3 = QScrollArea(self.tab_3)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 556, 466))
        self.horizontalLayout_5 = QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.widget_4 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy1)
        self.widget_4.setMinimumSize(QSize(200, 0))
        self.verticalLayout_4 = QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 150, -1, 150)
        self.selectBtn_3 = QPushButton(self.widget_4)
        self.selectBtn_3.setObjectName(u"selectBtn_3")

        self.verticalLayout_4.addWidget(self.selectBtn_3)

        self.dropLst_3 = QComboBox(self.widget_4)
        self.dropLst_3.setObjectName(u"dropLst_3")

        self.verticalLayout_4.addWidget(self.dropLst_3)


        self.horizontalLayout_5.addWidget(self.widget_4)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_4.addWidget(self.scrollArea_3, 0, 0, 1, 1)

        self.gradeTab.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_5 = QGridLayout(self.tab_4)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 1)
        self.scrollArea_4 = QScrollArea(self.tab_4)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 556, 466))
        self.horizontalLayout_6 = QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_5 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy1)
        self.widget_5.setMinimumSize(QSize(200, 0))
        self.verticalLayout_5 = QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 150, -1, 150)
        self.selectBtn_4 = QPushButton(self.widget_5)
        self.selectBtn_4.setObjectName(u"selectBtn_4")

        self.verticalLayout_5.addWidget(self.selectBtn_4)

        self.dropLst_4 = QComboBox(self.widget_5)
        self.dropLst_4.setObjectName(u"dropLst_4")

        self.verticalLayout_5.addWidget(self.dropLst_4)


        self.horizontalLayout_6.addWidget(self.widget_5)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_5.addWidget(self.scrollArea_4, 0, 0, 1, 1)

        self.gradeTab.addTab(self.tab_4, "")

        self.verticalLayout.addWidget(self.gradeTab)

        self.widget = QWidget(PersonaWindow)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.console = QTextBrowser(self.widget)
        self.console.setObjectName(u"console")

        self.horizontalLayout.addWidget(self.console)

        self.confirmBtn = QPushButton(self.widget)
        self.confirmBtn.setObjectName(u"confirmBtn")
        self.confirmBtn.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.confirmBtn)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(PersonaWindow)

        self.gradeTab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(PersonaWindow)
    # setupUi

    def retranslateUi(self, PersonaWindow):
        PersonaWindow.setWindowTitle(QCoreApplication.translate("PersonaWindow", u"Persona", None))
        self.selectBtn.setText(QCoreApplication.translate("PersonaWindow", u"Ekle", None))
        self.dropLst.setCurrentText("")
        self.gradeTab.setTabText(self.gradeTab.indexOf(self.tab), QCoreApplication.translate("PersonaWindow", u"9.S\u0131n\u0131f", None))
        self.selectBtn_2.setText(QCoreApplication.translate("PersonaWindow", u"Ekle", None))
        self.dropLst_2.setCurrentText("")
        self.gradeTab.setTabText(self.gradeTab.indexOf(self.tab_2), QCoreApplication.translate("PersonaWindow", u"10.S\u0131n\u0131f", None))
        self.selectBtn_3.setText(QCoreApplication.translate("PersonaWindow", u"Ekle", None))
        self.dropLst_3.setCurrentText("")
        self.gradeTab.setTabText(self.gradeTab.indexOf(self.tab_3), QCoreApplication.translate("PersonaWindow", u"11.S\u0131n\u0131f", None))
        self.selectBtn_4.setText(QCoreApplication.translate("PersonaWindow", u"Ekle", None))
        self.dropLst_4.setCurrentText("")
        self.gradeTab.setTabText(self.gradeTab.indexOf(self.tab_4), QCoreApplication.translate("PersonaWindow", u"12.S\u0131n\u0131f", None))
        self.console.setHtml(QCoreApplication.translate("PersonaWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Konsol</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&gt;&gt; L\u00fctfen toplam 40 kredi olacak \u015fekilde ders se\u00e7iniz.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.confirmBtn.setText(QCoreApplication.translate("PersonaWindow", u"Onayla", None))
    # retranslateUi

