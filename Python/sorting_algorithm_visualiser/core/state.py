from dataclasses import dataclass, field

@dataclass
class State:
    arr: list = field(default_factory=list)
    active: set = field(default_factory=set)
    sorted_: set = field(default_factory=set)
    pivot: set = field(default_factory=set)
    n: int = 64
 
    def reset_markers(self):
        self.active.clear()
        self.sorted_.clear()
        self.pivot.clear()
