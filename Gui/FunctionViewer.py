# -*- coding: utf8 -*-
from GraphicFun import GraphicFun, FuncAxis
import ui

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import debug

from Redist.pyfuzzy.set.Triangle import Triangle
from Redist.pyfuzzy.set.SFunction import SFunction
from Redist.pyfuzzy.set.ZFunction import ZFunction
from Redist.pyfuzzy.set.PiFunction import PiFunction
from Redist.pyfuzzy.set.Trapez import Trapez
import Redist.pyfuzzy.set

class Variable:
    def __init__(self, name):
        self.name = name
        self.values = {}


class Function:
    def __init__(self, name, **kwargs):
        self.name = name
        self.properties = kwargs
        self.FuzzyFunction = 0


    def clone(self):
        return Function(self.name, **self.properties)

    def __getattr__(self, item):
        return self.properties[item]

    def evaluate(self, precision):
        pass

class TriangularFunction(Function):
    def __init__(self, min=0, mid=50, max=100):
        super().__init__( "Triangle", MinX=min, MidX=mid, MaxX=max)

    def clone(self):
        return TriangularFunction(self.MinX, self.MidX, self.MaxX)

    def evaluate(self, precision):
        self.FuzzyFunction = Triangle(m=self.MidX
            ,alpha=self.MidX - self.MinX , beta=self.MaxX-self.MidX
            ,y_max=1, y_min=0)
        return [(self.MinX,0), (self.MidX,1), (self.MaxX, 0)]

class TrapezoidFunction(Function):
    def __init__(self,min = 0,m1= 2,m2=4,max=6):
        super().__init__(name = 'Trapezoid',MinX = min,MidX1 = m1,MidX2=m2,MaxX=max)

    def clone(self):
        return TrapezoidFunction(self.MinX,self.MidX1,self.MidX2,self.MaxX)

    def evaluate(self, precision):
        self.FuzzyFunction = Trapez(
            m1=self.MidX1,m2=self.MidX2
            ,alpha=self.MidX1-self.MinX, beta=self.MaxX-self.MidX2
            ,y_min=0,y_max=1)
        return [(self.MinX,0),(self.MidX1,1),(self.MidX2,1),(self.MaxX,0)]

class SingletonFunction(Function):
    def __init__(self,x=0):
        super().__init__(name = 'Singleton',X=x)

    def clone(self):
        return SingletonFunction(self.X)

    def evaluate(self, precision):
        self.FuzzyFunction = Redist.pyfuzzy.set.Singleton.Singleton(x=self.X)
        return [(self.X,1),(self.X,0)]

class SShapeFunction(Function):
    def __init__(self,mid=2,length =2):
        super().__init__(name='SShapeFunction',MidX=mid,Length = length)

    def clone(self):
        return SShapeFunction(self.MidX, self.Length)

    def evaluate(self, precision):
        self.FuzzyFunction = SFunction(a=self.MidX,delta=self.Length)
        ig = self.FuzzyFunction.getIntervalGenerator()
        points_x=[]
        next = ig.nextInterval(None,None)
        points = []
        while next is not None:
            x = next
            points_x.append(x)
            y = self.Calc_Y(x,self.MidX,self.Length/2)
            points.append((x,y))
            next = ig.nextInterval(next,None)
        return points

    def Calc_Y(self,x,a,d):
        if x <= a-d:
            return 0.0
        if x <= a:
            t = (x-a+d)/(2.0*d)
            return 2.0*t*t
        if x <= a+d:
            t = (a-x+d)/(2.0*d)
            return 1.0-2.0*t*t
        return 1.0

class ZShapeFunction(Function):
    def __init__(self,mid=2,length =2):
        super().__init__(name = 'ZShapeFunction',MidX=mid,Length = length)

    def clone(self):
        return ZShapeFunction(self.MidX, self.Length)

    def evaluate(self, precision):
        self.FuzzyFunction = ZFunction(a=self.MidX,delta=self.Length)
        ig = self.FuzzyFunction.getIntervalGenerator()
        points_x=[]
        next = ig.nextInterval(None,None)
        points = []
        while next is not None:
            x = next
            points_x.append(x)
            y = 1.0 - self.Calc_Y(x,self.MidX,self.Length/2)
            points.append((x,y))
            next = ig.nextInterval(next,None)
        return points

    def Calc_Y(self,x,a,d):
        if x <= a-d:
            return 0.0
        if x <= a:
            t = (x-a+d)/(2.0*d)
            return 2.0*t*t
        if x <= a+d:
            t = (a-x+d)/(2.0*d)
            return 1.0-2.0*t*t
        return 1.0

