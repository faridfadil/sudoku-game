# cell class 
class Cell:
    def set_number(self, number: int) -> None:
        self.number = number
    
    def get_number(self) -> int:
        return self.number

    def __str__(self) -> str:
        pass 