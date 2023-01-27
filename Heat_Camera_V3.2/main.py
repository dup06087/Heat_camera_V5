from PyQt5 import QtWidgets
from PyQt5.QtCore import *

import UI
from Cam_number import camera_num

### 장비가져오기 쓰레드 실행
thread_get_data = QThread()
class Worker_get_data(QObject):
    def __init__(self, parent=None):
        QObject.__init__(self, parent=parent)
        QtWidgets.QApplication.processEvents()

    def get_temperature(self):
        while True:
            aux = UI.Server.aux
            try:
                for i in range(camera_num):
                    UI.ui.status_label[i].setText('\n'.join(("Ch{} : ".format(k) + str(aux[i][k])) for k in range(len(aux[i]))))
                    QtWidgets.QApplication.processEvents()

            except:
                pass

            try:
                for k in range(len(aux[0])):
                    UI.MainWindow.ui.status_label.setText(
                        '\n'.join(("Ch{} : ".format(k) + str(aux[UI.ui.clicked_num][k])) for k in range(len(aux[UI.ui.clicked_num]))))
                    QtWidgets.QApplication.processEvents()

            except:
                pass

worker_get_data = Worker_get_data()
worker_get_data.moveToThread(thread_get_data)
thread_get_data.started.connect(worker_get_data.get_temperature())

thread_get_data.start()