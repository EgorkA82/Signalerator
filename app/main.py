import sys
import os
import subprocess
import rich.console as console

from argparse import ArgumentParser
from PyQt5.QtWidgets import QMainWindow, QApplication

from ui_mainwindow import Ui_MainWindow
from ui_controller import Ui_Controller
from connector import Connector
from signal_controller import Signal_Controller


class MainWindow(QMainWindow):
    def __init__(self, test_mode: bool=False) -> None:  # инициализируем объект
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()  # подгружаем объект интерфейса
        self.ui.setupUi(self)  # распаковываем объект интерфейса в отдельные функции
        
        self.ui_controller: Ui_Controller = Ui_Controller(self.ui)  # инициализируем объект работы с интерфейсом
        self.connector: Connector = Connector(self.ui_controller)  # инициализируем объект работы с подключением
        self.signal_controller = Signal_Controller(self.ui_controller, self.connector)
        self.ui_controller.status_bar.set_text("Проект Егора Бляблина // 2022") 
        
        self.init_events()  # инициализируем события
        self.connector.launch_ports_updater()  # запускаем обновления списка портов 
        
        if test_mode: exit(0)  # при тестовом запуске завершаем выполнение программы
    
    def init_events(self) -> None:
        self.ui.customSignalButton.toggled.connect(self.ui_controller.custom_signal_lineedit.toggle)  # разблокируем поле ввода функции
        self.ui.connectButton.clicked.connect(self.handleConnectButton)  # обрабатываем реакцию на нажатие

    def handleConnectButton(self) -> None:
        if not self.connector.connected:
            self.connector.open_connection(self.ui.portsList.currentData())  # открываем соединение
        else:
            self.connector.close_connection()  # закрываем соединение
    

if __name__ == '__main__':
    subprocess.run(f"pip install -r {os.path.dirname(__file__)}/requirements.txt")  # устанавливаем необходимые библиотеки
    
    os.system('cls')  # очищаем консоль
    console = console.Console()
    
    parser = ArgumentParser()
    parser.add_argument('-t', '--test', dest='test_mode', action='store_true', default=False) 
    args = parser.parse_args()  # считываем аргументы вызова программы
        
    with console.status("[green]Application is running[/green]\n"):
        app = QApplication([])  # создаем экземпляр приложения
        main_window = MainWindow(args.test_mode)  # создаем экземпляр главного окна
        main_window.show()  # включаем отображение главного окна
        sys.exit(app.exec_())  # запускаем приложение
