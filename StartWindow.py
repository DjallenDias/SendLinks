from tkinter import Tk, Button, Label
from TakeDay import Day
from SendLink import LinkHour, CallApp
class App:
	"""
	Essa classe inicia o navegador e logo depois uma janela de start para
	iniciar o enviamento dos links
	"""

	def __init__(self):
		super(App, self).__init__()
		self.driver = CallApp().openBrowser()
		self.window()
		self.labels()
		self.buttons()
		self.tab.mainloop()

	def window(self):
		self.tab = Tk()
		self.tab.title("")
		self.tab.geometry("230x70")

	def labels(self):
		self.dayText = f"Hoje é {Day().cathDay()[0]}-Feira"
		self.dayLabel = Label(self.tab, text=self.dayText, font=("", 15))
		self.dayLabel.place(relx=0, rely=0.02, relheight=0.35, relwidth=1)

	def buttons(self):
		self.startButton = Button(self.tab, text="Lançar Script!!", command=lambda: LinkHour(Day().cathDay()[1], self.driver), font=("", 15))
		self.startButton.place(relx=0.02, rely=0.5, relheight=0.46, relwidth=0.96)

if __name__ == '__main__':
	App()