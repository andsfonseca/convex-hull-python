class ConvexHull:
    """Classe que possui procedimentos para criar um fecho convexo

    Parameters:
        DivideAndConquerOnHull (Method): Executado pelo método de divisão e conquista quando um fecho é criado

    Returns:
        Object: Instância de ConvexHull
    """
    def __init__(self, DivideAndConquerOnHull = None):
        self.__DivideAndConquerOnHull = DivideAndConquerOnHull

    def DivideAndConquer(self, points, ):
        """Retorno o Fecho Convexo usando Divisão e conquista

        Parameters:
            points (Array): Array de Pontos

        Returns:
            Array: Fecho Convexo
        """
        points = self.__RemoveDuplicates(points)
        #Ordena os pontos
        points = self.__OrderByAxis(points, axis=1)
        points = self.__OrderByAxis(points)
        
        return self.__DivideAndConquerProcedure(points)

    def __DivideAndConquerProcedure(self, points):
        size = len(points)

        if(size == 1):
            return points

        left = self.__DivideAndConquerProcedure(points[0:size//2])
        right = self.__DivideAndConquerProcedure(points[size//2:])
        
        merge = self.__DivideAndConquerMerge(left, right)

        return merge

    def __DivideAndConquerMerge(self, left, right):

        #Recupera o Indice do ponto mais a direita do fecho esquerdo
        a_index = self.__GetIndexOfHighestPointbyAxis(left)
        #Recupera o Indice do ponto mais a esquerda do fecho direito
        b_index = self.__GetIndexOfLowestPointbyAxis(right)

        # #Tratativa: Se os pontos existem nos dois fechos
        # if(left[a_index] == right[b_index]):
        #     right.pop(b_index)
        #     if(len(right) == 0):
        #         return left
        #     b_index = self.__GetIndexOfLowestPointbyAxis(right)
            

        upper_a_index, upper_b_index = self.__DivideAndConquerFindUpperTangent(left, right, a_index, b_index)

        lower_a_index, lower_b_index = self.__DivideAndConquerFindLowerTangent(left, right, a_index, b_index)

        #Rotina de Remoção
        hull = []
        left_size = len(left)
        right_size = len(right)
        b_aux = upper_b_index

        while(b_aux != lower_b_index):
            hull.append(right[b_aux])
            b_aux = b_aux+1 if (b_aux+1 < right_size) else 0
        
        hull.append(right[b_aux])

        a_aux = lower_a_index
        while(a_aux != upper_a_index):
            hull.append(left[a_aux])
            a_aux = a_aux+1 if (a_aux+1 < left_size) else 0

        hull.append(left[a_aux])

        if(not self.__DivideAndConquerOnHull == None): self.__DivideAndConquerOnHull(left, right, hull)  
        return hull
    
    def __DivideAndConquerFindUpperTangent(self, left, right, a_index, b_index):

        left_size = len(left)
        right_size = len(right)

        prev_a = None
        prev_b = None

        while (True):
            prev_a = a_index
            prev_b = b_index

            b_next_index = b_index+1 if (b_index+1 < right_size) else 0
            a = left[a_index]
            b = right[b_index]
            b_next = right[b_next_index]
            # move p clockwise as long as it makes left turn
            direction = self.__GetCrossProductOfTwoVectors(a, b, b_next)
            while direction <= 0:
                #São pontos colineares e são os mesmos indices:
                if(direction == 0 and b_index == b_next_index): break
                if(direction == 0 and b_next[1] <= b[1]): break
                      
                # to_remove_b.append(b_index)
                b_index = b_next_index
                b_next_index = b_index+1 if (b_index+1 < right_size) else 0
                b = right[b_index]
                b_next = right[b_next_index]
                
                direction = self.__GetCrossProductOfTwoVectors(a, b, b_next)

            a_previous_index = a_index-1 if (a_index-1 >= 0) else left_size-1
            a = left[a_index]
            b = right[b_index]
            a_previous = left[a_previous_index]

            direction = self.__GetCrossProductOfTwoVectors(b, a, a_previous)
            # move p as long as it makes right turn
            while direction >= 0:
                if(direction == 0 and a_index == a_previous_index): break
                if(direction == 0 and a_previous[1] <= a[1]): break

                a_index = a_previous_index
                a_previous_index = a_index-1 if (a_index-1 >= 0) else left_size-1
                a = left[a_index]
                a_previous = left[a_previous_index]

                direction = self.__GetCrossProductOfTwoVectors(b, a, a_previous)
               
            if a_index == prev_a and b_index == prev_b:
                break
        return a_index, b_index

    def __DivideAndConquerFindLowerTangent(self, left, right, a_index, b_index):

        left_size = len(left)
        right_size = len(right)
        prev_a = None
        prev_b = None

        while (True):
            prev_a = a_index
            prev_b = b_index

            b_previous_index = b_index-1 if (b_index-1 >= 0) else right_size-1
            a = left[a_index]
            b = right[b_index]
            b_previous = right[b_previous_index]
            # move p clockwise as long as it makes left turn
            direction = self.__GetCrossProductOfTwoVectors(a, b, b_previous)
            while direction >= 0:
                #São pontos colineares e são os mesmos indices:
                if(direction == 0 and b_index == b_previous_index): break
                if(direction == 0 and b[1] <= b_previous[1]): break

                b_index = b_previous_index
                b_previous_index = b_index+1 if (b_index+1 < right_size) else 0
                b = right[b_index]
                b_previous = right[b_previous_index]

                direction = self.__GetCrossProductOfTwoVectors(a, b, b_previous)

            a_next_index = a_index+1 if (a_index+1 < left_size) else 0
            a = left[a_index]
            b = right[b_index]
            a_next = left[a_next_index]

            # move p as long as it makes right turn
            direction = self.__GetCrossProductOfTwoVectors(b, a, a_next)
            while direction <= 0:
                #São pontos colineares e são os mesmos indices:
                if(direction == 0 and a_index == a_next_index): break
                #São pontos colineares e mas com alturas difentes:
                if(direction == 0 and a[1] <= a_next[1]): break

                a_index = a_next_index
                a_next_index = a_index-1 if (a_index-1 >= 0) else left_size-1
                a = left[a_index]
                a_next = left[a_next_index]
                
                direction = self.__GetCrossProductOfTwoVectors(b, a, a_next)

            if a_index == prev_a and b_index == prev_b:
                break
        return a_index, b_index
    
    def __OrderByAxis (self, points, axis=0):
        """Ordena uma lista de pontos em um eixo

        Parameters:
            points (Array): Lista de Pontos
            axis (Integer): Eixo usado para realizar a ordenação

        Returns:
            Array: Lista de Pontos ordenados
        
        References:
            O método 'sorted' do python possui complexidade O(n log n).
            (https://en.wikipedia.org/wiki/Timsort)
        """
        if(axis >= len(points[0])):
            print("Não é possível ordenar nesse eixo")
            return None
        
        points = sorted(points, key=lambda p : p[axis])
        return points

    def __RemoveDuplicates(self, points):
        """Remove as duplicatas

        Parameters:
            points (Array): Lista de Pontos

        Returns:
            Array: Lista de Pontos sem duplicatas
        
        References:
            O método usa um dicionário para remover duplicatas, sendo então O(n)
        """
        pointsDictionary = {}
        for i in range(len(points)):
            pointsDictionary[str(points[i][0]) + "-" + str(points[i][1])] = points[i]
        
        return list(pointsDictionary.values())

    def __GetIndexOfLowestPointbyAxis (self, points, axis=0):
        """Recupera o Index de um ponto com o menor valor em um eixo

        Parameters:
            points (Array): Lista de Pontos
            axis (Integer): Eixo a ser buscado

        Returns:
            Integer: Index do Menor ponto
        """
        if(axis >= len(points[0])):
            print("Não é possível procurar nesse eixo")
            return None

        minValue = points[0][axis]
        minIndex = 0

        for i in range(1, len(points)):
            if( points[i][axis] < minValue):
                minIndex = i
                minValue = points[i][axis]

        return minIndex

    def __GetIndexOfHighestPointbyAxis (self, points, axis=0):
        """Recupera o Index de um ponto com o maior valor em um eixo

        Parameters:
            points (Array): Lista de Pontos
            axis (Integer): Eixo a ser buscado

        Returns:
            Integer: Index do Maior ponto
        """
        if(axis >= len(points[0])):
            print("Não é possível procurar nesse eixo")
            return None

        maxValue = points[0][axis]
        maxIndex = 0

        for i in range(1, len(points)):
            if( points[i][axis] > maxValue):
                maxIndex = i
                maxValue = points[i][axis]

        return maxIndex

    def __GetCrossProductOfTwoVectors(self, point1, point2, point3):
        """Retorna o produto cruzado do vetor p1p3 e p1p2
            
        Parameters:
            point1 (Array): Ponto 1
            point2 (Array): Ponto 2
            point3 (Array): Ponto 3

        Returns:
            Float: Retorna o produto cruzado dos vetores. (Se usar como vetor direção, valores positivos indicam sentido horário e negativos anti-horário)
        """

        return self.__GetCrossProductOfTwoSegments(point1, point3, point1, point2)

    def __GetCrossProductOfTwoSegments(self, s1Point1, s1Point2, s2Point1, s2Point2):
        """Retorna o produto cruzado de dois segmentos de reta (Pode ser usado para saber a direção)
        
        Parameters:
            s1Point1 (Array): Ponto Inicial do Segmento 1
            s1Point2 (Array): Ponto Final do Segmento 1
            s2Point1 (Array): Ponto Inicial do Segmento 2
            s2Point2 (Array): Ponto Final do Segmento 2

        Returns:
            Float: Produto Cruzado dos segmentos
        """

        pointA = [s1Point2[0] - s1Point1[0], s1Point2[1] - s1Point1[1]]
        pointB = [s2Point2[0] - s2Point1[0], s2Point2[1] - s2Point1[1]]

        return self.__GetCrossProductOfTwoPoints(pointA, pointB)

    def __GetCrossProductOfTwoPoints(self, point1, point2):
        """Retorna o produto cruzado de dois pontos
        
        Parameters:
            point1 (Array): Ponto 1
            point2 (Array): Ponto 2

        Returns:
            Float: Produto Cruzado dos pontos
        """
        return point1[0] * point2[1] - point2[0] * point1[1]