# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 09:33:21 2019

@author: Fabian
"""

import vtk

from PyQt5 import QtWidgets
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class ViewSlice():
    
    def __init__(self):
        self.viewer = vtk.vtkImageViewer2()
        #self.renwin = vtk.vtkRenderWindow()
    
    
    #sliceImage it's a vtkImageData
    def setSlice(self, sliceImage):    
        self.viewer.SetInputData(sliceImage)
        self.viewer.Render()
        self.viewer.GetRenderWindow().Render()


    def displaySlice(self, centralwidget):    
        #display the result
        sl = QtWidgets.QVBoxLayout(centralwidget)
        
        vtkWidget = QVTKRenderWindowInteractor()
        
        style = vtk.vtkInteractorStyleImage()
        vtkWidget.SetInteractorStyle(style)
        
        sl.addWidget(vtkWidget)
        
        renwin = vtkWidget.GetRenderWindow()
        self.viewer.SetRenderWindow(renwin)
        
        self.viewer.GetRenderer().ResetCamera()
       
        vtkWidget.Initialize()
        vtkWidget.Start()
        
        return sl
    
        