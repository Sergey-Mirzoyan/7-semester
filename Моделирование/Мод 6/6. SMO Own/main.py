from ui_mainwindow import Ui_Form
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
import sys
import Engine
from PyQt5 import uic
class MainWindow(QWidget):
    def __init__(self, parent=None):
        # super(MainWindow, self).__init__(parent)
        # self._ui = Ui_Form()
        # self._ui.setupUi(self)
        super(MainWindow, self).__init__(parent)
        self.ui = uic.loadUi("mainwindow.ui", self)

    def on_pushButton_model_clicked(self):
        u = self.ui
        client_m = float(u.le_client_m.text())
        client_d = float(u.le_client_d.text())

        op0_m=    float(u.le_op0_m.text())
        op0_d=    float(u.le_op0_d.text())
        op1_m=    float(u.le_op1_m.text())
        op1_d=    float(u.le_op1_d.text())
        op2_m=    float(u.le_op2_m.text())
        op2_d=    float(u.le_op2_d.text())

        car0_d =  float(u.le_car_d.text())
        car0_m =  float(u.le_car_m.text())

        ekg0_d =  float(u.le_uzi_d.text())
        ekg0_m=  float(u.le_uzi_m.text())

        prob_0 = float(u.le_ter0_p.text())
        prob_1 = float(u.le_ter1_p.text())
        prob_2 = float(u.le_ter2_p.text())
        prob_3 = float(u.le_car0_p.text())

        c_count=  int(u.le_client_count.text())


        maxQueue, allCount = Engine.event_based_modelling(client_m, client_d, op0_m,op0_d,op1_m,op1_d,op2_m,op2_d, car0_m, car0_d, ekg0_m, ekg0_d, prob_0, prob_1, prob_2, prob_3, c_count)
        
        self.ui.le_ter0_max.setText(str(maxQueue[0]))
        self.ui.le_ter1_max.setText(str(maxQueue[1]))
        self.ui.le_ter2_max.setText(str(maxQueue[2]))
        self.ui.le_car_max.setText(str(maxQueue[3]))
        self.ui.le_uzi_max.setText(str(maxQueue[4]))

        self.ui.le_ter0_all.setText(str(allCount[0]))
        self.ui.le_ter1_all.setText(str(allCount[1]))
        self.ui.le_ter2_all.setText(str(allCount[2]))
        self.ui.le_car_all.setText(str(allCount[3]))
        self.ui.le_uzi_all.setText(str(allCount[4]))


        
        
        


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == '__main__':
    sys.exit(main())