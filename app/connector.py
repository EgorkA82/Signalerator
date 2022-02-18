from PyQt5.QtCore import QIODevice
from PyQt5 import QtSerialPort

from thread import Thread
from worker import Worker
from ui_mainwindow import Ui_MainWindow


class Connector():
    def __init__(self, ui: Ui_MainWindow) -> None:
        self.connected: bool = False
        self.serial: QtSerialPort.QSerialPort = QtSerialPort.QSerialPort()
        self.serial.setBaudRate(9600)
        self.ui = ui
        self.acceptable_signatures = [signature.lower() for signature in ["Arduino", "CH340"]]
    
    def init_ports(self, ports_list: list) -> None:
        self.ports_list = ports_list
        self.serial_info: list = QtSerialPort.QSerialPortInfo()  # считываем информацию о последовательных портах
        self.update_ports_list()  # обновляем поле выбора порта
    
    def launch_ports_updater(self) -> None:
        self.ports_updater_thread: Thread = Thread()  # создаем поток
        self.ports_updater_worker: Worker = Worker(self.update_ports_list)  # создаем обработчик и передаем функцию
        
        self.ports_updater_thread.run(self.ports_updater_worker)  # запускаем поток и передаем обработчик
    
    def get_available_ports(self) -> list:
        return list(filter(lambda port: port.portName()[:3] == "COM" and int(port.portName()[3]) not in [1, 2], self.serial_info.availablePorts()))  # оставляем только COM-порты
    
    def update_ports_list(self) -> None:
        if not self.connected:
            self.ports_list.clear()
            self.available_ports: list = self.get_available_ports()
            
            self.stylish_connect_button(is_checkable=self.available_ports)
            
            for port in self.available_ports:
                self.ports_list.addItem(f"{port.portName()} | {port.description()}", port.portName())  # добавляем порт в список выбора
    
    def open_connection(self, port_name: str) -> bool:  # подключаемся к указанному порту
        self.serial.setPortName(port_name)
        self.connected = self.serial.open(QIODevice.WriteOnly)
        return self.connected
    
    def close_connection(self) -> bool:  # закрываем соединение
        self.serial.close()
        self.connected = False
        
    def write(self, message: str) -> None:  # отправляем сообщение
        assert self.connected == True
        self.serial.write(message)

    def stylish_connect_button(self, is_checkable: bool) -> None:
        border_radius = "5px"
        
        if is_checkable:
            if self.connected:
                self.ui.connectButton.setStyleSheet("""
                    QPushButton {
                        background-color: rgb(0, 180, 80);
                        color: rgb(255, 255, 255);
                        border-radius: """ + border_radius + """;
                    }"""
                )
                self.ui.connectButton.setText("Подключено")
            else:    
                self.ui.connectButton.setStyleSheet("""
                    QPushButton {
                        background-color: rgb(0, 163, 245);
                        color: rgb(255, 255, 255);
                        border-radius: """ + border_radius + """;
                    }

                    QPushButton:hover {
                        background-color: rgb(0, 143, 225)
                    }

                    QPushButton:pressed {
                        background-color: rgb(0, 123, 205)
                    }"""
                )
                self.ui.connectButton.setText("Подключиться")
        else:
            self.ui.connectButton.setStyleSheet("""
                QPushButton {
                    background-color: rgb(220, 220, 230);
                    border-radius: """ + border_radius + """;
                }"""
            )
            self.ui.connectButton.setText("Подключиться")
