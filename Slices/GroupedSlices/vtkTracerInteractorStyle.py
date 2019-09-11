
import vtk

class TracerInteractorStyle(vtk.vtkInteractorStyleImage):
    def __init__(self):
        super().__init__()
        self.Tracer=vtk.vtkImageTracerWidget()
        self.Tracer.GetLineProperty().SetLineWidth(1)
        self.Tracer.AddObserver(self.OnLeftButtonDown(),vtk.vtkCommand().EndInteractionEvent,1)
        return
    
    def catchEvent(self,):
    

c=TracerInteractorStyle()

