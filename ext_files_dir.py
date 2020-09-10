import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,\
    QAction, qApp, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5 import uic


form_class = uic.loadUiType('ext_files_dir.ui')[0]


class MyApp(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Extracting Files from Dir')
        self.setWindowIcon(QIcon('img/window_icon.png'))
        self.resize(500, 700)
        self.statusBar = self.statusBar()
        self.statusBar.showMessage('Hello')

        self.actionExit.triggered.connect(qApp.quit)
        self.actionView_statusbar.triggered.connect(self.toggleStat)
#        self.actionView_toolbar.triggered.connect(qApp.quit)

    def toggleStat(self, state):
        if state:
            self.statusBar.show()
        else:
            self.statusBar.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())
