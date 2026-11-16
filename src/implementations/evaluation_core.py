class EvaluationCore:    
    @staticmethod
    def value(s: str) -> int:
        return int(s)
    
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b
    
    @staticmethod
    def subtract(a: int, b: int) -> int:
        return a - b
    
    @staticmethod
    def multiply(a: int, b: int) -> int:
        return a * b
    
    @staticmethod
    def divide(a: int, b: int) -> int:
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a // b
    
    @staticmethod
    def modulo(a: int, b: int) -> int:
        if b == 0:
            raise ZeroDivisionError("Modulo by zero")
        return a % b

    @staticmethod
    def divide_func(a: int, b: int) -> int:
        return EvaluationCore.divide(a, b)
    
    @staticmethod
    def mmax(numbers: list[int]) -> int:
        if not numbers:
            raise ValueError("mmax requires at least one argument")
        return max(numbers)
    
    @staticmethod
    def mmin(numbers: list[int]) -> int:
        if not numbers:
            raise ValueError("mmin requires at least one argument")
        return min(numbers)
    
    @staticmethod
    def cell_reference(cell_id: str, values: dict[str, int]) -> int:
        return values.get(cell_id, 0)
    
    @staticmethod
    def unary_plus(operand: int) -> int:
        return operand
    
    @staticmethod
    def unary_minus(operand: int) -> int:
        return -operand
