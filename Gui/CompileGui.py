# -*- coding: utf8 -*-

import os

from PyQt4.uic import compileUi

def main():
    print("*** Compiling UI files ***")

    inPath = os.path.join(".")
    outPath = os.path.join(inPath, "ui.py")

    print("Input folder: {0}".format(inPath))
    print("Output file: {0}".format(outPath))

    if os.path.exists(outPath):
        print("Making backup copy: {0}.backup".format(outPath))
        gui = open(outPath, 'r')
        backup = open(outPath + '.backup', 'w')
        for line in gui.readlines():
            backup.write(line)
        gui.close()
        backup.close()

    outFile = open(outPath, "w")

    for f in os.listdir(inPath):
        if f.endswith(".ui"):
            print("Compiling file {0}".format(f))
            uiFile = open(os.path.join(inPath, f), 'r')
            compileUi(uiFile, outFile)
            uiFile.close()

    outFile.close()


if __name__ == "__main__":
    main()

