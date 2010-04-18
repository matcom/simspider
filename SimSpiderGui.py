# -*- coding: utf8 -*-

__author__ = 'Alejandro Piad'

import sys
import os

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import traceback

gui_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Gui'))
packages_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Packages'))
redist_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Redist'))
plugins_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Plugins'))

sys.path.append(gui_dir)
sys.path.append(packages_dir)
sys.path.append(redist_dir)
sys.path.append(plugins_dir)

print("Gui: {0}".format(gui_dir))
print("Packages: {0}".format(packages_dir))
print("Redist: {0}".format(redist_dir))
print("Plugins: {0}".format(plugins_dir))

from GraphViewer import GraphViewer
from Plugins import pluginManager
from config import config
import debug

from config import config
import debug
from GraphViewer import GraphViewer

from Plugins import pluginManager

def main():
    app = QApplication(sys.argv)

    # Configuracion inicial
    config.parseOptions(sys.argv[1:])

    # Chequear por error de inicio
    if os.path.exists('simspider-dump.log'):
        fp = open('simspider-dump.log')
        dump = fp.readline()
        fp.close()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Well, this is embarrassing...")
        msg.setText("It appears that our application crashed last time. "
                    "There should be a file name '{0}' out here somewhere. ".format(dump) + ""
                    "You could send this file to our team, and we will try to figure out what went wrong "
                    "and make life easier to the next user.")
        msg.exec_()

    logFile = config.Debug.get("LogFile", "simspider.log")

    # Archivo dump
    dump = open("simspider-dump.log", "w")
    dump.write(logFile)
    dump.close()

    # Debug
    listener = debug.FileListener(logFile)
    debug.addListener(listener)

    debug.defaultListener.resetFilters()
    debug.defaultListener.filter("graphviewer")
    debug.defaultListener.filter("propertyviewer")
    debug.defaultListener.filter("plugins")

    pluginManager.loadPlugins()

    try:
        win = createMainWindow()

        if win:
            win.show()
            app.exec_()

        listener.close()

        if os.path.exists(logFile):
            os.remove(logFile)

        os.remove("simspider-dump.log")

    except Exception as e:
        fp = open("simspider-dump.log")
        dump = fp.readline()
        fp.close()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Well, this is embarrassing...")
        msg.setText("It appears that our application has crashed. "
                    "Don't worry, your data is secured and will be there next time you open. "
                    "There should be a file name '{0}' out here somewhere. ".format(dump) + ""
                    "You could send this file to our team, and we will try to figure out what went wrong. "
                    "Also, the following detailed text can be useful to determine the type of error that ocurred. "
                    "You might as well send us that too. Goodbye and thanks for the fish.")

        trace = sys.exc_traceback

        msg.setDetailedText(str(e) + "\n" + "".join(traceback.format_tb(trace)))
        debug.error(main, e, throw=False)
        msg.exec_()


def createMainWindow():
    return GraphViewer()


if __name__ == "__main__":
    main()
