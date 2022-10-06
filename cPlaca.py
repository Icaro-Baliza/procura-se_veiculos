class Placa:

	def __init__(self, placa):


		self.__placa__ = placa

	def __str__(self):
		return self.__placa__

	def __verifica_placa(self, placa):

		verificacao = False

		if len(placa) == 8:

			for indice in range(8):
				v_ascii = ord(placa[indice])
				
				if (indice >= 3) and (indice != 4) and (  48 <= v_ascii <= 57):
					verificacao = True

				elif (3 >= indice) and (indice == 4) and ( 65  <= v_ascii <= 90 ):
					verificacao = True

				else:
					verificacao = False
					break

		return verificacao

	def get_placa(self):
		return self.__placa__

placa = Placa("HCD43B7")
