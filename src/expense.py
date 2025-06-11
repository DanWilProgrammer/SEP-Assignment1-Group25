from datetime import datetime
from typing import List, Dict, Optional
import json
from collections import defaultdict 

class Expense:
    def __init__(self, description: str, amount: float, payer: str, participants: List[str], 
                 category: str = "General", date: Optional[datetime] = None):
        self.description = description
        self.amount = amount
        self.payer = payer
        self.participants = participants
        self.category = category
        self.date = date or datetime.now()
        self.id = self._generate_id()

    def _generate_id(self) -> str:
        """Generate a unique ID for the expense."""
        return f"{self.payer}_{self.date.strftime('%Y%m%d_%H%M%S')}"
    
    def to_dict(self) -> Dict:
        """Convert expense to dictionary format."""
        return {
            'id': self.id,
            'description': self.description,
            'amount': self.amount,
            'payer': self.payer,
            'participants': self.participants,
            'category': self.category,
            'date': self.date.isoformat()
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "Expense":
        """Create expense from dictionary format."""
        expense = cls(
            description=data['description'],
            amount=data['amount'],
            payer=data['payer'],
            participants=data['participants'],
            category=data.get('category', 'General'),
            date=datetime.fromisoformat(data['date']) if isinstance(data['date'], str) else data['date']
        )
        expense.id = data['id']
        return expense

    @classmethod 
    def total_expenses(cls, expenses: List["Expense"]) -> float:
        """Calculate total amount of all expenses."""
        return sum(exp.amount for exp in expenses)

    @classmethod 
    def average_monthly_expenses(cls, expenses: List["Expense"]) -> float:
        """Calculate average monthly expenses."""
        if not expenses:
            return 0.0
            
        monthly_totals = defaultdict(float)
        for exp in expenses:
            key = (exp.date.year, exp.date.month)
            monthly_totals[key] += exp.amount

        if not monthly_totals:
            return 0.0

        return sum(monthly_totals.values()) / len(monthly_totals)

    @classmethod
    def total_expenses_per_category(cls, expenses: List["Expense"]) -> Dict[str, float]:
        """Calculate total expenses per category."""
        category_totals = defaultdict(float)
        for exp in expenses:
            category_totals[exp.category] += exp.amount
        return dict(category_totals)

    def __str__(self) -> str:
        """String representation of expense."""
        participants_str = ", ".join(self.participants)
        return f"{self.description} - ${self.amount:.2f} (Paid by: {self.payer}, Participants: {participants_str}, Category: {self.category})"
