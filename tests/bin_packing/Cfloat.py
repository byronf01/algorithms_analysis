from typing import TypeVar
from dataclasses import dataclass
import sys
from decimal import *
getcontext().prec = 15

@dataclass
class CFloat:
    val: float
    
    def __eq__(self, other) -> bool:
        return abs(self.val - other.val) <= sys.float_info.epsilon
    
    def __lt__(self, other) -> bool:
        return not (self == other) and self.val < other.val
    
    def __le__(self, other) -> bool:
        return self.__eq__(other) or self.__lt__(other)
    
    def __sub__(self, other):
        self.val = float(Decimal(str(self.val)) - Decimal(str(other.val)))