import Constraint
from typing import List, Dict

class EightQueensProblem(Constraint.CSP):
    def __init__(self):
        columns: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
        rows: Dict[int, List[int]] = {}
        for column in columns:
            rows[column] = [1, 2, 3, 4, 5, 6, 7, 8]
        super().__init__(columns, rows)
        super().add_constraint(Constraint.QueensConstraint(columns))