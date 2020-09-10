import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,\
        qApp, QWidget
from PyQt5.QtGui import QIcon
from PyQt5 import uic


form_class = uic.loadUiType('ext_files_dir.ui')[0]
help_class = uic.loadUiType('help.ui')[0]
license_class = uic.loadUiType('license.ui')[0]
about_class = uic.loadUiType('about.ui')[0]


class MyApp(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Extracting Files from Directory')
        self.setWindowIcon(QIcon('img/window_icon.png'))
        self.resize(500, 700)
        self.statusBar = self.statusBar()
        self.statusBar.showMessage('Hello')

        self.actionExit.triggered.connect(qApp.quit)
        self.actionView_statusbar.triggered.connect(self.toggleStat)
        self.actionView_toolbar.triggered.connect(self.toggleToolBar)
        self.actionHow_to_use.triggered.connect(self.howToUse)
        self.actionSee_the_license.triggered.connect(self.seeTheLicense)
        self.actionAbout_Creator.triggered.connect(self.aboutCreator)

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

    def howToUse(self):
        '''
        if win = HelpWindow() -> it goes out of scope!
        -> garbage collector removes this
        '''
        self.win = HelpWindow()

    def seeTheLicense(self):
        self.win = LicenseWindow()

    def aboutCreator(self):
        self.win = AboutWindow()


class HelpWindow(QWidget, help_class):
    def __init__(self, parent=None):
        super(HelpWindow, self).__init__(parent)
        self.setupUi(self)
        self.show()


class LicenseWindow(QWidget, license_class):
    def __init__(self, parent=None):
        super(LicenseWindow, self).__init__(parent)
        self.setupUi(self)
        self.show()


class AboutWindow(QWidget, about_class):
    def __init__(self, parent=None):
        super(AboutWindow, self).__init__(parent)
        self.setupUi(self)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())
