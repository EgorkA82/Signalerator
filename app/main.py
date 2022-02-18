import sys
import os
import subprocess

import rich.console as console
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from argparse import ArgumentParser

from connector import Connector


class MainWindow(QMainWindow):
    def __init__(self, test_mode: bool=False) -> None: # инициализация
        super(MainWindow, self).__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), 'mainwindow.ui'), self) # подгружаем файл интерфейса
        self.statusBar.showMessage("Проект Егора Бляблина // 2022")
        
        self.connector = Connector() # инициализируем объект работы со списком портов
        self.connector.init_ports(self.portsList) # инициализируем порты
    
        self.init_variables() # инициализируем переменные
        self.init_events() # инициализируем события
        self.connector.launch_ports_updater() # запускаем обновления списка портов
        
        if test_mode: exit(0)

    def init_variables(self) -> None:
        self.update_voltages() # обновляем значения напряжений
    
    def init_events(self) -> None:
        self.maxVoltageSpinBox.valueChanged.connect(self.update_voltages)
        self.customSignalButton.toggled.connect(self.custom_signal_lineedit_toggler) # разблокируем поле ввода функции

    def update_voltages(self) -> None:
        self.max_voltage: float = self.maxVoltageSpinBox.value()
        self.minVoltageSpinBox.setMaximum(self.max_voltage - 0.1)
        self.min_voltage: float = self.minVoltageSpinBox.value()
    
    def custom_signal_lineedit_toggler(self) -> None:
        self.customSignalLineEdit.setReadOnly(not self.customSignalButton.isChecked())
    

if __name__ == '__main__':
    subprocess.run(f"pip install -r {os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-1])}/requirements.txt")
    
    os.system('cls') # очищаем консоль
    console = console.Console()
    
    parser = ArgumentParser()
    parser.add_argument('-t', '--test', dest='test_mode', action='store_true', default=False) 
    args = parser.parse_args() # считываем аргументы вызова программы
        
    with console.status("[green]Application is running[/green]\n"):
        app = QApplication([]) # создание экземпляра приложения
        main_window = MainWindow(args.test_mode) # создание экземпляра главного окна
        main_window.show() # включение отображения главного окна
        sys.exit(app.exec_()) # запуск приложения
