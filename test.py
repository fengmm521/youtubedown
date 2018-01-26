#!/usr/bin/env python
#coding:utf-8
"""
  Author:  u"王浩" --<823921498@qq.com>
  Purpose: u"文件夹选择对话框"
  Created: 2014/8/26
"""

# import wx

# isWinSystem = False
# def get_desktop():
#     if isWinSystem:
#         import _winreg
#         key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
#         return _winreg.QueryValueEx(key, "Desktop")[0]
#     else:
#         return '~/'

# print get_desktop()

# ###############################################################################
# class DirDialog(wx.Frame):
#     """"""

#     #----------------------------------------------------------------------
#     def __init__(self):
#         """Constructor"""
#         wx.Frame.__init__(self,None,-1,u"文件夹选择对话框")
#         b = wx.Button(self,-1,u"文件夹选择对话框")
#         self.Bind(wx.EVT_BUTTON, self.OnButton, b)
        
#     #----------------------------------------------------------------------
#     def OnButton(self, event):
#         """"""
#         dlg = wx.DirDialog(self,u"选择文件夹",style=wx.DD_DEFAULT_STYLE)
#         if dlg.ShowModal() == wx.ID_OK:
#             print dlg.GetPath() #文件夹路径
            
#         dlg.Destroy()

# ###############################################################################
# if __name__ == '__main__':
#     frame = wx.PySimpleApp()
#     app = DirDialog()
#     app.Show()
#     frame.MainLoop()
    
import os

count = 10

def func0(p):
    if p == 0:
        yield 100
    else:
        index = 0
        while  True:
            index += 1
            if index >= count:
                break
            yield index

a = [1]

def func1():
    if a[0] == 1:
        a[0] = 0
        return func0(0)
    else:
        return func0(1)


def test():
    size = os.path.getsize('audio/audio.mp4')

    print size

    # try:
    #     try:
    #         a = 1/0.0
    #     except Exception as e1:
    #         print '1',e1
    # except Exception as e2:
    #     print '2',e2
if __name__ == '__main__':
    # for x in func1():
    #     if x == 100:
    #         print x
    #         continue
    test()
