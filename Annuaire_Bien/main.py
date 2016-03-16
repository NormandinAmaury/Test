import sys
from PyQt4 import QtCore, QtGui
from View import View


if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    window = View(app)
    window.show()
    sys.exit(app.exec_())