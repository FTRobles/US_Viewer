# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 09:33:21 2019

@author: Fabian
"""

import vtk

from PyQt5 import QtWidgets
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

polygon = 1
image = 0

class ViewSlice():
    
    def __init__(self):
        self.viewer = vtk.vtkImageViewer2()
        self.vtkWidget = QVTKRenderWindowInteractor()
    
    #sliceImage it's a vtkImageData
    def setSlice(self, sliceImage):    
        self.viewer.SetInputData(sliceImage)
        self.viewer.Render()
        self.viewer.GetRenderWindow().Render()

    def displaySlice(self, centralwidget):    
        #display the result
        sl = QtWidgets.QVBoxLayout(centralwidget)
        
        self.setInteractorStyle(image)
        
        sl.addWidget(self.vtkWidget)
        
        renwin = self.vtkWidget.GetRenderWindow()
        self.viewer.SetRenderWindow(renwin)
        
        self.viewer.GetRenderer().ResetCamera()
       
        self.vtkWidget.Initialize()
        self.vtkWidget.Start()
        
        return sl
    
    
    def addNewActor(self, actor):
        self.viewer.GetRenderer().AddActor(actor)
        return
    
    def setInteractorStyle(self, mode):
        if (mode == polygon):
            style = vtk.vtkInteractorStyleDrawPolygon()
#            print(style.GetPolygonPoints())
        elif (mode == image):
            style = vtk.vtkInteractorStyleImage()
            
        self.vtkWidget.SetInteractorStyle(style)
        return