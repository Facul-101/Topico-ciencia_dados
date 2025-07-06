from record import Record
from typing import Optional



class Node:

    def __init__(self, current_node: Record) -> None:
        self.current = current_node
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
