# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 13:33:00 2019

@author: Miguel Sánchez Cervantes

This class make a slice of the volume given (sagital, CORONAL, AXIAL)

constants
    SAGITAL,CORONAL And AXIAL are constant for 2D mode view
    sagitalElements, AXIALElements, CORONALElements are matrixes to make the slices of the volume
    X,Y,Z are the axes in which the object will rotate
    
Attributes
    sliceMode saves the type of slice of this object

    spacing,origin and dimensions save attributes of the volume that we want to slice
    centerSlice, positionCenter, rotCenter set the rotation center of the volume
    
    displayVolume save the image data of the volume
    resliceAxes save the 2D mode view Matrix
    reslicer is the object which make the slice
    transform is the object which define the transform for the reslicer

    angleX,Y and Z save the current angle of the object
    
    centerRef,centerRefMapper,centerRefActor.These attributes show the center of the slice.
    
methods
    setSlicesData()
        This method recieves 2 parameters: 
            volume_data, it is the data of the volume
            mode, it is the 2D view slice wanted to be displayed (CORONAL, AXIAL or sagital)
        This method sets attribute values of the class
        
    configView()
        This method recieves 1 parameter: mode, which is the slice type to make
        
        This method makes the slice.
        
    getOutput()
        This method returns the image data of the slice.
        
    rotate()
        This method recieves a 2 integer variables (an angle and an axis) as parameters.
        The slice will rotate in that axis the given angle. 
    
    getCenterRef()
        This method return de Actor of the rotation center point.
        
    setNewRotationCenter()
        This method recieves 2 float variables as parameters, a X and Y coordenates.
        It changes the rotation center of the slice and redraws the rotation center point in the new position
        
    setNewSliceSource()
        This method recieves a vtkImageData object as parameter.
        it changes the volume source to make the slice and updates the reslicer.
        
    displaceSlice()
        This method recieves a float parameter, the displacement.
        It Displaces the slice in its depth axis:
            Z for Sagital, X for Axial and Y for Coronal
