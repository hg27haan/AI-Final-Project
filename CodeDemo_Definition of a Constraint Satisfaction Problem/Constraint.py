from typing import TypeVar, Generic, List, Dict
from abc import ABC, abstractmethod

V = TypeVar("V")
D = TypeVar("D")

class Constraint(Generic[V, D]):
    def __init__(self, variables: List[V]) -> None:
        self.variables = variables
    @abstractmethod
    def satisfied(self, assigment: Dict[V, D]) -> bool:
        ...
        
class CSP:
    def __init__(self, variables: List[V], domains: Dict[V, D]) -> None:
        self.variables: List[V] = variables
        self.domains: Dict[V, D] = domains
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}
        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError("Mỗi biến nên được gán một miền giá trị")
    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Biến trong ràng buộc không có trong CSP")
            else:
                self.constraints[variable].append(constraint)

class QueensConstraint(Constraint[int, int]):
    def __init__(self, columns: List[int]) -> None:
        super().__init__(columns)
        self.columns: List[int] = columns
    def satisfied(self, assignment: Dict[int, int]) -> bool:
        for q1c, q1r in assignment.items():
            for q2c in range(q1c + 1, len(self.columns) + 1):
                if q2c in assignment:
                    q2r: int = assignment[q2c]
                    if q1r == q2r:
                        return False
                    if abs(q1r-q2r) == abs(q1c-q2c):
                        return False
        return True