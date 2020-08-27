from PyQt5.QtCore import QRunnable, pyqtSlot, QObject, pyqtSignal

class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal()
class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        
    @pyqtSlot()
    def run(self):
        try:
            self.fn(*self.args, **self.kwargs)
            self.signals.finished.emit()
        except:
            self.signals.error.emit()