from typing import Optional



class Record:
    def __init__(self, cpf: int, other_data: int):
        self.key = cpf
        self.file_idx = other_data

    def __lt__(self, other: "Record") -> bool:
        return self.key < other.key

    def __eq__(self, other: "Record") -> bool:
        return self.key == other.key

    def __repr__(self) -> str:
        return f"Record(KEY={self.key}, FILE={self.file_idx})"