"""
import vtk
import math

SAGITAL = 0
CORONAL = 2
AXIAL = 1
X=0
Y=1
Z=2

sagitalElements=[
        1,0,0,0,
        0,1,0,0,
        0,0,1,0,
        0,0,0,1
        ]

axialElements=[
        0,0,1,0,
        1,0,0,0,
        0,1,0,0,
        0,0,0,1
        ]

coronalElements=[
        1,0,0,0,
        0,0,1,0,
        0,1,0,0,
        0,0,0,1
        ]

class Slicer:
    
    def __init__(self):
        #the type of the slice
        self.sliceMode=0
        #save properties of the volume
        self.spacing=[]
        self.origin=[]
        self.dimensions=[]
        #save properties of the slice
        self.centerSlice=[]
        self.positionCenter=[]
        self.rotCenter=[]
        #data of the volume
        self.displayVolume=vtk.vtkImageData()
        
        #vtk objects to make the slice
        self.resliceAxes=vtk.vtkMatrix4x4()
        self.reslicer=vtk.vtkImageReslice()
        self.transform=vtk.vtkTransform()
        
        #save angles of rotation of the slice in each axes
        self.angleX=0
        self.angleY=0
        self.angleZ=0
        
        #visual reference for the rotation center
        self.centerRef=vtk.vtkRegularPolygonSource()
        self.centerRefMapper=vtk.vtkPolyDataMapper()
        self.centerRefActor=vtk.vtkActor()
        
        #
        self.sliceDisplacement=0
        
    #method that make the slice   
    def configView(self):
        
        #initialzing rotation center
        self.rotCenter.clear()
        self.rotCenter.append(self.positionCenter[1 if self.sliceMode==AXIAL else 0]-self.origin[1 if self.sliceMode==AXIAL else 0])
        self.rotCenter.append(self.positionCenter[1 if self.sliceMode==SAGITAL else 2]-self.origin[1 if self.sliceMode==SAGITAL else 2])
        
        #initializing slicer data
        self.transform.PostMultiply()
        
            #array to set the translate parameters depending on the mode chosed
        translate_array=[]
        translate_array.append(self.positionCenter[0] if self.sliceMode==AXIAL else self.origin[0])
        translate_array.append(self.positionCenter[1] if self.sliceMode==CORONAL else self.origin[1])
        translate_array.append(self.positionCenter[2] if self.sliceMode==SAGITAL else self.origin[2])
        
        self.transform.Translate(translate_array[0],translate_array[1],translate_array[2])
            #maping the 2D view Matrix with the mode and copying into resliceAxes
        switcher={
                0:sagitalElements,
                1:axialElements,
                2:coronalElements
                }
        self.resliceAxes.DeepCopy(switcher.get(self.sliceMode,lambda:sagitalElements))
        
        #making the slice
        self.reslicer.SetInputData(self.displayVolume)
        self.reslicer.SetOutputDimensionality(2)
        self.reslicer.SetResliceAxes(self.resliceAxes)
        self.reslicer.SetResliceTransform(self.transform)
        self.reslicer.SetInterpolationModeToCubic()
        self.reslicer.Update()
        
        #setting visual reference for rotation center
        self.centerRef.SetNumberOfSides(50)
        self.centerRef.SetRadius(0.5)
        self.centerRef.SetCenter(self.rotCenter[0],self.rotCenter[1],1)
        
        self.centerRefMapper.SetInputConnection(self.centerRef.GetOutputPort())
        self.centerRefActor.SetMapper(self.centerRefMapper)
        self.centerRefActor.GetProperty().SetColor(1.0,0.59,0.08)
        self.centerRefMapper.Update()
        
        return
    
    #return the vtkImageData of the slice
    def getOutput(self):
        self.reslicer.Update()
        return self.reslicer.GetOutput()
    
    #return the center reference point 
    def getCenterRef(self):
        return self.centerRefActor
    
    #set new rotation center for the slice 
    def setNewRotationCenter(self,clic_X,clic_Y):
        #change rotation center in selected view
        self.rotCenter[0]=clic_X
        self.rotCenter[1]=clic_Y
        
        #change rotation center in selected view
        self.centerRef.SetCenter(self.rotCenter[0],self.rotCenter[1],1)
        self.centerRefMapper.Update()
        
        return
    #set a new volume to make the slice
    def setNewSliceSource(self,volume_data):
        self.displayVolume.DeepCopy(volume_data)
        self.reslicer.Update()
        return
    #set the volume and the view mode to make the slice
    def setSlicesData(self,volume_data,mode):
        #setting volume data and the slice type
        self.displayVolume.DeepCopy(volume_data)
        self.sliceMode=mode
        
        #getting volume properties
        self.spacing=self.displayVolume.GetSpacing()
        self.origin=self.displayVolume.GetOrigin()
        self.dimensions=self.displayVolume.GetDimensions()
        
        #setting center of volume
        self.centerSlice.clear()
        self.centerSlice.append(math.floor(self.dimensions[0]*0.5)-1)
        self.centerSlice.append(math.floor(self.dimensions[1]*0.5)-1)
        self.centerSlice.append(math.floor(self.dimensions[2]*0.5)-1)
        
        self.positionCenter.clear()
        self.positionCenter.append(self.origin[0]+self.spacing[0]*self.centerSlice[0])
        self.positionCenter.append(self.origin[1]+self.spacing[1]*self.centerSlice[1])
        self.positionCenter.append(self.origin[2]+self.spacing[2]*self.centerSlice[2])
        
        #setting the displacement reference of the slice
        self.sliceDisplacement=self.centerSlice [(mode+2)%3]
        
        #configuration of 2D views
        self.configView()
        
        return
    
    #rotate the slice
    def rotate(self,angle,axis):
        
        #set the translate method array input
        index_temp_1=1 if self.sliceMode==SAGITAL else 0; #this variable helps to set the value of the translate array depending on the slice mode of the object
        translate_array=[]
        translate_array.append(self.sliceDisplacement*self.spacing[0] if self.sliceMode==AXIAL else self.rotCenter[0])
        translate_array.append(self.sliceDisplacement*self.spacing[1] if self.sliceMode==CORONAL else self.rotCenter[index_temp_1])
        translate_array.append(self.sliceDisplacement*self.spacing[2] if self.sliceMode==SAGITAL else self.rotCenter[1])
        
        #rotate slice
        self.transform.Translate(-translate_array[0],-translate_array[1],-translate_array[2])
            #rotating depending on the axis given
        if(axis==X):
            rotate = angle - self.angleX
            self.transform.RotateX(rotate)
            self.angleX=angle
        elif(axis==Y):
            rotate = angle - self.angleY
            self.transform.RotateY(rotate)
            self.angleY=angle
        elif(axis==Z):
            rotate = angle - self.angleZ
            self.transform.RotateZ(rotate)
            self.angleZ=angle
            
        self.transform.Translate(translate_array[0],translate_array[1],translate_array[2])
        
        self.reslicer.Update()
        return
    
    #displace the slice
    def displaceSlice(self,displacement):
        #change the slice displacement reference
        translate= displacement - self.sliceDisplacement
        
            #do the translate matrix depending on the slice mode
        if(self.sliceMode==SAGITAL):
            self.transform.Translate(0,0,translate*self.spacing[2])
        elif(self.sliceMode==AXIAL):
            self.transform.Translate(translate*self.spacing[0],0,0)
        elif(self.sliceMode==CORONAL):
            self.transform.Translate(0,translate*self.spacing[1],0)
        
        self.sliceDisplacement= displacement
        self.transform.Update()
        self.reslicer.Update()
        return