#!/usr/bin/env python

import wx

def load(event):
  f = open(filename.GetValue())
  contents.SetValue(f.read())
  f.close()
def save(event):
  f = open(filename.GetValue(), 'w')
  f.write(contents.GetValue())
  f.close()


def main():
  app = wx.App()
  win = wx.Frame(None,title="Simple Editor", size=(410,335))
  bkg = wx.Panel(win)
  
  loadButton = wx.Button(bkg, label = "Open")
  loadButton.Bind(wx.EVT_BUTTON, load)
  
  saveButton = wx.Button(bkg, label = "Save")
  saveButton.Bind(wx.EVT_BUTTON, save)
  
  filename = wx.TextCtrl(bkg)
  contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE|wx.HSCROLL)
  
  hbox = wx.BoxSizer()
  hbox.Add(filename, proportion=1, flag=wx.EXPAND)
  hbox.Add(loadButton, proportion=0, flag=wx.LEFT, border=5)
  hbox.Add(saveButton, proportion=0, flag=wx.LEFT, border=5)
  
  vbox = wx.BoxSizer(wx.VERTICAL)
  vbox.Add(hbox, proportion=0, flag=wx.EXPAND|wx.ALL, border=5)
  vbox.Add(contents, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT, border=5)
  
  bkg.SetSizer(vbox)
  win.Show()
  app.MainLoop()
  
# Remember to unindent this line!
if __name__ == '__main__':
  main()