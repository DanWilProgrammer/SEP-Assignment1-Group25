from datetime import datetime
from typing import List, Dict, Optional
import json

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