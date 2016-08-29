#Boa:Frame:Frame1
#coding=utf-8
import wx
    
def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON_ADD, wxID_FRAME1BUTTON_KEY, 
 wxID_FRAME1BUTTON_VIEW, wxID_FRAME1PANEL1, wxID_FRAME1PASSWORD, 
 wxID_FRAME1SELECT_INFO, wxID_FRAME1USERNAME, 
] = [wx.NewId() for _init_ctrls in range(8)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(506, 252), size=wx.Size(294, 252),
              style=wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX),
              title='\xb9\xa6\xc4\xdc\xb2\xcb\xb5\xa5')
        self.SetClientSize(wx.Size(278, 214))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(278, 214), style=0)

        self.button_add = wx.Button(id=wxID_FRAME1BUTTON_ADD, label='',
              name='button_add', parent=self.panel1, pos=wx.Point(16, 120),
              size=wx.Size(96, 80), style=wx.NO_BORDER)
        self.button_add.Bind(wx.EVT_MOUSE_EVENTS, self.OnButton_addMouseEvents)
        self.button_add.Bind(wx.EVT_LEFT_UP, self.OnButton_addLeftUp)

        self.button_key = wx.Button(id=wxID_FRAME1BUTTON_KEY, label='',
              name='button_key', parent=self.panel1, pos=wx.Point(168, 120),
              size=wx.Size(96, 80), style=wx.NO_BORDER)
        self.button_key.Bind(wx.EVT_MOUSE_EVENTS, self.OnButton_keyMouseEvents)
        self.button_key.Bind(wx.EVT_LEFT_UP, self.OnButton_keyLeftUp)

        self.button_view = wx.Button(id=wxID_FRAME1BUTTON_VIEW, label='',
              name='button_view', parent=self.panel1, pos=wx.Point(88, 24),
              size=wx.Size(112, 80), style=wx.NO_BORDER)
        self.button_view.Bind(wx.EVT_MOUSE_EVENTS,
              self.OnButton_viewMouseEvents)
        self.button_view.Bind(wx.EVT_LEFT_UP, self.OnButton_viewLeftUp)

        self.select_info = wx.StaticText(id=wxID_FRAME1SELECT_INFO,
              label='         ', name='select_info', parent=self.panel1,
              pos=wx.Point(48, 8), size=wx.Size(192, 14),
              style=wx.ALIGN_CENTRE)
        self.select_info.SetForegroundColour(wx.Colour(255, 255, 0))

        self.username = wx.TextCtrl(id=wxID_FRAME1USERNAME, name='username',
              parent=self.panel1, pos=wx.Point(32, 240), size=wx.Size(100, 22),
              style=0, value='username')

        self.password = wx.TextCtrl(id=wxID_FRAME1PASSWORD, name='password',
              parent=self.panel1, pos=wx.Point(160, 240), size=wx.Size(100, 22),
              style=0, value='password')

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.SetTransparent(220)
        self.SetBackgroundColour(wx.Colour(24,24,24))
        self.button_add.SetBackgroundColour(wx.Colour(24,24,24))
        self.button_add.SetBitmap(wx.Bitmap("button-add.png"));
        self.button_key.SetBackgroundColour(wx.Colour(24,24,24))
        self.button_key.SetBitmap(wx.Bitmap("button-unlock.png"));
        self.button_view.SetBackgroundColour(wx.Colour(24,24,24))
        self.button_view.SetBitmap(wx.Bitmap("button-view.png"));

    def OnButton_addMouseEvents(self, event):
        self.select_info.Label="添加密码记录";
        event.Skip()

    def OnButton_viewMouseEvents(self, event):
        self.select_info.Label="查看密码记录";
        event.Skip()

    def OnButton_keyMouseEvents(self, event):
        self.select_info.Label="解析密钥信息";
        event.Skip()

    def OnButton_addLeftUp(self, event):
        import AddPassInfo;
        Frame_add=AddPassInfo.create(None);
        Frame_add.loginusername.Value=self.username.Value;
        Frame_add.loginpassword.Value=self.password.Value;
        Frame_add.loginusername.Show(False);
        Frame_add.loginpassword.Show(False);
        Frame_add.Show(True);#Show The Frame
        event.Skip()

    def OnButton_viewLeftUp(self, event):
        import ViewPassList;
        Frame_View=ViewPassList.create(None);
        Frame_View.loginusername.Value=self.username.Value;
        Frame_View.loginpassword.Value=self.password.Value;
        Frame_View.loginusername.Show(False);
        Frame_View.loginpassword.Show(False);
        Frame_View.Show(True);
        
        event.Skip()

    def OnButton_keyLeftUp(self, event):
        import jiexipic;
        Frame_jiexi=jiexipic.create(None);
        Frame_jiexi.loginusername.Value=self.username.Value;
        Frame_jiexi.loginpassword.Value=self.password.Value;
        Frame_jiexi.loginusername.Show(False);
        Frame_jiexi.loginpassword.Show(False);
        Frame_jiexi.Show(True);
        event.Skip()


