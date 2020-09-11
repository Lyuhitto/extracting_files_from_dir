import sys
import os
import shutil
import webbrowser
from PyQt5.QtWidgets import QApplication, QMainWindow,\
        qApp, QWidget, QFileDialog, QDialog
from PyQt5.QtGui import QIcon
from PyQt5 import uic


form_class = uic.loadUiType('ext_files_dir.ui')[0]
help_class = uic.loadUiType('help.ui')[0]
license_class = uic.loadUiType('license.ui')[0]
about_class = uic.loadUiType('about.ui')[0]
error_class = uic.loadUiType('error_dialog.ui')[0]


class MyApp(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('img/window_icon.png'))
        self.statusBar = self.statusBar()
        self.statusBar.showMessage('Hello')
        # variable of progress bar
        self.progress = self.extractProgress.value()

        # menubar and toolbar action
        self.actionExit.triggered.connect(qApp.quit)
        self.actionView_statusbar.triggered.connect(self.toggleStat)
        self.actionView_toolbar.triggered.connect(self.toggleToolBar)
        self.actionHow_to_use.triggered.connect(self.howToUse)
        self.actionSee_the_license.triggered.connect(self.seeTheLicense)
        self.actionAbout_Creator.triggered.connect(self.aboutCreator)
        self.actionReset_Window.triggered.connect(self.resetWindow)

        # buttons action
        self.browseExtract.clicked.connect(self.extractClicked)
        self.browseSaveTo.clicked.connect(self.saveClicked)
        self.loadFileList.clicked.connect(self.loadList)
        self.extractButton.clicked.connect(self.extractFolder)

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

    def extractClicked(self):
        self.resetProgress()
        dirName = QFileDialog.getExistingDirectory(self)
        self.lineEditExtract.setText(dirName)

    def loadList(self):
        self.resetProgress()
        dirName = self.lineEditExtract.text()
        self.listOfFile = os.listdir(dirName)
        self.listFiles.setText('\n'.join(self.listOfFile))

    def saveClicked(self):
        self.resetProgress()
        dirName = QFileDialog.getExistingDirectory(self)
        self.lineEditSaveTo.setText(dirName)

    def extractFolder(self):
        self.resetProgress()
        dirPath = self.lineEditExtract.text()
        try:
            for f in self.listOfFile:
                shutil.move(dirPath + '/' + f, self.lineEditSaveTo.text())
                self.progress += round(1/len(self.listOfFile)*100)
                if self.progress > 100:
                    self.progress = 100
                self.extractProgress.setValue(self.progress)
        except shutil.Error as msg:
            print(f'Error!: {msg}')
            errorDialog = ErrorWindow()
            errorDialog.modifyMsg(str(msg))
            errorDialog.exec_()

    def resetWindow(self):
        self.resetProgress()
        self.lineEditExtract.clear()
        self.listFiles.clear()
        self.lineEditSaveTo.clear()

    def resetProgress(self):
        self.extractProgress.setValue(0)


class HelpWindow(QWidget, help_class):
    def __init__(self, parent=None):
        super(HelpWindow, self).__init__(parent)
        self.setupUi(self)
        self.show()
        self.helpClose.clicked.connect(lambda: self.close())


class LicenseWindow(QWidget, license_class):
    def __init__(self, parent=None):
        super(LicenseWindow, self).__init__(parent)
        self.setupUi(self)
        self.show()
        self.licenseClose.clicked.connect(lambda: self.close())


class AboutWindow(QWidget, about_class):
    def __init__(self, parent=None):
        super(AboutWindow, self).__init__(parent)
        self.setupUi(self)
        self.show()
        self.aboutClose.clicked.connect(lambda: self.close())
        self.goToGithub.clicked.connect(
            lambda: webbrowser.open('https://github.com/Lyuhitto')
            )


class ErrorWindow(QDialog, error_class):
    def __init__(self, parent=None):
        super(ErrorWindow, self).__init__(parent)
        self.setupUi(self)
        self.errorClose.clicked.connect(lambda: self.close())

    def modifyMsg(self, msg):
        self.errorMessage.setText(msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())
