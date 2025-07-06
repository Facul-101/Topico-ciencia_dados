

class Person:
    def __init__(self, cpf: int, nome: str, nascimento: str, deletado: bool = False):
        self.cpf = cpf
        self.name = nome
        self.birfday = nascimento
        self.deleted = deletado

    def __repr__(self):
        if self.deleted:
            return "<Registro deletado>"
        return f"Pessoa(CPF={self.cpf}, Nome={self.name}, Nasc={self.birfday})"
