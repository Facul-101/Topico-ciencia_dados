from pilha import Pilha

# Problem/references:
# https://en.wikipedia.org/wiki/Tower_of_Hanoi
# https://www.freecodecamp.org/news/analyzing-the-algorithm-to-solve-the-tower-of-hanoi-problem-686685f032e3/
# https://www.chessandpoker.com/tower-of-hanoi.html

class TorreHanoi:

    def __init__(self, pin_number: int) -> None:
        self.pin_n = pin_number
        self.start  = Pilha('i', pin_number)
        self.middle = Pilha('i', pin_number)
        self.end    = Pilha('i', pin_number)
        
        self.start.name  = 'A'                  # type: ignore
        self.middle.name = 'B'                  # type: ignore
        self.end.name    = 'C'                  # type: ignore
        
        self.solved = False
        self.move_count = 0

        self.reset()

    def reset(self):

        # TODO: reset stack

        for i in range(self.pin_n, 0, -1):
            self.start.empilha(i)

    def solve(self):
        self.show_state()

        if self.solved:
            self.show_moves_count()
            return
        
        self._solving_moves(self.pin_n, self.start, self.middle, self.end)
        self.show_moves_count()
        self.solved = True

    def _solving_moves(self, pin_index: int, source: Pilha, axillary: Pilha, destination: Pilha):
        if pin_index == 1:
            self._move(source, destination)
            return
        
        self._solving_moves(pin_index - 1, source=source,   axillary=destination, destination=axillary)
        self._move(source, destination)
        self._solving_moves(pin_index - 1, source=axillary, axillary=source,      destination=destination)

    def _move(self, source: Pilha, destination: Pilha):
        pin = source.desempilha()
        destination.empilha(pin)
        self.move_count += 1
        print(f"Move pin from {source.name} to {destination.name}") # type: ignore
        self.show_state()
    
    def show_state(self):

        space = self.pin_n + 2
        full_width = space*2 + 1

        start_data: list[int]  = (list(self.start._stack_data) + [0]*(self.pin_n - self.start.tamanho()))[::-1]
        middle_data: list[int] = (list(self.middle._stack_data) + [0]*(self.pin_n - self.middle.tamanho()))[::-1]
        end_data: list[int]    = (list(self.end._stack_data) + [0]*(self.pin_n - self.end.tamanho()))[::-1]

        print(f"{'|':^{full_width}} {'|':^{full_width}} {'|':^{full_width}}")
        print(f"{'|':^{full_width}} {'|':^{full_width}} {'|':^{full_width}}")

        spacer = ' '
        for index, (start_value, middle_value, end_value) in enumerate(zip(start_data, middle_data, end_data)):

            if (index + 1) == self.pin_n:
                spacer = '_'
            
            print(f"{'#'*start_value:{spacer}>{space}}|{'#'*start_value:{spacer}<{space}}", end=' ')
            print(f"{'#'*middle_value:{spacer}>{space}}|{'#'*middle_value:{spacer}<{space}}", end=' ')
            print(f"{'#'*end_value:{spacer}>{space}}|{'#'*end_value:{spacer}<{space}}")
        
        print(f"{self.start.name:^{full_width}} {self.middle.name:^{full_width}} {self.end.name:^{full_width}}") # type: ignore
        print('\n')

    def show_moves_count(self):
        print(f"{self.move_count} moves were made")


if __name__ == "__main__":
    torre = TorreHanoi(12)
    torre.solve()
