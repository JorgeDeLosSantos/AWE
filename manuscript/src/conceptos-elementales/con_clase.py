# -*- coding: utf-8 -*-
import wx

class MiFrame(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent=parent,id=wx.ID_ANY,title=title)
        self.Show()

class App(wx.App):
    def OnInit(self):
        frame = MiFrame(None, u"wxFrame Demo")
        return True


if __name__=='__main__':
    app = App()
    frame = MiFrame(None, u"wxFrame Demo")
    app.MainLoop()