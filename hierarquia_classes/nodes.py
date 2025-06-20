from typing import Any, Optional



class TwoWaysNode:

    def __init__(self, value: Any) -> None:
        self.value = value
        self.next: Optional[TwoWaysNode] = None
        self.previous: Optional[TwoWaysNode] = None

class OneWayNode:
    
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next: Optional[OneWayNode] = None
