from ..matrices import STDMatrix, SQMatrix, UPTMatrix, DWTMatrix, DIGMatrix
from typing import Optional
import os

class MainFrame:

    def __init__(self) -> None:
        self.DIR = os.path.dirname(__file__)
        self.mtx_list: dict[str, STDMatrix] = {}
        self.header: list[str] = [self.get_h0(), '']

        self.start()
    
    def start(self):

        self.cycle()
        print("Bem vindo a calculadora matricial no terminal")

        while True:

            opt = self.int_dialog(file_name="menu", inputs=list(range(10)))
            self.clear_hearder()

            match opt:
                case 0:
                    break

                case 1:
                    self.insert_matrix()

                case 2:
                    self.calc()

                case 3:
                    self.load_mtx()

                case 4:
                    self.save_mtx()

                case 5:
                    self.remove_mtx()

                case 6:
                    self.list_all_mtcs()

                case 7:
                    self.save_all()

                case 8:
                    self.load_list()

                case 9:
                    self.clear_list()

            self.cycle()

    # region Menu

    def insert_matrix(self):
        
        opt = self.int_dialog(file_name='mtx_type', inputs=list(range(1, 7)))

        match opt:
            
            case 1:
                self.insert_sq_mtx()
            
            case 2:
                self.insert_upt_mtx()

            case 3:
                self.insert_dwt_mtx()

            case 4:
                self.insert_dig_mtx()

            case 5:
                self.insert_idt()
            
            case 6:
                self.insert_std_mtx()

    def calc(self):
        
        self.show_loaded_names()
        feed_back = ''
        
        while True:
            for t in self.header:
                if len(t) > 0:
                    print(t)
            
            print("Os operadores disponibilizados nessa versão são: '+', '-' e '*'")
            print("objetos podem ser números ou matrizes armazenadas em memória")
            print("Para fazer um cálculo basta digitar '{objeto_1} {operado} {objeto_2}' (uma operação por vez)")
            print("Para salvar novas matrizes basta iniciar o cálculo com '{nome} = {definição_objeto/operação}'")
            print("Definição de objeto é feita por uma sequência de listas (salve objetos e olhe como ele são salvos)")
            print("Chamar uma matriz diretamete ('{nome}') faz com que seu valor apareça na tela")
            print("'_' para voltar ao menu")
            print(feed_back)
            option = input("==> ").strip().replace(' ', '')

            if option == '_':
                return
            
            name: Optional[str] = None
            operation: str

            if '=' in option:
                name, operation = option.split('=')
            else:
                operation = option

            result: Optional[STDMatrix] = None
            for operator in ['+', '-', '*']:
                if operator in operation:
                    obj1, obj2 = operation.split(operator)

                    if obj1 in self.mtx_list:
                        obj1 = f'self.mtx_list["{obj1}"]'

                    if obj2 in self.mtx_list:
                        obj2 = f'self.mtx_list["{obj2}"]'

                    try:
                        result = eval(f'{obj1}{operator}{obj2}')
                    except ValueError as e:
                        print(e)
                    break
            else:
                result = self.try_parse_to_mtx(operation)

            if operation in self.mtx_list:
                result = self.mtx_list[operation]

            if result is None:
                print("Falha a operação")
            elif name is None:
                result.show()
            else:
                self.mtx_list[name] = result
            
            input('Aperte enter para continuar...')
            self.cycle()
            self.show_loaded_names()

    def load_mtx(self):
        mtx_folder = self.DIR + "/mtx"
        txt_files = [f[1:-4] for f in os.listdir(mtx_folder) if f.endswith('.txt') and f.startswith('_')]

        file = self.str_dialog(text=f"Matrizes salvas - {txt_files}\nEscolha uma delas para carregar", inputs=txt_files)

        if file is None:
            return

        with open(mtx_folder + f'/_{file}.txt', 'r') as f:
            f_data = f.readline().replace('\n', '').split(' - ')

        self.mtx_list[file] = eval(f'{f_data[0]}({f_data[1]})')
        self.mtx_loaded(file)

    def save_mtx(self):
        self.show_loaded_names()
        name = self.str_dialog(text='Qual matrix gostaria de salvar?', inputs=list(self.mtx_list.keys()))
        if name is None:
            return
        
        with open(self.DIR + f'/mtx/_{name}.txt', 'w') as file:
            file.write(f"{type(self.mtx_list[name]).__name__} - {self.mtx_list[name].data}")

    def remove_mtx(self):
        self.show_loaded_names()
        name = self.str_dialog(text='Qual matrix gostaria de excluir da memória?', inputs=list(self.mtx_list.keys()))

        if name is None:
            return

        self.mtx_list.pop(name, None)
        self.header.append(f"Matrix {name} removida da memória")
    
    def list_all_mtcs(self):
        
        for key, value in self.mtx_list.items():
            print(f"{key}: {type(value).__name__}")
            value.show()
        
        input('Aperte enter para voltar...')

    def save_all(self):
        self.show_loaded_names()
        name = self.str_dialog(text='Qual nome gostaria de dar a essa lista?')
        if name is None:
            return
        
        with open(self.DIR + f'/mtx/{name}.txt', 'w') as file:
            for key, value in self.mtx_list.items():
                file.write(f"{key} - {type(value).__name__} - {value.data}\n")

        self.header.append(f"Lista {name} salva com sucesso")

    def load_list(self):
        mtx_folder = self.DIR + "/mtx"
        txt_files = [f[:-4] for f in os.listdir(mtx_folder) if f.endswith('.txt') and not f.startswith('_')]

        file = self.str_dialog(text=f"Listas salvas - {txt_files}\nEscolha uma delas para carregar", inputs=txt_files)

        if file is None:
            return

        with open(mtx_folder + f'/{file}.txt', 'r') as f:

            for line in f.readlines():
                f_data = line.replace('\n', '').split(' - ')
                self.mtx_list[f_data[0]] = eval(f'{f_data[1]}({f_data[2]})')

        self.header.append(f"Lista {file} armazenada com sucesso")

    def clear_list(self):
        self.mtx_list.clear()

    # endregion

    # region INSERT 

    def insert_sq_mtx(self):
        self.header.append('Matrix MxM')
        n_lines = self.int_dialog(file_name='mtx_lines')
        if n_lines is None:
            return

        self.header[-1] = f'Matrix {n_lines}x{n_lines}'

        data = [[0.0 for _ in range(n_lines)] for i in range(n_lines)]
        for l in range(n_lines):
            for c in range(n_lines):
                data[l][c] = self.float_dialog(text=f'Insira o valor da coordenada {l}x{c}')

                
        
        self.show_loaded_names()
        name = self.str_dialog(file_name="mtx_name")
        if name is None:
            return

        self.mtx_list[name] = SQMatrix(data)

        self.clear_hearder()

    def insert_upt_mtx(self):
        self.header.append('Matrix MxM')
        n_lines = self.int_dialog(file_name='mtx_lines')
        if n_lines is None:
            return
        self.header[-1] = f'Matrix {n_lines}x{n_lines}'

        data = [[0.0 for _ in range(n_lines - i)] for i in range(n_lines)]
        for l in range(n_lines):
            for c in range(n_lines - l):
                data[l][c] = self.float_dialog(text=f'Insira o valor da coordenada {l}x{c}')
        
        self.show_loaded_names()
        name = self.str_dialog(file_name="mtx_name")
        if name is None:
            return

        self.mtx_list[name] = UPTMatrix(data)

        self.clear_hearder()
        self.mtx_loaded(name)

    def insert_dwt_mtx(self):
        self.header.append('Matrix MxM')
        n_lines = self.int_dialog(file_name='mtx_lines')
        if n_lines is None:
            return
        self.header[-1] = f'Matrix {n_lines}x{n_lines}'

        data = [[0.0 for _ in range(i + 1)] for i in range(n_lines)]
        for l in range(n_lines):
            for c in range(l + 1):
                data[l][c] = self.float_dialog(text=f'Insira o valor da coordenada {l}x{c}')
        
        self.show_loaded_names()
        name = self.str_dialog(file_name="mtx_name")
        if name is None:
            return

        self.mtx_list[name] = DWTMatrix(data)

        self.clear_hearder()
        self.mtx_loaded(name)

    def insert_dig_mtx(self):
        self.header.append('Matrix MxM')
        n_lines = self.int_dialog(file_name='mtx_lines')
        if n_lines is None:
            return
        self.header[-1] = f'Matrix {n_lines}x{n_lines}'

        data = [0.0 for _ in range(n_lines)]
        for l in range(n_lines):
            data[l] = self.float_dialog(text=f'Insira o valor da coordenada {l}x{l}')

        self.show_loaded_names()
        name = self.str_dialog(file_name="mtx_name")
        if name is None:
            return

        self.mtx_list[name] = DIGMatrix(data)

        self.clear_hearder()
        self.mtx_loaded(name)

    def insert_std_mtx(self):
        self.header.append('Matrix MxN')
        n_lines = self.int_dialog(file_name='mtx_lines')
        if n_lines is None:
            return
        self.header[-1] = f'Matrix {n_lines}xN'
        n_columns = self.int_dialog(file_name='mtx_columns')
        if n_columns is None:
            return
        self.header[-1] = f'Matrix {n_lines}x{n_columns}'

        data: list[list[float]] = [[0.0 for _ in range(n_columns)] for _ in range(n_lines)]
        for l in range(n_lines):
            for c in range(n_columns):
                data[l][c] = self.float_dialog(text=f'Insira o valor da coordenada {l}x{c}')
        
        self.show_loaded_names()
        name = self.str_dialog(file_name="mtx_name")
        if name is None:
            return

        self.mtx_list[name] = STDMatrix(data)

        self.clear_hearder()
        self.mtx_loaded(name)

    def insert_idt(self):
        self.header.append('Matrix MxM')
        n_lines = self.int_dialog(file_name='mtx_lines')
        if n_lines is None:
            return
        self.header[-1] = f'Matrix {n_lines}x{n_lines}'

        data = [1.0 for _ in range(n_lines)]
        
        self.show_loaded_names()
        name = self.str_dialog(file_name="mtx_name")
        if name is None:
            return

        self.mtx_list[name] = DIGMatrix(data)

        self.clear_hearder()
        self.mtx_loaded(name)

    # endregion

    # region Header

    def get_h0(self):
        return f"{len(self.mtx_list)} matrizes em memória"

    def mtx_loaded(self, name: str):
        self.header.append(f'Matriz {name} armazenada com sucesso')

    def show_loaded_names(self):

        text = '['
        for key, value in self.mtx_list.items():
            text = ''.join([text, f"{key}: {type(value).__name__}{value.get_std_shape()} | "])
        text = ''.join([text, ']'])
        self.header[1] = (''.join(['Matrizes em memória: ', text]))

    # endregion

    # region UTILS

    def get_txt(self, file_name: str):
        with open(self.DIR + f"/dialog/{file_name}.txt", 'r') as file:
            text = file.read()

            return text

    def cycle(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.header[0] = self.get_h0()

    def try_parse_to_mtx(self, operation: str) -> Optional[STDMatrix]:
        result: Optional[STDMatrix] = None

        if not (operation.startswith('[')):
            return
        
        if not (operation.endswith(']')):
            return
        
        try:
            outer_list = list(operation[1:-1].split(','))
        except Exception:
            return

        try:
            result = DIGMatrix([float(i) for i in outer_list])
        except (ValueError, TypeError):
            pass

        if result is not None:
            return result
        
        try:
            outer_list = list(operation[2:-2].split('],['))
            full_data = [[float(i) for i in list(line.split(','))] for line in outer_list]
        except Exception:
            return
        
        try:
            result = DWTMatrix(full_data)
        except (ValueError, TypeError):
            pass

        if result is not None:
            return result
        
        try:
            result = UPTMatrix(full_data)
        except (ValueError, TypeError):
            pass

        if result is not None:
            return result
        
        try:
            result = SQMatrix(full_data)
        except (ValueError, TypeError):
            pass

        if result is not None:
            return result
        
        try:
            result = STDMatrix(full_data)
        except (ValueError, TypeError):
            pass

        return result

    # endregion

    # region Dialog

    def float_dialog(self, file_name: Optional[str]=None, text: Optional[str]=None) -> float:
        assert (isinstance(text, str) and file_name is None) or (text is None and isinstance(file_name, str))

        if text is None:
            text = self.get_txt(file_name) # type: ignore


        while True:
            for t in self.header:
                if len(t) > 0:
                    print(t)
            
            print(text)
            print("'_' para voltar ao menu")
            option = input("==> ").strip()
            if option == '_':
                break

            self.cycle()
            try:
                num_option = float(option)
            except Exception as e:
                pass
            else:
                break

        return num_option

    def int_dialog(self, file_name: Optional[str]=None, text: Optional[str]=None, inputs: list[int]=[]) -> Optional[int]:
        assert (isinstance(text, str) and file_name is None) or (text is None and isinstance(file_name, str))

        if text is None:
            text = self.get_txt(file_name) # type: ignore

        while True:
            for t in self.header:
                if len(t) > 0:
                    print(t)
            
            print(text)
            print("'_' para voltar ao menu")
            option = input("==> ").strip()

            if option == '_':
                break

            try:
                num_option = int(option)
            except Exception as e:
                num_option = -1

            self.cycle()
            if num_option in inputs or (not inputs and num_option > 0):
                return num_option
            else:
                print("## Invalid input ##")

    def str_dialog(self, file_name: Optional[str]=None, text: Optional[str]=None, inputs: list[str]=[]) -> Optional[str]:
        assert (isinstance(text, str) and file_name is None) or (text is None and isinstance(file_name, str))

        if text is None:
            text = self.get_txt(file_name) # type: ignore

        while True:
            for t in self.header:
                if len(t) > 0:
                    print(t)
            
            print(text)
            print("'_' para voltar ao menu")
            option = input("==> ").strip()
            if option == '_':
                break

            self.cycle()
            if option in inputs or (not inputs and len(option) > 0):
                return option
            else:
                print("## Invalid input ##")

    def clear_hearder(self): 

        while len(self.header) > 2:
            self.header.pop()

    # endregion
