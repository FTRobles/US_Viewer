# -*- coding: utf-8 -*-
#
# Created by: PyQt5 UI code generator 5.6
#
"""
This class setup and display the main window for the 3D viewer.

Methods

setupUi(self, main_window)
    This method is used to configure all the widgets of the main window, it contains a frame to display the 
    file selected and a tool bar whit a single bottom called "Open" whith a menu where the user can choose between MHD or VOL
    Input: It receives a QtWidgets.QMainWindow() object
    Output: None
        
openFileNameDialog(self, type_of_file):
    This method displays the file explorer where the user can choose the file of the kind previously selected,
    this kinds are (for the moment): MHD and VOL.
    Input:  
"""
# Declaracion de funciones
# Nombre, que hace, parametros de entrada y salida
# openFileNameDialog
#
#
# Declaracion de variables
# nombre, para que se ocupa
# main_window
#
#
# central_widget
#
#
# frame
#
#
# menu_bar
#
#
# menu_open
#
#
# action_vol
#
#
# grid_layout
#

import vtk

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from ClassReadVolume import ReadVolume
from ClassSlicer  import Slicer
from classViewSlice import ViewSlice
from classChangeSliceRotation import Ui_ChangeSliceRotation

AXIAL   = 1 
CORONAL = 2
SAGITAL = 0

class Ui_main_window(object):
    def setupUi(self, main_window):
        
        main_window.setObjectName("main_window")
        main_window.resize(800, 600)
        
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")
        main_window.setCentralWidget(self.central_widget) 
        
        grid_layout = QtWidgets.QGridLayout(self.central_widget)
        grid_layout.setObjectName("grid_layout")
        
        self.frame = QtWidgets.QFrame(self.central_widget)
        self.frame.setGeometry(QtCore.QRect(19, 19, 761, 511))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        grid_layout.addWidget(self.frame, 0, 0, 1, 1)
        
        menu_bar = QtWidgets.QMenuBar(main_window)
        menu_bar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        menu_bar.setObjectName("menu_bar")
        main_window.setMenuBar(menu_bar)

        self.menu_open = QtWidgets.QMenu(menu_bar)
        self.menu_open.setObjectName("menu_open")
        
        self.action_vol = QtWidgets.QAction(main_window)
        self.action_vol.setObjectName("action_vol")
        self.menu_open.addAction(self.action_vol)
        
        self.action_mhd = QtWidgets.QAction(main_window)
        self.action_mhd.setObjectName("action_mhd")
        self.menu_open.addAction(self.action_mhd)
        
        menu_bar.addAction(self.menu_open.menuAction())

        self.retranslateUi(main_window)
 
        self.action_vol.triggered.connect(lambda: self.openFileNameDialog("vol"))
        self.action_mhd.triggered.connect(lambda: self.openFileNameDialog("mhd"))
        
        QtCore.QMetaObject.connectSlotsByName(main_window)

    
    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Visualizador"))
        self.menu_open.setTitle(_translate("main_window", "Open"))
        self.action_vol.setText(_translate("main_window", "VOL"))
        self.action_mhd.setText(_translate("main_window", "MHD"))
        return
    
    def openFileNameDialog(self, type_of_file):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        
        mode = ""
        if (type_of_file == "vol"):
            mode = "VOL Files (*.vol)"
        elif (type_of_file == "mhd"):
            mode = "MHD Files (*.mhd)"
            
        file_name,_ = QFileDialog.getOpenFileName(None,"Archivos", "C:/Users/Fabian/Documents/Viewer/Files/Data",mode, options=options)   
            
        if file_name:
            reader = ReadVolume()
            reader.setFilename(str(file_name))
            
            if (type_of_file == "vol"):
                reader.openVol()
            elif (type_of_file == "mhd"):
                reader.openMHD()
            
            vol_image = reader.getOutput()
            
            slicer = Slicer()
            slicer.setSlicesData(vol_image, SAGITAL)
            sliceImage = slicer.getOutput()
            
            viewer =  change_slice__rot_ui.getViewSlice()
            viewer.setSlice(sliceImage)
            
            frame_vol = viewer.displaySlice(self.central_widget)
            self.frame.setLayout(frame_vol)
            
            change_slice__rot_ui.setVolumeRotate(vol_image)     
            
        return
    
     
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    main_window.show()
    
    ChangeSliceRotation = QtWidgets.QWidget()
    change_slice__rot_ui = Ui_ChangeSliceRotation()
    change_slice__rot_ui.setupUi(ChangeSliceRotation)
    ChangeSliceRotation.show()
    
    sys.exit(app.exec_())

