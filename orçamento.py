import pandas as pd
import decimal as dm
import locale
import os

clear = lambda:os.system('cls')

locale.setlocale(locale.LC_MONETARY,'')
mycontext = dm.Context(prec=4)
dm.setcontext(mycontext)

class Cotacao:
	def __init__(self):
		print("---------COTACAO---------")
	def choose(self, choice1 = 0, tabelas =[]):
		self.tabelas = ['Impressão Digital','Recorte','Lançamento']
		choice1 = int(input("\n1 - Impressão Digital\n\n2 - Recorte\n\n3 - Lançamento\n\nEscolha a tabela: "))
		self.choice1 = self.tabelas[choice1]
	def list(self, produto = []):
		Impressão_Digital = ["IMAX","Digimax", "Stop Light", "Blockout", "Transparente Fosco","Fix Color","Super Brilho","Alta Performance","Revest Wall","Refletivo Digital"]
		if self.choice1 == self.tabelas[1]:
			for i in Impressão_Digital:
				print("\n",Impressão_Digital.index(i),i)
			produto1 = int(input("\nEscolha o produto: "))
			self.produto = produto 
			self.produto.append(Impressão_Digital[produto1])
	def pric(self, desconto, contador, largura = [], preço = [], quantidade = [], espessura = []):

		self.preço = preço
		self.desconto = (100-desconto)/100
		self.quantidade = quantidade
		self.contador = contador
		self.largura = largura
		self.espessura = espessura
		larguras = ()
		if self.produto[self.contador] == "IMAX":
			espessura = 0.20
			largura = 1.22
			preço = 244.57*self.desconto
		elif self.produto[self.contador] == "Digimax":
			espessuras = [0.08,0.10]
			choice4 = int(input("\n0 - Digimax 0,08\n1 - Digmiax 0,10\nEscolha a espessura: "))
			espessura = espessuras[choice4]
			if espessura == espessuras[0]:
				larguras = (1.00,1.06,1.22,1.40,1.52,2.00)
				preços = (297.03,314.85,362.37,415.83,451.48,632.57)
			elif espessura == espessuras[1]:
				preços = (369.73,391.91,451.07,517.62,561.99,621.15,698.79,786.45)
				larguras = (1.00,1.06,1.22,1.40,1.52,1.60,1.80,2.00)

		elif self.produto[self.contador] == 'Stop Light':
			espessuras = [0.08,0.10]
			choice4 = int(input("\n0 - Stop Light 0,08\n1 - Stop Light 0,10\n \nEscolha a espessura: "))
			espessura = espessuras[choice4]
			if espessura == espessuras[0]:
				preços = (470.25, 585.88)
				larguras = (1.22,1.52)
			elif espessura == espessuras[1]:
				preços = (369.78,451.13,562.07,698.90)
				larguras = (1,1.22,1.52,1.8)
		elif self.produto[self.contador] =='Blockout':
			espessura = 0.10
			larguras = (1.06,1.22,1.52)
			preços = (469.57, 541.82, 675.06)

		elif self.produto[self.contador] =='Transparente Fosco':
			espessura = 0.08
			larguras = (1,1.22,1.52)
			preços = (453.81,533.66,689.80)
		elif self.produto[self.contador] == 'Fix Color':
			espessuras = [0.08,0.10]
			choice4 = int(input("\n0 - Fix Color 0,08\n1 - Fix Color 0,10\n \nEscolha a espessura: "))
			espessura = espessuras[choice4]
			if espessura == espessuras[0]:
				larguras = (1,1.06,1.22,1.52)
				preços = (331.84,351.75,404.84,504.39)
			elif espessura == espessuras[1]:
				larguras = (1,1.22,1.52)
				preços = (361.72,441.30,549.82)
		elif self.produto[self.contador] == 'Super Brilho':
			espessura = 0.10
			larguras = (1.06,1.22,1.40,1.52)
			preços = (452.77,521.11,597.99,649.25)
		elif self.produto[self.contador] == 'Alta Performance':
			espessura = 0.07
			larguras = (1.22,1.52)
			preços = (643.49,801.73)
		elif self.produto[self.contador] == 'Revest Wall':
			espessura = 0.14
			largura = 1.22
			preço = 477.78*self.desconto
		elif self.produto[self.contador] == 'Refletivo digital':
			espessura = 0.8
			largura = 1.22
			preço = 4407.35*self.desconto
		
		if len(larguras) > 0:	
			for i in larguras:
				print("\n",larguras.index(i),"-",i)
			choice3 = int(input('\nEscolha a largura: '))
			largura = larguras[choice3]
			dic_preço = dict(zip(larguras,preços))
			preço = (dic_preço[largura]*self.desconto)

		self.largura.append(largura)
		self.espessura.append(espessura)
		quantidade1 = int(input("\nInsira a quantidade que deseja: "))
		self.quantidade.append(quantidade1)
		print(preço)
		print(type(preço))
		TWOPLACES = dm.Decimal(10)**-2
		quantif = lambda x:dm.Decimal(x).quantize(TWOPLACES)
		preço = quantif(preço)
		self.preço.append(preço)
	def final(self, total=[]):
		self.total = list(map(lambda x,y:x*y,self.preço,self.quantidade))
		dicta = pd.DataFrame({'Produto':self.produto,'Espessura':self.espessura, 'Largura':self.largura, 'Vlr unit.(R$)':self.preço, 'Qtd':self.quantidade,'Total(R$)': self.total})
		dicta.insert(6,'TotalC(R$)',dicta['Total(R$)'].cumsum())
		print("\n",dicta)
		pd.DataFrame(dicta).to_excel('cotadinho.xlsx')






			

def loop():
	contadora = 0
	cota1 = Cotacao()
	while True:
		cota1.choose()
		clear()
		cota1.list()
		clear()
		desc = int(input("\nInsira o desconto desejado: "))
		clear()
		cota1.pric(desc, contadora)
		clear()
		contadora += 1 
		cota1.final()
		a = input("repeat?: ")
		while a!='n' and a!='y':
			a = input("repeat?: ")
		if a.lower() == "n":
			break



loop()



