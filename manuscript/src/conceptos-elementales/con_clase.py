# -*- coding: utf-8 -*-
import wx

class MiFrame(wx.Frame):
    def __init__(self,parent,**kwargs):
        wx.Frame.__init__(self,parent=parent,**kwargs)
        self.Show()

class App(wx.App):
    def OnInit(self):
        frame = MiFrame(None, u"wxFrame Demo")
        return True


if __name__=='__main__':
    app = wx.App()
    frame = MiFrame(None, title=u"wxFrame Demo")
    app.MainLoop()