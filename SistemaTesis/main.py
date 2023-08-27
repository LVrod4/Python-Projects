import sys, webbrowser, subprocess, re
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QMainWindow
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from db import *
from urllib.parse import urlencode

flask_process = subprocess.Popen(['python3', 'app.py'])

class LogInApp(QMainWindow):
	def __init__(self):
		super(LogInApp, self).__init__()
		self.setWindowTitle("BENEDICTO MARMOL")

		loadUi("login.ui", self)
		self.LogIn_Btn.clicked.connect(self.login)
		self.Sign_Btn.clicked.connect(self.show_reg)
				
	def login(self): 
		user = self.UserIN.text()
		Passw = self.PassIN.text()
		
		if not user or not Passw:
			QMessageBox.warning(self, "Error", "Por favor ingrese todos los datos")
			return
		
		#if not user.isdigit() or not re.match(r'^(33|34)\d{6}$', user):
		if not user.isdigit() or not re.match(r'^\d{7,8}$', user):
			QMessageBox.warning(self, "Error", "El número de cédula debe ser un número entre 7 y 8 dígitos")
			return

		conn = sql.connect("Users.db")
		cursor = conn.cursor()
		instruction = cursor.execute("SELECT * FROM Users WHERE UserName=? AND Password=?", (user, Passw))
		result = instruction.fetchone()
		self.UserIN.setText("")
		self.PassIN.setText("")
		if result:
			QMessageBox.information(self, "Éxito", "Bienvenido!")
			self.show_home()

		else:
			QMessageBox.information(self, "Error", "Usuario/Contraseña inválido\nSi no tiene un usuario, regístrese")

	def show_home(self):
		widget.setCurrentIndex(1)

	def show_reg(self):
		widget.setCurrentIndex(2)

