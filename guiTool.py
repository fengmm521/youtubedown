#!/usr/bin/env python
#coding:UTF-8
import wx  
  
class TextFrame(wx.Frame):  
  
    def __init__(self):  
        wx.Frame.__init__(self, None, -1, 'Text Entry Example',   
                size=(860, 520))  
        panel = wx.Panel(self, -1)   
        multiLabel = wx.StaticText(panel, -1, "youtube下载页面网址:")  
        multiText = wx.TextCtrl(panel, -1,  
               "Here is a looooooooooooooong line of text set in the control.\n"  
               "See that it wrapped, and that this line is after a blank",  
               size=(700, 300), style=wx.TE_MULTILINE) #创建一个文本控件  
        multiText.SetInsertionPoint(0) #设置插入点  
  
        btn = wx.Button(panel,label='开始下载',pos=(10,50),size = (100,50))

        self.Bind(wx.EVT_BUTTON,self.OnDownload,btn)

        richLabel = wx.StaticText(panel, -1, "下载祥情:")  
        richText = wx.TextCtrl(panel, -1,   
                "If supported by the native control, this is reversed, and this is a different font.",  
                size=(700, 150), style=wx.TE_MULTILINE) #创建丰富文本控件  
        richText.SetInsertionPoint(0)  
        richText.SetStyle(44, 52, wx.TextAttr("white", "black")) #设置文本样式  
        points = richText.GetFont().GetPointSize()   
        f = wx.Font(points + 3, wx.ROMAN, wx.ITALIC, wx.BOLD, True) #创建一个字体  
        richText.SetStyle(68, 82, wx.TextAttr("blue", wx.NullColour, f)) #用新字体设置样式  
        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)  
        sizer.AddMany([multiLabel, multiText, richLabel, richText])  
        panel.SetSizer(sizer)  

        print multiText.GetLabel()

    def OnDownload(self,weburl):
        print 'start download'
  
    def downloadOK(self,msg):
        print msg

if __name__ == '__main__':  
    app = wx.PySimpleApp()  
    frame = TextFrame()  
    frame.Show()  
    app.MainLoop()  