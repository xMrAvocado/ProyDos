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
        def selSexo():
            try:
                if var.ui.rbtFem.isChecked():
                    print('Has elegido femenino')
                if var.ui.rbtMasc.isChecked():
                    print('Has elegido masculino')
            except Exception as error:
                print('Error: %' % str(error))
        def selPago():
            try:
                if var.ui.chkEfec.isChecked():
                    print('Pagas Efectivo')
                if var.ui.chkTar.isChecked():
                    print('Pagas con Targeta')
                if var.ui.chkTrans.isChecked():
                    print('Pagas con Transferencia')
            except Exception as error:
                print('Error: %' % str(error))

        def selProv(prov):
            try:
                print('Has seleccionado la provincia de ', prov)
                return prov
            except Exception as error:
                print('Error: %' % str(error))
