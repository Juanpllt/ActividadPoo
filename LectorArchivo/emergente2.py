from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class Ui_Emergente(QWidget):

    def __init__(self, interfaz, texto):
        super().__init__()
        self.interfaz = interfaz
        self.texto = texto
        self.title = 'Atención'
        self.width = 245
        self.height = 120

    def inicializar_GUI(self):
        # Inicializamos la ventana
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('atencion.png')) 
        self.setFixedSize(self.width, self.height)
        self.distribuidor_base = QVBoxLayout(self)

        # Creación del espacio de los botones
        self.widget_botones = QWidget()
        self.distribuidor_botones = QGridLayout()
        self.widget_botones.setLayout(self.distribuidor_botones)

        # Creación de las etiquetas
        self.etiqueta_bienvenida = QLabel(self.texto)
        self.etiqueta_bienvenida.setAlignment(Qt.AlignCenter)
        self.distribuidor_base.addWidget(self.etiqueta_bienvenida, Qt.AlignCenter)

        # Creación de los botones
        self.botonAceptar = QPushButton("Aceptar", self)
        self.botonAceptar.setFixedSize(150, 40)
        self.botonAceptar.setToolTip("Añadir Actividad")
        self.distribuidor_botones.addWidget(self.botonAceptar, 0, 0, Qt.AlignLeft)
        self.distribuidor_base.addWidget(self.widget_botones, Qt.AlignCenter)
        self.botonAceptar.clicked.connect(self.accionCerrar)

        # Hacemos la ventana visible
        self.show()

    def accionCerrar(self):
        self.close()
