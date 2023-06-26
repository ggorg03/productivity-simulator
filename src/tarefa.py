import random as rd

class Tarefa:
    def __init__(self, dificuldade:float = None, tentativas:int = 0, ehConcluida:bool = False):
        self.dificuldade = rd.random() if dificuldade is None else dificuldade 
        self.tentativas = tentativas
        self.ehConcluida = ehConcluida
    
    def inc_tentativa(self) -> None:
        self.tentativas+=1
        
    def reset_dificuldade(self) -> None:
        self.dificuldade = rd.random()

    def __str__(self):
        return str(self.dificuldade)
    
    def __eq__(self, obj) -> bool:
        return isinstance(obj, Tarefa) and \
               self.dificuldade == obj.dificuldade and \
               self.ehConcluida == obj.ehConcluida and \
               self.tentativas == obj.tentativas
                    