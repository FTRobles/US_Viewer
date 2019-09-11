"""
Created by: Jose Quevedo
This class setup and display the main window for the 3D viewer.

Methods:
    setupUi(self, main_window)
        This method is used to configure all the widgets of the main window, it contains a frame to display the 
        file selected and a tool bar whit a single bottom called "Open" whith a menu where the user can choose between MHD or VOL
        Input: It receives a QtWidgets.QMainWindow() object
        Output: None
            
    openFileNameDialog(self, type_of_file):
        This method displays the file explorer where the user can choose the file of the kind previously selected,
        this kinds are (for the moment): MHD and VOL.
        Input:  type_of_file this parameter it's sent by the buttons of the toolbar, it can be "vol" or "mhd"
        Output: None
    
Variables:
    

"""
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

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from classDisplayVol import DisplayVol
from classChangeVolumePropertiesWidget import Ui_ChangeVolumePropertiesWidget
from ClassReadVolume import ReadVolume

class Ui_main_window(object):
   
    def setupUi(self, main_window):    
        # Begins code auto generated
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
        # Ends code auto generated
        
        # When one of the buttons it's clicked it calls the function openFileNameDialog
        self.action_vol.triggered.connect(lambda: self.openFileNameDialog("vol"))
        self.action_mhd.triggered.connect(lambda: self.openFileNameDialog("mhd"))
        
        QtCore.QMetaObject.connectSlotsByName(main_window)

    
    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "3D Viewer"))
        self.menu_open.setTitle(_translate("main_window", "Open"))
        self.action_vol.setText(_translate("main_window", "VOL"))
        self.action_mhd.setText(_translate("main_window", "MHD"))
        return
    
    def openFileNameDialog(self, type_of_file):
        # This variable is used tu setup tu options in the file explorer
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        
        mode = ""
        if (type_of_file == "vol"):
            mode = "VOL Files (*.vol)"
        elif (type_of_file == "mhd"):
            mode = "MHD Files (*.mhd)"
            
        # We display the file explorer only showing the kind of files selected
        file_name,_ = QFileDialog.getOpenFileName(None,"Archivos", "C:/Users/Fabian/Documents/Viewer/Files/Data",mode, options=options)   
            
        # If the patch of the file it's valid
        if file_name:
            # We create a reader and set the path of the file
            reader = ReadVolume()
            reader.setFilename(str(file_name))
            
            # We use the type_of_file to know what method of the clase ReadVolume to use
            if (type_of_file == "vol"):
                reader.openVol()
            elif (type_of_file == "mhd"):
                reader.openMHD()
            
            # Once the image is processed, we obtain an object of type vtkImageData
            # This vtkImageData must be save to open 3D and 2D views
            vol_image = reader.getOutput()
            
            # We create a displayer of the class DisplayVol and set up the vtkImageData
            displayer = DisplayVol()
            displayer.setVol(vol_image)
            
            # frame_vol will contain de representation of the   Volume
            frame_vol = displayer.displayVol(self.central_widget)
            self.frame.setLayout(frame_vol)
            change_volume_prop_ui.setQVTKImageWidget(displayer)           
            
            
        return    
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    main_window.show()
    
    ChangeVolumePropertiesWidget = QtWidgets.QWidget()
    change_volume_prop_ui = Ui_ChangeVolumePropertiesWidget()
    change_volume_prop_ui.setupUi(ChangeVolumePropertiesWidget)
    ChangeVolumePropertiesWidget.show()
    
    sys.exit(app.exec_())
