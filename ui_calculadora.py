# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculadoraxBFwxA.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 10, 301, 161))
        self.frame.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 170, 0);\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.valor1 = QLabel(self.frame)
        self.valor1.setObjectName(u"valor1")

        self.verticalLayout.addWidget(self.valor1)

        self.ivalor1 = QLineEdit(self.frame)
        self.ivalor1.setObjectName(u"ivalor1")

        self.verticalLayout.addWidget(self.ivalor1)

        self.valor2 = QLabel(self.frame)
        self.valor2.setObjectName(u"valor2")

        self.verticalLayout.addWidget(self.valor2)

        self.ivalor2 = QLineEdit(self.frame)
        self.ivalor2.setObjectName(u"ivalor2")

        self.verticalLayout.addWidget(self.ivalor2)

        self.btnbotao = QPushButton(self.centralwidget)
        self.btnbotao.setObjectName(u"btnbotao")
        self.btnbotao.setGeometry(QRect(20, 450, 261, 111))
        font = QFont()
        font.setFamilies([u"Impact"])
        font.setPointSize(48)
        self.btnbotao.setFont(font)
        self.btnbotao.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.total = QLabel(self.centralwidget)
        self.total.setObjectName(u"total")
        self.total.setGeometry(QRect(80, 190, 131, 61))
        self.total.setFont(font)
        self.total.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 330, 111, 118))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.CBsomar = QRadioButton(self.frame_2)
        self.CBsomar.setObjectName(u"CBsomar")

        self.verticalLayout_2.addWidget(self.CBsomar)

        self.CBsubtrair = QRadioButton(self.frame_2)
        self.CBsubtrair.setObjectName(u"CBsubtrair")

        self.verticalLayout_2.addWidget(self.CBsubtrair)

        self.CBmultiplicar_2 = QRadioButton(self.frame_2)
        self.CBmultiplicar_2.setObjectName(u"CBmultiplicar_2")

        self.verticalLayout_2.addWidget(self.CBmultiplicar_2)

        self.CBdividir = QRadioButton(self.frame_2)
        self.CBdividir.setObjectName(u"CBdividir")

        self.verticalLayout_2.addWidget(self.CBdividir)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CALCULADORA", None))
        self.valor1.setText(QCoreApplication.translate("MainWindow", u"Valor 1", None))
        self.valor2.setText(QCoreApplication.translate("MainWindow", u"Valor 2", None))
        self.btnbotao.setText(QCoreApplication.translate("MainWindow", u"CALCULAR", None))
        self.total.setText("")
        self.CBsomar.setText(QCoreApplication.translate("MainWindow", u"Somar", None))
        self.CBsubtrair.setText(QCoreApplication.translate("MainWindow", u"Subtrair", None))
        self.CBmultiplicar_2.setText(QCoreApplication.translate("MainWindow", u"Multiplicar", None))
        self.CBdividir.setText(QCoreApplication.translate("MainWindow", u"Dividir", None))
    # retranslateUi

