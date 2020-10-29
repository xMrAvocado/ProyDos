from ventana import *
import sys,var,events,clientes

class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_venPrincipal()
        var.ui.setupUi(self)
        #Código de conexión de los eventos

        var.rbtSex = (var.ui.rbtFem, var.ui.rbtMasc)
        '''Botones'''
        #var.ui.btnAceptar.clicked.connect(events.Eventos.Saludo)
        var.ui.btnSalir.clicked.connect(events.Eventos.Salir)

        '''Controles del menú var'''
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)

        var.ui.editDni.editingFinished.connect(clientes.Clientes.validarDNI())

        for i in var.rbtSex:
            i.toggled.connect(clientes.Clientes.selSexo)
if __name__=='__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())