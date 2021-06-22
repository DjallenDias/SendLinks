from time import asctime
class Day:
	"""
	Essa classe contém um função que pega a data e hora atuais do sistema e
	retorna o dia (Português completo) e o dia (Abreviado Inglês)
	"""

	def cathDay(self):
		self.day_En = asctime().split()[0]
		if self.day_En == "Mon":
			self.day_Pt = "Segunda"
		elif self.day_En == "Tue":
			self.day_Pt = "Terça"
		elif self.day_En == "Wed":
			self.day_Pt = "Quarta"
		elif self.day_En == "Thu":
			self.day_Pt = "Quinta"
		elif self.day_En == "Fri":
			self.day_Pt = "Sexta"
		return (self.day_Pt, self.day_En)