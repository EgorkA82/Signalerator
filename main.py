import sys
from PyQt5 import QtWidgets, uic


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None: # инициализация
        super(MainWindow, self).__init__()
        uic.loadUi('mainwindow.ui', self) # подгружаем файл интерфейса
        self.init_variables()
        self.init_event_connections()

    def init_variables(self) -> None:
        self.set_voltages()
    
    def init_event_connections(self) -> None:
        self.maxVoltageSpinBox.valueChanged.connect(self.set_voltages)
        self.customSignalButton.toggled.connect(self.custom_signal_lineedit_toggler)

    def set_voltages(self) -> None:
        self.min_voltage: float = self.minVoltageSpinBox.value()
        self.max_voltage: float = self.maxVoltageSpinBox.value()
        self.minVoltageSpinBox.setMaximum(self.max_voltage - 0.1)
        print(f"{self.max_voltage:.1f}")
    
    def custom_signal_lineedit_toggler(self) -> None:
        self.customSignalLineEdit.setReadOnly(not self.customSignalButton.isChecked())
    

if __name__ == '__main__':
    app = QtWidgets.QApplication([]) # создание экземпляра приложения
    main_window = MainWindow() # создание экземпляра главного окна
    main_window.show() # включение отображения главного окна
    sys.exit(app.exec_()) # запуск приложения
