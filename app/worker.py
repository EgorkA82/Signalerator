from typing import Callable
from PyQt5.QtCore import QRunnable


class Worker(QRunnable):    
    def __init__(self, target: Callable):  # инициализируем объект
        super().__init__()  # наследуем методы родителя
        self.target = target  # считываем функцию
    
    def run(self) -> None:  # исполняем функцию
        self.target()