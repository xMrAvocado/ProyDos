import var,sys

class Eventos():
    '''Eventos generales'''

    '''def Saludo(self):
        try:
            var.ui.lblSaludo.setText('Has pulsado el botón')
        except Exception as error:
            print('Error: %s' % str(error))'''


    def Salir(self):
        try:
            sys.exit()
        except Exception as error:
            print('Error: %s' % str(error))

            '''setText es para que escriba algo

            getText es para recoger lo que he escrito'''

    def cargarProv():
        """
        carga las provincias al iniciar el programa
        :return:
        """
        try:
            prov = ['','A Coruña','Lugo','Ourense','Pontevedra']
            for i in prov:
                var.ui.cmbProv.addItem(i)
        except Exception as error:
            print('Error: %' % str(error))