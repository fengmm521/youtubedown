#!/usr/bin/env python
#coding:utf-8
"""
  Author:  u"王浩" --<823921498@qq.com>
  Purpose: u"文件夹选择对话框"
  Created: 2014/8/26
"""

import wx

isWinSystem = False
def get_desktop():
    if isWinSystem:
        import _winreg
        key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
        return _winreg.QueryValueEx(key, "Desktop")[0]
    else:
        return '~/'

print get_desktop()

###############################################################################
class DirDialog(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self,None,-1,u"文件夹选择对话框")
        b = wx.Button(self,-1,u"文件夹选择对话框")
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)
        
    #----------------------------------------------------------------------
    def OnButton(self, event):
        """"""
        dlg = wx.DirDialog(self,u"选择文件夹",style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            print dlg.GetPath() #文件夹路径
            
        dlg.Destroy()

###############################################################################
if __name__ == '__main__':
    frame = wx.PySimpleApp()
    app = DirDialog()
    app.Show()
    frame.MainLoop()
    