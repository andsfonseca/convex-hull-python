import time

class Timer:
    """Cria um temporizador

    Parameters:
        start (Boolean): Informa se deve iniciar o temporizador ao ser instanciado

    Returns:
        Object: Instância do Temporizador
    """
    def __init__(self, start=False):
        self.timer = None

        if start:
            self.Start()

    def Start(self):
        """Inicia o Temporizador"""
            
        if(self.timer != None):
            print("O temporizador já está em execução.")
            return

        self.timer = time.time()
        pass

    def Stop(self):
        """Encerra o Temporizador

        Returns:
            Float: Tempo de Execução
        """
        
        if(self.timer == None):
            print("O temporizador não foi iniciado.")
            return
    
        end = time.time()
        timef = end - self.timer
        self.timer = None
        return timef

