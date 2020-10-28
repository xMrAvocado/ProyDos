import var
class Clientes():
    # Clase gestión clientes
    def validarDNI(dni):

        try:
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = '1234567890'
            dni = dni.upper()
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                return len(dni == len([n for n in dni if n in numeros])) and tabla[int(dni) % 23] == dig_control
            return False
        except:
            print('Error en el módulo de validacióndel DNI')
            return None
    def validoDni(self):
        '''Muestra mensaje de DNI válido'''
        try:
            dni = var.ui.editDni.text()

            if Clientes.validarDNI(dni):
                var.ui.lblValidar.setStylesheet('QLabel {color: green;}')
                var.ui.lblValidar.setText('V')
                var.ui.editDni.setText(dni.upper())
            else:
                var.ui.lblValidar.setStylesheet('QLabel {color: red;}')
                var.ui.lblValidar.setText('X')
                var.ui.editDni.setText(dni.upper())

        except:

            print('Error en el módulo de validacióndel DNI')
            return None