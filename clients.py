from PyQt5 import QtWidgets

import var


class Clientes():
    '''
    eventos clientes
    '''
    def validarDni(dni):
        '''
        Código que controla si el dni o nie es correcto
        :return:
        '''
        try:
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'
            dig_ext = 'XYZ'
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = '0123456789'
            dni = dni.upper()
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni  = dni.replace(dni[0],reemp_dig_ext[dni[0]])
                return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni)%23 ] == dig_control

        except:
            print('Error módulo validar DNI')
            return None

    def validoDni():
        '''
        muestra mensaje de dni válido
        :return:
        '''
        try:
            dni = var.ui.editDni.text()
            if Clientes.validarDni(dni):
                var.ui.lblValidar.setStyleSheet('QLabel {color: green;}')
                var.ui.lblValidar.setText('V')
                var.ui.editDni.setText(dni.upper())
            else:
                var.ui.lblValidar.setStyleSheet('QLabel {color: red;}')
                var.ui.lblValidar.setText('X')
                var.ui.editDni.setText(dni.upper())

        except:
            print('Error módulo escribir valido DNI')
            return None

    def selSexo():
        try:
            if var.ui.rbtFem.isChecked():
                var.sex = 'Mujer'
            if var.ui.rbtMasc.isChecked():
                var.sex = 'Hombre'
        except Exception as error:
            print('Error: %s' % str(error))

    def selPago():
        try:
            if var.ui.chkEfec.isChecked():
                var.pay.append('Efectivo')
            if var.ui.chkTar.isChecked():
                var.pay.append('Targeta')
            if var.ui.chkTrans.isChecked():
                var.pay.append('Transferencia')

        except Exception as error:
            print('Error: %s' % str(error))

    def selProv(prov):
        try:
            global vpro
            vpr = prov
        except Exception as error:
            print('Error: %s' % str(error))

    '''
    Abrir la ventana calendario
    '''
    def abrirCalendar():
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print('Error: %s ' % str(error))

    '''
    Este módulo se ejecuta cuando clickeamos en un día del calendar, es decir, clicked.connect de calendar
    '''

    def cargarFecha(qDate):
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.editClialta.setText(str(data))
            var.dlgcalendar.hide()
        except Exception as error:
            print('Error cargar fecha: %s ' % str(error))



    def showClientes(self):
        '''
        Cargará los clientes en la tabla
        :return:
        '''
        try:
            #Preparamos el registro
            newcli = []
            clitab = [] #Será lo que carguemos en la tabla
            client = [var.ui.editDni, var.ui.editApel, var.ui.editNome, var.ui.editDir, var.ui.editClialta]
            k = 0
            for i in client:
                newcli.append(i.text()) #Cargamos los valores que hay en los editline
                if k < 3:
                    clitab.append(i.text)
                    k += 1
            newcli.append(vpro)
            #Elimina duplicados
            var.pay = set(var.pay)
            for j in var.pay:
                newcli.append(j)
            newcli.append(var.sex)
            print(newcli)
            print(clitab)
            #Aquí empieza a trabajar con la TableWidget
            row = 0
            column = 0
            var.ui.cliTab.insertRow(row)
            for registro in clitab:
                cell = QtWidgets.QTableWidgetItem(registro)
                var.ui.cliTab.setItem(row, column, cell)
                column += 1

        except Exception as error:
            print('Error: %s' % str(error))








