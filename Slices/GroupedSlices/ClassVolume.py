# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 11:43:24 2019

@author: Miguel Sánchez Cervantes

this class helps to rotate the volume and obtain the new vtkImageData.

constants:
    X,Y,Z make easy to work with the rotation in each 
    SAGITAL, Axial and CORONAL help to know which slice is changing the rotation center
attributes:
    volume. saves the data of the volume
    transform and reslice. help with the rotation
    center. is an array that saves the center of the volume.
    angle X,Y,Z save the angle of rotation of the volume
methods:
    setVolume() recieves a vtkImgeData object as parameter.
    It sets the inital values of the attributes
    
    rotate() recieves an angle and an axis as parameters.
    It does the rotation of the volume.
    
    getOutput() return the vtkImageData object resulted after rotation
    
    setNewRotationCenter() changes the rotation center of the volume
    
    displaceVolume()
    recieves a displacement and a view mode
    it displace the entire volume in the direction of the slice's depth axis:
        Z for Sagital, X for Axial and Y for Coronal
"""
import vtk
X=0
Y=1
Z=2

SAGITAL=0
AXIAL=1
CORONAL=2

class Volume:
    def __init__(self):
        #volume data
        self.volume=vtk.vtkImageData()
        
        #these attributtes do the rotation
        self.transform=vtk.vtkTransform()
        self.reslice=vtk.vtkImageReslice()
        
        #center of the volume
        self.center=[]
        
        #angles of rotation
        self.angleX=0
        self.angleY=0
        self.angleZ=0
    
    #set de volume and some attributes
    def setVolume(self,vol_data):
        #copying vtkImageData object given into volume
        self.volume.DeepCopy(vol_data)
        
        #obtaining bounds of volume
        bounds=self.volume.GetBounds()
        
        #calculate the center
        self.center.append((bounds[1]+bounds[0])/2.0)
        self.center.append((bounds[3]+bounds[2])/2.0)
        self.center.append((bounds[5]+bounds[4])/2.0)
        
        #set the reslice initial values 
        self.reslice.SetInputData(self.volume)
        self.reslice.SetResliceTransform(self.transform)
        self.reslice.SetInterpolationModeToCubic()
        self.reslice.SetOutputSpacing(self.volume.GetSpacing()[0],self.volume.GetSpacing()[1],self.volume.GetSpacing()[2])
        self.reslice.SetOutputOrigin(self.volume.GetOrigin()[0],self.volume.GetOrigin()[1],self.volume.GetOrigin()[2])
        self.reslice.SetOutputExtent(self.volume.GetExtent())
        self.transform.Update()
        self.reslice.Update()
        
        return
    
    #rotate the entire volume
    def rotate(self,angle,axis):
        
        self.transform.Translate(self.center[0], self.center[1], self.center[2])
        #doing the rotation depending on the axis and angle given
        if(axis==X):
            rotate=angle-self.angleX
            self.transform.RotateX(rotate)
            self.angleX=angle
        elif(axis==Y):
            rotate=angle-self.angleY
            self.transform.RotateY(rotate)
            self.angleY=angle
        elif(axis==Z):
            rotate=angle-self.angleZ
            self.transform.RotateZ(rotate)
            self.angleZ=angle
            
        self.transform.Translate(-self.center[0], -self.center[1], -self.center[2])
        self.transform.Update()
        self.reslice.Update()
        return
    
    # new rotation center for the volume
    def setNewRotationCenter(self,clic_X,clic_Y,mode):
        
        #change the rotation center depending on the view
        if(mode==SAGITAL):
            self.center[0]=clic_X
            self.center[1]=clic_Y
        elif(mode==AXIAL):
            self.center[2]=clic_X
            self.center[1]=clic_Y
        elif(mode==CORONAL):
            self.center[2]=clic_X
            self.center[0]=clic_Y
        return
    
    #get the modificated volume            
    def getOutput(self):
        #returns the volume rotated
        return self.reslice.GetOutput()
    
    #displaces the entire volume
    def displaceVolume(self,displacement,mode):
        #getting spacing of the volume
        spacing=self.volume.GetSpacing()
        
        #doing the displacement depending on the view mode given
        if(mode==SAGITAL):
            translate=self.center[2]+displacement
            self.transform.Translate(0,0,translate*spacing[2])
            self.center[2]=translate
        elif(mode==AXIAL):
            translate=self.center[0]+displacement
            self.transform.Translate(translate*spacing[0],0,0)
            self.center[0]=translate
        elif(mode==CORONAL):
            translate=self.center[1]+displacement
            self.transform.Translate(0,translate*spacing[1],0)
            self.center[1]=translate
            
        #updating the transform and reslice
        self.transform.Update()
        self.reslice.Update()
        return

