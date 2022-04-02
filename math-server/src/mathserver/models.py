from sqlalchemy import Column, Integer, Numeric, Enum
from .db_setup import Base
from .operators import Operator


class Note(Base):
    __tablename__ = 'history'

    id = Column(Integer, primary_key=True)
    operator = Column('operator', Enum(Operator))
    number1 = Column('number1', Numeric)
    number2 = Column('number2', Numeric)
    result = Column('result', Numeric)

    def __init__(self, op, n1, n2, res):
        self.operator = op
        self.number1 = n1
        self.number2 = n2
        self.result = res

    def __repr__(self):
        return f"{self.operator}, number1 = {self.number1}, number2 = {self.number2}, result = {self.result}"