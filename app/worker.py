from typing import Callable
from PyQt5.QtCore import QRunnable


class Worker(QRunnable):    
    def __init__(self, target: Callable):
        super(Worker, self).__init__()
        self.target = target # считываем функцию
    
    def run(self) -> None:
        self.target() # исполняем функцию