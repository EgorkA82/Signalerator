from PyQt5.QtCore import QIODevice
from PyQt5.QtWidgets import QComboBox
from PyQt5 import QtSerialPort

from thread import Thread
from worker import Worker
from ui_controller import Ui_Controller

class Connector():
    def __init__(self, ui_controller: Ui_Controller) -> None:  # инициализируем объект
        self.connected: bool = False
        
        self.serial: QtSerialPort.QSerialPort = QtSerialPort.QSerialPort()  # создаем объект порта
        self.serial.setBaudRate(9600)  # устанавливаем скорость общения устройств
        self.serial_info: list = QtSerialPort.QSerialPortInfo()  # считываем информацию о последовательных портах
        
        self.ui_controller: Ui_Controller = ui_controller  # наследуем объект работы с интерфейсом
        self.ports_list: QComboBox = self.ui_controller.ports_list()  # получаем объект работы со списком портов
        
        self.acceptable_signatures: list = [signature.lower() for signature in ["Arduino", "CH340"]]  # устанавливаем допустимые сигнатуры совместимых устройств
        self.update_ports_list()  # обновляем поле выбора порта
    
    def launch_ports_updater(self) -> None:  # запускаем обновление списка портов в отдельном потоке
        self.ports_updater_thread: Thread = Thread()  # создаем поток
        self.ports_updater_worker: Worker = Worker(self.update_ports_list)  # создаем обработчик и передаем функцию
        
        self.ports_updater_thread.run(self.ports_updater_worker)  # запускаем поток и передаем обработчик
    
    def get_available_ports(self) -> list:  # возвращаем список доступных COM-портов
        return list(filter(lambda port: port.portName()[:3] == "COM" and int(port.portName()[3]) not in [1, 2], self.serial_info.availablePorts()))  # оставляем только COM-порты кроме 1-го и 2-го
    
    def update_ports_list(self) -> None:  # обновляем список портов
        self.available_ports: list = self.get_available_ports()  # получаем список достуных портов
        current_port_is_in_ports: bool = any([self.serial.portName() in port.portName() for port in self.available_ports])  # проверка на наличие порта в списке доступных
        
        if self.connected and not current_port_is_in_ports:  # проверка на незапланированное отключение устройства
            self.connected: bool = False
            self.ui_controller.set_mode(Ui_Controller.NOT_CONNECTED, ports_are_available=bool(self.available_ports))  # выполняем необходимое изменение интерфейса
            self.serial.close()  # закрываем подключение

        if not self.connected:
            self.ports_list.clear()  # очищаем список портов
            for port in self.available_ports:
                self.ports_list.addItem(f"{port.portName()} | {port.description()}", port.portName())  # добавляем порт в список выбора
                
            self.ui_controller.set_mode(Ui_Controller.NOT_CONNECTED, ports_are_available=bool(self.available_ports))  # выполняем необходимое изменение интерфейса
    
    def open_connection(self, port_name: str) -> bool:  # подключаемся к указанному порту
        self.ui_controller.set_mode(Ui_Controller.CONNECTING)  # выполняем необходимое изменение интерфейса
        
        self.serial.setPortName(port_name)  # устанавливаем имя используемого порта
        self.connected: bool = self.serial.open(QIODevice.ReadWrite)  # открываем соединение
        
        if self.connected:  # проверяем успешность подключения
            self.ui_controller.set_mode(Ui_Controller.CONNECTED)  # выполняем необходимое изменение интерфейса
        else:
            self.ui_controller.set_mode(Ui_Controller.NOT_CONNECTED, ports_are_available=bool(self.available_ports))  # выполняем необходимое изменение интерфейса
        
        return self.connected  # возвращаем успешность подключения
    
    def close_connection(self) -> bool:  # отключаемся от испольемого порта
        self.serial.close()  # закрываем соединение
        self.connected: bool = False
        
        self.ui_controller.set_mode(Ui_Controller.NOT_CONNECTED, ports_are_available=bool(self.available_ports))  # выполняем необходимое изменение интерфейса
        
    def write(self, message: str) -> None:  # отправляем сообщение
        self.serial.write(message)
