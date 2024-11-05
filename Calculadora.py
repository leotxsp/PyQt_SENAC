import sys
from PySide6 import QtWidgets
from ui_calculadora import Ui_MainWindow

class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main,self).__init__()
        self.setupUi(self)
        self.btnbotao.clicked.connect(self.calcular)
        
    def calcular(self):
        v1 = int(self.ivalor1.text())
        v2 = int(self.ivalor2.text())
        if self.CBsomar.isChecked():
            resultado = self.somar(v1,v2)
        elif self.CBsubtrair.isChecked():
            resultado = self.subtrair(v1,v2)
        elif self.CBmultiplicar_2.isChecked():
            resultado = self.multiplicar(v1,v2)
        elif self.CBdividir.isChecked():
            resultado = self.dividir(v1,v2)
        self.total.setText(str(resultado))
    def somar(self,v1,v2):
        resultado = v1+v2
        return resultado
    
    def subtrair(self,v1,v2):
        resultado = v1-v2
        return resultado
    
    def multiplicar(self,v1,v2):
        resultado = v1*v2
        return resultado
    
    def dividir(self,v1,v2):
        resultado = v1/2
        return resultado


app = QtWidgets.QApplication(sys.argv)

window = Main()
window.show()

app.exec()