from vensalir import *
import var, events

class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir,self), __init__()
        var.avisosalir = Ui_venSalir()
        var.avisosalir = setupUi(self)
        var.avisosalir.btnBoxSalir.button(QtWidgets.QDialogButtonSex.Yes).clicked.connect(events.Eventos.Salir)
        var.avisosalir.btnBoxSalir.button(QtWidgets.QDialogButtonSex.No).clicked.connect(events.Eventos.Salir)
