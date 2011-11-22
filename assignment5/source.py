#!/usr/bin/env python

import wx
    
    
class calc(wx.Frame):
  
    def __init__(self):
        super(calc, self).__init__(None, title="SVCalc", size=(300, 250))
        self.drawCalc()
        self.Show()     
    
    def pushb0:
        display.SetValue("0")
        # also need to create the part that does the math
    b1 = (wx.Button(self, label='1'), 0, wx.EXPAND)
    b2 = (wx.Button(self, label='2'), 0, wx.EXPAND)
    b3 = (wx.Button(self, label='3'), 0, wx.EXPAND)
    b4 = (wx.Button(self, label='4'), 0, wx.EXPAND)
    b5 = (wx.Button(self, label='5'), 0, wx.EXPAND)
    b6 = (wx.Button(self, label='6'), 0, wx.EXPAND)
    b7 = (wx.Button(self, label='7'), 0, wx.EXPAND)
    b8 = (wx.Button(self, label='8'), 0, wx.EXPAND)
    b9 = (wx.Button(self, label='9'), 0, wx.EXPAND)
    b0 = (wx.Button(self, label='0'), 0, wx.EXPAND)
    bdivide = (wx.Button(self, label='/'), 0, wx.EXPAND)
    bmultiply = (wx.Button(self, label='*'), 0, wx.EXPAND)
    bsubtract = (wx.Button(self, label='-'), 0, wx.EXPAND)
    bdecimal = (wx.Button(self, label='.'), 0, wx.EXPAND)
    bequals = (wx.Button(self, label='='), 0, wx.EXPAND)
    badd = (wx.Button(self, label='+'), 0, wx.EXPAND)
    
    
    def drawCalc(self):

        vbox = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, style=wx.TE_RIGHT)
        vbox.Add(self.display, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=5)
        gridbox = wx.GridSizer(4, 4, 5, 5)
        
        # Create buttons - I hate this
        b0 = (wx.Button(self, label='0'), 0, wx.EXPAND)
        b1 = (wx.Button(self, label='1'), 0, wx.EXPAND)
        b2 = (wx.Button(self, label='2'), 0, wx.EXPAND)
        b3 = (wx.Button(self, label='3'), 0, wx.EXPAND)
        b4 = (wx.Button(self, label='4'), 0, wx.EXPAND)
        b5 = (wx.Button(self, label='5'), 0, wx.EXPAND)
        b6 = (wx.Button(self, label='6'), 0, wx.EXPAND)
        b7 = (wx.Button(self, label='7'), 0, wx.EXPAND)
        b8 = (wx.Button(self, label='8'), 0, wx.EXPAND)
        b9 = (wx.Button(self, label='9'), 0, wx.EXPAND)
        b0 = (wx.Button(self, label='0'), 0, wx.EXPAND)
        bdivide = (wx.Button(self, label='/'), 0, wx.EXPAND)
        bmultiply = (wx.Button(self, label='*'), 0, wx.EXPAND)
        bsubtract = (wx.Button(self, label='-'), 0, wx.EXPAND)
        bdecimal = (wx.Button(self, label='.'), 0, wx.EXPAND)
        bequals = (wx.Button(self, label='='), 0, wx.EXPAND)
        badd = (wx.Button(self, label='+'), 0, wx.EXPAND)
        
        # Add buttons to grid, in order
        gridbox.AddMany( [b7, b8, b9, bdivide, b4, b5, b6, bmultiply, b1, b2, b3, bsubtract, b0, bdecimal, bequals, badd] )
        
        # Add gridbox to the background
        vbox.Add(gridbox, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)
        
        # Start binding events - I also hate this
        

def main():
    app = wx.App()
    startnew = calc()
    app.MainLoop()
    
    
# Remember to unindent this line!
if __name__ == '__main__':
    main()