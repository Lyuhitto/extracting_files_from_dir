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
        self.statusBar = self.statusBar()
        self.statusBar.showMessage('Hello')

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

        # set viewStatAction action
        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleStat)

        # set viewToolBAct action
        viewToolBarAct = QAction('View toolbar', self, checkable=True)
        viewToolBarAct.setStatusTip('View toolbar')
        viewToolBarAct.setChecked(True)
        viewToolBarAct.triggered.connect(self.toggleToolBar)

        # set extracting action
        """todo"""

        # set tool bar icon
        # set exit icon
        self.toolBar = self.addToolBar('Exit')
        self.toolBar.addAction(exitAction)

        # set change language icon
        """todo"""

        # set open help message icon
        """todo"""

        # set menubar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        viewMenu = menubar.addMenu('&View')
        viewMenu.addAction(viewStatAct)
        viewMenu.addAction(viewToolBarAct)

    # widget display in the middle of the screen
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def toggleStat(self, state):
        if state:
            self.statusBar.show()
        else:
            self.statusBar.hide()

    def toggleToolBar(self, state):
        if state:
            self.toolBar.setVisible(True)
        else:
            self.toolBar.setVisible(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())
