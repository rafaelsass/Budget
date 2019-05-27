class Cotacao:
	def __init__(self, mc):
		print("---------COTAÇÃO---------")
	def choose(self, choice1 = 0, tabelas =[]):
		self.tabelas = ['Impressão Digital','Recorte','Lançamento']
		choice1 = int(input("Escolha a tabela:\n1 - Impressão Digital\n2 - Recorte\n3 - Lançamento\n"))
		self.choice1 = self.tabelas[choice1]
	def list(self, choice2 = 0):
		Impressão_Digital = ["Digimax RBT Blockout","Digimax Stop Light 0,08, Digimax","Digimax Stop Light 0,10","Digimax Transparente Fosco","Digimax Fix Color 0,08", "Digimax Fix Color 0.10"]
		if self.choice1 == self.tabelas[1]:
			for i in Impressão_Digital:
				print(Impressão_Digital.index(i),i)
			self.choice2 = int(input("Escolha o produto: ")
