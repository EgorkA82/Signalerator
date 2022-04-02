from PyQt5.QtCore import QThread, QObject, QTimer

from worker import Worker


class Thread(QObject):    
    def __init__(self, interval_ms: int, worker: Worker) -> None:  # инициализируем объект
        super().__init__()  # наследуем методы родителя
        self.thread: QThread = QThread(self)  # создаем поток
        self.timer: QTimer = QTimer()  # создаем объект таймера
        self.timer.setInterval(interval_ms)
        self.timer.timeout.connect(worker.run)  # устанавливаем интервальное исполнение обработчика
        self.moveToThread(self.thread)  # переносим исполнение потока из главного потока в рабочий
        
    def run(self) -> None:  # запускаем интервальное исполнение обработчика
        self.timer.start()  # запускаем таймер