class PiShapeFunction(Function):
    def __init__(self,mid=2,length =2):
        super().__init__(name='PiShapeFunction',MidX=mid,Length = length)

    def clone(self):
        return PiShapeFunction(self.MidX, self.Length)

    def evaluate(self, precision):
        self.FuzzyFunction = PiFunction(a=self.MidX,delta=self.Length/2)
        ig = self.FuzzyFunction.getIntervalGenerator()
        points_x=[]
        next = ig.nextInterval(None,None)
        points = []
        while next is not None:
            x = next
            points_x.append(x)
            y = self.Calc_Y(x,self.MidX,self.Length/2)
            points.append((x,y))
            next = ig.nextInterval(next,None)
        return points

    def Calc_Y(self,x,a,d):
        d = d/2
        if x < a:
            return SFunction(a-d,d)(x)
        else:
            return ZFunction(a+d,d)(x)

class SquareFunction(Function):
    def __init__(self, min=0, max=100):
        super().__init__( name ="Square", MinX=min, MaxX=max)

    def clone(self):
        return SquareFunction(self.MinX, self.MaxX)

    def evaluate(self, precision):
        square =[(self.MinX,0), (self.MinX, 1), (self.MaxX, 1), (self.MaxX, 0)]
        self.FuzzyFunction = Trapez(self.MinX,self.MaxX,alpha=0,beta=0,y_max=1,y_min=0)
        return square


class FunctionViewer(QDialog):
    def __init__(self, functions, variable):
        QDialog.__init__(self)

        self.functions = functions
        self.variable = variable
        self.functionNames = list(self.functions.keys())

        self.ui = ui.Ui_DgFuntions()
        self.ui.setupUi(self)

        self.pages = 0

        self.ui.toolBox.setVisible(False)

        self.ui.btnAdd.clicked.connect(self.addValue)
        self.ui.btnRemove.clicked.connect(self.removeValue)

        self.scene = QGraphicsScene()
        self.scene.setItemIndexMethod(QGraphicsScene.NoIndex)

        self.ui.functionView.setScene(self.scene)
        self.ui.functionView.setAttribute(Qt.WA_Hover)
        self.axis = FuncAxis(self.ui.functionView)
        self.scene.addItem(self.axis)
        self.scene.setSceneRect(-5,-5,110,110)

        for name, func in self.variable.values.items():
            self.addValueControl(name, func)

    #Agrega un valor linguístico
    def addValue(self):
        text, ok = QInputDialog.getText(self, "Add a new value", "Name")

        if not ok:
            return

        self.variable.values[text] = Function("None")
        self.addValueControl(text, Function("None"))

    #Elimina un valor linguístico
    def removeValue(self):
        page = self.ui.toolBox.currentWidget()
        text = self.ui.toolBox.itemText(self.ui.toolBox.currentIndex())

        if self.pages >= 1:
            self.ui.toolBox.removeItem(self.ui.toolBox.currentIndex())

            if hasattr(page, "function") and page.function:
                self.scene.removeItem(page.function)

            page.deleteLater()

        self.pages -= 1

        self.variable.values.pop(text)

        if not self.pages:
            self.ui.btnRemove.setEnabled(False)
            self.ui.toolBox.setVisible(False)

        self.scene.update()

    #Agrega para un valor linguístico agrega todos los controles.
    def addValueControl(self, name, func):
        if not self.pages:
            self.ui.toolBox.setVisible(True)
            self.ui.btnRemove.setEnabled(True)

            page = self.ui.toolBox.widget(0)
            self.ui.toolBox.setItemText(0, name)
            layout = page.layout()

            if layout:
                layout.deleteLater()

        else:
            page = QWidget()
            self.ui.toolBox.addItem(page, name)

        layout = QFormLayout()
        page.setLayout(layout)

        combo = QComboBox()
        combo.addItems(self.functionNames)

        for i,s in enumerate(self.functionNames):
            if s == func.name:
                combo.setCurrentIndex(i)
                break

        layout.addRow("Type", combo)

        def setupItem():
            func = self.functions[combo.currentText()].clone()

            if hasattr(page, "function") and page.function:
                self.scene.removeItem(page.function)

            page.function = GraphicFun(func, self.ui.functionView)
            self.scene.addItem(page.function)

            while layout.count() > 2:
                item = layout.takeAt(2)
                item.widget().deleteLater()

            for name, value in func.properties.items():
                spin = QDoubleSpinBox()

                spin.setMinimum(-1000)
                spin.setMaximum(1000)
                spin.setValue(value)
                layout.addRow(name, spin)

                spin.valueChanged.connect(self.connectValueChanged(func, name))

            self.scene.update()

        combo.currentIndexChanged.connect(setupItem)
        setupItem()

        self.pages += 1

    def connectValueChanged(self, func, name):
        def valueChanged(value):
            func.properties[name] = value
            self.scene.update()

        return valueChanged

