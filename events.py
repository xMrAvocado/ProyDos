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