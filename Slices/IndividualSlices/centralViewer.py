"""
@author: Jose Quevedo V.

This class setup and display the main window for the 4 views of the volume, Sagital, Axial, Coronal and 3D Volume. 
When the sliders in the ChangeVolumePropertiesWidget are moved this affect only to the view selected in the rotation and by the displace slicer

Methods
    setupUi(self, main_window)
        This method is used to configure all the widgets of the main window, it contains a frame to display the 
        file selected and a tool bar whit a single bottom called "Open" whith a menu where the user can choose between MHD or VOL
        Input: It receives a QtWidgets.QMainWindow() object
        Output: None
            
     retranslateUi(self, MainWindow)
        This method is auto generated by Qt Creator and set the string names in the window
        Input: Form is a QtWidget object
        Output: None
    
    openFileNameDialog(self, type_of_file):
        This method displays the file explorer where the user can choose the file of the kind previously selected,
        this kinds are (for the moment): MHD and VOL.
        Input: type_of_file is a string that indicates the kind of file to open
        Output:None
        
    changeViewSelected(self, viewSelected):
        This method it's activated when the buttons (Sagital, Axial, Coronal) are pushed, and chage the ChangeVolumePropertiesWidget 
        to the view selected
        Input: viewSelected integer that indicates to the ChangeVolumePropertiesWidget which view I want to rotate and displace.
              SAGITAL = 0
              AXIAL   = 1 
              CORONAL = 2  
              the view by default is SAGITAL
        Output:None
                
                
Constants 
    This constants are used to manage the three 2D views 
    SAGITAL = 0
    AXIAL   = 1 
    CORONAL = 2
"""

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from ClassReadVolume import ReadVolume
from ClassSlicer  import Slicer
from classViewSlice import ViewSlice
from classChangeSliceRotation import Ui_ChangeSliceRotation

from classDisplayVol import DisplayVol
from classChangeVolumePropertiesWidget import Ui_ChangeVolumePropertiesWidget

SAGITAL = 0
AXIAL   = 1 
CORONAL = 2

class Ui_MainWindow(object):
    def setupUi(self, main_window):
        # Begins code auto generated
        # This code is auto generated by Qt Designer
        main_window.setObjectName("main_window")
        main_window.resize(815, 652)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        
        self.gridLayoutWidget = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        
        self.frameSagital = QtWidgets.QFrame(self.centralwidget)
        self.frameSagital.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameSagital.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSagital.setObjectName("frameSagital")
        self.gridLayout.addWidget(self.frameSagital,  0, 0, 1, 1)
        
        self.frameAxial = QtWidgets.QFrame(self.centralwidget)
        self.frameAxial.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameAxial.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameAxial.setObjectName("frameAxial")
        self.gridLayout.addWidget(self.frameAxial,  0, 1, 1, 1)
        
        self.frameCoronal = QtWidgets.QFrame(self.centralwidget)
        self.frameCoronal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameCoronal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameCoronal.setObjectName("frameCoronal")
        self.gridLayout.addWidget(self.frameCoronal, 1, 0, 1, 1)
        
        self.frame3DView = QtWidgets.QFrame(self.centralwidget)
        self.frame3DView.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame3DView.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame3DView.setObjectName("frame3DView")
        self.gridLayout.addWidget(self.frame3DView, 1, 1, 1, 1)        
        
        self.gridLayout.addWidget(self.frameSagital, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.pushButtonSagital = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSagital.setObjectName("pushButtonSagital")
        self.horizontalLayout.addWidget(self.pushButtonSagital)
        
        self.pushButtonAxial = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAxial.setObjectName("pushButtonAxial")
        self.horizontalLayout.addWidget(self.pushButtonAxial)
        
        self.pushButtonCoronal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCoronal.setObjectName("pushButtonCoronal")
        self.horizontalLayout.addWidget(self.pushButtonCoronal)
        
#        self.pushButton3D = QtWidgets.QPushButton(self.centralwidget)
#        self.pushButton3D.setObjectName("pushButton3D")
#        self.horizontalLayout.addWidget(self.pushButton3D)       
        
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 90)
        self.verticalLayout.setStretch(1, 10)
        self.gridLayoutWidget.addLayout(self.verticalLayout, 0, 0, 1, 1)
        
        main_window.setCentralWidget(self.centralwidget)
        
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
         
        # These are the functions that are activated in case the buttons are clicked.
        self.action_vol.triggered.connect(lambda: self.openFileNameDialog("vol"))
        self.action_mhd.triggered.connect(lambda: self.openFileNameDialog("mhd"))
        
        # These are the functions that are activated in case the buttons are clicked to  
        # select the view we want to rotate or displace
        self.pushButtonSagital.pressed.connect(lambda: self.changeViewSelected(SAGITAL))
        self.pushButtonAxial.pressed.connect(lambda: self.changeViewSelected(AXIAL))
        self.pushButtonCoronal.pressed.connect(lambda: self.changeViewSelected(CORONAL))
        
        QtCore.QMetaObject.connectSlotsByName(main_window)
        return

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Viewer"))
        self.menu_open.setTitle(_translate("main_window", "Open"))
        self.action_vol.setText(_translate("main_window", "VOL"))
        self.action_mhd.setText(_translate("main_window", "MHD"))
        self.pushButtonSagital.setText(_translate("main_window", "Sagital"))
        self.pushButtonAxial.setText(_translate("main_window", "Axial"))
        self.pushButtonCoronal.setText(_translate("main_window", "Coronal"))
