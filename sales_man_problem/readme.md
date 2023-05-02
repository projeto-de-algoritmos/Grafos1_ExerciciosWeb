# [Sales man](https://lesales_man_problem/etcode.com/problems/shortest-path-visiting-all-nodes/)


Você tem um grafo não direcionado e conectado de n nós rotulados de 0 a n - 1. Você recebe um gráfico de array onde graph[i] é uma lista de todos os nós conectados com o nó i por uma aresta.

Retorna o comprimento do caminho mais curto que visita cada nó. Você pode iniciar e parar em qualquer nó, pode revisitar os nós várias vezes e pode reutilizar arestas.


#
*Exemplo 1:*

![App Screenshot](https://assets.leetcode.com/uploads/2021/05/12/shortest1-graph.jpg)



Entrada: gráfico = [[1,2,3],[0],[0],[0]]

Saída: 4

Explicação: Um caminho possível é  [1,0,2,0,3]
#
*Exemplo 2:*

![App Screenshot](https://assets.leetcode.com/uploads/2021/05/12/shortest2-graph.jpg)


Entrada: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]

Saída: 4

Explicação: Um caminho possível é [0,1,4,2,3]