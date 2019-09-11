# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChangeVolumePropertiesWidget.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import vtk
import math

from classDisplayVol import DisplayVol

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChangeVolumePropertiesWidget(object):
    
    def __init__(self):
        self.displayer = DisplayVol()
        return
    
    def setupUi(self, ChangeVolumePropertiesWidget):
        ChangeVolumePropertiesWidget.setObjectName("ChangeVolumePropertiesWidget")
        ChangeVolumePropertiesWidget.resize(457, 186)
        
        horizontalLayout_6 = QtWidgets.QHBoxLayout(ChangeVolumePropertiesWidget)
        horizontalLayout_6.setContentsMargins(11, 11, 11, 11)
        horizontalLayout_6.setSpacing(6)
        horizontalLayout_6.setObjectName("horizontalLayout_6")
        
        gridLayout_2 = QtWidgets.QGridLayout()
        gridLayout_2.setContentsMargins(11, 11, 11, 11)
        gridLayout_2.setSpacing(6)
        gridLayout_2.setObjectName("gridLayout_2")
       
        horizontalLayout = QtWidgets.QHBoxLayout()
        horizontalLayout.setContentsMargins(11, 11, 11, 11)
        horizontalLayout.setSpacing(6)
        horizontalLayout.setObjectName("horizontalLayout")
        
        gridLayout_2.addLayout(horizontalLayout, 4, 0, 1, 1)
        
        horizontalLayout_2 = QtWidgets.QHBoxLayout()
        horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        horizontalLayout_2.setSpacing(6)
        horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        horizontalLayout_3 = QtWidgets.QHBoxLayout()
        horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        horizontalLayout_3.setSpacing(6)
        horizontalLayout_3.setObjectName("horizontalLayout_3")
        
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
         
        horizontalLayout_3.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(ChangeVolumePropertiesWidget)
        
        font = QtGui.QFont()
        font.setStrikeOut(False)
        font.setKerning(True)
        
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        horizontalLayout_3.addWidget(self.label)
        
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        
        horizontalLayout_3.addItem(spacerItem2)
        horizontalLayout_2.addLayout(horizontalLayout_3)
        gridLayout_2.addLayout(horizontalLayout_2, 0, 0, 1, 1)
        
        horizontalLayout_4 = QtWidgets.QHBoxLayout()
        horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        horizontalLayout_4.setSpacing(6)
        horizontalLayout_4.setObjectName("horizontalLayout_4")
        
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontalLayout_4.addItem(spacerItem3)
        
        self.label_3 = QtWidgets.QLabel(ChangeVolumePropertiesWidget)
        self.label_3.setObjectName("label_3")
        horizontalLayout_4.addWidget(self.label_3)
        
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontalLayout_4.addItem(spacerItem4)
        gridLayout_2.addLayout(horizontalLayout_4, 5, 0, 1, 1)

        
        
        self.lowerThresholdSlider = QtWidgets.QSlider(ChangeVolumePropertiesWidget)
        self.lowerThresholdSlider.setOrientation(QtCore.Qt.Horizontal)
        self.lowerThresholdSlider.setObjectName("lowerThresholdSlider")
        self.lowerThresholdSlider.setTickInterval(1)
        self.lowerThresholdSlider.setRange(0,255.0)
        self.lowerThresholdSlider.setValue(0.0)
        gridLayout_2.addWidget(self.lowerThresholdSlider, 1, 0, 1, 1)
        
        self.lowerThresholdDisplay = QtWidgets.QLineEdit(ChangeVolumePropertiesWidget)
        self.lowerThresholdDisplay.setMaximumSize(QtCore.QSize(51, 22))
        self.lowerThresholdDisplay.setObjectName("lowerThresholdDisplay")
        horizontalLayout.addWidget(self.lowerThresholdDisplay)
        self.lowerThresholdDisplay.setText("0");
        
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontalLayout.addItem(spacerItem)
        
        self.upperThresholdSlider = QtWidgets.QSlider(ChangeVolumePropertiesWidget)
        self.upperThresholdSlider.setOrientation(QtCore.Qt.Horizontal)
        self.upperThresholdSlider.setObjectName("upperThresholdSlider")
        self.upperThresholdSlider.setRange(0,255.0)
        self.upperThresholdSlider.setValue(255.0)
        gridLayout_2.addWidget(self.upperThresholdSlider, 2, 0, 1, 1)
        horizontalLayout_6.addLayout(gridLayout_2)
        
        self.upperThresholdDisplay = QtWidgets.QLineEdit(ChangeVolumePropertiesWidget)
        self.upperThresholdDisplay.setMaximumSize(QtCore.QSize(51, 22))
        self.upperThresholdDisplay.setObjectName("upperThresholdDisplay")
        horizontalLayout.addWidget(self.upperThresholdDisplay)
        self.upperThresholdDisplay.setText("255");
        
       
        self.opacitySlider = QtWidgets.QSlider(ChangeVolumePropertiesWidget)
        self.opacitySlider.setOrientation(QtCore.Qt.Horizontal)
        self.opacitySlider.setObjectName("opacitySlider")
        self.opacitySlider.setRange(0,100.0)
        self.opacitySlider.setValue(100.0)
        gridLayout_2.addWidget(self.opacitySlider, 6, 0, 1, 1)
        
        self.retranslateUi(ChangeVolumePropertiesWidget)
        
        self.volumeScalarOpacity = vtk.vtkPiecewiseFunction()
        self.opacityVal = 1.0
        self.lowerThreshVal = 0
        self.upperThreshVal = 0
        
        self.opacitySlider.valueChanged.connect(self.changeOpacity)
        self.lowerThresholdSlider.valueChanged.connect(lambda: self.changeThreshold("lower"))
        self.upperThresholdSlider.valueChanged.connect(lambda: self.changeThreshold("upper"))
        
        QtCore.QMetaObject.connectSlotsByName(ChangeVolumePropertiesWidget)
        return

    def retranslateUi(self, ChangeVolumePropertiesWidget):
        _translate = QtCore.QCoreApplication.translate
        ChangeVolumePropertiesWidget.setWindowTitle(_translate("ChangeVolumePropertiesWidget", "ChangeVolumePropertiesWidget"))
        self.label.setText(_translate("ChangeVolumePropertiesWidget", " Thresholds"))
        self.label_3.setText(_translate("ChangeVolumePropertiesWidget", "Opacity"))
        return


    def changeThreshold(self, tag):
        
        if (tag == "lower"):
            tickValue = self.lowerThresholdSlider.value()
            
            if (tickValue < self.upperThresholdSlider.value()):
                self.lowerThreshVal = tickValue
                self.upperThreshVal = self.upperThresholdSlider.value()
            else:
                self.lowerThreshVal = self.upperThresholdSlider.value()
                self.upperThreshVal = tickValue
        elif (tag == "upper"):
            tickValue = self.upperThresholdSlider.value()
        
            if (tickValue < self.lowerThresholdSlider.value()):
                self.lowerThreshVal = tickValue
                self.upperThreshVal = self.lowerThresholdSlider.value()
            else:
                self.lowerThreshVal = self.lowerThresholdSlider.value()
                self.upperThreshVal = tickValue
            
        self.lowerThresholdDisplay.setText(str(self.lowerThreshVal))
        self.upperThresholdDisplay.setText(str(self.upperThreshVal))

        self.middlePoint = self.lowerThreshVal + math.floor((self.upperThreshVal - self.lowerThreshVal)*0.5);
        
        self.changeVolumeScalarOpacity()
        return
    
    def changeOpacity(self):
        tickValue = self.opacitySlider.value()
        
        self.opacityVal = tickValue * 0.01
        
        self.changeVolumeScalarOpacity()
        return
    
    def changeVolumeScalarOpacity(self):
        self.volumeScalarOpacity.RemoveAllPoints();
        self.volumeScalarOpacity.AddPoint(self.lowerThreshVal-1, 0);
        self.volumeScalarOpacity.AddPoint(self.lowerThreshVal, self.opacityVal);
        self.volumeScalarOpacity.AddPoint(self.upperThreshVal+1, 0);
        self.volumeScalarOpacity.AddPoint(self.upperThreshVal, self.opacityVal);
        
        self.displayer.setVolumeOpacity(self.volumeScalarOpacity)
        return
    
    
    def setQVTKImageWidget(self, displayer):
        self.displayer = displayer
        return
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
#    ChangeVolumePropertiesWidget = QtWidgets.QWidget()
#    ui = Ui_ChangeVolumePropertiesWidget()
#    ui.setupUi(ChangeVolumePropertiesWidget)
#    ChangeVolumePropertiesWidget.show()
    sys.exit(app.exec_())

