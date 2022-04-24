import time
import numpy as np
import math
from typing import Callable

from worker import Worker
from thread import Thread
from connector import Connector
from ui_controller import Ui_Controller


class Signal_Controller:
    def __init__(self, ui_controller: Ui_Controller, connector: Connector) -> None:
        self.NO_SIGNAL = None
        self.RECTANGLE_SIGNAL: Callable = self.rectangle_signal
        self.TRIANGULAR_SIGNAL: Callable = self.triangular_signal
        self.SINUSOID: Callable = self.sinusoid
        self.CUSTOM_SIGNAL: Callable = self.custom_signal
        self.ui_controller = ui_controller
        self.connector = connector
        
        eval_safe_list = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos',
                    'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor',
                    'fmod', 'frexp', 'hypot', 'ldexp', 'log', 'log10',
                    'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt',
                    'tan', 'tanh']
        self.eval_safe_dict = {k: getattr(math, k) for k in eval_safe_list} | {'round': round}
        
        self.mode: Callable | None = self.NO_SIGNAL
        self.period: int = int(self.ui_controller.ui.periodSpinBox.value() * 1000)
        self.last_values = np.zeros(100)
        self.axis = np.arange(100)
        self.progress: float = 0
        self.previous_time: float = None
        self.previous_signal = None
        
        self.ui_controller.ui.noSignalButton.clicked.connect(lambda: self.set_mode(self.NO_SIGNAL))
        self.ui_controller.ui.rectangleSignalButton.clicked.connect(lambda: self.set_mode(self.RECTANGLE_SIGNAL))
        self.ui_controller.ui.triangularSignalButton.clicked.connect(lambda: self.set_mode(self.TRIANGULAR_SIGNAL))
        self.ui_controller.ui.sinusoidButton.clicked.connect(lambda: self.set_mode(self.SINUSOID))
        self.ui_controller.ui.customSignalButton.clicked.connect(lambda: self.set_mode(self.CUSTOM_SIGNAL))
        self.ui_controller.ui.customSignalLineEdit.textChanged.connect(lambda: self.ui_controller.custom_signal_lineedit.verify(self.eval_safe_dict))
        self.ui_controller.ui.periodSpinBox.valueChanged.connect(self.update_period)
        
        self.launch()
        
    def set_mode(self, mode: Callable | None) -> None:
        self.mode: Callable | None = mode
        self.progress = 0
        self.ui_controller.custom_signal_lineedit.clear()
        
        if mode == self.NO_SIGNAL:
            self.connector.send_value(0)
    
    def update_period(self) -> None:
        """Updates self.period in msec"""
        self.period = int(self.ui_controller.ui.periodSpinBox.value() * 1000)
    
    def launch(self) -> None:
        self.signal_generator_worker: Worker = Worker(self.send_signal, lambda: self.connector.connected == True)
        self.signal_generator_thread: Thread = Thread(interval_ms=40, worker=self.signal_generator_worker)
        
        self.signal_generator_thread.run()
    
    def send_signal(self) -> None:
        if self.mode == self.NO_SIGNAL or not self.connector.connected:
            return
        
        if self.previous_time is None:
            self.previous_time = time.time()
            return
                    
        self.progress = (self.progress + (time.time() - self.previous_time) * 1000 / self.period) % 1
        self.previous_time = time.time()
        
        self.last_values = np.append(self.last_values[1:], Connector.convert(self.mode(), 0, 1, self.connector.min_voltage, self.connector.max_voltage))
        
        self.ui_controller.plotter.clear()
        self.ui_controller.plotter.plot(self.axis, self.last_values)
        
        match self.mode:
            case self.NO_SIGNAL:
                return
            case _:
                value = self.mode()
        
        self.ui_controller.ui.currentVoltageLCD.display(f"{Connector.convert(value, 0, 1, self.connector.min_voltage, self.connector.max_voltage):.1f}")
    
        if self.connector.connected and self.previous_signal != value:        
            self.connector.send_value(value)
            self.previous_signal = value
    
    def rectangle_signal(self) -> int:
        return 1 if self.progress < 0.5 else 0
    
    def triangular_signal(self) -> float:
        return 2 * (self.progress if self.progress < 0.5 else -self.progress + 1)
    
    def sinusoid(self) -> float:
        return 0.5 * math.sin(2 * math.pi * self.progress) + 0.5
    
    def custom_signal(self) -> int | float:
        self.eval_safe_dict['x'] = self.progress
        
        try:
            value = float(eval(self.ui_controller.ui.customSignalLineEdit.text(), {"__builtins__": None}, self.eval_safe_dict))
            if value < 0:
                return 0
            if value > 1:
                return 1
            return value
        except:
            return 0
