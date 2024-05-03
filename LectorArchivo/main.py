from window import *
from Archivo import Archivo
from typing import Any

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    archivo = Any
    
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.setWindowIcon(QIcon('txt.png')) 
        self.setWindowTitle("Lector de archivos")
        self.buscar.clicked.connect(self.buscarArchivo)
        self.verEstadisticas.clicked.connect(self.crearEstadisticas)
        self.cambiarLetra.clicked.connect(self.cambiarUnaLetra)
    
    def buscarArchivo(self):
        options = QtWidgets.QFileDialog.Options()
        file, _= QtWidgets.QFileDialog.getOpenFileName(None, options=options)
        
        if file:
            archivo = open(file, "r")
            texto = archivo.read()
            self.archivo = Archivo(texto)
            archivo.close()
            self.textoArchivo.setText(texto)
            
    def crearEstadisticas(self):
        try:
            self.archivo.analizarTexto()
            self.archivo.verEstadisticas()
            with open('estadistica.txt', 'w') as archivo1:
                archivo1.write(self.archivo.textoNuevo)
            
            self.textoEstadistica.setText(self.archivo.textoNuevo)
        except Exception as e:
            print("Ha ocurrido un error",e)
            
    def cambiarUnaLetra(self):
        try:
            if (len(str(self.letraCambio.text())) ==1 ) and (len(str(self.letraCambio_2.text()))==1):
                self.archivo.analizarTexto()
                self.archivo.modificarTexto(self.letraCambio.text(), self.letraCambio_2.text())
                self.textoArchivo.setText(self.archivo.texto)
                with open('archivoNuevo.txt', 'w') as archivo:
                    archivo.write(self.archivo.texto)
            else:
                self.ventanaEmergente.inicializar_GUI()
                
            
        except Exception as e:
            print("Ha ocurrido un error aqui",e)
        
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = MyWindow()
    gui.show()
    sys.exit(app.exec_())
    
