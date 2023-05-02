# [Numero de provincias](https://leetcode.com/problems/number-of-provinces/)


Existem n cidades. Alguns deles estão conectados, enquanto outros não. Se a cidade a está conectada diretamente com a cidade b, e a cidade b está conectada diretamente com a cidade c, então a cidade a está conectada indiretamente com a cidade c.

Uma província é um grupo de cidades conectadas direta ou indiretamente e nenhuma outra cidade fora do grupo.

Você recebe uma matriz n x n isConnected onde isConnected[i][j] = 1 se a i-ésima cidade e a j-ésima cidade estiverem diretamente conectadas, e isConnected[i][j] = 0 caso contrário.

Retorna o número total de províncias.


#
*Exemplo 1:*

![App Screenshot](https://assets.leetcode.com/uploads/2020/12/24/graph1.jpg)



Entrada: isConnected = [[1,1,0],[1,1,0],[0,0,1]]

Saída: 2
#
*Exemplo 2:*

![App Screenshot](https://assets.leetcode.com/uploads/2020/12/24/graph2.jpg)


Entrada: isConnected = [[1,0,0],[0,1,0],[0,0,1]]

Saída: 3
