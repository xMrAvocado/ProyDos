from ventana import *
import sys,var,events,clientes,avisosalir


class DialogCalendar(QtWidgets.QDialog):
    def
class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_venPrincipal()
        var.ui.setupUi(self)
        #Código de conexión de los eventos

        var.rbtSex = (var.ui.rbtFem, var.ui.rbtMasc)
        var.chkPago = (var.ui.chkEfec, var.ui.chkTar, var.ui.chkTrans)
        var.dlgSalir = DialogSalir()
        var.dlgCAlendar = DialogCalendar()
        '''Botones'''
        #var.ui.btnAceptar.clicked.connect(events.Eventos.Saludo)
        QtWidgets.QAction(self).triggered()
        var.ui.btnSalir.clicked.connect(events.Eventos.Salir)

        '''Controles del menú var'''
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)

        var.ui.editDni.editingFinished.connect(clientes.Clientes.validarDNI())

        for i in var.rbtSex:
            i.toggled.connect(clientes.Clientes.selSexo)
        for i in var.chkPago:
            i.stateChanged.connect()
        var.ui.cmbProv.activated[str].connect(clientes.Clientes.selProv)
        '''
        Llamada a módulos iniciales
        '''
        events.Eventos.cargarProv()

    def closeEvent(self, event):
        events.Eventos.Salir()
if __name__=='__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())

