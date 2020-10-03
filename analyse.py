from timer import Timer
from convexHull import ConvexHull
import random
from canvas import Canvas

def getRandomPoints(amount=100, rangeInX=[0, 10000], rangeInY=[0, 10000]):
    """"Criar um Array de pontos de maneira aleatória

    Parameters:
        amount (int): Quantidade de Pontos
        rangeInX (Array): Intervalo da Coordenada X
        rangeInY (Array): Intervalo da Coordenada Y

    Returns:
        Array: Array de Pontos
        Array: Ponto Minimo em X
        Array: Ponto Maximo em X
        Array: Ponto Minimo em Y
        Array: Ponto Maximo em Y

    """
    points = []

    for _ in range(amount):
        point = [random.randint(rangeInX[0], rangeInX[1]),
                 random.randint(rangeInY[0], rangeInY[1])]

        points.append(point)

    return points

pointsSize = [100, 1000, 10000, 100000, 1000000]

for size in pointsSize:
    points = getRandomPoints(size)
    
    convex = ConvexHull()

    localTimer = Timer(True)
    convex.DivideAndConquer(points)
    print(">> Fecho Convexo de", size, "executado em:", localTimer.Stop())