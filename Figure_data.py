from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QDialog, QWidget
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import sys
import numpy as np
import matplotlib.pyplot as plt

class Figure_data(FigureCanvas):
      def __init__(self, parent):
            super(self.__class__, self).__init__()
            self.fig = Figure()
            self.axes = self.fig.add_subplot(111)
            self.axes.errorbar(Time_std,delta_corr_std, yerr=error_std, fmt='ko', ecolor='k', capthick=2)
            self.axes.errorbar(Time_unk,delta_corr_unk, yerr=error_unk, fmt='bo', ecolor='k', capthick=2)
            self.axes.set_xlabel('Time(h)')
            self.axes.set_ylabel(r"$\delta^{18}O_{RAW}  ($\permil$)$")
            FigureCanvas.__init__(self, self.fig)
            self.setParent(parent)
            FigureCanvas.setSizePolicy(self,
                                      QSizePolicy.Expanding,
                                      QSizePolicy.Expanding)
            FigureCanvas.updateGeometry(self)

class Figure_data_Window(QWidget):
       def __init__(self):
           QWidget.__init__(self)
           self.setWindowTitle("Figure data")
           self.main_widget = QWidget(self)
           vbl = QVBoxLayout(self.main_widget)
           qmc = Figure_data(self.main_widget)
           ntb = NavigationToolbar(qmc, self.main_widget)
           vbl.addWidget(qmc)
           vbl.addWidget(ntb)
           self.main_widget.setFocus()
           self.setCentralWidget(self.main_widget)