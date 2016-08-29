#Boa:Frame:Frame1
#coding=UTF-8
import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1PANEL1, 
] = [wx.NewId() for _init_ctrls in range(3)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(504, 209), size=wx.Size(230, 320),
              style=wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX),
              title='\xcd\xbc\xc6\xac\xc3\xdc\xd4\xbf\xd0\xc5\xcf\xa2')
        self.SetClientSize(wx.Size(214, 282))
        self.SetTransparent(220)
        self.SetBackgroundColour(wx.Colour(24,24,24))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(214, 282),
              style=wx.TAB_TRAVERSAL)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1,
              label='\xcc\xed\xbc\xd3\xc3\xdc\xd4\xbf', name='button1',
              parent=self.panel1, pos=wx.Point(56, 16), size=wx.Size(100, 255),
              style=wx.NO_BORDER)
        self.button1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              ''))

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.SetTransparent(220)
        self.SetBackgroundColour(wx.Colour(24,24,24))
        self.button1.SetBackgroundColour(wx.Colour(24,24,24))
        self.button1.SetBitmap(wx.Bitmap("key.png"));
        wx.MessageBox("请务必保存好图片密钥，它位于程序文件夹 key.png",'程序密钥',wx.OK|wx.ICON_INFORMATION)