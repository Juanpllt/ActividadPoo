import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from emergente2 import Ui_Emergente



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(681, 676)
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame1 = QFrame(self.centralwidget)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setGeometry(QRect(10, 10, 661, 661))
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.frame1.setFrameShadow(QFrame.Raised)
        self.buscar = QPushButton(self.frame1)
        self.buscar.setObjectName(u"buscar")
        self.buscar.setGeometry(QRect(320, 40, 91, 31))
        font = QFont()
        font.setPointSize(12)
        self.buscar.setFont(font)
        self.archivo = QLabel(self.frame1)
        self.archivo.setObjectName(u"archivo")
        self.archivo.setGeometry(QRect(10, 10, 51, 21))
        font1 = QFont()
        font1.setPointSize(11)
        self.archivo.setFont(font1)
        self.rutaArchivo = QLineEdit(self.frame1)
        self.rutaArchivo.setObjectName(u"rutaArchivo")
        self.rutaArchivo.setGeometry(QRect(10, 39, 301, 31))
        font2 = QFont()
        font2.setPointSize(14)
        self.rutaArchivo.setFont(font2)
        self.rutaArchivo.setReadOnly(True)
        self.textoArchivo = QTextEdit(self.frame1)
        self.textoArchivo.setObjectName(u"textoArchivo")
        self.textoArchivo.setGeometry(QRect(10, 80, 381, 571))
        self.textoArchivo.setFont(font)
        self.letraCambio = QLineEdit(self.frame1)
        self.letraCambio.setObjectName(u"letraCambio")
        self.letraCambio.setGeometry(QRect(420, 100, 111, 31))
        self.letraCambio.setFont(font2)
        self.letraCambio_2 = QLineEdit(self.frame1)
        self.letraCambio_2.setObjectName(u"letraCambio_2")
        self.letraCambio_2.setGeometry(QRect(540, 100, 111, 31))
        self.letraCambio_2.setFont(font2)
        self.cambiarLetra = QPushButton(self.frame1)
        self.cambiarLetra.setObjectName(u"cambiarLetra")
        self.cambiarLetra.setGeometry(QRect(490, 150, 91, 31))
        self.cambiarLetra.setFont(font)
        self.verEstadisticas = QPushButton(self.frame1)
        self.verEstadisticas.setObjectName(u"verEstadisticas")
        self.verEstadisticas.setGeometry(QRect(470, 190, 121, 41))
        self.verEstadisticas.setFont(font)
        self.textoEstadistica = QTextEdit(self.frame1)
        self.textoEstadistica.setObjectName(u"textoEstadistica")
        self.textoEstadistica.setGeometry(QRect(410, 240, 241, 411))
        self.textoEstadistica.setFont(font)
        self.label = QLabel(self.frame1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(460, 80, 31, 16))
        self.label_2 = QLabel(self.frame1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(560, 80, 81, 16))
        MainWindow.setCentralWidget(self.centralwidget)

        self.ventanaEmergente = Ui_Emergente(MainWindow, "Por favor ingrese solo una letra en cada casilla")

        '''self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.button = QPushButton("Cerrar")
        self.button.clicked.connect(self.close)
        self.layout.addWidget(self.button)'''
        
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.buscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.archivo.setText(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.rutaArchivo.setText("")
        self.cambiarLetra.setText(QCoreApplication.translate("MainWindow", u"Cambiar", None))
        self.verEstadisticas.setText(QCoreApplication.translate("MainWindow", u"Ver Estadisticas", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Letra ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Letra a cambiar", None))