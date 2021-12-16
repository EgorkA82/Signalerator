import sys
from PyQt5 import QtWidgets, uic
from argparse import ArgumentParser


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, test_mode) -> None: # инициализация
        super(MainWindow, self).__init__()
        uic.loadUi('mainwindow.ui', self) # подгружаем файл интерфейса
        self.init_variables()
        self.init_event_connections()
        
        if test_mode: exit(0)

    def init_variables(self) -> None:
        self.set_voltages()
    
    def init_event_connections(self) -> None:
        self.maxVoltageSpinBox.valueChanged.connect(self.set_voltages)
        self.customSignalButton.toggled.connect(self.custom_signal_lineedit_toggler)

    def set_voltages(self) -> None:
        self.min_voltage: float = self.minVoltageSpinBox.value()
        self.max_voltage: float = self.maxVoltageSpinBox.value()
        self.minVoltageSpinBox.setMaximum(self.max_voltage - 0.1)
    
    def custom_signal_lineedit_toggler(self) -> None:
        self.customSignalLineEdit.setReadOnly(not self.customSignalButton.isChecked())
    

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-t', '--test', dest='test_mode', action='store_true', default=False)
    args = parser.parse_args()
    
    app = QtWidgets.QApplication([]) # создание экземпляра приложения
    main_window = MainWindow(args.test_mode) # создание экземпляра главного окна
    main_window.show() # включение отображения главного окна
    sys.exit(app.exec_()) # запуск приложения