#        self.pushButton3D.setText(_translate("main_window", "3D"))

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
        file_name,_ = QFileDialog.getOpenFileName(None,"Archivos", "../../Data",mode, options=options)   
          
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
            
            # The dimensions of the volume are obtained to set up the minimum and maximum of the displacement in X, Y and Z axis
            change_slice__rot_ui.setMax(vol_image.GetDimensions())
            
            ### DEFAULT ###
#            The Slicer for the view (Sagital, Axial or Coronal) of the volume is created
#            slicerDefault = Slicer()
            
#            We establish  the volume read and the view we want
#            slicerDefault.setSlicesData(vol_image, DEFAULT)
            
#            The vtkImageData it's obtained
#            sliceImageDefault = slicerDefault.getOutput()
            
#            The viewer of the selected view it's obtained and we set the vtkImageData
#            viewerDef = change_slice__rot_ui.getViewSliceDefault()
#            viewerDef.setSlice(sliceImageDefault)

#            frame_def = viewerDef.displaySlice(self.centralwidget)
#            self.frameDefault.setLayout(frame_def)

#            change_slice__rot_ui.setSliceRotateDefault(slicerDeafult)     
            
            
            ### SAGITAL ###
            slicerSagital = Slicer()
            slicerSagital.setSlicesData(vol_image, SAGITAL)
            sliceImageSagital = slicerSagital.getOutput()
            
            viewerSag = change_slice__rot_ui.getViewSliceSagital()
            viewerSag.setSlice(sliceImageSagital)
            
            frame_sag = viewerSag.displaySlice(self.centralwidget)
            self.frameSagital.setLayout(frame_sag)
            
            change_slice__rot_ui.setSliceRotateSagital(slicerSagital)     
 
    
            ### AXIAL ###
            slicerAxial = Slicer()
            slicerAxial.setSlicesData(vol_image, AXIAL)
            sliceImageAxial = slicerAxial.getOutput()
            
            viewerAxi = change_slice__rot_ui.getViewSliceAxial()
            viewerAxi.setSlice(sliceImageAxial)
            
            frame_axi = viewerAxi.displaySlice(self.centralwidget)
            self.frameAxial.setLayout(frame_axi)
            
            change_slice__rot_ui.setSliceRotateAxial(slicerAxial)  
    
            
            ### CORONAL ###
            slicerCoronal = Slicer()
            slicerCoronal.setSlicesData(vol_image, CORONAL)
            sliceImageCoronal = slicerCoronal.getOutput()
            
            viewerCor = change_slice__rot_ui.getViewSliceCoronal()
            viewerCor.setSlice(sliceImageCoronal)
            
            frame_cor = viewerCor.displaySlice(self.centralwidget)
            self.frameCoronal.setLayout(frame_cor)
            
            change_slice__rot_ui.setSliceRotateCoronal(slicerCoronal)
            
            ### 3D ###
            displayer = DisplayVol()
            displayer.setVol(vol_image)
            
            # frame_vol will contain de representation of the Volume
            frame_vol = displayer.displayVol(self.centralwidget)
            self.frame3DView.setLayout(frame_vol)
            change_volume_prop_ui.setQVTKImageWidget(displayer)         
        return
    
    def changeViewSelected(self, viewSelected):
        change_slice__rot_ui.setViewToMove(viewSelected)
        return


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    
    
    ChangeSliceRotation = QtWidgets.QWidget()
    change_slice__rot_ui = Ui_ChangeSliceRotation()
    change_slice__rot_ui.setupUi(ChangeSliceRotation)
    ChangeSliceRotation.show()
    
    ChangeVolumePropertiesWidget = QtWidgets.QWidget()
    change_volume_prop_ui = Ui_ChangeVolumePropertiesWidget()
    change_volume_prop_ui.setupUi(ChangeVolumePropertiesWidget)
    ChangeVolumePropertiesWidget.show()
    
    sys.exit(app.exec_())

