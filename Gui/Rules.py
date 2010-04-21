# -*- coding: utf8 -*-

from PropertyViewer import *
import ui

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import debug
from Plugins import pluginManager

import rules

class RuleDialog(QDialog):
    def __init__(self, **kwargs):
        QDialog.__init__(self)

        self.ui = ui.Ui_DgRules()
        self.ui.setupUi(self)
        self.attributes = kwargs

        self.highlighter = SyntaxHighlighter(self.ui.txeEditRules.document())
        self.rules = []

        self.ui.txeEditRules.textChanged.connect(self._parseRules)

    def _parseRules(self):
        self.rules = []
        errors = []

        str = self.ui.txeEditRules.toPlainText().splitlines()

        index = 0
        for rule in str:
            try:
                index += 1
                self.rules.append(rules.parse(rule))
            except rules.ParsingException as e:
                errors.append((e.print(), index))

        self.ui.ptxeException.setPlainText("\n".join(["Line {0}: {1}".format(index, e) for e, index in errors]))


class SyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, document):
        QSyntaxHighlighter.__init__(self, document)

    def highlightBlock(self, text):

        format1 = QTextCharFormat()
        format1.setFontWeight(QFont.Bold)
        format1.setForeground(Qt.darkMagenta)

        format2 = QTextCharFormat()
        format2.setFontWeight(QFont.Bold)
        format2.setForeground(Qt.blue)

        format3 = QTextCharFormat()
        format2.setFontWeight(QFont.Bold)
        format3.setForeground(Qt.darkRed)

        def Reg(string):
            return QRegExp("(^|\\s){0}($|\\s|\\n)".format(string))

        regexes = [(Reg(item), format1) for item in [rules.ifToken, rules.thenToken]] \
                + [(Reg(item), format2) for item in [rules.andToken, rules.orToken, rules.notToken]] \
                + [(Reg(item), format3) for item in [rules.assignToken]]

        for reg, format in regexes:
            index = reg.indexIn(text)
            while index >= 0:
                length = reg.matchedLength()
                self.setFormat(index, length, format)
                index = reg.indexIn(text, index + length)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    dlg = RuleDialog()
    dlg.show()

    app.exec_()
