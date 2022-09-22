from PyQt5.QtWidgets import QRadioButton, QComboBox, QPushButton, QLabel, QWidget, QLineEdit, QStyle
from pyqtgraph import PlotWidget

from ui_mainwindow import Ui_MainWindow


class Ui_Controller:
    CONNECTED = "CONNECTED"
    CONNECTING = "CONNECTING"
    NOT_CONNECTED = "NOT CONNECTED"
        
    def __init__(self, ui: Ui_MainWindow) -> None:  # инициализируем объект
        self.ui: Ui_MainWindow = ui
        self.ports_list: QComboBox = self.Ports_List(ui)
        self.connect_button: QPushButton = self.Connect_Button(ui)
        self.connect_status_label: QLabel = self.Connect_Status_Label(ui)
        self.custom_signal_lineedit: QLineEdit = self.Custom_Signal_LineEdit(ui)
        self.signals_form: QWidget = self.Signals_Form(ui)
        self.status_bar = self.Status_Bar(ui)
        self.plotter: PlotWidget = self.ui.graphWidget
        
        self.ui.currentVoltageLCD.display("0.0")
        
    def set_mode(self, mode, ports_are_available: bool=False) -> None:  # устанавливаем режима интерфейса
        match mode:
            case "CONNECTED":  # режим "подключено"
                self.connect_button.set_connected()
                self.connect_status_label.set_connected()
                self.signals_form.set_checkable(True)
                self.ports_list.freeze()
            case "CONNECTING":  # режим "подключение"
                self.connect_button.set_not_connected(checkable=False)
                self.connect_status_label.set_connecting()
                self.signals_form.set_checkable(False)
                self.ports_list.freeze()
            case "NOT CONNECTED":  # режим "не подключено"
                self.connect_button.set_not_connected(checkable=ports_are_available)
                self.connect_status_label.set_not_connected()
                self.signals_form.set_checkable(False)
                self.ports_list.unfreeze()
    
    
    class Ports_List:  # класс для работы с объектом списка доступных портов
        def __init__(self, ui: Ui_MainWindow) -> None:  # инициализируем класс
            self.ui: Ui_MainWindow = ui
        
        def __call__(self) -> QComboBox:  # возвращаем объект списка по вызову класса как функции
            return self.ui.portsList
        
        def freeze(self):  # замораживаем текущий список
            self().setEnabled(False)
            
        def unfreeze(self):  # размораживаем текущий список
            self().setEnabled(True)
    
    
    class Custom_Signal_LineEdit:  # класс для работы со строкой пользовательской функции сигнала
        def __init__(self, ui: Ui_MainWindow) -> None:  # инициализируем класс
            self.ui: Ui_MainWindow = ui
        
        def update(self) -> None:
            self().style().polish(self())
        
        def toggle(self) -> None:  # отключаем возможность писать в поле, если не активирован режим пользовательской функции
            self().setReadOnly(not self.ui.customSignalButton.isChecked())
            self.clear()

        def verify(self, eval_safe_dict: dict) -> None:
            try:
                float(eval(self().text(), {"__builtins__": None}, eval_safe_dict))
                self().setProperty("verified", "true")
            except:
                self().setProperty("verified", "false")
            finally:
                self.update()

        def __call__(self) -> QLineEdit:  # возвращаем объект поля ввода по вызову класса как функции
            return self.ui.customSignalLineEdit
        
        def clear(self) -> None:
            self().clear()
            self.update()
        

    class Connect_Button:  # класс для работы с кнопкой подключения
        def __init__(self, ui: Ui_MainWindow) -> None:  # инициализируем класс
            self.ui: Ui_MainWindow = ui
        
        def update(self) -> None:
            self().style().polish(self())
        
        def __call__(self) -> QPushButton:
            return self.ui.connectButton
        
        def set_connected(self) -> None:  # устанавливаем отображение при установленном подключении
            self().setCheckable(True)
            self().setProperty("connected", True)
            self().setText("Отключиться")
            self.update()
        
        def set_not_connected(self, checkable: bool) -> None:  # устанавливаем отображение при отсутствии подключения            
            self().setCheckable(checkable)
            self().setProperty("connected", False)
            self().setText("Подключиться")
            self.update()


    class Connect_Status_Label:  # класс для работы с надписью о статусе подключения
        def __init__(self, ui: Ui_MainWindow) -> None:  # инициализируем класс
            self.ui: Ui_MainWindow = ui

        def __call__(self) -> QLabel:
            return self.ui.connectStatusLabel
        
        def update(self) -> None:
            self().style().polish(self())
        
        def set_connecting(self) -> None:  # устанавливаем отображение в процессе подключения
            self().setText("подключение")
            self().setProperty("connected", True)
            self.update()
        
        def set_connected(self) -> None:  # устанавливаем отображение при установленном подключении
            self().setText("подключено")
            self().setProperty("connected", True)
            self.update()
        
        def set_not_connected(self) -> None:  # устанавливаем отображение при отсутствии подключения
            self().setText("не подключено")
            self().setProperty("connected", False)
            self.update()
        

    class Signals_Form:  # класс для работы с полем выбора вида сигнала
        def __init__(self, ui: Ui_MainWindow) -> None:  # инициализируем класс
            self.ui: Ui_MainWindow = ui
        
        def set_checkable(self, checkable: bool) -> None:  # устанавливаем возможнось выбора сигнала
            # при установке возможности выбора сигнала устанавливаем всем сигналам возможность быть выбранными
            # в противном случае активируем пункт отключения и блокируем выбор остальных опций
            if not checkable:
                self.ui.noSignalButton.setChecked(True)
            
            for radio_button in self.ui.signalFormsForm.findChildren(QRadioButton):
                if radio_button is not self.ui.noSignalButton:
                    radio_button.setCheckable(checkable)


    class Status_Bar:  # класс для работы со статус-баром
        def __init__(self, ui: Ui_MainWindow) -> None:  # инициализируем класс
            self.ui: Ui_MainWindow = ui

        def set_text(self, text: str):  # устанавливаем текст
            self.ui.statusBar.showMessage(text)
