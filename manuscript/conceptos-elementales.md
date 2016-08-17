{mainmatter}

# Lo básico

## Una primera aplicación

Una aplicación muy básica en wxPython puede construirse con unas pocas líneas:

    import wx

    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, u"wxPython Demo")
    frame.Show()
    app.MainLoop()

![Imagen 01](images/conceptos-elementales/primera_aplicacion.png)

Primero, y como siempre, importamos la librería wxPython para poder utilizar 
las clases y funciones disponibles en esta. 

Posteriormente se debe instanciar un objeto de la clase `wx.App`, que representa 
a la aplicación por si misma. La clase `wx.App` se utiliza para inicializar 
el sistema de wxPython y todo el conjunto de interfaces gráficas, además de controlar 
el intercambio de información y el manejo de los eventos lanzados. 
Cada aplicación debe tener una instancia `wx.App`, y esta debe crearse antes de 
instanciar cualquier otro objeto gráfico de wxPython, para asegurar que el 
sistema de wxWidgets se ha inicializado correctamente [^wxapp]. Es más, si en el ejemplo 
anterior intenta inicializar el Frame antes de `wx.App`, entonces wxPython lanzará un 
error como el que se muestra enseguida (*el cual es bastante explícito*):

{linenos=off}
    Traceback (most recent call last):
      File "C:\Users\adminIS\Desktop\LABPro\_books_\PB1703 - AWE\AWE\manuscript\src\
    conceptos-elementales\primera_aplicacion.py", line 4, in <module>
        frame = wx.Frame(None, wx.ID_ANY, u"wxPython Demo")
      File "C:\Python27\lib\site-packages\wx-2.9.5-msw\wx\_windows.py", line 580, in
     __init__
        _windows_.Frame_swiginit(self,_windows_.new_Frame(*args, **kwargs))
    wx._core.PyNoAppError: The wx.App object must be created first!

[^wxapp]: https://wxpython.org/docs/api/wx.App-class.html


## Con clase

Bla bla bla 
