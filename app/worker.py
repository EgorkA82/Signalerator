from typing import Callable
from PyQt5.QtCore import QRunnable


class Worker(QRunnable):    
    def __init__(self, target: Callable, activator: bool=True):  # инициализируем объект
        super().__init__()  # наследуем методы родителя
        self.target = target  # считываем функцию
        self.activator = activator
    
    def run(self) -> None:  # исполняем функцию
        if self.activator:
            self.target()
