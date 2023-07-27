# Problema 1 - Procura-se Veículos

## Introdução:
O presente trabalho discorre sobre a solução do problema proposto: um algoritmo capaz de ordernar uma lista de n placas em formato PIV, sistema alfanumérico composto por quatro letras e três números, no formato AAA0A00 (como mostra a figura 1). Com esse formato, a base de dados poderia chegar até 456.976.000 combinações de placas. Por isso, algoritmos com complexidade O(n²) seriam uma péssima escolha para o problema. Em teoria, a melhor complexidade para um algoritmo de ordenação seria O(n.logn). Entretanto, ao saber o tamanho e o formato das placas, é possivel escolher um algoritmo mais eficiente e que possa ser paralelizado. Desse modo, para solucionar o problema, foi escolhido o algoritmo *radixsort.

![Exemplo de Placa](imgs/PlacaMercosul.jpg)

Figura 1 - Exemplo de Placa Mersocul

## Radixsort:
O radixsort é um algoritmo baseado no countingsort, que consiste criar um vetor com N entradas, em que N é o número de elementos diferentes possíveis para o valor de entrada. Este vetor funcionará como um contador que será incrementado para cada valor igual ao elemento. Após esse processo, é conhecida a quantidade de posições necessárias para cada valor de entrada da chave. Com isso, os elementos são transferidos para as posições corretas da lista principal. O radix sort utiliza esse processo para ordernar os elementos de uma lista, analisando apenas uma parte por vez de cada elemento, utilizando o countingsort várias vezes para cada parte. Isso pode ser feito pelo método MSB (começa no bit mais significativo) ou o LSB (começa no bit menos significativo). Para esse problema, foi escolhido o radixsort LSB. 


## Complexidade
Por não utilizar comparações para ordenar, o radixsort é muito utilizado para ordenação lexográfica e principalmente para ordernar chaves com tamanho pequeno, e isso se encaixa perfeitamente com o problema proposto. De acordo com André Oliveira, entre outros autores, em [2], esse algoritmo tem complexidade O(n). Logo, é muito eficiente para ordernar listas com grandes números de elementos, como é o caso do problema proposto. Além disso, Nadathur Satish, entre outros autores, em [1], implementou um método de paralelização do radixsort, dividindo as sequencias em blocos e sendo processadas por processadores independentes. Desse modo, o algoritmo pode chegar a complexidade O(logn), o que seria ótimo para um grande número de elementos (como pode ser visto na figura 2).

![Exemplo de Placa](imagem_2022-10-06_234152442.png)

Figura 2 - Tabela de complexidade


## Solução
Para solucionar o problema, foram desenvolvidas duas TADs, sendo uma classe de placas que só aceita entradas em formato como o Padrão Mercosul, e outra classe que seria formada pelo mesmo padrão PIV. A partir de exemplo de códigos na internet do radix, foi adaptado um método na classe lista_placas que pudesse ordernar os elementos contidos, a partir da contagem em ASCII de cada uma das entradas da placa e inserindo, utilizando um vetor auxiliar, em sua correta posição.





# Referências Bibliográficas:

[1] N. Satish, M. Harris and M. Garland. **Designing efficient sorting algorithms for manycore GPUs**. Disponível em: https://mgarland.org/files/papers/nvr-2008-001.pdf

[2] A. Oliveira and U. Souza. **Algoritmos Paralelos De Ordenação**. Disponível em: https://1library.org/document/q05k3rlv-andré-faria-oliveira-uéverton-santos-algoritmos-paralelos-ordenação.html

[3] M. Rafael, P. Mariotto and A. Vinícius. **Método de ordenação de dados radixsort**. 

[4] Canal YoungmiSmile, **Radix Sort on the Playground.**. Disponível em: https://www.youtube.com/watch?v=ibtN8rY7V5k