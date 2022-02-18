import PyQt5.QtCore as QtCore

from PyQt5 import QtSerialPort

from thread import Thread
from worker import Worker


class Connector():
    def __init__(self) -> None:
        self.connected: bool = False
        self.serial: QtSerialPort.QSerialPort = QtSerialPort.QSerialPort()
        self.serial.setBaudRate(9600)
    
    def init_ports(self, ports_list: list) -> None:
        self.ports_list = ports_list
        self.serial_info: list = QtSerialPort.QSerialPortInfo() # считываем информацию о последовательных портах
        self.update_ports_list() # обновляем поле выбора порта
    
    def launch_ports_updater(self) -> None:
        self.ports_updater_thread: Thread = Thread() # создаем поток
        self.ports_updater_worker: Worker = Worker(self.update_ports_list) # создаем обработчик и передаем функцию
        
        self.ports_updater_thread.run(self.ports_updater_worker) # запускаем поток и передаем обработчик
    
    def get_available_ports(self) -> list:
        return filter(lambda port: port.portName()[:3] == "COM", self.serial_info.availablePorts()) # оставляем только COM-порты
    
    def update_ports_list(self) -> None:
        if not self.connected:
            self.ports_list.clear()
            self.available_ports = self.get_available_ports()
            
            for port in self.available_ports:
                self.ports_list.addItem(f"{port.portName()} | {'Arduino' if 'Arduino' in port.description() else 'Неизвестное устройство'}", port.portName()) # добавляем порт в список выбора
    
    def open_connection(self, port_name: str) -> bool: # подключаемся к указанному порту
        self.serial.setPortName(port_name)
        self.connected = self.serial.open(QtCore.QIODevice.WriteOnly)
        return self.connected
    
    def close_connection(self) -> bool: # закрываем соединение
        self.serial.close()
        self.connected = False
        
    def write(self, message: str) -> None: # отправляем сообщение
        assert self.connected == True
        self.serial.write(message)
