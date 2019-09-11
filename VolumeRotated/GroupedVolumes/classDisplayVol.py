# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 11:35:59 2019

@author: Miguel Sánchez Cervantes
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
    
    def setVol(self,displayVolume):
        volumeScalarOpacity= vtk.vtkPiecewiseFunction()
        volumeScalarOpacity.AddPoint(0,1.0)
        volumeScalarOpacity.AddPoint(255,1.0)
        
        self.volumeProperty.SetScalarOpacity(volumeScalarOpacity)
        
        volumeColor=vtk.vtkColorTransferFunction()
        volumeColor.AddRGBPoint(0,0.0,0.0,0.0)
        volumeColor.AddRGBPoint(64,0.25,0.25,0.25)
        volumeColor.AddRGBPoint(128,0.5,0.5,0.5)
        volumeColor.AddRGBPoint(192,0.75,0.75,0.75)
        volumeColor.AddRGBPoint(255,1.0,1.0,1.0)
        self.volumeProperty.SetColor(volumeColor)
        
        #compositeFunction=vtk.vtkVolumeRayCastCompositeFunction()
        
        volumeMapper=vtk.vtkGPUVolumeRayCastMapper()
        #volumeMapper.SetVolumeRayCastFunction(compositeFunction)
        #volumeMapper.CroppingOff()
        volumeMapper.SetInputData(displayVolume)
        
        self.volume.SetMapper(volumeMapper)
        self.volume.SetOrigin(0,0,0)
        self.volume.SetProperty(self.volumeProperty)
        self.volume.Update()
        
        return

    def displayVol(self,centralwidget):    
        renderer=vtk.vtkRenderer()
        renderer.SetBackground(183.0/255.0,197.0/255.0,253.0/255.0)
        renderer.AddVolume(self.volume)
        renderer.GetActiveCamera().SetFocalPoint(self.volume.GetCenter())
        renderer.GetActiveCamera().Roll(90)
        
        
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
    