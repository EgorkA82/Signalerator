from PyQt5.QtCore import QThread, QObject, QTimer

from worker import Worker


class Thread(QObject):    
    def __init__(self) -> None:
        super().__init__()
        self.thread: QThread = QThread(self)  # создаем поток
        self.moveToThread(self.thread)  # переносим исполнение потока из главного потока в рабочий
        
    def run(self, worker: Worker, interval: int=1000) -> None:
        self.timer: QTimer = QTimer()
        self.timer.setInterval(interval)
        self.timer.timeout.connect(worker.run)  # устанавливаем интервальное исполнение обработчика
        self.timer.start()
