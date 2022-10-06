import sys

import cPlaca 
import cLista 

if (len(sys.argv) > 1):
    arquivo = str(sys.argv[1])

conjunto = open(arquivo, "r")
lista = cLista.lista_placas()

for linha in conjunto:
	placa = cPlaca.Placa(linha.strip())
	lista.adiciona(placa)


conjunto.close()


lista.ordena()

with open("resultado_final.piv", "w") as resultado:
	resultado.write(str(lista))

