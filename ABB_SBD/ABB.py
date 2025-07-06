from typing import Optional, Iterable
from record import Record
from collections import deque
from copy import deepcopy
from node import Node


# Codigo gerado manualmente, referencias usadas:
# - https://www.freecodecamp.org/portuguese/news/arvores-binarias-de-busca-bst-explicada-com-exemplos/
# - https://www.ime.usp.br/~pf/algoritmos/aulas/binst.html
# - https://www.ime.usp.br/~song/mac5710/slides/06bst.pdf

class ABB:
    
    def __init__(self, data: Optional[Iterable[Record]]=None) -> None:
        self.root: Optional[Node] = None

        if data is not None:
            for reg in data:
                self.insert(deepcopy(reg))

    def insert(self, record: Record):
        def _inserir(node: Optional[Node], _record: Record) -> Node:
            if node is None:
                return Node(_record)
            
            if _record < node.current:
                node.left = _inserir(node.left, _record)
            
            elif _record > node.current:
                node.right = _inserir(node.right, _record)
            
            return node

        self.root = _inserir(self.root, record)

    def find(self, cpf: int) -> Optional[Record]:

        def _recursive_find(node: Optional[Node]) -> Optional[Record]:
            if node is None:
                return None
            if cpf < node.current.key:
                return _recursive_find(node.left)
            elif cpf > node.current.key:
                return _recursive_find(node.right)
            return node.current

        return _recursive_find(self.root)

    def remove(self, cpf: int) -> None:
        
        def _min(no: Node) -> Node:
            atual = no
            while atual.left is not None:
                atual = atual.left
            return atual

        def _recursive_remove(node: Optional[Node], _cpf: int) -> Optional[Node]:
            
            if node is None:
                return None
            
            if _cpf < node.current.key:
                node.left = _recursive_remove(node.left, _cpf)
            
            elif _cpf > node.current.key:
                node.right = _recursive_remove(node.right, _cpf)
            
            else:
                
                if node.left is None:
                    return node.right
                
                elif node.right is None:
                    return node.left
                
                min_right_node = _min(node.right)
                node.current = min_right_node.current
                node.right = _recursive_remove(node.right, min_right_node.current.key)
                # node.left = node.left
            
            return node
        
        self.root = _recursive_remove(self.root, cpf)

    def clear(self):
        self.root = None
    
    def delete_branch(self, cpf: int):

        def _recursive_delete(node: Optional[Node], _cpf: int):

            if node is None:
                return None
            
            if _cpf < node.current.key:
                node.left = _recursive_delete(node.left, _cpf)
            
            elif _cpf > node.current.key:
                node.right = _recursive_delete(node.right, _cpf)
            
            else:
                return None
        
        self.root = _recursive_delete(self.root, cpf)

    def orded_record_list(self) -> list[Record]:

        registros = []

        def _orded_reg(node: Optional[Node]):

            if node is not None:
                _orded_reg(node.left)
                _orded_reg(node.right)
                registros.append(node.current)

        _orded_reg(self.root)
        return registros
    
    def breadth_traversal(self) -> list[Record]:

        registros = []

        que = deque([self.root])
        while que:
            node: Node = que.popleft()     # type: ignore
            registros.append(node.current)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)

        return registros

