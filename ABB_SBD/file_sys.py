from typing import Optional
from person import Person


class FilesSys:
    def __init__(self):
        self.data: list[Person] = []

    def insert(self, person: Person) -> int:
        self.data.append(person)
        return len(self.data) - 1  # retorna o índice

    def find_person(self, idx: int) -> Optional[Person]:
        if 0 <= idx < len(self.data):
            return self.data[idx]
        return None

    def delete(self, idx: int) -> None:
        if 0 <= idx < len(self.data):
            self.data[idx].deleted = True

    def list(self) -> list[Person]:
        return self.data