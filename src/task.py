import random as rd

class Task:
    id = 0
    
    def __init__(self, dificulty:float = None, tryes:int = 0, is_finished:bool = False):
        self.id = Task.id
        self.dificulty = rd.random() if dificulty is None else dificulty 
        self.tryes = tryes
        self.is_finished = is_finished
        # increment global id counter
        Task.id =+ 1
    
    def add_try(self) -> None:
        self.tryes+=1
        
    def reset_dificulty(self) -> None:
        self.dificulty = rd.random()

    def __str__(self):
        return str(self.dificulty)
    
    def __eq__(self, obj) -> bool:
        return isinstance(obj, Task) and \
               self.dificulty == obj.dificulty and \
               self.is_finished == obj.is_finished and \
               self.tryes == obj.tryes