# ###################################################
# Classe de lista que só recebe placas como parâmetro
# ###################################################

import cPlaca

# *******************************************************
class lista_placas:



# *******************************************************
	def __init__(self):

		self.__num_obj__     = 0
		self.__lista__       = []
		self.__ordenado__    = False


# *******************************************************
	def adiciona(self, placa):

		if isinstance(placa, cPlaca.cPiv):				#So aceitas objetos da classe cPiv como elemento

			self.__lista__.append(placa)
			self.__num_obj__ += 1
			self.__ordenado__ = False

		else:
			print("{} não é uma placa válida\n".format(placa))

# *******************************************************
	def __str__(self):
		
		out_str = ""

		for elemento in range(self.__num_obj__):
			out_str += ("{}\n".format(self.__lista__[elemento]))

		return out_str


# *******************************************************
	def get_tamanho(self):

		return self.__num_obj__


# *******************************************************
	def ordena(self):

		if self.__num_obj__ > 1 :
			self.__lista__ = self.__radixSort()

		else:
			self.__lista__


# *******************************************************
	def __countingSort(self, lista, indice, nContador):

		tamanho  = self.__num_obj__ 
		contador = [0]*nContador
		saida    = [0]*tamanho



		for i in range(tamanho):
			placa = lista[i]
			index = placa.rep(indice)
			contador[index] += 1

		for i in range(1, nContador):
			contador[i] += contador[i-1]


		i = tamanho - 1
		while i >= 0:
			placa = lista[i]
			index = placa.rep(indice)
			saida[contador[index]-1] = lista[i]
			contador[index] -= 1
			i-=1

		return saida


# *******************************************************
	def __radixSort(self):

		lista = self.__lista__

		for indice in range (6, -1, -1):


			if (indice>=3 and indice!=4):		
				lista = self.__countingSort(lista, indice, 10)



			else:							    
				lista = self.__countingSort(lista, indice, 26)


		return lista









		