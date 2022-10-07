# Problema 1 - Procura-se Veículos

## Introdução:
O presente trabalho discorre sobre a solução do problema proposto: um algoritmo capaz de ordernar uma lista de n placas em formato PIV, sistema alfanumérico composto por quatro letras e três números, no formato AAA0A00 (como mostra a figura [1]). Com esse formato, a base de dados poderia chegar até 456.976.000 combinações de placas. Por isso, algoritmos com complexidade O(n²) seriam uma péssima escolha para o problema. Em teoria, a melhor complexidade para um algoritmo de ordenação seria O(n.logn). Entretanto, ao saber o tamanho e o formato das placas, é possivel escolher um algoritmo mais eficiente e que possa ser paralelizado. Desse modo, para solucionar o problema, foi escolhido o algoritmo *radixsort.

![Exemplo de Placa](imgs/PlacaMercosul.jpg)

## Radixsort:
O radixsort é um algoritmo baseado no countingsort, que consiste criar um vetor com N entradas, em que N é o número de elementos diferentes possíveis para o valor de entrada. Este vetor funcionará como um contador que será incrementado para cada valor igual ao elemento. Após esse processo, é conhecida a quantidade de posições necessárias para cada valor de entrada da chave. Com isso, os elementos são transferidos para as posições corretas da lista principal. O radix sort utiliza esse processo para ordernar os elementos de uma lista, analisando apenas uma parte por vez de cada elemento, utilizando o countingsort várias vezes para cada parte. Isso pode ser feito pelo método MSB (começa no bit mais significativo) ou o LSB (começa no bit menos significativo). Para esse problema, foi escolhido o radixsort LSB. O vídeo [2] explica esse processo.


## Complexidade
Por não utilizar comparações para ordenar, o radixsort é muito utilizado para ordenação lexográfica e principalmente para ordernar chaves com tamanho pequeno, e isso se encaixa perfeitamente com o problema proposto. De acordo com André Oliveira, entre outros autores, em [3], esse algoritmo tem complexidade O(n). Logo, é muito eficiente para ordernar listas com grandes números de elementos, como é o caso do problema proposto. Além disso, Nadathur Satish, entre outros autores, em [4], implementou um método de paralelização do radixsort, dividindo as sequencias em blocos e sendo processadas por processadores independentes. Desse modo, o algoritmo pode chegar a complexidade O(logn), o que seria ótimo para um grande número de elementos.

## Conclusão
Para solucionar o problema foi desenvolvido duas TADs, sendo uma classe de placas que só aceita entradas em formato como o Padrão Mercosul, além de outra classe que seria formada pelo mesmo padrão PIV. A partir de exemplo de códigos na internet do radix como em [4], foi adaptado um metodo na classe lista_placas em que pudesse ordernar os elementos contidos, a partir da contagem em ASCII de cada uma das entradas da placa e inserindo, utilizando de um vetor auxiliar, inserindo em sua correta posição. 



# Referências Bibliográficas:
