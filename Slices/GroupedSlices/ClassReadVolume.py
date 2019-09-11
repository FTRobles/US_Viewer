# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 12:57:47 2019

@author: Miguel Sánchez Cervantes

This class open and read the volume file. It opens .vol and .mhd files.

attributes:
    filename saves the name of the file to be open
    volume is the image data of the volume
methods:
    setFilename()
        recieves a string as parameter and sets it as filename
    openVol()
        open and read a .vol file, then save the vtkImageData object in "volume" attribute
    openMHD()
        open and read a .mhd file, then save the vtkImageData object in "volume" attribute
    getOutput()
        returns the vtkImageData object that contains the data of the volume
"""
import vtk
import struct
import os.path as path

class ReadVolume():
    def __init__(self):
        #attributes
        self.filename="" 
        self.volume=vtk.vtkImageData()
        return
    
    def setFilename(self,str_filename):
        self.filename=str_filename
        return
    
    def openVol(self):
        if path.exists(self.filename):
            #open the file
            fd=open(self.filename,'rb')
            
            #read the file
            data_buffer=fd.read()
            
            #First tag si in first 14 bits
            file_format=data_buffer[0:13].decode("utf-8")
            print("Format: "+file_format)
            
            #search for ffff04000000, where important info begin
            positions=[]
            ind=0;
            for x in data_buffer:
                if x==255:
                    positions.append(ind)
                ind+=1
                
            #vector with position of ffff04000000 tag
            vector_posi=[]
            for x in positions:
                if ((data_buffer[x+1]==255)and(data_buffer[x+2]==4)and(data_buffer[x+3]==0)
                and(data_buffer[x+4]==0)and(data_buffer[x+5]==0)):
                    vector_posi.append(x)
            
            #Get manufacturer info
            manufacturer=data_buffer[vector_posi[2]+42:vector_posi[2]+56].decode("8859")
            print("Manufacturer: "+manufacturer)
            
            #Get index for patient and institute data
            vector_study=[]
            index=vector_posi[3]+6
            cont=0
            
            while(cont<4):
                #search for 000000 or 001001
                if (((data_buffer[index]==0)and(data_buffer[index+1]==0)and
                    (data_buffer[index+2]==0))or((data_buffer[index]==0)and
                    (data_buffer[index+1]==16)and (data_buffer[index+2]==1))):
                    vector_study.append(index)
                    cont+=1
                index+=1
                
            vector_inst=[]
            index=vector_posi[4]+6
            cont=0
            
            while(cont<2):
                 #search for 000000 or 002001
                 if (((data_buffer[index]==0)and(data_buffer[index+1]==0)and
                    (data_buffer[index+2]==0))or((data_buffer[index]==0)and
                    (data_buffer[index+1]==32)and (data_buffer[index+2]==1))):
                    vector_inst.append(index)
                    cont+=1
                 index+=1
                     
            #get patient and institute data
            patient_id = data_buffer[vector_study[0]+3:vector_study[1]].decode("utf-8")
            patient_name = data_buffer[vector_study[2]+3:vector_study[3]].decode("utf-8")
            institute_name = data_buffer[vector_inst[0]+3:vector_inst[1]].decode("utf-8")
            gems=data_buffer[vector_posi[6]+18:vector_posi[6]+35].decode("utf-8")
            
            print("Patient ID: "+patient_id)
            print("Patient Name: "+patient_name)
            print("Institute Name: "+institute_name)
            print("GEMS: "+gems)
            
            #init codes x,y,z
            index=vector_posi[10]+6
            cont=0
             
            while(cont<5):
                
                #x init code 0 192 1 0 2 0 0 0
                if((data_buffer[index]==0)and(data_buffer[index+1]==192)and(data_buffer[index+2]==1)
                and(data_buffer[index+3]==0)and(data_buffer[index+4]==2)and(data_buffer[index+5]==0)
                and(data_buffer[index+6]==0)and(data_buffer[index+7]==0)):
                    
                    x=data_buffer[index+8]+(data_buffer[index+9]*256)#Calculate value of x
                    
                    print(x)
                    cont+=1
                    
                #y init code 0 192 2 0 2 0 0 0
                if((data_buffer[index]==0)and(data_buffer[index+1]==192)and(data_buffer[index+2]==2)
                and(data_buffer[index+3]==0)and(data_buffer[index+4]==2)and(data_buffer[index+5]==0)
                and(data_buffer[index+6]==0)and(data_buffer[index+7]==0)):
                    
                    y=data_buffer[index+8]+(data_buffer[index+9]*256)#Calculate value of y
                    
                    print(y)
                    cont+=1
                    
                #z init code 0 192 1 0 2 0 0 0
                if((data_buffer[index]==0)and(data_buffer[index+1]==192)and(data_buffer[index+2]==3)
                and(data_buffer[index+3]==0)and(data_buffer[index+4]==2)and(data_buffer[index+5]==0)
                and(data_buffer[index+6]==0)and(data_buffer[index+7]==0)):
                    
                    z=data_buffer[index+8]+(data_buffer[index+9]*256)#Calculate value of z
                    
                    print(z)
                    cont+=1
                    
                #voxel size init code 0 193 1 0 8 0 0 0
                if((data_buffer[index]==0)and(data_buffer[index+1]==193)and(data_buffer[index+2]==1)
                and(data_buffer[index+3]==0)and(data_buffer[index+4]==8)and(data_buffer[index+5]==0)
                and(data_buffer[index+6]==0)and(data_buffer[index+7]==0)):
                    
                    vox_size=struct.unpack('d', data_buffer[index+8:index+16])[0]*1000
                    print(vox_size)
                    cont+=1
                
                #Volume size init code 0 208 1 0
                if((data_buffer[index]==0)and(data_buffer[index+1]==208)and(data_buffer[index+2]==1)
                and(data_buffer[index+3]==0)):
                    
                    vol_size=struct.unpack('i',data_buffer[index+4:index+8])[0]

                    print(vol_size)
                    cont+=1
                
                index+=1
                
            #extracting volume data
            vol=data_buffer[index+7:index+vol_size +7]
    
                
            #creating the vtk volume
            self.volume.SetExtent(0,x,0,y,0,z)
            self.volume.SetSpacing(vox_size,vox_size,vox_size)
            self.volume.SetOrigin(0,0,0)
            self.volume.AllocateScalars(3,1)
            
            pointData=vtk.vtkUnsignedCharArray()
            pointData.SetNumberOfComponents(1)
            
            pix=0
            for k in range(0,z):
                for j in range(y-1,-1,-1):
                    for i in range(0,x):
                        self.volume.SetScalarComponentFromFloat(i,j,k,0,vol[pix])
                        pix+=1
            
        else:
            print("Incorrect filename")
        
        return
    
    def openMHD(self):
        reader=vtk.vtkMetaImageReader()
        reader.SetFileName(self.filename)
        reader.Update()
        self.volume.DeepCopy(reader.GetOutput())
        return
    
    def getOutput(self):
        return self.volume
