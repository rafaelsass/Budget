import pandas as pd
import decimal as dm
import locale
import os

clear = lambda:os.system('cls')

locale.setlocale(locale.LC_MONETARY,'')
mycontext = dm.Context(prec=9,rounding = dm.ROUND_DOWN)
dm.setcontext(mycontext)

class Cotacao:
	def __init__(self):
		print("---------COTACAO---------")
	def choose(self, choice1 = 0, tabelas =[]):
		self.tabelas = tabelas
		self.tabelas = ['Impressão Digital','Recorte','Lançamento']
		for i in self.tabelas:
			print(self.tabelas.index(i)+1,'-',i)
		choice1 = int(input('\nEscolha a tabela: '))
		self.choice1 = self.tabelas[choice1-1]
	def list(self, produto = [],tabelona = [], choice2= 0,produtera=[]):
		
		self.produtera = produtera
		self.tabelona = tabelona
		self.produto = produto 
		Impressão_Digital = ["IMAX","Digimax", "Stop Light", "Blockout", "Transparente Fosco","Fix Color","Super Brilho","Alta Performance","Revest Wall","Refletivo Digital"]
		Recorte = ['Color Max', 'Color Escovado', 'Cristal Color', 'Color Fluorescente', 'Color Jateado','Jateado Transparente', 'Gold Max', 'Gold Fosco', 'Gold Jateado', 
		'Gold Escovado', 'Gold Fibra', 'Gold Alto Brilho', 'Max Lux', 'Gold Madeira', 'Gold Pedras', 'Gold Telado', 'Gold Artistico', "Gold Savana", 'Gold Couro Corino',
		'Mascara Transferência', "Removivel Fumê", 'Mascara de Poreteção RBT', 'Antiderrapante','Piso Max', 'Adesivo Dupla face Bopp', 'Refletivo colorido', 'Eletrostatico',
		'Poliéster', '3D Transparente', '3D Opaco', 'Digiwall', 'Gold Metalic', 'Gold Artistico Transparente', 'Gold Telado Transparente', 'Gold Escovado Transparente', 
		'Gold Fibra 4D', 'Protect Gloss', 'Gold Alta performance Brilho', 'Gold Alta Performance Perolizado', 'Gold Alta Performance Fosco', 'Gold Alta Performance Fosco Perolizado', 
		'Gold Illusion', 'Cromado Brilho','Cromado Fosco', 'Jateado Transparente Decorativo', 'Fix Color Colorido', 'Gold Croco', 'Gold Max Jateado Metalico']
		Lançamento = ['Silver Max Semi Brilho', 'Silver Max Fosco', 'Color Max Fosco', 'Gold Max Semi Brilho', 'Gold Max Fosco', 'Gold Pedras', 'Antiderrapante']
		
		if self.choice1 == self.tabelas[0]:
			self.tabelona = Impressão_Digital
			for i in Impressão_Digital:
				print("\n",Impressão_Digital.index(i)+1,i)
		elif self.choice1 == self.tabelas[1]:
			self.tabelona = Recorte
			for i in Recorte:
				print('\n', Recorte.index(i)+1,i)
		elif self.choice1 == self.tabelas[2]:
			self.tabelona = Lançamento
			for i in Lançamento:
				print('\n', Lançamento.index(i)+1,i)

		produto1 = int(input("\nEscolha o produto: "))
		self.choice2 = produto1
		self.produtera.append(self.tabelona[self.choice2-1])
		
		
	def pric(self, desconto, contador, largura = [], preço = [], quantidade = [], espessura = [], cor=[]):

		self.cor = cor
		self.preço = preço
		self.desconto = (100-desconto)/100
		self.quantidade = quantidade
		self.contador = contador
		self.largura = largura
		self.espessura = espessura
		if self.choice1 == self.tabelas[0]:
			if self.produtera[self.contador] == "IMAX":
				espessura = 0.20
				largura = 1.22
				preço = 244.57*self.desconto
			elif self.produtera[self.contador] == "Digimax":
				espessuras = [0.08,0.10]
				choice4 = int(input("\n0 - Digimax 0,08\n \n1 - Digmiax 0,10\n \nEscolha a espessura: "))
				espessura = espessuras[choice4]
				if espessura == espessuras[0]:
					larguras = (1.00,1.06,1.22,1.40,1.52,2.00)
					preços = (297.03,314.85,362.37,415.83,451.48,632.57)
				elif espessura == espessuras[1]:
					preços = (369.73,391.91,451.07,517.62,561.99,621.15,698.79,786.45)
					larguras = (1.00,1.06,1.22,1.40,1.52,1.60,1.80,2.00)

			elif self.produtera[self.contador] == 'Stop Light':
				espessuras = [0.08,0.10]
				choice4 = int(input("\n0 - Stop Light 0,08\n \n1 - Stop Light 0,10\n \nEscolha a espessura: "))
				espessura = espessuras[choice4]
				if espessura == espessuras[0]:
					preços = (470.25, 585.88)
					larguras = (1.22,1.52)
				elif espessura == espessuras[1]:
					preços = (369.78,451.13,562.07,698.90)
					larguras = (1,1.22,1.52,1.8)
			elif self.produtera[self.contador] =='Blockout':
				espessura = 0.10
				larguras = (1.06,1.22,1.52)
				preços = (469.57, 541.82, 675.06)

			elif self.produtera[self.contador] =='Transparente Fosco':
				espessura = 0.08
				larguras = (1,1.22,1.52)
				preços = (453.81,533.66,689.80)
			elif self.produtera[self.contador] == 'Fix Color':
				espessuras = [0.08,0.10]
				choice4 = int(input("\n0 - Fix Color 0,08\n \n1 - Fix Color 0,10\n \nEscolha a espessura: "))
				espessura = espessuras[choice4]
				if espessura == espessuras[0]:
					larguras = (1,1.06,1.22,1.52)
					preços = (331.84,351.75,404.84,504.39)
				elif espessura == espessuras[1]:
					larguras = (1,1.22,1.52)
					preços = (361.72,441.30,549.82)
			elif self.produtera[self.contador] == 'Super Brilho':
				espessura = 0.10
				larguras = (1.06,1.22,1.40,1.52)
				preços = (452.77,521.11,597.99,649.25)
			elif self.produtera[self.contador] == 'Alta Performance':
				espessura = 0.07
				larguras = (1.22,1.52)
				preços = (643.49,801.73)
			elif self.produtera[self.contador] == 'Revest Wall':
				espessura = 0.14
				largura = 1.22
				preço = 477.78*self.desconto
			elif self.produtera[self.contador] == 'Refletivo Digital':
				espessura = 0.8
				largura = 1.22
				preço = 4407.35*self.desconto
		
		elif self.choice1 == self.tabelas[1]:
			if self.produtera[self.contador] == "Color Max":
				cores = []
				espessura = [0.08]
				
		clear()
		if len(larguras) > 0:	
			for i in larguras:
				print("\n",larguras.index(i)+1,"-",i)
			choice3 = int(input('\nEscolha a largura: '))
			largura = larguras[choice3-1]
			dic_preço = dict(zip(larguras,preços))
			preço = (dic_preço[largura]*self.desconto)

		clear()
		self.largura.append(largura)
		self.espessura.append(espessura)
		quantidade1 = int(input("\nInsira a quantidade que deseja: "))
		self.quantidade.append(quantidade1)
		self.produto.append(self.tabelona[self.choice2-1]+' '+str(espessura)+' '+str(largura))

		preço = dm.Decimal.from_float(preço).quantize(dm.Decimal('0.01'))
		self.preço.append(preço)

	def final(self, total=[]):
		self.total = list(map(lambda x,y:x*y,self.preço,self.quantidade))
		print(self.produto,self.preço,self.quantidade,self.total)
		dicta = pd.DataFrame({'Descricao do produto':self.produto, 'Vlr unit.(R$)':self.preço, 'Qtd':self.quantidade,'Total(R$)': self.total})
		dicta.insert(4,'TotalC(R$)',dicta['Total(R$)'].cumsum())
		print("\n",dicta)
		pd.DataFrame(dicta).to_excel('cotadinho.xlsx')






			

def loop():
	contadora = 0
	cota1 = Cotacao()
	while True:
		clear()
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









