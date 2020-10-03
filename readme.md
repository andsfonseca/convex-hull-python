# Fecho Convexo

Inicialmente este trabalho foi realizado para a cadeira de Geometria Computacional - PUC-Rio

## O que é?

[Descrição da Wikipedia](https://pt.wikipedia.org/wiki/Envolt%C3%B3ria_convexa)

## Notas
 - Foi usado a biblioteca **tkinter** para visualização
 - Foi usado a biblioteca **timer** para contagem de tempo
 - A classe **ConvexHull** contém os métodos principais utilizados
 - O arquivo **example.py** mostra um experimento com um arquivo
 - O arquivo **analyse.py** mostra um experimentos com pontos aleatórios

## Uso

```python
from convexHull import ConvexHull

convex = ConvexHull()
result = convex.DivideAndConquer(points)
```

## Experimentos

| Quantidade de Pontos | Tempo de Execução |
|:--------------------:|:-----------------:|
|          100         |        0,00       |
|         1000         |        0,04       |
|         10000        |        0,41       |
|        100000        |        4,05       |
|        1000000       |       40,38       |


