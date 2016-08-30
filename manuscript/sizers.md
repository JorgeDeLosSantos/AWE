# Los sizers: organizando controles

En este capítulo veremos cómo posicionar y organizar los controles mediante 
el uso de sizers, los cuales son mecanismos de distribución automática de 
controles gráficos mediante algoritmos de posicionamiento.

## Posicionamiento absoluto

El *posicionamiento absoluto* es la manera más sencilla para posicionar 
y organizar controles dentro de una interfaz gráfica de wxPython. Esto 
consiste en manejar de forma manual el tamaño y posición de los controles 
mediante las propiedades `size` y `pos`,  respectivamente. Revise el siguiente 
ejemplo.

    import wx

    class MiFrame(wx.Frame):
        def __init__(self,parent,**kwargs):
            wx.Frame.__init__(self,parent=parent,**kwargs)
            self.bt1 = wx.Button(self, -1, u"Botón 1", pos=(50,60), size=(100,20))
            self.bt2 = wx.Button(self, -1, u"Botón 2", pos=(50,120), size=(100,20))
            self.Show()

    if __name__=='__main__':
        app = wx.App()
        frame = MiFrame(None, title=u"Posicionamiento absoluto", size=(300,200))
        app.MainLoop()


Puede notar que a los *keyword arguments* `pos` y `size` se les pasa una tupla de 
dos elementos, que indican las coordenadas *x* e *y* del extremo superior izquierdo 
del control gráfico en el caso de la posición, y el ancho y alto del mismo en el caso del tamaño, 
siendo en ambos casos pixeles las unidades de medida.