"""
@author: Jose Quevedo V.

This class setup and display the main window for the 4 views of the volume, Sagital, Axial, Coronal and 3D Volume. 
When the sliders in the ChangeVolumePropertiesWidget are moved this affect the three 2D views at the same time in the rotation, we can 
choose from the buttons which one we want to modificate by the displace slicer

Methods
   setVol(self,displayVolume)
        This method set the piecewise function of opacity to the volume and the initial values
        Input: displayVolume is a vtkImageData that contains the information of the volume
        Output: None

   displayVol(self,centralwidget)
        This method sets the render and the camera and set the renwin interactor to the centralwidget
        and start the render in the window
        Input: centralwidget is the widget that will contain the frame
        Output: vl is a QVBoxLayout whith the frame

   setVolumeOpacity(self,newVolumeScalarOpacity)
        This method set the new picewise function to the volume controlled by the sliders
        Input: newVolumeScalarOpacity is a picewise function.
        Output: None
        
Variables
    volume is a vtkVolume() that contains the information of the volume
    
    volumeProperty is a vtkVolumeProperty() that contains the the properties of the volume
    such as the picewise function, opacity, etc.
    
    renwin is the vtkRenderWindow() where the volume wil display
"""

import vtk

from PyQt5 import QtWidgets
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class DisplayVol():
    
    def __init__(self):
        self.volume=vtk.vtkVolume()
        self.volumeProperty=vtk.vtkVolumeProperty()
        self.renwin = vtk.vtkRenderWindow()
        return
    #set the initial values of the attributes

    def setVol(self,displayVolume):
        #set the piecewise function for the opacity
        volumeScalarOpacity= vtk.vtkPiecewiseFunction()
        volumeScalarOpacity.AddPoint(0,1.0)
        volumeScalarOpacity.AddPoint(255,1.0)
        
        self.volumeProperty.SetScalarOpacity(volumeScalarOpacity)
        
        #set the piece wise function for the Color ranges
        volumeColor=vtk.vtkColorTransferFunction()
        volumeColor.AddRGBPoint(0,0.0,0.0,0.0)
        volumeColor.AddRGBPoint(64,0.25,0.25,0.25)
        volumeColor.AddRGBPoint(128,0.5,0.5,0.5)
        volumeColor.AddRGBPoint(192,0.75,0.75,0.75)
        volumeColor.AddRGBPoint(255,1.0,1.0,1.0)
        self.volumeProperty.SetColor(volumeColor)
        
        
        volumeMapper=vtk.vtkGPUVolumeRayCastMapper()
        volumeMapper.SetInputData(displayVolume)
        
        #set initial values for the volume
        self.volume.SetMapper(volumeMapper)
        self.volume.SetOrigin(0,0,0)
        self.volume.SetProperty(self.volumeProperty)
        self.volume.Update()
        
        return

    def displayVol(self,centralwidget):  
        
        #set render initial values
        renderer=vtk.vtkRenderer()
        renderer.SetBackground(183.0/255.0,197.0/255.0,253.0/255.0)
        renderer.AddVolume(self.volume)
        renderer.GetActiveCamera().SetFocalPoint(self.volume.GetCenter())
        renderer.GetActiveCamera().Roll(90)
        
        #set camera in a position where it sees the volume
        cameraPos=[]
        cameraPos.append(self.volume.GetCenter()[0]+self.volume.GetMaxXBound()+30)
        cameraPos.append(self.volume.GetCenter()[1])
        cameraPos.append(self.volume.GetCenter()[2])
        
        renderer.GetActiveCamera().SetPosition(cameraPos)
        
        vl = QtWidgets.QVBoxLayout(centralwidget)
        vtkWidget = QVTKRenderWindowInteractor()
        vl.addWidget(vtkWidget)

        self.renwin = vtkWidget.GetRenderWindow()
        self.renwin.AddRenderer(renderer)
        iren = self.renwin.GetInteractor()
        
        iren.Initialize()
        iren.Start()
        
        return vl
    
    def setVolumeOpacity(self,newVolumeScalarOpacity):
        
        self.volumeProperty.SetScalarOpacity(newVolumeScalarOpacity)
        self.renwin.Render()
        return
    