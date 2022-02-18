import sys
import os
import subprocess
import rich.console as console

from argparse import ArgumentParser
from PyQt5.QtWidgets import QMainWindow, QApplication

import connector
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, test_mode: bool=False) -> None:  # инициализация
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.statusBar.showMessage("Проект Егора Бляблина // 2022")
        
        self.connector = connector.Connector(self.ui)  # инициализируем объект работы со списком портов
        self.connector.init_ports(self.ui.portsList)  # инициализируем порты
    
        self.init_variables()  # инициализируем переменные
        self.init_events()  # инициализируем события
        self.connector.launch_ports_updater()  # запускаем обновления списка портов
        
        if test_mode: exit(0)

    def init_variables(self) -> None:
        self.isConnected = False
        self.update_voltages()  # обновляем значения напряжений
    
    def init_events(self) -> None:
        self.ui.maxVoltageSpinBox.valueChanged.connect(self.update_voltages)
        self.ui.customSignalButton.toggled.connect(self.custom_signal_lineedit_toggler)  # разблокируем поле ввода функции
        self.ui.connectButton.clicked.connect(self.handleConnectButton)

    def update_voltages(self) -> None:
        self.max_voltage: float = self.ui.maxVoltageSpinBox.value()
        self.ui.minVoltageSpinBox.setMaximum(self.max_voltage - 0.1)
        self.min_voltage: float = self.ui.minVoltageSpinBox.value()
    
    def custom_signal_lineedit_toggler(self) -> None:
        self.ui.customSignalLineEdit.setReadOnly(not self.ui.customSignalButton.isChecked())
    
    def handleConnectButton(self) -> None:
        if not self.connector.connected:
            self.connector.open_connection(self.ui.portsList.currentData())
        else:
            self.connector.close_connection()
        
        self.ui.connectStatusLabel = "подключено" if self.connector.connected else "не подключено"
    

if __name__ == '__main__':
    subprocess.run(f"pip install -r {os.path.dirname(__file__)}/requirements.txt")
    
    os.system('cls')  # очищаем консоль
    console = console.Console()
    
    parser = ArgumentParser()
    parser.add_argument('-t', '--test', dest='test_mode', action='store_true', default=False) 
    args = parser.parse_args()  # считываем аргументы вызова программы
        
    with console.status("[green]Application is running[/green]\n"):
        app = QApplication([])  # создание экземпляра приложения
        main_window = MainWindow(args.test_mode)  # создание экземпляра главного окна
        main_window.show()  # включение отображения главного окна
        sys.exit(app.exec_())  # запуск приложения
