# ###################################################
#       Classe de objetos no formato PIV
# ###################################################


class cPiv:



# *******************************************************   
	def __init__(self, placa):								

		if self.__verifica_placa(placa):  		#Faz a verificação se está no formato PIV	
			self.__placa__ = placa
		else:
			self.__placa__ = None

	def __str__(self):
		return self.__placa__


# *******************************************************
	def rep(self, indice):					    #Devolve o valor representativo do indice no caso de números de 0 a 9 e de letras de 0 a 26

		valor = ord(self.__placa__[indice])				

		if (48 <= valor <= 57):
			return valor - 48

		elif ( 65  <= valor <= 90 ):
			return valor - 65
		

# *******************************************************		
	def __verifica_placa(self, placa):			

		verificacao = False


		if len(placa) == 7:

			for indice in range(7):
				v_ascii = ord(placa[indice])
		
				if (indice >= 3) and (indice != 4) and (  48 <= v_ascii <= 57):
					verificacao = True

				elif ((indice <= 3) or (indice == 4)) and ( 65  <= v_ascii <= 90 ):
					verificacao = True

				else:
					verificacao = False
					break


		return verificacao


# *******************************************************
	def get_placa(self):
		return self.__placa__



