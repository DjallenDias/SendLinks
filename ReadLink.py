class ReadTxt:
	#A função seguinte lê os arquivos com base em seu arg
	#Escolhendo qual arquivo abrir, dependendo de seu valor
	def takeLink(self, arg):
		with open(f"LinksInTxt/link{arg}.txt") as arq:
			return arq.readlines()