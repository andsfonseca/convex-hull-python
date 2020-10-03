import tkinter

#Tamanho do Ponto
POINT_SIZE = 6

class Canvas:
    """Cria uma Instancia do Canvas

    Parameters:
        title (String): Nome da Janela
        width (Integer): Comprimento da Janela
        height (Integer): Altura da Janela
        inverted (Boolean): Indica que os objetos instanciados no canvas, vão ser instanciados com seu Y invertido em relação a janela

    Returns:
        Object: Instância do Canvas
    """
    def __init__(self, title="Canvas", width=1000, height=1000, inverted=False):
        self.windows = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.windows, bg="white", height=height, width=width)
        self.windows.title(title)
        self.inverted = inverted
        self.height = height
        self.width = width

    def Show(self):
        """Inicia o Loop de Exibição da Janela
        """
        self.canvas.pack()
        self.canvas.mainloop()
    
    def DrawPoint(self, point, fill='red'):
        """Desenha um ponto no canvas

        Parameters:
            point (Array): Ponto a ser desenhado
            fill (String): Cor do Ponto
        """
        point = point[:]
        if(self.inverted):
            point[1] = self.height - point[1]
        self.canvas.create_oval(point[0] - (POINT_SIZE//2), point[1] - (POINT_SIZE//2), point[0] + (POINT_SIZE//2), point[1] + (POINT_SIZE//2), fill=fill)

    def DrawLine(self, point1, point2, fill='black'):
        """Desenha uma linha entre dois pontos de referência

        Parameters:
            point1 (Array): Ponto que indica o início da linha
            point2 (Array): Ponto que indica o fim da linha
            fill (String): Cor da Linha
        """
        point1 = point1[:]
        point2 = point2[:]
        if(self.inverted):
            point1[1] = self.height - point1[1]
            point2[1] = self.height - point2[1]
        self.canvas.create_line(point1[0],point1[1],point2[0],point2[1], fill=fill)
