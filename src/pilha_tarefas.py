import random as rd

from .tarefa import Tarefa

class PilhaTarefas:
    def __init__(self):
        self.pilha = []
        
    def size(self):
        return len(self.pilha)
        
    def gerar_novas_tarefas(self, quantidade:int = 1) -> None:
        self.pilha+= [Tarefa(rd.random()) for tarefa in range(quantidade)]
        
    def adicionar_tarefas(self, tarefas:list, append:bool = True) -> None:
        if(not append):
            self.pilha = self.pilha + tarefas
        else:
            self.pilha = tarefas + self.pilha
        
    def pegar_tarefas(self, quantidade:int = 1) -> list:
        tarefas = self.pilha[:quantidade]
        self.pilha = self.pilha[quantidade:]
        
        return tarefas

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, PilhaTarefas):
            return False
        
        if self.size() != obj.size():
            return False
        
        for t in self.pilha:
            if(t not in obj.pilha):
                return False
        
        return True

    def __str__(self) -> str:
        str(self.pilha)