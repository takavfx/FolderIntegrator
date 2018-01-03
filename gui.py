import os
import sys
import webbrowser
from functools import partial

from Qt import QtCore
from Qt import QtWidgets
from Qt import QtGui
from Qt import QtCompat

import core as Core
reload(Core)

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

class MainWindow(QtWidgets.QMainWindow):
    
    _windowWidth  = 400
    _windowHeight = 600
    _windowName   = 'FolderIntegrator'
    _windowTitle  = 'FolderIntegrator ' + 'v0.1.0'

    UIPATH = os.path.join(CURRENT_DIR, 'ui', 'gui.ui')


    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        self.UI = QtCompat.load_ui(self.UIPATH)
        self.setCentralWidget(self.UI)

        self.setObjectName(self._windowName)
        self.setWindowTitle(self._windowTitle)
        self.setWindowIcon(QtGui.QIcon(os.path.join(CURRENT_DIR, 'static', 'folder.svg')))

        self.setAcceptDrops(True)

        self.initGUI()
        self.setSignals()


    def closeEvent(self, event):
        self.setParent(None)


    def initGUI(self):
        self.resize(self._windowWidth, self._windowHeight)

        self.UI.statusbar.clearMessage()

        self.UI.filesListWidget.setAlternatingRowColors(True)
        self.UI.filesListWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)


    def setSignals(self):
        self.UI.openRepoAction.triggered.connect(self.openGitHubRepo)
        self.UI.runButton.clicked.connect(self.run)
        self.UI.filesListWidget.customContextMenuRequested.connect(self.showCellMenu)


    ## Drop Event
    def dropEvent(self, event):
        self.UI.statusbar.clearMessage()
        files = []
        for url in event.mimeData().urls():
            target_file = unicode(url.toLocalFile())
            name, ext = os.path.splitext(target_file)
            if ext in ['.zip'] or os.path.isdir(target_file):
                self.UI.filesListWidget.addItem(target_file)
                # files.append(target_file)
            else:
                self.UI.statusbar.showMessage('Some errors happned. Check terminal output.')

 
    ## Drag Enter Event
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()


    def showCellMenu(self, pos):

        contextMenu = QtWidgets.QMenu()
        currentItem = self.UI.filesListWidget.itemAt(pos.x(), pos.y())

        # if currentItem is None:
        #     return
        
        clearAction = QtWidgets.QAction("Clear", self)
        clearAction.triggered.connect(self.clearList)
        clearAction.setIcon(QtGui.QIcon(os.path.join(CURRENT_DIR, 'static', 'clear.svg')))

        contextMenu.addAction(clearAction)

        contextMenu.exec_(
                self.UI.filesListWidget.mapToGlobal(
                        QtCore.QPoint(pos.x(), pos.y())
                    )
            )


    def clearList(self):
        self.UI.filesListWidget.clear()


    def run(self):
        files = []
        for x in range(self.UI.filesListWidget.count()-1):
            files.append(self.UI.filesListWidget.item(x).text())
        Core.integrate(files)


    def openGitHubRepo(self):
        webbrowser.open(r'https://github.com/takavfx/FolderIntegrator')



def main():
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()
    