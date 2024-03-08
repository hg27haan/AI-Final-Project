
import Constraint
from typing import List, Dict, Optional, TypeVar, Type

V = TypeVar("V")
D = TypeVar("D")

class Problem_Solver:
    def __init__(self): pass
    def train(self, problem: Type[Constraint.CSP]): pass
    def solve(self): pass

class CSP_Solver(Problem_Solver):
    def __init__(self):
        Problem_Solver.__init__(self)
    def train(self, problem: Type[Constraint.CSP]):
        self.problem = problem
    def solve(self):
        solution = self.backtracking_search()
        return solution
    def consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
        for constraint in self.problem.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True
    def backtracking_search(self, assignment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
        if len(assignment) == len(self.problem.variables):
            return assignment
        unassigned: List[V] = [v for v in self.problem.variables if v not in assignment]
        first: V = unassigned[0]
        for value in self.problem.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            if self.consistent(first, local_assignment):
                result: Optional[Dict[V, D]] = self.backtracking_search(local_assignment)
                if result is not None:
                    return result
        return None