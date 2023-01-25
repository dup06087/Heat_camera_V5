import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import child_window_saved
from PyQt5.QtCore import *
from get_cam_num import camera_num

# for i in range(child_window_saved.New_server.aux):
#     print(child_window_saved.New_server.aux[i])

### Qt 실행
# app = QtWidgets.QApplication(sys.argv)
# MainWindow = QtWidgets.QMainWindow()
# ui = prac_scroll.Ui_MainWindow()
# ui = prac_childwindow.Ui_MainWindow()
# ui.setupUi(MainWindow)
# MainWindow.show()

### 장비가져오기 쓰레드 실행
thread_get_data = QThread()
class Worker_get_data(QObject):
    def __init__(self, parent=None):
        QObject.__init__(self, parent=parent)
        QtWidgets.QApplication.processEvents()

    def get_temperature(self):   ### 반드시 str값!!!
        while True:
            aux = child_window_saved.New_server.aux
            try:
                for i in range(camera_num):
                    child_window_saved.ui.status_label[i].setText('\n'.join(("Ch{} : ".format(k) + str(aux[i][k])) for k in range(len(aux[i]))))
                        # print("Not showing subwindow")
                    QtWidgets.QApplication.processEvents()  ### 중요

                    # if (int(Get_Equipment_status.temp_outputs[i]) >= 25) and (int(Get_Equipment_status.volt1_outputs[i]) >= 25) and (int(Get_Equipment_status.volt2_outputs[i]) >= 25) and (int(Get_Equipment_status.volt3_outputs[i]) >= 25) and (int(Get_Equipment_status.current_outputs[i]) >= 25):
                    #     child_window_saved.ui.lbl_prob_chk[i].setStyleSheet("background-color: rgb(255, 0, 0);")
                    #     try:
                    #         child_window_saved.MainWindow.ui.lbl_prob_chk[i].setStyleSheet("background-color: rgb(255, 0, 0);")
                    #     except:
                    #         pass
                    # else:
                    #     child_window_saved.ui.lbl_prob_chk[i].setStyleSheet("background-color: rgb(255, 255, 255);")
                    #     try:
                    #         child_window_saved.MainWindow.ui.lbl_prob_chk[i].setStyleSheet("background-color: rgb(255, 255, 255);")
                    #     except:
                    #         pass

            except:
                # print("UI loading...")
                pass

            try:
                for k in range(len(aux[0])):
                    child_window_saved.MainWindow.ui.status_label.setText(
                        '\n'.join(("Ch{} : ".format(k) + str(aux[child_window_saved.ui.clicked_num][k])) for k in range(len(aux[child_window_saved.ui.clicked_num]))))
                    QtWidgets.QApplication.processEvents()  ### 중요

            except:
                # print("child window loading")
                pass

worker_get_data = Worker_get_data()
worker_get_data.moveToThread(thread_get_data)
thread_get_data.started.connect(worker_get_data.get_temperature())

thread_get_data.start()

# sys.exit(prac_childwindow.app.exec_())
