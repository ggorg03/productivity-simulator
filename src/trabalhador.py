import random as rd

from .tarefa import Tarefa
from .pilha_tarefas import PilhaTarefas


class Trabalhador:
    def __init__(self, quantidade:int = 3, # quantidade de tarefas por período 
                       qualidade:float = None, # é uma probabilidade - [0, 1]
    ):
        # atributos iniciais do trabalhador
        self.quantidade = quantidade 
        self.qualidade = rd.random() if qualidade is None else qualidade
        self.pilha_de_tarefas = PilhaTarefas()
    
    def realiza_tarefa(self, tarefa:Tarefa) -> Tarefa:
        tarefa.tentativas += 1
        if(tarefa.dificuldade <= self.qualidade):
            tarefa.ehConcluida = True
        else:
            tarefa.reset_dificuldade()
            
        return tarefa
    
    def recebe_novas_tarefas(self, quantidade_novas_tarefas:int) -> None:
        self.pilha_de_tarefas.gerar_novas_tarefas(quantidade_novas_tarefas)
        
    
    
    def trabalha(self, quantidade_novas_tarefas:int = 5) -> list[Tarefa]:
        tarefas = self.pilha_de_tarefas.pegar_tarefas(self.quantidade)
        tarefas = [self.realiza_tarefa(tarefa) for tarefa in tarefas]
        
        tarefas_bem_sucedidas = [tarefa for tarefa in tarefas if tarefa.ehConcluida]
        tarefas_mal_sucedidas = [tarefa for tarefa in tarefas if not tarefa.ehConcluida]
        
        self.pilha_de_tarefas.adicionar_tarefas(tarefas_mal_sucedidas)
        
        return tarefas_bem_sucedidas
    
    def __eq__(self, obj) -> bool:
        return  isinstance(obj, Trabalhador) and \
                self.quantidade == obj.quantidade and \
                self.qualidade == obj.qualidade and \
                self.pilha_de_tarefas == obj.pilha_de_tarefas
     
    def __str__(self) -> str:
        return str(self.pilha_de_tarefas)