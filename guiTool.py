#!/usr/bin/env python
#coding:UTF-8
import wx  

#wxFormBuilder用法：http://www.yiibai.com/wxpython/wxpython_gui_builder_tools.html

#wxPython所有控件说明:http://www.yiibai.com/wxpython/wxpython_major_classes.html
  
class TextFrame(wx.Frame):  
  
    def __init__(self):  
        wx.Frame.__init__(self, None, -1, 'Text Entry Example',   
                size=(300, 250))  
        panel = wx.Panel(self, -1)   

        #对话框用法:http://www.yiibai.com/wxpython/wx_dialog_class.html

        #StaticText用法:http://www.yiibai.com/wxpython/wx_statictext_class.html
        multiLabel = wx.StaticText(panel, -1, "Multi-line")  
        #TextCtrl用法:http://www.yiibai.com/wxpython/wx_textctrl_class.html
        multiText = wx.TextCtrl(panel, -1,  
               "Here is a looooooooooooooong line of text set in the control.\n\n"  
               "See that it wrapped, and that this line is after a blank",  
               size=(200, 100), style=wx.TE_MULTILINE) #创建一个文本控件  
        multiText.SetInsertionPoint(0) #设置插入点  
  
        richLabel = wx.StaticText(panel, -1, "Rich Text")  
        richText = wx.TextCtrl(panel, -1,   
                "If supported by the native control, this is reversed, and this is a different font.",  
                size=(200, 100), style=wx.TE_MULTILINE|wx.TE_RICH2) #创建丰富文本控件  
        richText.SetInsertionPoint(0)  
        richText.SetStyle(44, 52, wx.TextAttr("white", "black")) #设置文本样式  
        points = richText.GetFont().GetPointSize()   
        f = wx.Font(points + 3, wx.ROMAN, wx.ITALIC, wx.BOLD, True) #创建一个字体  
        richText.SetStyle(68, 82, wx.TextAttr("blue", wx.NullColour, f)) #用新字体设置样式  
        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)  
        sizer.AddMany([multiLabel, multiText, richLabel, richText])  
        panel.SetSizer(sizer)  
  
if __name__ == '__main__':  
    app = wx.PySimpleApp()  
    frame = TextFrame()  
    frame.Show()  
    app.MainLoop()  