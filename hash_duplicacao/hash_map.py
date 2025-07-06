from typing import Callable, Generic, List, Optional, Tuple, TypeVar

# Não sei pq mas nunca timha me perguntado se Python tinha 'generics', aprentemente sim:
# - https://mypy.readthedocs.io/en/stable/generics.html
# - https://medium.com/@steveYeah/using-generics-in-python-99010e5056eb
# OBS: Vou manter o seu uso na sintax antiga para conseguir rodar com python <3.12
K = TypeVar('K')  # Tipo da chave (ex: int para CPF)
V = TypeVar('V')  # Tipo do dado associado

# Referencias para as funcoes hash:
# - https://www.geeksforgeeks.org/dsa/hash-functions-and-list-types-of-hash-functions/
# - https://en.wikipedia.org/wiki/Hash_table

class HashMap(Generic[K, V]):
    def __init__(
            self, 
            size: int = 10, 
            hash_function: Optional[Callable[[K], int]] = None
        ):

        self.size: int = size
        self.map: List[List[Tuple[K, V]]] = [[] for _ in range(size)]  # encadeamento exterior
        self.hash_f: Callable[[K], int] = hash_function if hash_function is not None else self.division_hash

        self.num_collisions = 0
        self.num_duplicates = 0

    # region Hashing functions

    def division_hash(self, chave: K) -> int:
        return hash(chave) % self.size

    def multiplication_hash(self, chave: K) -> int:
        A: float = 0.6180339887
        chave_int = hash(chave)
        return int(self.size * ((chave_int * A) % 1))

    def fold_hash(self, chave: K) -> int:
        chave_str: str = str(chave)
        partes: List[int] = [int(chave_str[i:i+2]) for i in range(0, len(chave_str), 2)]
        return sum(partes) % self.size

    def redefine_hash_function(self, nova_funcao_hash: Callable[[K], int]) -> None:
        self.hash_f = nova_funcao_hash

    # endregion

    # region Operation functions

    def insert(self, key: K, value: V) -> None:
        idx: int = self.hash_f(key)
        for i, (k, _) in enumerate(self.map[idx]):
            if k == key:
                self.map[idx][i] = (key, value)
                return
        self.map[idx].append((key, value))

    def find(self, key: K) -> Optional[V]:
        idx: int = self.hash_f(key)
        for k, v in self.map[idx]:
            if k == key:
                return v
        return None

    def remove(self, key: K) -> bool:
        idx: int = self.hash_f(key)
        for i, (k, _) in enumerate(self.map[idx]):
            if k == key:
                del self.map[idx][i]
                return True
        return False

    def __getitem__(self, indice: int) -> List[Tuple[K, V]]:
        return self.map[indice]

    def __str__(self) -> str:
        return "\n".join(f"{i}: {bucket}" for i, bucket in enumerate(self.map))
    
    # endregion

    # region Specific functionality
    
    def unique_insert(self, key: K, value: V) -> bool:
        idx = self.hash_f(key)
        
        for k, v in self.map[idx]:
        
            if k == key:
                self.num_collisions += 1
        
                if v == value:
                    self.num_duplicates += 1
                    return False
        
                else:
                    return False
        
        self.map[idx].append((key, value))
        return True

    def __iter__(self):
        for bucket in self.map:
            for _, dado in bucket:
                yield dado

    def __len__(self):
        return sum(len(bucket) for bucket in self.map)

    # endregion

if __name__ == "__main__":
    hash_table = HashMap[int, str](size=5)
    hash_table.redefine_hash_function(hash_table.fold_hash)

    hash_table.insert(1, "A")
    hash_table.insert(2, "B")
    hash_table.insert(3, "C")
    hash_table.insert(6, "D")
    hash_table.insert(8, "E")

    print("Buscar 1:", hash_table.find(8))

    print("\nTabela atual:")
    print(hash_table)

    hash_table.remove(1)
    hash_table.remove(2)

    print("\nTabela atual:")
    print(hash_table)