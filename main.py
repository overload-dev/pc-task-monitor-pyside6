import sys
import math
import psutil
import cpuinfo

from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, QThread, SIGNAL
from uis.ui_main import Ui_MainWindow
import time


def load_update_datas():
    cpu = {
        'freq': f'{str(psutil.cpu_freq().current / 1024)} GHz',
        'usage_per': psutil.cpu_percent(interval=0.5)
    }

    m = psutil.virtual_memory()

    memory = {
        'used': str(round(m.used / 1024 ** 3)) + ' GB',
        'free': str(round(m.free / 1024 ** 3)) + ' GB',
        'usage_per': str(m.percent) + ' %'
    }

    return cpu, memory


def load_init_datas():
    # cpu 사용율
    cpu = {
        'cpu_model': cpuinfo.cpu.info[0]['ProcessorNameString'],
        'freq': f'{str(psutil.cpu_freq().current/1024)} GHz',  # 수시로 변함
        'usage_per': psutil.cpu_percent(interval=0.1),  # 수시로 변함
        'core_count_phy': psutil.cpu_count(logical=False),
        'core_count_log': psutil.cpu_count(logical=True),
    }

    # 메모리
    m = psutil.virtual_memory()
    memory = {
        'total': str(round(m.total / 1024 ** 3)) + ' GB',
        'used': str(round(m.used / 1024 ** 3)) + ' GB',  # 수시로 변함
        'free': str(round(m.free / 1024 ** 3)) + ' GB',  # 수시로 변함
        'usage_per': str(m.percent) + ' %',  # 수시로 변함
    }
    return cpu, memory


class LoadThread(QThread):

    def __init__(self, proc):
        super().__init__()
        self.proc = proc

    def run(self):
        while True:
            cpu, memory = load_update_datas()
            self.emit(SIGNAL(self.proc({'cpu': cpu, 'memory': memory})))
            time.sleep(0.5)


class WindowClass(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__(flags=Qt.Window)
        self.setupUi(self)

        cpu, memory = load_init_datas()
        # cpu
        self.label_cpu_usage_per.setText(str(cpu['usage_per']) + ' %')
        self.label_cpu_model.setText(cpu['cpu_model'])
        self.label_freq.setText(cpu['freq'])
        self.label_core_phy.setText(str(cpu['core_count_phy']))
        self.label_core_log.setText(str(cpu['core_count_log']))

        # memory
        self.label_memory_usage_per.setText(memory['usage_per'])
        self.label_memory_total.setText(memory['total'])
        self.label_memory_free.setText(memory['free'])
        self.label_memory_used.setText(memory['used'])
        self.pc_task = None

        self.load_thread = LoadThread(self.proc)

        self.load_thread.start()

    def proc(self, result):

        self.label_cpu_usage_per.setText(str(result['cpu']['usage_per']) + ' %')
        self.label_freq.setText(result['cpu']['freq'])

        self.label_memory_usage_per.setText(result['memory']['usage_per'])
        self.label_memory_free.setText(result['memory']['free'])
        self.label_memory_used.setText(result['memory']['used'])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()

    myWindow.show()
    sys.exit(app.exec())
