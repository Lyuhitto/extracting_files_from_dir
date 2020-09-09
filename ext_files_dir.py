import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,\
    QAction, qApp, QDesktopWidget
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Extracting Files from Dir')
        self.setWindowIcon(QIcon('img/web.png'))
        self.resize(500, 350)
        self.center()

        # set actions
        # set exit action
        exitAction = QAction(QIcon('img/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        # set change language action
        """todo"""

        # set open help message action
        """todo"""

        # set change language icon
        """todo"""

        # set open help message icon
        """todo"""

        # set extracting action
        """todo"""

        # set tool bar icon
        # set exit icon
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        self.statusBar()

        # set menubar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

    # widget display in the middle of the screen
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())
