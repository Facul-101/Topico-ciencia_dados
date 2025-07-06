from file_sys import FilesSys
from typing import Optional
from person import Person
from record import Record
from ABB import ABB

def find_cpf(tree: ABB, file: FilesSys, cpf: int) -> Optional[Person]:
    recod_idx = tree.find(cpf)
    if recod_idx is None:
        print("Registro nao encontrado na ABB.")
        return None

    person = file.find_person(recod_idx.file_idx)
    if person is None or person.deleted:
        print("Registro não encontrado no arquivo (possivelmente foi deletado).")
        return None

    return person

def inserir_person(tree: ABB, file: FilesSys, person: Person):
    idx = file.insert(person)
    record_idx = Record(person.cpf, idx)
    tree.insert(record_idx)

def remove_person(tree: ABB, file: FilesSys, cpf: int):
    record_idx = tree.find(cpf)
    if record_idx is not None:
        file.delete(record_idx.file_idx)
        tree.remove(cpf)

def export_orded_data(tree: ABB, file: FilesSys) -> list[Person]:
    orded_data: list[Person] = []
    
    for record_idx in tree.orded_record_list():
        pessoa = file.find_person(record_idx.file_idx)
        if pessoa and not pessoa.deleted:
            orded_data.append(pessoa)
    
    return orded_data


if __name__ == "__main__":
    tree = ABB()
    arquivo = FilesSys()

    for i in range(1, 10):
        inserir_person(tree, arquivo, Person(int(str(i)*3), chr(i + 65), str(i)))

    print(find_cpf(tree, arquivo, 222))
    remove_person(tree, arquivo, 222)
    print(find_cpf(tree, arquivo, 222))

    print("\nLista ordenada:")
    for pessoa in export_orded_data(tree, arquivo):
        print('- ', pessoa)

    print(tree.breadth_traversal())