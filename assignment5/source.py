#!/usr/bin/env python

import wx

def addButtons(win):
    button1 = wx.Button(win,label="1")
    
    
class calc(wx.Frame):
  
    def __init__(self):
        super(calc, self).__init__(None, title="Calculator", 
            size=(300, 250))
            
        self.drawCalc()
        self.Show()     
        
    def drawCalc(self):

        vbox = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, style=wx.TE_RIGHT)
        vbox.Add(self.display, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=5)
        gridbox = wx.GridSizer(4, 4, 5, 5)

        gridbox.AddMany( [
            (wx.Button(self, label='7'), 0, wx.EXPAND),
            (wx.Button(self, label='8'), 0, wx.EXPAND),
            (wx.Button(self, label='9'), 0, wx.EXPAND),
            (wx.Button(self, label='/'), 0, wx.EXPAND),
            (wx.Button(self, label='4'), 0, wx.EXPAND),
            (wx.Button(self, label='5'), 0, wx.EXPAND),
            (wx.Button(self, label='6'), 0, wx.EXPAND),
            (wx.Button(self, label='*'), 0, wx.EXPAND),
            (wx.Button(self, label='1'), 0, wx.EXPAND),
            (wx.Button(self, label='2'), 0, wx.EXPAND),
            (wx.Button(self, label='3'), 0, wx.EXPAND),
            (wx.Button(self, label='-'), 0, wx.EXPAND),
            (wx.Button(self, label='0'), 0, wx.EXPAND),
            (wx.Button(self, label='.'), 0, wx.EXPAND),
            (wx.Button(self, label='='), 0, wx.EXPAND),
            (wx.Button(self, label='+'), 0, wx.EXPAND) ])

        vbox.Add(gridbox, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)


def main():
    app = wx.App()
    startnew = calc()
    app.MainLoop()
    
    
# Remember to unindent this line!
if __name__ == '__main__':
    main()