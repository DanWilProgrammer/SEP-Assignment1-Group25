from datetime import datetime
from typing import List, Dict, Optional
import json
from collections import defaultdict 

class Expense:
    def __init__(self, description: str, amount: float, category: str = "General", date: Optional[datetime] = None):
        self.description = description
        self.amount = amount
        self.category = category
        self.date = date or datetime.now()
        self.id = self._generate_id()

    def _generate_id(self) -> str:
        """Generate a unique ID for the expense."""
        return f"{self.date.strftime('%Y%m%d_%H%M%S')}"

    def to_dict(self) -> Dict:
        """Convert expense to dictionary format."""
        return {
            'id': self.id,
            'description': self.description,
            'amount': self.amount,
            'category': self.category,
            'date': self.date.isoformat()
        }

    @classmethod 
    def total_expenses(cls, expenses: List["Expense"]) -> float:
        return sum(exp.amount for exp in expenses)

    @classmethod 
    def average_monthly_expenses(cls, expenses: List["Expense"]) -> float:
        monthly_totals = defaultdict(float)
        for exp in expenses:
            key = (exp.date.year, exp.date.month)
            monthly_totals[key] += exp.amount

        if not monthly_totals:
            return 0.0

        return sum(monthly_totals.values()) / len(monthly_totals)

    @classmethod
    def total_expenses_per_category(cls, expenses: List["Expense"]) -> Dict[str, float]:
        category_totals = defaultdict(float)
        for exp in expenses:
            category_totals[exp.category] += exp.amount
        return dict(category_totals)