class HomeApp(QMainWindow):
	def __init__(self):
		super(HomeApp,self).__init__()
		loadUi("home.ui",self)
		self.Back2Home.clicked.connect(lambda: self.HomeStacked.setCurrentIndex(0)) 
		self.NewStudnt.clicked.connect(lambda: self.HomeStacked.setCurrentIndex(1)) 	
		self.GenConst.clicked.connect(lambda: self.HomeStacked.setCurrentIndex(2))  
		self.PrimConst.clicked.connect(lambda: self.HomeStacked.setCurrentIndex(3))  
		self.StudData.clicked.connect(lambda: self.HomeStacked.setCurrentIndex(4))  
		self.InfoShow.clicked.connect(lambda: self.HomeStacked.setCurrentIndex(5))  
		self.About.clicked.connect(lambda: self.HomeStacked.setCurrentIndex(5)) 

		self.ConstEstu.clicked.connect(lambda: self.GenStacked.setCurrentIndex(1)) 
		self.ConstCond.clicked.connect(lambda: self.GenStacked.setCurrentIndex(2)) 
		self.ConstRet.clicked.connect(lambda: self.GenStacked.setCurrentIndex(3))

		self.ConstPros.clicked.connect(lambda: self.PrimStacked.setCurrentIndex(1))
		self.ConstRetP.clicked.connect(lambda: self.PrimStacked.setCurrentIndex(2))

		self.NoCed.clicked.connect(lambda: self.Register.setCurrentIndex(1))
		self.Ced.clicked.connect(lambda: self.Register.setCurrentIndex(2))

		self.NoC_StuReg_Btn.clicked.connect(self.NoC_StuReg)
		self.StuReg_Btn.clicked.connect(self.C_StuReg)
		self.SearchConstEst_Btn.clicked.connect(self.SearchConstEst)
		self.SearchConstProsecPrim_Btn.clicked.connect(self.SearchConstProsec)
		self.SearchConstRetP_Btn.clicked.connect(self.SearchConstRete)
		self.SearchConstCond_Btn.clicked.connect(self.SearchConstCond)
		self.SearchConstRet_Btn.clicked.connect(self.SearchConstReti)
		self.SearchData_Btn.clicked.connect(self.SearchStudData)
		
		self.NoC_RepComboCed.addItems(['V-','E-'])
		self.NoC_StudComboCed.addItems(['V-','E-'])
		self.ComboCed.addItems(['V-','E-'])
		self.StudComboCed.addItems(['V-','E-'])

		self.ComboGrade.addItems(['PRIMER GRADO', 'SEGUNDO GRADO', 'TERCER GRADO', 'CUARTO GRADO', 'QUINTO GRADO', 'SEXTO GRADO', 'PRIMER AÑO', 'SEGUNDO AÑO', 'TERCER AÑO'])
		self.ComboSec.addItems(['A', 'B', 'C', 'D'])

		self.ComboPrimAct.addItems(['PRIMER GRADO', 'SEGUNDO GRADO', 'TERCER GRADO', 'CUARTO GRADO', 'QUINTO GRADO', 'SEXTO GRADO'])
		self.ComboPrimLit.addItems(['A', 'B', 'C', 'D'])

		self.ComboRetP.addItems(['PRIMER GRADO', 'SEGUNDO GRADO', 'TERCER GRADO', 'CUARTO GRADO', 'QUINTO GRADO', 'SEXTO GRADO'])
	
		self.RetActGrade.addItems(['PRIMER GRADO', 'SEGUNDO GRADO', 'TERCER GRADO', 'CUARTO GRADO', 'QUINTO GRADO', 'SEXTO GRADO', 'PRIMER AÑO', 'SEGUNDO AÑO', 'TERCER AÑO'])
		self.RazSelect.addItems(['CAMBIO DE RESIDENCIA', 'PROBLEMAS DE SALUD', 'PROBLEMAS DE CONDUCTA'])

		self.NoC_Estados = {'Amazonas': ['Alto Orinoco', 'Atabapo', 'Atures', 'Autana', 'Manapiare', 'Maroa', 'Río Negro'],
		  				'Anzoátegui': ['Anaco', 'Aragua', 'Bolívar', 'Bruzual', 'Cajigal', 'Carvajal', 'Freites', 'Guanipa', 'Guanta', 'Independencia', 'Libertad', 'Sir Arthur McGregor', 'Miranda', 'Monagas', 'Peñalver', 'Píritu', 'San Juan de Capistrano', 'Santa Ana', 'Simón Rodríguez', 'Sotillo', 'Turístico Diego Bautista Urbaneja'],
                        'Apure': ['Achaguas', 'Biruaca', 'Pedro Camejo', 'Muñoz', 'Páez', 'Rómulo', 'San Fernando'],
                        'Aragua': ['Alcántara', 'Bolívar', 'Camatagua', 'Girardot', 'Lamas', 'Libertador', 'Mariño', 'Mario Briceño Iragorry', 'Michelena', 'Ocumare de la Costa de Oro', 'Revenga', 'Ribas', 'San Casimiro', 'San Sebastián', 'Sucre', 'Tovar', 'Urdaneta', 'Zamora'],
						'Barinas': ['Alberto Arvelo Torrealba', 'Andrés Eloy Blanco', 'Antonio José de Sucre', 'Arismendi', 'Barinas', 'Bolívar', 'Cruz Paredes', 'Ezequiel Zamora', 'Obispos', 'Pedraza', 'Rojas', 'Sosa'],
						'Bolívar': ['Angostura', 'Angostura del Orinoco', 'Caroní', 'Cedeño', 'Chien', 'El Callao', 'Gran Sabana', 'Piar', 'Roscio', 'Sifontes', 'Sucre'],
						'Carabobo': ['Bejuma', 'Carlos Arvelo', 'Diego Ibarra', 'Guacara', 'Juan José Mora', 'Libertador', 'Los Guayos', 'Miranda', 'Montalbán', 'Naguanagua', 'Puerto Cabello', 'San Diego', 'San Joaquín', 'Valencia'],
						'Cojedes': ['Anzoátegui', 'San Carlos', 'Girardot', 'Lima Blanco', 'Pao de San Juan Bautista', 'Ricaurte', 'Rómulo Gallegos', 'Tinaco', 'Tinaquillo'],
						'Delta Amacuro': ['Antonio Díaz', 'Casacoima', 'Pedernales', 'Tucupita'],
						'Distrito Capital': ['Libertador'],
						'Falcón': ['Acosta', 'Bolívar', 'Buchivacoa', 'Carirubana', 'Colina', 'Dabajuro', 'Democracia', 'Falcón', 'Federación', 'Iturriza', 'Jacura', 'Los Taques', 'Manaure', 'Mauroa', 'Miranda', 'Palmasola', 'Petit', 'Píritu', 'San Francisco', 'Sucre', 'Silva', 'Tocópero', 'Unión', 'Urumaco', 'Zamora'],
						'Guárico': ['Camaguán', 'Chaguaramas', 'El Socorro', 'Francisco de Miranda', 'José Félix Ribas', 'José Tadeo Monagas', 'Juan Germán Roscio', 'Juan José Rondón', 'Julián Mellado', 'Leonardo Infante', 'Ortiz', 'San Gerónimo de Guayabal', 'San José de Guaribe', 'Santa María de Ipire', 'Zaraza'],
						'Lara': ['Andrés Eloy Blanco', 'Crespo', 'Iribarren', 'Jiménez', 'Morán', 'Palavecino', 'Simón Planas', 'Torres', 'Urdaneta'],
						'La Guaira': ['Vargas'],
						'Mérida': ['Alberto Adriani', 'Andrés Bello', 'Antonio Pinto Salinas', 'Aricagua', 'Arzobispo Chacón', 'Campo Elías', 'Caracciolo Parra Olmedo', 'Cardenal Quintero', 'Guaraque', 'Julio Cesar Salas', 'Justo Briceño', 'Libertador', 'Miranda', 'Obispo Ramos de Lora', 'Padre Noguera', 'Pueblo Llano', 'Rangel', 'Rivas Dávila', 'Santos Marquina', 'Sucre', 'Tovar', 'Tulio Febres Cordero', 'Zea'],
						'Miranda': ['Acevedo', 'Andrés Bello', 'Baruta', 'Bolívar', 'Brión', 'Buroz', 'Carrizal', 'Chacao', 'Cristóbal Rojas', 'El Hatillo', 'Guaicaipuro', 'Gual', 'Independencia', 'Lander', 'Los Salias', 'Páez', 'Paz Castillo', 'Plaza', 'Sucre', 'Urdaneta', 'Zamora'],
						'Monagas': ['Acosta', 'Aguasay', 'Bolívar', 'Caripe', 'Cedeño', 'Libertador', 'Maturín', 'Piar', 'Punceres', 'Santa Bárbara', 'Sotillo', 'Uracoa', 'Zamora'],
						'Nueva Esparta': ['Antolín del Campo', 'Antonio Díaz', 'Arismendi', 'García', 'Gómez', 'Macanao', 'Maneiro', 'Marcano', 'Mariño', 'Tubores', 'Villalba'],
						'Portuguesa': ['Agua Blanca', 'Araure', 'Esteller', 'Guanare', 'Guanarito', 'José Vicente de Unda', 'Ospino', 'Páez', 'Papelón', 'San Genaro de Boconoíto', 'San Rafael de Onoto', 'Santa Rosalía', 'Sucre', 'Turén'],
						'Sucre': ['Andrés Eloy Blanco', 'Andrés Mata', 'Arismendi', 'Benítez', 'Bermúdez', 'Bolívar', 'Cajigal', 'Cruz Salmerón Acosta', 'Libertador', 'Mariño', 'Mejía', 'Montes', 'Ribero', 'Sucre', 'Valdez'],
						'Táchira': ['Andrés Bello', 'Antonio Rómulo Costa', 'Ayacucho', 'Bolívar', 'Cárdenas', 'Córdoba', 'Fernández', 'Francisco de Miranda', 'García de Hevia', 'Guásimos', 'Independencia', 'Jáuregui', 'José María Vargas', 'Junín', 'Libertad', 'Libertador', 'Lobatera', 'Michelena', 'Panamericano', 'Pedro María Ureña', 'Rafael Urdaneta', 'Samuel Dario Maldonado', 'San Cristóbal', 'San Judas Tadeo', 'Seboruco', 'Simón Rodríguez', 'Sucre', 'Torbes', 'Uribante'],
						'Trujillo': ['Andrés Bello', 'Boconó', 'Bolívar', 'Candelaria', 'Carache', 'Carvajal', 'Escuque', 'Juan Vicente Campo Elías', 'La Ceiba', 'Márquez Cañizales', 'Miranda', 'Monte Carmelo', 'Motatán', 'Pampán', 'Pampanito', 'Rangel', 'Sucre', 'Trujillo', 'Urdaneta', 'Valera'],
						'Yaracuy': ['Arístides Bastidas', 'Bolívar', 'Bruzual', 'Cocorote', 'Independencia', 'José Antonio Páez', 'La Trinidad', 'Manuel Monge', 'Nirgua', 'Peña', 'San Felipe', 'Sucre', 'Urachiche', 'Veroes'],
						'Zulia': ['Almirante Padilla', 'Baralt', 'Cabimas', 'Catatumbo', 'Colón', 'Francisco Javier Pulgar', 'Guajira', 'Jesús Enrique Lossada', 'Jesús María Semprún', 'La Cañada de Urdaneta', 'Lagunillas', 'Machiques', 'Mara', 'Maracaibo', 'Miranda', 'Rosario de Perijá', 'San Francisco', 'Santa Rita', 'Simón Bolívar', 'Sucre', 'Valmore Rodríguez']}
		
		self.NoC_Stud_State.addItems(list(self.NoC_Estados.keys()))
		self.NoC_Stud_State.currentIndexChanged.connect(self.NoC_UpdateCity)
		self.NoC_UpdateCity()

		self.Estados = {'Amazonas': ['Alto Orinoco', 'Atabapo', 'Atures', 'Autana', 'Manapiare', 'Maroa', 'Río Negro'],
		  				'Anzoátegui': ['Anaco', 'Aragua', 'Bolívar', 'Bruzual', 'Cajigal', 'Carvajal', 'Freites', 'Guanipa', 'Guanta', 'Independencia', 'Libertad', 'Sir Arthur McGregor', 'Miranda', 'Monagas', 'Peñalver', 'Píritu', 'San Juan de Capistrano', 'Santa Ana', 'Simón Rodríguez', 'Sotillo', 'Turístico Diego Bautista Urbaneja'],
                        'Apure': ['Achaguas', 'Biruaca', 'Pedro Camejo', 'Muñoz', 'Páez', 'Rómulo', 'San Fernando'],
                        'Aragua': ['Alcántara', 'Bolívar', 'Camatagua', 'Girardot', 'Lamas', 'Libertador', 'Mariño', 'Mario Briceño Iragorry', 'Michelena', 'Ocumare de la Costa de Oro', 'Revenga', 'Ribas', 'San Casimiro', 'San Sebastián', 'Sucre', 'Tovar', 'Urdaneta', 'Zamora'],
						'Barinas': ['Alberto Arvelo Torrealba', 'Andrés Eloy Blanco', 'Antonio José de Sucre', 'Arismendi', 'Barinas', 'Bolívar', 'Cruz Paredes', 'Ezequiel Zamora', 'Obispos', 'Pedraza', 'Rojas', 'Sosa'],
						'Bolívar': ['Angostura', 'Angostura del Orinoco', 'Caroní', 'Cedeño', 'Chien', 'El Callao', 'Gran Sabana', 'Piar', 'Roscio', 'Sifontes', 'Sucre'],
						'Carabobo': ['Bejuma', 'Carlos Arvelo', 'Diego Ibarra', 'Guacara', 'Juan José Mora', 'Libertador', 'Los Guayos', 'Miranda', 'Montalbán', 'Naguanagua', 'Puerto Cabello', 'San Diego', 'San Joaquín', 'Valencia'],
						'Cojedes': ['Anzoátegui', 'San Carlos', 'Girardot', 'Lima Blanco', 'Pao de San Juan Bautista', 'Ricaurte', 'Rómulo Gallegos', 'Tinaco', 'Tinaquillo'],
						'Delta Amacuro': ['Antonio Díaz', 'Casacoima', 'Pedernales', 'Tucupita'],
						'Distrito Capital': ['Libertador'],
						'Falcón': ['Acosta', 'Bolívar', 'Buchivacoa', 'Carirubana', 'Colina', 'Dabajuro', 'Democracia', 'Falcón', 'Federación', 'Iturriza', 'Jacura', 'Los Taques', 'Manaure', 'Mauroa', 'Miranda', 'Palmasola', 'Petit', 'Píritu', 'San Francisco', 'Sucre', 'Silva', 'Tocópero', 'Unión', 'Urumaco', 'Zamora'],
						'Guárico': ['Camaguán', 'Chaguaramas', 'El Socorro', 'Francisco de Miranda', 'José Félix Ribas', 'José Tadeo Monagas', 'Juan Germán Roscio', 'Juan José Rondón', 'Julián Mellado', 'Leonardo Infante', 'Ortiz', 'San Gerónimo de Guayabal', 'San José de Guaribe', 'Santa María de Ipire', 'Zaraza'],
						'Lara': ['Andrés Eloy Blanco', 'Crespo', 'Iribarren', 'Jiménez', 'Morán', 'Palavecino', 'Simón Planas', 'Torres', 'Urdaneta'],
						'La Guaira': ['Vargas'],
						'Mérida': ['Alberto Adriani', 'Andrés Bello', 'Antonio Pinto Salinas', 'Aricagua', 'Arzobispo Chacón', 'Campo Elías', 'Caracciolo Parra Olmedo', 'Cardenal Quintero', 'Guaraque', 'Julio Cesar Salas', 'Justo Briceño', 'Libertador', 'Miranda', 'Obispo Ramos de Lora', 'Padre Noguera', 'Pueblo Llano', 'Rangel', 'Rivas Dávila', 'Santos Marquina', 'Sucre', 'Tovar', 'Tulio Febres Cordero', 'Zea'],
						'Miranda': ['Acevedo', 'Andrés Bello', 'Baruta', 'Bolívar', 'Brión', 'Buroz', 'Carrizal', 'Chacao', 'Cristóbal Rojas', 'El Hatillo', 'Guaicaipuro', 'Gual', 'Independencia', 'Lander', 'Los Salias', 'Páez', 'Paz Castillo', 'Plaza', 'Sucre', 'Urdaneta', 'Zamora'],
						'Monagas': ['Acosta', 'Aguasay', 'Bolívar', 'Caripe', 'Cedeño', 'Libertador', 'Maturín', 'Piar', 'Punceres', 'Santa Bárbara', 'Sotillo', 'Uracoa', 'Zamora'],
						'Nueva Esparta': ['Antolín del Campo', 'Antonio Díaz', 'Arismendi', 'García', 'Gómez', 'Macanao', 'Maneiro', 'Marcano', 'Mariño', 'Tubores', 'Villalba'],
						'Portuguesa': ['Agua Blanca', 'Araure', 'Esteller', 'Guanare', 'Guanarito', 'José Vicente de Unda', 'Ospino', 'Páez', 'Papelón', 'San Genaro de Boconoíto', 'San Rafael de Onoto', 'Santa Rosalía', 'Sucre', 'Turén'],
						'Sucre': ['Andrés Eloy Blanco', 'Andrés Mata', 'Arismendi', 'Benítez', 'Bermúdez', 'Bolívar', 'Cajigal', 'Cruz Salmerón Acosta', 'Libertador', 'Mariño', 'Mejía', 'Montes', 'Ribero', 'Sucre', 'Valdez'],
						'Táchira': ['Andrés Bello', 'Antonio Rómulo Costa', 'Ayacucho', 'Bolívar', 'Cárdenas', 'Córdoba', 'Fernández', 'Francisco de Miranda', 'García de Hevia', 'Guásimos', 'Independencia', 'Jáuregui', 'José María Vargas', 'Junín', 'Libertad', 'Libertador', 'Lobatera', 'Michelena', 'Panamericano', 'Pedro María Ureña', 'Rafael Urdaneta', 'Samuel Dario Maldonado', 'San Cristóbal', 'San Judas Tadeo', 'Seboruco', 'Simón Rodríguez', 'Sucre', 'Torbes', 'Uribante'],
						'Trujillo': ['Andrés Bello', 'Boconó', 'Bolívar', 'Candelaria', 'Carache', 'Carvajal', 'Escuque', 'Juan Vicente Campo Elías', 'La Ceiba', 'Márquez Cañizales', 'Miranda', 'Monte Carmelo', 'Motatán', 'Pampán', 'Pampanito', 'Rangel', 'Sucre', 'Trujillo', 'Urdaneta', 'Valera'],
						'Yaracuy': ['Arístides Bastidas', 'Bolívar', 'Bruzual', 'Cocorote', 'Independencia', 'José Antonio Páez', 'La Trinidad', 'Manuel Monge', 'Nirgua', 'Peña', 'San Felipe', 'Sucre', 'Urachiche', 'Veroes'],
						'Zulia': ['Almirante Padilla', 'Baralt', 'Cabimas', 'Catatumbo', 'Colón', 'Francisco Javier Pulgar', 'Guajira', 'Jesús Enrique Lossada', 'Jesús María Semprún', 'La Cañada de Urdaneta', 'Lagunillas', 'Machiques', 'Mara', 'Maracaibo', 'Miranda', 'Rosario de Perijá', 'San Francisco', 'Santa Rita', 'Simón Bolívar', 'Sucre', 'Valmore Rodríguez']}
		
		self.Stud_State.addItems(list(self.Estados.keys()))
		self.Stud_State.currentIndexChanged.connect(self.UpdateCity)
		self.UpdateCity()
	
		
	def NoC_UpdateCity(self):
		NoC_State_Select = self.NoC_Stud_State.currentText()
		
		City = self.NoC_Estados.get( NoC_State_Select, [])
		
		self.NoC_Stud_City.clear()
		self.NoC_Stud_City.addItems(City)


	def UpdateCity(self):
		State_Select = self.Stud_State.currentText()
		
		City = self.Estados.get( State_Select, [])
		
		self.Stud_City.clear()
		self.Stud_City.addItems(City)

	def NoC_StuReg(self):	
		NoC_CedVE = self.NoC_RepComboCed.currentText() #V/E representante
		NoC_RepCed = self.NoC_RepCed_IN.text() #Cedula representante
		NoC_RepN = self.NoC_RepN_In.text() #Nombres representante
		NoC_RepL = self.NoC_RepL_In.text() #Apellidos representante
		NoC_RepTlf = self.NoC_RepTlf_In.text() #Tlf representante
		NoC_RepD = self.NoC_RepD_In.text() #Direccion representante

		NoC_StudVE = self.NoC_StudComboCed.currentText()
		NoC_StudN = self.NoC_StudN_In.text() #Nombres estudiante
		NoC_StudL = self.NoC_StudL_In.text() #Apellidos estudiante
		NoC_StudB = self.NoC_StudB_In.text() #Naci estudiante
		NoC_StudSt = self.NoC_Stud_State.currentText()
		NoC_StudCt = self.NoC_Stud_City.currentText()
		
		LetterSpace = QRegExp("[a-zA-ZáéíóúüñÑÁÉÍÓÚ\s]+")
		ValidLS = QRegExpValidator(LetterSpace)
		self.NoC_RepN_In.setValidator(ValidLS)
		self.NoC_RepL_In.setValidator(ValidLS)
		self.NoC_RepD_In.setValidator(ValidLS)
		self.NoC_StudN_In.setValidator(ValidLS)
		self.NoC_StudL_In.setValidator(ValidLS)

		LetterSpace = QRegExp("[a-zA-ZáéíóúüñÑÁÉÍÓÚ\s]+")
		ValidLS = QRegExpValidator(LetterSpace)
		
		if not self.NoC_RepN_In.hasAcceptableInput() or not self.NoC_RepL_In.hasAcceptableInput() or not self.NoC_StudN_In.hasAcceptableInput() or not self.NoC_StudL_In.hasAcceptableInput():
			QMessageBox.warning(self, "Error", "El campo solo debe contener letras")
			return
		
		if not NoC_RepCed or not NoC_RepN or not NoC_RepL or not NoC_RepTlf or not NoC_RepD or not NoC_StudN or not NoC_StudL or not NoC_StudB or not NoC_StudSt or not NoC_StudCt:
			QMessageBox.warning(self, "Error", "Por favor ingrese todos los datos")
			return
		
		#if not user.isdigit() or not re.match(r'^(33|34)\d{6}$', user):
		if not NoC_RepTlf.isdigit() or not re.match(r'^(0412|0414|0424|0416|0426)\d{7}$', NoC_RepTlf):
			QMessageBox.warning(self, "Error", "Ingrese un número de teléfono válido")
			return 
		
		if not NoC_RepCed.isdigit() or not re.match(r'^\d{7,8}$', NoC_RepCed):
			QMessageBox.warning(self, "Error", "El número de cédula debe ser un número entre 7 y 8 dígitos, y solo debe contener números")
			return
		
		#IdNum_F = '{}.{}.{}'.format(IdNum[:2], IdNum[2:5], IdNum[5:])
		
		NoC_RepN = NoC_RepN.upper()
		NoC_RepL = NoC_RepL.upper()
		NoC_RepD = NoC_RepD.upper()
		NoC_StudN = NoC_StudN.upper()
		NoC_StudL = NoC_StudL.upper()
		

		conn = sql.connect("Students.db")
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM Students WHERE RepCed = ?", (NoC_RepCed,))
		result = cursor.fetchone()
		self.NoC_RepCed_IN.setText("")
		self.NoC_StudN_In.setText("")
		self.NoC_StudL_In.setText("")
		self.NoC_RepN_In.setText("")
		self.NoC_RepL_In.setText("")
		self.NoC_RepTlf_In.setText("")
		self.NoC_RepD_In.setText("")

		if result:
			QMessageBox.information(self, "Error", "El estudiante ya está registrado\nIntente nuevamente")
		else:
			cursor.execute("INSERT INTO Students (StudVE, StudN, StudL, StudB, StudSt, StudCt, RepVE, RepCed, RepN, RepL, RepTlf, RepD) VALUES('"+ NoC_StudVE +"', '"+ NoC_StudN +"', '"+ NoC_StudL +"', '"+ NoC_StudB +"', '"+ NoC_StudSt +"', '"+ NoC_StudCt +"', '"+ NoC_CedVE +"', '"+ NoC_RepCed +"', '"+ NoC_RepN +"', '"+ NoC_RepL +"', '"+ NoC_RepTlf +"', '"+ NoC_RepD +"')")
			conn.commit()
			QMessageBox.information(self, "Éxito", "¡Estudiante registrado!")

		conn.commit()
		conn.close()


		## CEDULA ESCOLARRRRR 
		A = 1
		conexion = sql.connect('Students.db')	
		cursor = conexion.cursor()
		cursor.execute('SELECT StudB FROM Students WHERE RepCed = ?', (NoC_RepCed,))
		resultado = cursor.fetchone()
		B = resultado[0][-2:]
		
		cursor.execute('SELECT RepCed FROM Students WHERE RepCed = ?', (NoC_RepCed,))
		resultado = cursor.fetchone()
		C = resultado[0]
		if len(str(C)) <= 7:  # Si tiene menos o igual a 7 dígitos
			C = str(C).zfill(8)  # Agregar un cero a la izquierda
		conexion.close()

		
		D = f'{A}{B}{C}'
		conexion = sql.connect('Students.db')
		cursor = conexion.cursor()
		cursor.execute('UPDATE Students SET StudCed = ? WHERE RepCed = ?', (D, NoC_RepCed))
		conexion.commit()
		conexion.close()

	def C_StuReg(self):
		CedVE = self.ComboCed.currentText() #V/E representante
		RepCed = self.RepCed_IN.text() #Cedula representante
		RepN = self.RepN_In.text() #Nombres representante
		RepL = self.RepL_In.text() #Apellidos representante
		RepTlf = self.RepTlf_In.text() #Tlf representante
		RepD = self.RepD_In.text() #Direccion representante

		StudVE = self.StudComboCed.currentText()
		StudCed = self.StudCed_IN.text() 
		StudN = self.StudN_In.text() #Nombres estudiante
		StudL = self.StudL_In.text() #Apellidos estudiante
		StudB = self.StudB_In.text() #Naci estudiante
		StudSt = self.Stud_State.currentText()
		StudCt = self.Stud_City.currentText()
		
		LetterSpace = QRegExp("[a-zA-ZáéíóúüñÑÁÉÍÓÚ\s]+")
		ValidLS = QRegExpValidator(LetterSpace)
		self.RepN_In.setValidator(ValidLS)
		self.RepL_In.setValidator(ValidLS)
		self.RepD_In.setValidator(ValidLS)
		self.StudN_In.setValidator(ValidLS)
		self.StudL_In.setValidator(ValidLS)

		LetterSpace = QRegExp("[a-zA-ZáéíóúüñÑÁÉÍÓÚ\s]+")
		ValidLS = QRegExpValidator(LetterSpace)
		
		if not RepCed or not RepN or not RepL or not RepTlf or not RepD or not StudCed or not StudN or not StudL or not StudB or not StudSt or not StudCt:
			QMessageBox.warning(self, "Error", "Por favor ingrese todos los datos")
			return
		
		if not self.RepN_In.hasAcceptableInput() or not self.RepL_In.hasAcceptableInput() or not self.StudN_In.hasAcceptableInput() or not self.StudL_In.hasAcceptableInput():
			QMessageBox.warning(self, "Error", "El campo solo debe contener letras")
			return
				
		#if not user.isdigit() or not re.match(r'^(33|34)\d{6}$', user):
		if not RepTlf.isdigit() or not re.match(r'^(0412|0414|0424|0416|0426)\d{7}$', RepTlf):
			QMessageBox.warning(self, "Error", "Ingrese un número de teléfono válido")
			return 
		
		if not RepCed.isdigit() or not re.match(r'^\d{7,8}$', RepCed):
			QMessageBox.warning(self, "Error", "El número de cédula debe ser un número entre 7 y 8 dígitos, y solo debe contener números")
			return
		
		if not StudCed.isdigit() or not re.match(r'^\d{8}$', StudCed):
			QMessageBox.warning(self, "Error", "El número de cédula debe ser un número de 8 dígitos, y solo debe contener números")
			return
		
		#StudCed_F = '{}.{}.{}'.format(StudCed[:2], StudCed[2:5], StudCed[5:])
	
		RepN = RepN.upper()
		RepL = RepL.upper()
		RepD = RepD.upper()
		StudN = StudN.upper()
		StudL = StudL.upper()
		

		connect = sql.connect("Students.db")
		cursor1 = connect.cursor()
		cursor1.execute("SELECT * FROM Students WHERE StudCed = ?", (StudCed,))
		result2 = cursor1.fetchone()
		self.RepCed_IN.setText("")
		self.StudCed_IN.setText("")
		self.StudN_In.setText("")
		self.StudL_In.setText("")
		self.RepN_In.setText("")
		self.RepL_In.setText("")
		self.RepTlf_In.setText("")
		self.RepD_In.setText("")

		if result2:
			QMessageBox.information(self, "Error", "El estudiante ya está registrado\nIntente nuevamente")
		else:
			cursor1.execute("INSERT INTO Students (StudVE, StudCed, StudN, StudL, StudB, StudSt, StudCt, RepVE, RepCed, RepN, RepL, RepTlf, RepD) VALUES('"+ StudVE +"', '"+ StudCed +"', '"+ StudN +"', '"+ StudL +"', '"+ StudB +"', '"+ StudSt +"', '"+ StudCt +"', '"+ CedVE +"', '"+ RepCed +"', '"+ RepN +"', '"+ RepL +"', '"+ RepTlf +"', '"+ RepD +"')")
			connect.commit()
			QMessageBox.information(self, "Éxito", "¡Estudiante registrado!")

		connect.commit()
		connect.close()


	def SearchConstEst(self):	
		input_value = self.Ced_Search_EST.text()
		self.ComboGrade.currentText()
		self.ComboSec.currentText()
		grado_num = self.ComboGrade.currentIndex()
		grado_sec = self.ComboSec.currentIndex()

		if not input_value:
			QMessageBox.warning(self, "Error", "Por favor ingrese todos los datos")
			return
		
		if not input_value.isdigit():
			QMessageBox.warning(self, "Error", "Sólo puede ingresar números")
			return

		#input_value = '{}.{}.{}'.format(input_value[:2], input_value[2:5], input_value[5:])

		params = {'input_value': input_value, 'grado':grado_num, 'seccion':grado_sec}
		url = 'http://localhost:8080/ConstEst/?' + urlencode(params)
		webbrowser.open(url)
		self.Ced_Search_EST.setText("")
	
	def SearchConstProsec(self):
		input_value = self.Ced_Search_Prim.text()
		self.ComboPrimAct.currentText()
		self.ComboPrimLit.currentText()
		grado_actP = self.ComboPrimAct.currentIndex()
		grado_newP = grado_actP + 1
		grado_lit = self.ComboPrimLit.currentIndex()

		if not input_value:
			QMessageBox.warning(self, "Error", "Por favor ingrese todos los datos")
			return
		
		if not input_value.isdigit():
			QMessageBox.warning(self, "Error", "Sólo puede ingresar números")
			return

		#input_value = '{}.{}.{}'.format(input_value[:2], input_value[2:5], input_value[5:])
		
		params = {'input_value': input_value, 'gradoAP':grado_actP, 'gradoNP':grado_newP, 'literal':grado_lit}
		url = 'http://localhost:8080/ConstProsec/?' + urlencode(params)
		webbrowser.open(url)
		self.Ced_Search_Prim.setText("")

	def SearchConstRete(self):
		input_value = self.Ced_Search_RetP.text()
		self.ComboRetP.currentText()
		grado_reten = self.ComboRetP.currentIndex()

		if not input_value:
			QMessageBox.warning(self, "Error", "Por favor ingrese todos los datos")
			return
		
		if not input_value.isdigit():
			QMessageBox.warning(self, "Error", "Sólo puede ingresar números")
			return

		#input_value = '{}.{}.{}'.format(input_value[:2], input_value[2:5], input_value[5:])

		params = {'input_value': input_value, 'gradoRETE':grado_reten}
		url = 'http://localhost:8080/ConstRetP/?' + urlencode(params)
		webbrowser.open(url)
		self.Ced_Search_RetP.setText("")
	
	def SearchConstCond(self):
		input_value = self.Ced_Search_Cond.text()

		if not input_value:
			QMessageBox.warning(self, "Error", "Por favor ingrese todos los datos")
			return
		
		if not input_value.isdigit():
			QMessageBox.warning(self, "Error", "Sólo puede ingresar números")
			return

		#input_value = '{}.{}.{}'.format(input_value[:2], input_value[2:5], input_value[5:])

		params = {'input_value': input_value}
		url = 'http://localhost:8080/ConstCond/?' + urlencode(params)
		webbrowser.open(url)
		self.Ced_Search_Cond.setText("")
	
	def SearchConstReti(self):
		input_value = self.Ced_Search_RET.text()
		self.RetActGrade.currentText()
		self.RazSelect.currentText()
		ret_grad = self.RetActGrade.currentIndex()
		ret_raz = self.RazSelect.currentIndex()

		if not input_value:
			QMessageBox.warning(self, "Error", "Por favor ingrese todos los datos")
			return
		
		if not input_value.isdigit():
			QMessageBox.warning(self, "Error", "Sólo puede ingresar números")
			return

		#input_value = '{}.{}.{}'.format(input_value[:2], input_value[2:5], input_value[5:])
		
		params = {'input_value': input_value, 'grado':ret_grad, 'razon':ret_raz}
		url = 'http://localhost:8080/ConstReti/?' + urlencode(params)
		webbrowser.open(url)
		self.Ced_Search_RET.setText("")

	def SearchStudData(self):
		input_value = self.SearchData_In.text()

		if not input_value:
			QMessageBox.warning(self, "Error", "Por favor ingrese todos los datos")
			return
		
		if not input_value.isdigit():
			QMessageBox.warning(self, "Error", "Sólo puede ingresar números")
			return

		#input_value = '{}.{}.{}'.format(input_value[:2], input_value[2:5], input_value[5:])

		params = {'input_value': input_value}
		url = 'http://localhost:8080/StudData/?' + urlencode(params)
		webbrowser.open(url)
		self.SearchData_In.setText("")

class SignInApp(QDialog):
	def __init__(self):
		super(SignInApp, self).__init__()
		loadUi("registerscreen.ui", self)
		self.Sign_BtnBD.clicked.connect(self.reg)
		self.Return_Btn.clicked.connect(self.ReturnLogin)

	def reg(self):
		user = self.UserUP.text()
		Passw = self.PassUP.text()

		if not user or not Passw:
			QMessageBox.warning(self, "Error", "Por favor ingrese todos los datos")
			return
		
		if not user.isdigit() or not re.match(r'^\d{7,8}$', user):
			QMessageBox.warning(self, "Error", "El número de cédula debe ser un número entre 7 y 8 dígitos")
			return

		conn = sql.connect("Users.db")
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM Users WHERE UserName = ?", (user,))
		result = cursor.fetchone()
		self.UserUP.setText("")
		self.PassUP.setText("")
		if result:
			QMessageBox.information(self, "Error", "Usuario ya registrado\nIntente nuevamente")
		else:
			cursor.execute("INSERT INTO Users VALUES('"+ user +"', '"+ Passw +"')")
			conn.commit()
			QMessageBox.information(self, "Éxito", "Registro exitoso\nYa puede iniciar sesión")

	def ReturnLogin(self):
		widget.setCurrentIndex(0)


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
LogForm = LogInApp()
HomeForm = HomeApp()
SignForm = SignInApp()
widget.addWidget(LogForm)
widget.addWidget(HomeForm)
widget.addWidget(SignForm)
widget.setCurrentIndex(0)
widget.setFixedWidth(1000)
widget.setFixedHeight(520)
widget.show()



sys.exit(app.exec_())