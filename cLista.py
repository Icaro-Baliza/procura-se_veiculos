# ###################################################
# Classe de lista que só recebe placas como parâmetro
# ###################################################

import cPlaca

# *******************************************************
# ***                                                 ***
# *******************************************************
class lista_placas:
# *******************************************************
# ***                                                 ***
# *******************************************************
	def __init__(self):

		self.__num_obj__     = 0
		self.__lista__       = []
		self.__ordenado__    = False

# *******************************************************
# ***       Adiciona um objeto placa à lista          ***
# *******************************************************
	def adiciona(self, placa):

		if self.__verifica_entrada(placa):
			placa = str(placa)
			self.__lista__.append(placa)
			self.__num_obj__ += 1
			self.__ordenado__ = False

# *******************************************************
# ***         Remove um elemento da lista             ***
# *******************************************************
	def remove(self, placa):

		if self.__verifica_entrada(placa):
			pertence, posição = self.__lista__.busca(placa)
			
			if pertence:
				del(self.__lista__[posição])
				self.__num_obj__ -= 1
		
			else:
				print("A placa {} não pertence à lista".format(placa))

# *******************************************************
# ***       Remove todos elementos da lista           ***
# *******************************************************
	def limpa(self):
		
		self.__lista__    = []
		self.__num_obj__  = 0
		self.__ordenado__ = False

# *******************************************************
# ***                                                 ***
# *******************************************************
	def __str__(self):
		
		out_str = ""

		for elemento in range(self.__num_obj__):
			out_str += ("{}\n".format(self.__lista__[elemento]))

		return out_str

# *******************************************************
# ***         Devolve o tamanho da lista              ***
# *******************************************************
	def get_tamanho(self):

		return self.__num_obj__

# *******************************************************
# ***  Escolhe a busca, verificando se esta ordenado  ***
# *******************************************************	
	def busca(self, placa):

		if self.__verifica_entrada(placa):

			if self.__ordenado__ :
				return self.__lista__.__busca_bin(self, placa)

			else:
				return self.__lista__.__busca_seq(self, placa)

# *******************************************************
# ***                                                 ***
# *******************************************************
	def ordena(self):

		if self.__num_obj__ > 1 :
			self.__lista__ = self.__radixSort()

		else:
			self.__lista__

# *******************************************************
# ***                                                 ***
# *******************************************************
	def __verifica_entrada(self, placa):

		verifica = False

		if isinstance(placa, cPlaca.Placa):
			verifica = True

		else:
			print("{} não é uma placa válida".format(placa))

		return verifica

# *******************************************************
# ***      Faz busca binario de um elemento           ***
# *******************************************************
	def __busca_bin(self, placa):
		pass

# *******************************************************
# ***      Faz busca sequencial de um elemento        ***
# *******************************************************
	def __busca_seq(self, placa):
		pass

# *******************************************************
# ***                                                 ***
# *******************************************************
	def __countingSort(self, lista, indice, nContador, nASCII):

		tamanho  = self.__num_obj__ 
		contador = [0]*nContador
		saida    = [0]*tamanho



		for i in range(tamanho):
			index = ord( str(lista[i])[indice] ) - nASCII
			contador[index] += 1

		for i in range(1, nContador):
			contador[i] += contador[i-1]


		i = tamanho - 1
		while i >= 0:
			index = ord( str(lista[i])[indice] ) - nASCII 
			saida[contador[index]-1] = lista[i]
			contador[index] -= 1
			i-=1

		return saida

# *******************************************************
# ***                                                 ***
# *******************************************************
	def __radixSort(self):

		lista = self.__lista__

		for indice in range (6, -1, -1):

			if (indice>=3 and indice!=4):		#Verifica se é número
				lista = self.__countingSort(lista, indice, 10, 48)



			else:							    #Verifica se é letra
				lista = self.__countingSort(lista, indice, 26, 65)


		return lista









		