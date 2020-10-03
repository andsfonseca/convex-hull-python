from canvas import Canvas
from timer import Timer
from convexHull import ConvexHull
import re

'''Definições'''
PATH_POINTS_FILE = "data/fecho1.txt"
PATH_OUTPUT_CONVEX = "data/fecho1_output.txt"
SHOW_DEBUG_TIMER = True
SHOW_CANVAS = True

'''Funções Auxiliares'''
def getPointsFromFile(path=PATH_POINTS_FILE):
    """Recupera os pontos a partir de um aquivo pre-formatado

    Parameters:
        path (String): Caminho para o arquivo

    Returns:
        Array: Array de Pontos
        Array: Ponto Minimo em X
        Array: Ponto Maximo em X
        Array: Ponto Minimo em Y
        Array: Ponto Maximo em Y

    """
    if(SHOW_DEBUG_TIMER): localTimer = Timer(True)
    points = []

    min_x = []
    max_x = []
    min_y = []
    max_y = []
    firstIteration = True

    file = open(path, "r")

    for line in file:
        point = [int(d) for d in re.findall(r'-?\d+', line)]
        
        #Se é a primeira vez executado
        if(firstIteration):
            firstIteration = False
            min_x = max_x = min_y = max_y = point
        #Senão
        else:
            if(point[0] < min_x[0]): min_x = point
            if(point[0] > max_x[0]): max_x = point
            if(point[1] < min_y[1]): min_y = point
            if(point[1] > max_y[1]): max_y = point

        points.append(point)

    if(SHOW_DEBUG_TIMER): print(">> Pontos lidos em:", localTimer.Stop())
    return points, min_x, min_y, max_x, max_y

def pointAsKey (point): 
    """Transforma um ponto em padrão de String

    Parameters:
        point (Array): Ponto a ser transformado

    Returns:
        String: Ponto em String
    """
    return str(point[0]) + "-" + str(point[1])

def saveDiagonalInFile(points, hull, path=PATH_OUTPUT_CONVEX):
    """Salva um arquivo com os verticies pertecentes ao fecho (Sentido Anti-Horário)

    Parameters:
        points (Array): Array de Pontos
        hull (Array): Array de Pontos do Fecho
        path (String): Caminho para o arquivo
    """
    dictionary = {}
    for i in range(len(points)):
        dictionary[pointAsKey(points[i])] = i

    f= open(path,"w+")
    hull.reverse()
    for p in hull:
        f.write("%d\n" % (dictionary[pointAsKey(p)]))

def ShowPoints(points):
    """Função Criada para exibir os pontos

    Parameters:
        points (Array): Lista de Pontos

    """
    canvas = Canvas(title="Exibição dos Pontos", width=(min_x[0] + max_x[0]), height=(min_y[1] + max_y[1]), inverted=False)

    for p in points:
        canvas.DrawPoint(p, fill='black')
    
    canvas.Show()

#Apenas para Debugar
def ShowPointsAtMerge(left, right, merge):
    """Função Criada para exibir os pontos durante o Merge

    Parameters:
        left (Array): Lista de Pontos pertecente ao fecho esquerdo
        right (Array): Lista de Pontos pertecente ao fecho direito
        merge (Array): Lista de Pontos pertecente ao fecho combinado

    """
    canvas = Canvas(title="Exibição dos Merge", width=(min_x[0] + max_x[0]), height=(min_y[1] + max_y[1]), inverted=False)

    for p in left:
        canvas.DrawPoint(p, fill='blue')
    
    for p in right:
        canvas.DrawPoint(p, fill='green')

    firstPoint = None
    lastPoint = None
    for p in merge:
        canvas.DrawPoint(p)

        if(lastPoint == None):
            firstPoint = p
        else:
            canvas.DrawLine(lastPoint, p)
        
        lastPoint = p
        
    canvas.DrawLine(lastPoint, firstPoint)

    
    canvas.Show()

def ShowPointsWithPolygon(points, polygon):

    """Função Criada para exibir os pontos

    Parameters:
        points (Array): Lista de Pontos

    """
    canvas = Canvas(title="Exibição dos Pontos", width=(min_x[0] + max_x[0]), height=(min_y[1] + max_y[1]), inverted=False)

    for p in points:
        canvas.DrawPoint(p, fill='black')

    firstPoint = None
    lastPoint = None
    for p in polygon:
        canvas.DrawPoint(p)

        if(lastPoint == None):
            firstPoint = p
        else:
            canvas.DrawLine(lastPoint, p)
        
        lastPoint = p
        
    canvas.DrawLine(lastPoint, firstPoint)

    canvas.Show()

'''Main'''
#Carrega os pontos de um arquivo
points, min_x, min_y, max_x, max_y = getPointsFromFile()

#Exibe os pontos
if (SHOW_CANVAS):
    ShowPoints(points)

#Algoritmo do Fecho Convexo
# convex = ConvexHull(DivideAndConquerOnHull=ShowPointsAtMerge)
convex = ConvexHull()

if(SHOW_DEBUG_TIMER): localTimer = Timer(True)
result = convex.DivideAndConquer(points)
if(SHOW_DEBUG_TIMER): print(">> Fecho Executado em:", localTimer.Stop())

if (SHOW_CANVAS):
    ShowPointsWithPolygon(points, result)

saveDiagonalInFile(points, result)

