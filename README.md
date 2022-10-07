# Problema 1 - Procura-se Veículos

## Introdução:
O referente problema prôpos que fosse feito um algoritmo que fosse capaz de ordernar uma lista de n placas em formato PIV, sistema alfanumérico composto por quatro letras e três números, no formato **AAA0A00** como mostra a figura [1], com esse formato a base de dados poderia chegar até 456.976.000 combinações de placas. Por isso algoritmos com complexidade O(n²) seriam uma pessima escolha para o problema. Em teoria a melhor complexidade para um algoritmo de ordenação seria O(n.logn), porém ao saber o tamanho e o formato das placas é possivel escolher um algoritmo mais eficiente. E que além disso tal algoritmo fosse possivel ser paralelizado. Desse modo para solucionar o problema foi escolhido o algoritmo *radixsort. 

## Radixsort:
O radixsort é um algoritmo baseado no countingsort, que consiste criar um vetor com N entradas, em que N é o número de elementos diferentes possíveis para o valor de entrada. Este vetor funcionará como um contador que será incrementado para cada valor igual ao elemento. Após esse processo é conhecido a quantidade de posições necessárias para cada valor de entrada da chave. Com isso os elementos são transferidos para as posições corretas da lista principal. 
O radix sort utiliza desse processo para ordernar os elementos de uma lista, ele analisa apenas uma parte por vez de cada elemento, utilizando o countingsort varias vezes para cada parte. Podendo ser pelo método 
MSB (começa na parte mais significativa até a menos) ou o LSB (começa na parte menos significativa ate a mais), para esse problema foi escolhido o radixsort LSB. O vídeo [2] explica esse processo.

## Complexidade
Por não utilizar comparações para ordenar, o radixsort é muito utilizado para ordenação lexografica e principalmente para ordernar chaves com tamanho pequeno, isso se encaixa perfeitamente com o problema proposto. De acordo com André Oliveira em [3] esse algoritmo tem complexidade O(n), desse modo sendo muito eficiente para ordernar listas com grandes números de elementos, como é o caso do problema proposto. Além disso Nadathur Satish em [4], um método de paralelização do radixsort, dividindo as sequencias em blocos e sendo processadas por processadores idependentes. Desse modo o algoritmo pode chegar a complexidade O(logn), o que seria ótimo para um grande número de elementos.


# Referências Bibliográficas:
