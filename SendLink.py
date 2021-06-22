from time import sleep, asctime
from selenium import webdriver
from ReadLink import ReadTxt
from SendMesage import TypeWords
class CallApp:
	"""
	Essa classe guarda uma função que abre o navegador e retorna o seu webdriver.
	"""

	def openBrowser(self):
		self.driver = webdriver.Firefox(executable_path="")
		self.driver.get("https://web.whatsapp.com")
		return self.driver

class LinkHour:
	"""
	Ao iniciar (__init__), é lido o dia (abreviado em inglês) e o driver da classe
	anterior (CallApp) para ser usado na continuação nas chamadas do navegador
	"""

	def __init__(self, arg, driver):
		self.driver = driver
		self.day_En = arg
		self.send()

	def send(self):
		#'self.id' segue uma lógica que, quando envia algo, soma 2 nele, pulando para o próximo link
		self.id = 1
		while True:
			self.cond = self.verifyHour()
			if self.cond:
				try:
					self.allLinks = ReadTxt().takeLink(self.day_En)
					self.lista = self.allLinks[self.id-1:self.id+1]
					if len(self.lista) == 2:
						self.link = f"{self.lista[0]}{self.lista[1]}"
					else:
						print(self.lista)
						break

				except Exception as a:
					print(a)
					break

				else:
					print(self.link)
					TypeWords(self.driver).type(self.link)
					self.id += 2
					sleep(60)

	def takeTime(self):
		return asctime().split()[3][:5:]

	def verifyHour(self):
		if self.takeTime() == "13:30":
			return True
		elif self.takeTime() == "13:35":
			return True
		elif self.takeTime() == "13:40":
			return True
		elif self.takeTime() == "13:45":
			return True
		elif self.takeTime() == "13:50":
			return True
