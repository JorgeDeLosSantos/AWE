# -*- coding: utf-8 -*-
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