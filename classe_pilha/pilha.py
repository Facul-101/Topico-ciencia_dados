from array import array
from typing import Literal

class PilhaCheiaErro(Exception):
    
    def __str__(self) -> str:
        return "Stack is full"

class PilhaVaziaErro(Exception):
    
    def __str__(self) -> str:
        return "Stack is empty"

class TrocaErro(Exception):
    pass

class TipoErro(Exception):
    pass

class Pilha:
    def __init__(self, tipo: Literal['i', 'u'], capacidade: int) -> None:
        assert tipo in ('i', 'u'), TipoErro("Tipo deve ser 'i' (inteiro) ou 'u' (caractere unicode)")
        
        self._type = int if tipo == 'i' else str
        self._stack_data = array(tipo)
        self._capacity = capacidade

    def empilha(self, data: int | str) -> None:
        if self.pilha_esta_cheia():
            raise PilhaCheiaErro()
        if not isinstance(data, self._type):
            raise TipoErro(f"Wrong type: expected {self._type}, passed {type(data)}")
        if isinstance(data, str) and len(data) != 1: # Já existe um erro desse na classe array
            raise ValueError("Multiple chars strings can not be stored")

        self._stack_data.append(data)

    def desempilha(self) -> int | str:
        if self.pilha_esta_vazia():
            raise PilhaVaziaErro()
        
        return self._stack_data.pop()

    def pilha_esta_vazia(self) -> bool:
        return len(self._stack_data) == 0

    def pilha_esta_cheia(self) -> bool:
        return len(self._stack_data) >= self._capacity

    def troca(self) -> None:
        if len(self._stack_data) < 2:
            raise TrocaErro(f"Not enough elements to swap values ({self.tamanho()} elements is not enough)")
        
        self._stack_data[-1], self._stack_data[-2] = self._stack_data[-2], self._stack_data[-1]

    def tamanho(self) -> int:
        return len(self._stack_data)

# Exemplo de uso da Pilha:
if __name__ == "__main__":
    pilha = Pilha('i', 5)
    pilha.empilha(1)
    pilha.empilha(2)
    pilha.empilha(3)
    print("Topo desempilhado:", pilha.desempilha())
    print("Tamanho:", pilha.tamanho())
    pilha.empilha(4)
    pilha.empilha(5)
    pilha.troca()
    print("Elementos na pilha:", list(pilha._stack_data))
    print("Pilha está cheia?", pilha.pilha_esta_cheia())
    print("Pilha está vazia?", pilha.pilha_esta_vazia())