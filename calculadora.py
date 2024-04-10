import sys
from numpy import sin, cos, tan, log, exp, arcsin, arctan, arccos
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QLCDNumber, QLabel,QMenuBar,  QStatusBar, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5 import uic

#librerías propias incluidas en el proyecto
import convert
from ISR import getISR
from units import conv
from estilos import styleOp, styleCombo, styleNum

class Ventana(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        uic.loadUi("calculadora.ui",self)
        self.setWindowTitle("Calculator")
        self.seleccionarModo()

        self.error = False #Variable que desactiva los botones en un zeroDivisionError
        self.percentMode = False #Variable de apoyo en el modo Finance
        self.modoSeleccionado = "Basic" #Modo por defecto
        self.base = 'Bin'   #Base por defecto en el modo Programmer
        self.valorPorMostrar = '0' #Variable de apoyo para el siguiente input en todos los modos
        self.prevOperation = ''  # Variable de apoyo en el modo básico
        self.operacionSeleccionada = ''  # Vaiable de apoyo en el modo básico
        self.slots = []  # Lista de apoyo en el módo básico
        self.unPunto = True  # Variable de apoyo para evitar que se escriba más de un punto por input

        self.setGeometry(0,0,400,230) #(450,200,400,230)
        self.botonA.setGeometry(230, 43, 61, 31)
        self.botonB.setGeometry(230, 73, 61, 31)
        self.botonC.setGeometry(230, 103, 61, 31)
        self.comboBox2.setGeometry(50, 133, 61, 29)
        self.boton1.setStyleSheet(styleNum)
        self.boton2.setStyleSheet(styleNum)
        self.boton3.setStyleSheet(styleNum)
        self.boton4.setStyleSheet(styleNum)
        self.boton5.setStyleSheet(styleNum)
        self.boton6.setStyleSheet(styleNum)
        self.boton7.setStyleSheet(styleNum)
        self.boton8.setStyleSheet(styleNum)
        self.boton9.setStyleSheet(styleNum)
        self.boton0.setStyleSheet(styleNum)
        self.botonA.setStyleSheet(styleNum)
        self.botonB.setStyleSheet(styleNum)
        self.botonC.setStyleSheet(styleNum)
        self.botonD.setStyleSheet(styleNum)
        self.botonE.setStyleSheet(styleNum)
        self.botonF.setStyleSheet(styleNum)
        self.botonPunto.setStyleSheet(styleNum)
        self.operacion1.setStyleSheet(styleOp)
        self.operacion2.setStyleSheet(styleOp)
        self.operacion3.setStyleSheet(styleOp)
        self.operacion4.setStyleSheet(styleOp)
        self.botonBorrar.setStyleSheet(styleOp)
        self.botonIgual.setStyleSheet(styleOp)
        self.botonIVA.setStyleSheet(styleOp)
        self.botonISR.setStyleSheet(styleOp)
        self.botonPercent.setStyleSheet(styleOp)
        self.botonInv.setStyleSheet(styleOp)
        self.comboBox.setStyleSheet(styleCombo)
        self.comboBox2.setStyleSheet(styleCombo)
        self.comboBox3.setStyleSheet(styleCombo)
        self.comboBox4.setStyleSheet(styleCombo)


        self.labelPercent.hide()
        self.comboBox3.hide()
        self.comboBox4.hide()

        self.comboBox.currentIndexChanged.connect(self.seleccionarModo) #ComboBox para escoger el modo de la calculadora
        self.comboBox2.currentIndexChanged.connect(self.seleccionarBase) #Combobox para escoger el tipo de conversión en modo programador
        self.comboBox3.currentIndexChanged.connect(self.seleccionarModo)

        # Señales de los botones alfanuméricos
        self.boton1.clicked.connect(self.obtenerDatos)
        self.boton2.clicked.connect(self.obtenerDatos)
        self.boton3.clicked.connect(self.obtenerDatos)
        self.boton4.clicked.connect(self.obtenerDatos)
        self.boton5.clicked.connect(self.obtenerDatos)
        self.boton6.clicked.connect(self.obtenerDatos)
        self.boton7.clicked.connect(self.obtenerDatos)
        self.boton8.clicked.connect(self.obtenerDatos)
        self.boton9.clicked.connect(self.obtenerDatos)
        self.boton0.clicked.connect(self.obtenerDatos)
        self.botonA.clicked.connect(self.obtenerDatos)
        self.botonB.clicked.connect(self.obtenerDatos)
        self.botonC.clicked.connect(self.obtenerDatos)
        self.botonD.clicked.connect(self.obtenerDatos)
        self.botonE.clicked.connect(self.obtenerDatos)
        self.botonF.clicked.connect(self.obtenerDatos)

        #señales de los botones no alfanuméricos
        self.botonIVA.clicked.connect(self.obtenerDatosF)
        self.botonISR.clicked.connect(self.operar)
        self.botonPercent.clicked.connect(self.obtenerDatosF)
        self.botonPunto.clicked.connect(self.obtenerDatos)
        self.botonBorrar.clicked.connect(self.borrar)
        self.botonInv.clicked.connect(self.invertir) #Botón para operaciones inversas en el modo Scientific

        #Señales de los botones de operación.
        self.operacion1.clicked.connect(self.operar)
        self.operacion2.clicked.connect(self.operar)
        self.operacion3.clicked.connect(self.operar)
        self.operacion4.clicked.connect(self.operar)
        self.botonIgual.clicked.connect(self.operar)

    def invertir(self):
        if self.inversa:
            self.operacion1.setText('Asin(x)')
            self.operacion2.setText('Acos(x)')
            self.operacion3.setText('Atan(x)')
            self.inversa = False
        else:
            self.operacion1.setText('Sin(x)')
            self.operacion2.setText('Cos(x)')
            self.operacion3.setText('Tan(x)')
            self.inversa = True

    def seleccionarBase(self): #Funcion para seleccionar la base del input
        if self.comboBox2.currentIndex() == 0: #Modo binario
            self.base = 'Bin'
            self.operacion1.setEnabled(False) #No se puede convertir de binario a binario, por eso la opción 1 se apaga
            self.operacion2.setEnabled(True)
            self.operacion3.setEnabled(True)
            self.operacion4.setEnabled(True)
            #En binario sólo se puede escribir con 0 y 1
            self.boton0.setEnabled(True)
            self.boton1.setEnabled(True)
            self.boton2.setEnabled(False)
            self.boton3.setEnabled(False)
            self.boton4.setEnabled(False)
            self.boton5.setEnabled(False)
            self.boton6.setEnabled(False)
            self.boton7.setEnabled(False)
            self.boton8.setEnabled(False)
            self.boton9.setEnabled(False)
            self.botonA.setEnabled(False)
            self.botonB.setEnabled(False)
            self.botonC.setEnabled(False)
            self.botonD.setEnabled(False)
            self.botonE.setEnabled(False)
            self.botonF.setEnabled(False)
        elif self.comboBox2.currentIndex() == 1: #Modo octal
            self.base = 'Oct'
            self.operacion1.setEnabled(True)
            self.operacion2.setEnabled(False) #No se puede convertir de octal a octal, por eso la opción 2 se apaga
            self.operacion3.setEnabled(True)
            self.operacion4.setEnabled(True)
            # En octal sólo se puede escribir con números entre el 0 y 7
            self.boton0.setEnabled(True)
            self.boton1.setEnabled(True)
            self.boton2.setEnabled(True)
            self.boton3.setEnabled(True)
            self.boton4.setEnabled(True)
            self.boton5.setEnabled(True)
            self.boton6.setEnabled(True)
            self.boton7.setEnabled(True)
            self.boton8.setEnabled(False)
            self.boton9.setEnabled(False)
            self.botonA.setEnabled(False)
            self.botonB.setEnabled(False)
            self.botonC.setEnabled(False)
            self.botonD.setEnabled(False)
            self.botonE.setEnabled(False)
            self.botonF.setEnabled(False)
        elif self.comboBox2.currentIndex() == 2: #Modo decimal
            self.base = 'Dec'
            self.operacion1.setEnabled(True)
            self.operacion2.setEnabled(True)
            self.operacion3.setEnabled(False) #No se puede convertir de decimal a decimal, por eso la opción 3 se apaga
            self.operacion4.setEnabled(True)
            # En decimal sólo se puede escribir con números entre el 0 y 9
            self.boton0.setEnabled(True)
            self.boton1.setEnabled(True)
            self.boton2.setEnabled(True)
            self.boton3.setEnabled(True)
            self.boton4.setEnabled(True)
            self.boton5.setEnabled(True)
            self.boton6.setEnabled(True)
            self.boton7.setEnabled(True)
            self.boton8.setEnabled(True)
            self.boton9.setEnabled(True)
            self.botonA.setEnabled(False)
            self.botonB.setEnabled(False)
            self.botonC.setEnabled(False)
            self.botonD.setEnabled(False)
            self.botonE.setEnabled(False)
            self.botonF.setEnabled(False)
        elif self.comboBox2.currentIndex() == 3: #Modo hexadecimal
            self.base = 'Hex'
            self.operacion1.setEnabled(True)
            self.operacion2.setEnabled(True)
            self.operacion3.setEnabled(True)
            self.operacion4.setEnabled(False) #No se puede convertir de hexadecimal a hexadecimal, por eso la opción 4 se apaga
            # En hexadecimal se puede escribir con todos los dígitos del 0 al 9, y con las letras de la A a la F
            self.boton0.setEnabled(True)
            self.boton1.setEnabled(True)
            self.boton2.setEnabled(True)
            self.boton3.setEnabled(True)
            self.boton4.setEnabled(True)
            self.boton5.setEnabled(True)
            self.boton6.setEnabled(True)
            self.boton7.setEnabled(True)
            self.boton8.setEnabled(True)
            self.boton9.setEnabled(True)
            self.botonA.setEnabled(True)
            self.botonB.setEnabled(True)
            self.botonC.setEnabled(True)
            self.botonD.setEnabled(True)
            self.botonE.setEnabled(True)
            self.botonF.setEnabled(True)

    def seleccionarModo(self):
        if self.comboBox.currentIndex() == 0: #Si el comboBox1 está en 0, es modo básica
            self.operacion1.setText("+")
            self.operacion2.setText("-")
            self.operacion3.setText("*")
            self.operacion4.setText("/")
            self.botonIgual.setText("=")
            self.modoSeleccionado = "Basic"

        elif self.comboBox.currentIndex() == 1: #Si el comboBox1 está en 1, es modo científica
            self.operacion1.setText("Sin(x)")
            self.operacion2.setText("Cos(x)")
            self.operacion3.setText("Tan(x)")
            self.operacion4.setText("Ln(x)")
            self.botonIgual.setText("Exp(x)")
            self.botonInv.show()
            self.inversa = True
            self.modoSeleccionado = "Scientific"

        elif self.comboBox.currentIndex() == 2: #Si el comboBox1 está en 3, es modo finanzas
            self.operacion1.setText("+")
            self.operacion2.setText("-")
            self.operacion3.setText("*")
            self.operacion4.setText("/")
            self.botonIgual.setText("=")
            self.botonIVA.show()
            self.botonISR.show()
            self.botonPercent.show()
            self.modoSeleccionado = "Finance"

        elif self.comboBox.currentIndex() == 3: #Si el comboBox1 está en 3, es modo programador
            self.operacion1.setText("Bin")
            self.operacion2.setText("Oct")
            self.operacion3.setText("Dec")
            self.operacion4.setText("Hex")
            self.modoSeleccionado = "Programmer"
            self.seleccionarBase()
            self.botonA.show()
            self.botonB.show()
            self.botonC.show()
            self.botonD.show()
            self.botonE.show()
            self.botonF.show()
            self.botonPunto.setEnabled(False)
            self.comboBox2.show()
            self.operacion1.setGeometry(230, 133, 61, 31)
            self.operacion2.setGeometry(291, 133, 60, 31)
            self.operacion3.setGeometry(230, 160, 61, 31)
            self.operacion4.setGeometry(290, 160, 61, 31)

        else: #Si el comboBox1 está cualquier otro valor, es modo libre
            self.operacion1.hide()
            self.operacion2.hide()
            self.operacion3.hide()
            self.operacion4.hide()
            self.modoSeleccionado = "Converter"
            self.comboBox3.show()
            self.comboBox4.show()
            if self.comboBox3.currentText() == 'Length':self.setConvertions(['in-cm', 'cm-in', 'ft-m', 'm-ft', 'mille-km', 'km-mille'])
            elif self.comboBox3.currentText() == 'Mass': self.setConvertions(['kg-oz', 'oz-kg', 'lb-kg', 'kg-lb'])
            elif self.comboBox3.currentText() == 'Pressure': self.setConvertions(['atm-pa', 'pa-atm', 'mmHg-pa', 'pa-mmHg', 'kgf/cm2-pa', 'pa-kgf/cm2'])
            elif self.comboBox3.currentText() == 'Temperature':self.setConvertions(['°f-°c', '°c-°f'])
            elif self.comboBox3.currentText() == 'Angle': self.setConvertions(['rad-°', '°-rad'])
            elif self.comboBox3.currentText() == 'Power': self.setConvertions(['hp-kw', 'kw-hp'])

        if self.comboBox.currentIndex() !=1:
            self.botonInv.hide()
            self.botonIgual.setText('=')

        if self.comboBox.currentIndex() != 2:
            self.botonIVA.hide()
            self.botonISR.hide()
            self.botonPercent.hide()

        if self.comboBox.currentIndex() != 3:
            #Cualquier modo diferente al programador invisibiliza las letras A,B,C,D,E,F, enciende el botón punto y apaga el comboBox2
            self.botonA.hide()
            self.botonB.hide()
            self.botonC.hide()
            self.botonD.hide()
            self.botonE.hide()
            self.botonF.hide()
            self.botonPunto.setEnabled(True)
            self.comboBox2.hide()
            self.boton0.setEnabled(True)
            self.boton1.setEnabled(True)
            self.boton2.setEnabled(True)
            self.boton3.setEnabled(True)
            self.boton4.setEnabled(True)
            self.boton5.setEnabled(True)
            self.boton6.setEnabled(True)
            self.boton7.setEnabled(True)
            self.boton8.setEnabled(True)
            self.boton9.setEnabled(True)
            #En modo programador algunas operaciones se inhabilitan. Al salir del modo programador, todas las operaciones deben estar habilitadas
            self.operacion1.setEnabled(True)
            self.operacion2.setEnabled(True)
            self.operacion3.setEnabled(True)
            self.operacion4.setEnabled(True)
            self.operacion1.setGeometry(230, 43, 61, 31)
            self.operacion2.setGeometry(230, 73, 61, 31)
            self.operacion3.setGeometry(230, 103, 61, 31)
            self.operacion4.setGeometry(230, 133, 61, 31)

        if self.comboBox.currentIndex() != 4:
            self.operacion1.show()
            self.operacion2.show()
            self.operacion3.show()
            self.operacion4.show()
            self.comboBox3.hide()
            self.comboBox4.hide()

    def setConvertions(self, list):
        self.comboBox4.clear()
        self.comboBox4.addItems(list)
    def obtenerDatos(self):
        #Esta función concatena el valor de las teclas pulsadas en una variable llamada valor por mostrar
        btn_txt = str(self.sender().text())
        #Si la variable auxiliar del punto está habilitada, cuando es presionado el botón punto, se concatena y se deshabilita la variable
        if btn_txt == ".":
            if self.unPunto:
                self.valorPorMostrar += btn_txt
                self.unPunto = False
        else: self.valorPorMostrar += btn_txt

        #Si el primer valor es 0, el cero se borra.
        if self.valorPorMostrar[0] == '0':
            self.valorPorMostrar = self.valorPorMostrar[1:]
        self.pantalla.display(self.valorPorMostrar)
        if self.prevOperation == '':
            try:
                del self.slots[0]
                self.percentMode = False
                self.labelPercent.hide()
            except:
                pass
    def obtenerDatosF(self):
        #Esta función concatena el valor de las teclas pulsadas en la variable llamada valor por mostrar. Añade funcionalidades financieras a la funcion original
        btn_txt = str(self.sender().text())
        if btn_txt == '%':
            self.percentMode = True
            self.labelPercent.show()
        elif btn_txt == 'IVA':
            if self.valorPorMostrar[0] == '0':
                self.valorPorMostrar = '16'
                self.percentMode = True
                self.labelPercent.show()
        self.pantalla.display(self.valorPorMostrar)
        if self.prevOperation == '':
            try:
                self.percentMode = False
                self.labelPercent.hide()
                del self.slots[0]
            except:
                pass

    def guardarEnSlot(self): #Función de apoyo en modo básico
        self.slots.append(float(self.pantalla.value()))
        self.valorPorMostrar = '0'
        self.unPunto = True

    def operar(self, op = ''):
        try: operation = self.sender().text()
        except: operation = op
        #El try except anterior sirve para identificar si quien llama la función es un botón en pantalla o uno del teclado
        if self.modoSeleccionado == 'Basic':
            # Lógica del modo básico
            if operation == '+':
                if len(self.slots) == 0: self.guardarEnSlot() #Si no hay datos guardados, se guardan
                else:
                    self.slots[0] += float(self.pantalla.value())
                    self.valorPorMostrar = '0'
                    self.unPunto = True
                self.prevOperation = operation
            elif operation == '-':
                if len(self.slots) == 0: self.guardarEnSlot()
                else:
                    self.slots[0] -= float(self.pantalla.value())
                    self.valorPorMostrar = '0'
                    self.unPunto = True
                self.prevOperation = operation
            elif operation == '*':
                if len(self.slots) == 0: self.guardarEnSlot()
                else:
                    self.slots[0] *= float(self.pantalla.value())
                    self.valorPorMostrar = '0'
                    self.unPunto = True
                self.prevOperation = operation
            elif operation == '/':
                if len(self.slots) == 0: self.guardarEnSlot()
                else:
                    try:
                        self.slots[0] /= float(self.pantalla.value())
                        self.valorPorMostrar = '0'
                        self.unPunto = True
                    except:
                        self.error = True
                        self.habilitarBotones(False)
                        self.pantalla.display('error')
                        self.valorPorMostrar = '0'
                        try: del self.slots[0]
                        except: pass
                        self.botonIgual.setText('ok')
                self.prevOperation = operation
            elif operation == '=':
                if self.prevOperation == '+': self.slots[0] += float(self.valorPorMostrar)
                elif self.prevOperation == '-': self.slots[0] -= float(self.valorPorMostrar)
                elif self.prevOperation == '*': self.slots[0] *= float(self.pantalla.value())
                elif self.prevOperation == '/':
                    try:
                        self.slots[0] /= float(self.pantalla.value())
                    except ZeroDivisionError:
                        self.error = True
                        self.habilitarBotones(False)
                        self.pantalla.display('error')
                        self.valorPorMostrar = '0'
                        try: del self.slots[0]
                        except: pass
                        self.botonIgual.setText('ok')
                if not self.error:
                    if any(self.slots): self.pantalla.display(str(self.slots[0]))
                    self.prevOperation = ''
                    self.valorPorMostrar = '0'
                    self.unPunto = True
                    try: del self.slots[0]
                    except IndexError: pass
            elif operation == 'ok':
                self.habilitarBotones(True)
                self.pantalla.display('0')
                self.botonIgual.setText('=')
                self.error = False

        #Lógica del modo científico
        elif self.modoSeleccionado == 'Scientific':
            #operation = self.sender().text()
            if operation == 'Sin(x)': self.resultado = sin(self.pantalla.value())
            elif operation == 'Cos(x)': self.resultado = cos(self.pantalla.value())
            elif operation == 'Tan(x)': self.resultado = tan(self.pantalla.value())
            elif operation == 'Ln(x)': self.resultado = log(self.pantalla.value())
            elif operation == 'Exp(x)': self.resultado = exp(self.pantalla.value())
            elif operation == 'Asin(x)': self.resultado = arcsin(self.pantalla.value())
            elif operation == 'Acos(x)': self.resultado = arccos(self.pantalla.value())
            elif operation == 'Atan(x)': self.resultado = arctan(self.pantalla.value())
            self.pantalla.display(str(self.resultado))
            self.valorPorMostrar = '0'

        #Lógica del modo finanzas
        elif self.modoSeleccionado == 'Finance':
            if not self.percentMode:
                if operation == '+':
                    if len(self.slots) == 0: self.guardarEnSlot()
                    else:
                        self.slots[0] += float(self.pantalla.value())
                        self.valorPorMostrar = '0'
                        self.unPunto = True
                    self.prevOperation = operation
                elif operation == '-':
                    if len(self.slots) == 0: self.guardarEnSlot()
                    else:
                        self.slots[0] -= float(self.pantalla.value())
                        self.valorPorMostrar = '0'
                        self.unPunto = True
                    self.prevOperation = operation
                elif operation == '*':
                    if len(self.slots) == 0: self.guardarEnSlot()
                    else:
                        self.slots[0] *= float(self.pantalla.value())
                        self.valorPorMostrar = '0'
                        self.unPunto = True
                    self.prevOperation = operation
                elif operation == '/':
                    if len(self.slots) == 0: self.guardarEnSlot()
                    else:
                        try:
                            self.slots[0] /= float(self.pantalla.value())
                            self.valorPorMostrar = '0'
                            self.unPunto = True
                        except:
                            self.error = True
                            self.habilitarBotones(False)
                            self.pantalla.display('error')
                            self.valorPorMostrar = '0'
                            try: del self.slots[0]
                            except: pass
                            self.botonIgual.setText('ok')
                    self.prevOperation = operation
                elif operation == 'ISR':
                    self.pantalla.display(str(getISR(float(self.pantalla.value()))))
                    self.valorPorMostrar = '0'

                elif operation == '=':
                    self.percentMode = False
                    self.labelPercent.hide()
                    if self.prevOperation == '+': self.slots[0] += float(self.valorPorMostrar)
                    elif self.prevOperation == '-': self.slots[0] -= float(self.valorPorMostrar)
                    elif self.prevOperation == '*': self.slots[0] *= float(self.pantalla.value())
                    elif self.prevOperation == '/':
                        try: self.slots[0] /= float(self.pantalla.value())
                        except ZeroDivisionError:
                            self.error = True
                            self.habilitarBotones(False)
                            self.pantalla.display('error')
                            self.valorPorMostrar = '0'
                            try: del self.slots[0]
                            except: pass
                            self.botonIgual.setText('ok')
                    if not self.error:
                        if any(self.slots): self.pantalla.display(str(self.slots[0]))
                        self.unPunto = True
                        self.prevOperation = ''
                        self.valorPorMostrar = '0'
                        try: del self.slots[0]
                        except IndexError: pass
                elif operation == 'ok':
                    self.habilitarBotones(True)
                    self.pantalla.display('0')
                    self.botonIgual.setText('=')
                    self.error = False
            else:
                if operation == '+':
                    if len(self.slots) == 0: self.guardarEnSlot()
                    else:
                        self.slots[0] *= 1 + float(self.pantalla.value())/100
                        self.valorPorMostrar = '0'
                        self.unPunto = True
                    self.prevOperation = operation
                elif operation == '-':
                    if len(self.slots) == 0: self.guardarEnSlot()
                    else:
                        self.slots[0] *= 1 - float(self.pantalla.value())/100
                        self.valorPorMostrar = '0'
                        self.unPunto = True
                    self.prevOperation = operation
                elif operation == '*':
                    if len(self.slots) == 0: self.guardarEnSlot()
                    else:
                        self.slots[0] *= float(self.pantalla.value())/100
                        self.valorPorMostrar = '0'
                        self.unPunto = True
                    self.prevOperation = operation
                elif operation == '/':
                    if len(self.slots) == 0: self.guardarEnSlot()
                    else:
                        try:
                            self.slots[0] /= float(self.pantalla.value())/100
                            self.valorPorMostrar = '0'
                            self.unPunto = True
                        except:
                            self.error = True
                            self.habilitarBotones(False)
                            self.pantalla.display('error')
                            self.valorPorMostrar = '0'
                            try: del self.slots[0]
                            except: pass
                            self.botonIgual.setText('ok')
                    self.prevOperation = operation
                elif operation == '=':
                    self.percentMode = False
                    self.labelPercent.hide()
                    if self.prevOperation == '+': self.slots[0] *= 1 + float(self.valorPorMostrar)/100
                    elif self.prevOperation == '-':
                        self.slots[0] *= 1 - float(self.valorPorMostrar)/100
                    elif self.prevOperation == '*': self.slots[0] *= float(self.pantalla.value())/100
                    elif self.prevOperation == '/':
                        try: self.slots[0] /= float(self.pantalla.value()) / 100
                        except ZeroDivisionError:
                            self.error = True
                            self.habilitarBotones(False)
                            self.pantalla.display('error')
                            self.valorPorMostrar = '0'
                            try: del self.slots[0]
                            except: pass
                            self.botonIgual.setText('ok')
                    if not self.error:
                        if any(self.slots): self.pantalla.display(str(self.slots[0]))
                        self.prevOperation = ''
                        self.valorPorMostrar = '0'
                        self.unPunto = True
                        try: del self.slots[0]
                        except IndexError: pass

                elif operation == 'ok':
                    self.habilitarBotones(True)
                    self.pantalla.display('0')
                    self.botonIgual.setText('=')
                    self.error = False

        #Lógica del modo programador
        elif self.modoSeleccionado == 'Programmer':
            #try:
                newBase = self.sender().text()
                if self.base == ('Bin'):
                    if newBase == 'Oct': self.convertion = convert.binToOct(str(int(self.pantalla.value())))
                    elif newBase == 'Dec': self.convertion = convert.binToDec(str(int(self.pantalla.value())))
                    elif newBase == 'Hex': self.convertion = convert.binToHex(str(int(self.pantalla.value())))
                    elif newBase == '=': pass
                elif self.base == 'Oct':
                    if newBase == 'Bin': self.convertion = convert.octToBin(str(int(self.pantalla.value())))
                    elif newBase == 'Dec': self.convertion = convert.octToDec(str(int(self.pantalla.value())))
                    elif newBase == 'Hex': self.convertion = convert.octToHex(str(int(self.pantalla.value())))
                    elif newBase == '=': pass
                elif self.base == 'Dec':
                    if newBase == 'Bin': self.convertion = convert.decToBin(str(int(self.pantalla.value())))
                    elif newBase == 'Oct': self.convertion = convert.decToOct(str(int(self.pantalla.value())))
                    elif newBase == 'Hex': self.convertion = convert.decToHex(str(int(self.pantalla.value())))
                    elif newBase == '=': pass
                elif self.base == 'Hex':
                    if newBase == 'Bin': self.convertion = convert.hexToBin(str(self.valorPorMostrar))
                    elif newBase == 'Oct': self.convertion = convert.hexToOct(str(self.valorPorMostrar))
                    elif newBase == 'Dec': self.convertion = convert.hexToDec(str(self.valorPorMostrar))
                    elif newBase == '=': pass
                self.pantalla.display(self.convertion)
                self.valorPorMostrar = '0'
            #except:
                #pass

        #Lógica del modo libre
        elif self.modoSeleccionado == 'Converter':
            try: btn_txt = self.sender().text()
            except: btn_txt = op
            if btn_txt == '=':
                self.pantalla.display(str(conv(float(self.pantalla.value()), self.comboBox4.currentText())))
                self.valorPorMostrar = '0'

    def borrar(self):
        if self.valorPorMostrar != '':
            self.valorBorrado = self.valorPorMostrar[-1]
            if self.valorBorrado == ".": self.unPunto = True
            if self.valorPorMostrar != "0":
                self.valorPorMostrar = self.valorPorMostrar[:-1]
                if len(self.valorPorMostrar) == 0: self.valorPorMostrar = '0'
        self.pantalla.display(self.valorPorMostrar)

    def keyPressEvent(self, event): #Función para reconocer las teclas presionadas en el teclado, y dar instrucciones de operacion
        self.keysNum = {48: '0', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 54: '6', 55: '7', 56: '8', 57: '9', 46: '.',65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F'}
        if event.key() == 16777219: self.borrar()
        if self.modoSeleccionado in ('Basic', 'Scientific', 'Finance'):
            self.keys = dict(list(self.keysNum.items())[0:11]) #Permite escribir los numeros y el punto en los modos Basic, Scientific y Finance
            dictionary = {43: '+', 45: '-', 42: '*', 47: '/', 16777220: '='}
            if self.modoSeleccionado != 'Scientific' and event.key() in dictionary.keys(): self.operar(dictionary[event.key()])
        elif self.modoSeleccionado == 'Converter':
            self.keys = dict(list(self.keysNum.items())[0:11])
            if event.key() == 16777220: self.operar('=')
        else:
            if self.base == 'Bin':self.keys = dict(list(self.keysNum.items())[0:2])
            elif self.base == 'Oct': self.keys = dict(list(self.keysNum.items())[0:8])
            elif self.base == 'Dec': self.keys = dict(list(self.keysNum.items())[0:10])
            elif self.base == 'Dec': self.keys = dict(list(self.keysNum.items())[0:10])
            elif self.base == 'Hex': self.keys = self.keysNum

        if event.key() in self.keys.keys():
            btn_txt = self.keys[event.key()]
            if btn_txt == ".":
                if self.unPunto:
                    self.valorPorMostrar += btn_txt
                    self.unPunto = False
            else: self.valorPorMostrar += btn_txt
            if self.valorPorMostrar[0] == '0': self.valorPorMostrar = self.valorPorMostrar[1:]
            self.pantalla.display(self.valorPorMostrar)
            if self.prevOperation == '':
                try: del self.slots[0]
                except: pass

    def habilitarBotones(self, habilitar): #Función de apoyo cuando existe un ZeroDivisionError
        self.boton0.setEnabled(habilitar)
        self.boton1.setEnabled(habilitar)
        self.boton2.setEnabled(habilitar)
        self.boton3.setEnabled(habilitar)
        self.boton4.setEnabled(habilitar)
        self.boton5.setEnabled(habilitar)
        self.boton6.setEnabled(habilitar)
        self.boton7.setEnabled(habilitar)
        self.boton8.setEnabled(habilitar)
        self.boton9.setEnabled(habilitar)
        self.botonPunto.setEnabled(habilitar)
        self.operacion1.setEnabled(habilitar)
        self.operacion2.setEnabled(habilitar)
        self.operacion3.setEnabled(habilitar)
        self.operacion4.setEnabled(habilitar)
        self.botonBorrar.setEnabled(habilitar)
        self.comboBox.setEnabled(habilitar)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
    ventana.setFixedSize(400,230)
    ventana.show()
    app.exec_()