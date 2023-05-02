# [Verifica se um grafo é bipartido](https://leetcode.com/problems/is-graph-bipartite/)


 Existe um gráfico não direcionado com n nós, onde cada nó é numerado entre 0 e n - 1. Você recebe um gráfico de matriz 2D, onde gráfico[u] é uma matriz de nós à qual o nó u é adjacente. Mais formalmente, para cada v no grafo[u], existe uma aresta não direcionada entre o nó u e o nó v. O grafo tem as seguintes propriedades:

Não há bordas próprias (o gráfico[u] não contém u).
Não há arestas paralelas (graph[u] não contém valores duplicados).
Se v está em gráfico[u], então u está em gráfico[v] (o gráfico não é direcionado).
O grafo pode não estar conectado, o que significa que pode haver dois nós u e v tais que não haja caminho entre eles.
Um grafo é bipartido se os nós puderem ser particionados em dois conjuntos independentes A e B, de modo que cada aresta no grafo conecte um nó no conjunto A e um nó no conjunto B.

Retorna verdadeiro se e somente se for bipartido.


#
*Exemplo 1:*

![App Screenshot](https://assets.leetcode.com/uploads/2020/10/21/bi2.jpg)

Entrada: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Saida: false

Explicação: Não há como particionar os nós em dois conjuntos independentes de forma que cada aresta conecte um nó em um e um nó no outro.
Example 2:
#
*Exemplo 2:*

![App Screenshot](https://assets.leetcode.com/uploads/2020/10/21/bi1.jpg)

Entrada: graph = [[1,3],[0,2],[1,3],[0,2]]
Saida: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
