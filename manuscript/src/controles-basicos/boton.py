# -*- coding: utf-8 -*-
import wx
import random

class MiFrame(wx.Frame):
    def __init__(self,parent,**kwargs):
        wx.Frame.__init__(self,parent=parent,**kwargs)
        self.sz = wx.BoxSizer(wx.VERTICAL)
        
        self.bt = wx.Button(self, -1, u"Cambiar color")
        self.sz.Add(self.bt, 0, wx.ALIGN_CENTER)
        
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.bt)
        
        self.SetSizer(self.sz)
        self.Show()

    def OnClick(self,event):
        """
        Cambia el color de la ventana de manera aleatoria
        """
        clr = [random.randint(0,255) for k in range(3)] # RGB
        self.SetBackgroundColour(clr)
        self.Refresh() # Actualizar/


if __name__=='__main__':
    app = wx.App()
    frame = MiFrame(None, title=u"wxButton Demo", size=(300,200))
    app.MainLoop()

