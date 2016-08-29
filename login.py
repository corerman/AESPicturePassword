#Boa:Frame:Frame1
#coding=UTF-8
import wx
from urllib2 import urlopen;
Server="http://lab.icorer.com/";
Server_data_root=Server+"data/";

Server_login_script=Server+"login_check.php";  # username password

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1GAUGE1, wxID_FRAME1LASTPASSWORD, 
 wxID_FRAME1LASTUSERNAME, wxID_FRAME1LOGIN, wxID_FRAME1NEWUSER, 
 wxID_FRAME1PANEL1, wxID_FRAME1PASSWORD, wxID_FRAME1USERNAME, 
] = [wx.NewId() for _init_ctrls in range(9)]

def test_server():
    try:
        print("Checking NetWork...")
        server_check_url=Server+"/login_check.php"
        http_handle=urlopen(server_check_url);
    except:
        wx.MessageBox("Server connection error !",'Error',wx.OK|wx.ICON_ERROR)
        exit();

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(676, 353), size=wx.Size(275, 173),
              style=wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX),
              title='\xb5\xc7\xc2\xbc')
        self.SetClientSize(wx.Size(259, 135))
        self.Centre(wx.BOTH)
        self.SetTransparent(220)
        self.SetBackgroundColour(wx.Colour(24,24,24))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(259, 135),
              style=wx.TAB_TRAVERSAL)

        self.login = wx.Button(id=wxID_FRAME1LOGIN, label='\xb5\xc7\xc2\xbc',
              name='login', parent=self.panel1, pos=wx.Point(56, 104),
              size=wx.Size(56, 24), style=0)
        self.login.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL, False,''))
        self.login.Bind(wx.EVT_LEFT_UP, self.OnLoginLeftUp)

        self.username = wx.TextCtrl(id=wxID_FRAME1USERNAME, name='username',
              parent=self.panel1, pos=wx.Point(40, 24), size=wx.Size(192, 24),
              style=0, value='UserName')
        self.username.Bind(wx.EVT_LEFT_DOWN, self.OnUsernameLeftDown)

        self.password = wx.TextCtrl(id=wxID_FRAME1PASSWORD, name='password',
              parent=self.panel1, pos=wx.Point(40, 64), size=wx.Size(192, 24),
              style=wx.TE_PASSWORD, value='password')
        self.password.Bind(wx.EVT_LEFT_DOWN, self.OnPasswordLeftDown)

        self.newuser = wx.Button(id=wxID_FRAME1NEWUSER,
              label='\xd7\xa2\xb2\xe1', name='newuser', parent=self.panel1,
              pos=wx.Point(160, 104), size=wx.Size(56, 24), style=0)
        self.newuser.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              ''))
        self.newuser.Bind(wx.EVT_LEFT_UP, self.OnNewuserLeftUp)

        self.gauge1 = wx.Gauge(id=wxID_FRAME1GAUGE1, name='gauge1',
              parent=self.panel1, pos=wx.Point(-8, -8), range=150,
              size=wx.Size(288, 16), style=wx.GA_HORIZONTAL)
        self.gauge1.SetHelpText('loading...')
        self.gauge1.SetLabel('')
        self.gauge1.SetValue(0)

        self.lastusername = wx.TextCtrl(id=wxID_FRAME1LASTUSERNAME,
              name='lastusername', parent=self.panel1, pos=wx.Point(24, 168),
              size=wx.Size(100, 22), style=0, value='last user name')

        self.lastpassword = wx.TextCtrl(id=wxID_FRAME1LASTPASSWORD,
              name='lastpassword', parent=self.panel1, pos=wx.Point(144, 168),
              size=wx.Size(100, 22), style=0, value='last password')

    def __init__(self, parent):
        import ctypes;
        ctypes.windll.kernel32.SetConsoleTitleA("console1")
        import win32gui;
        h = win32gui.FindWindow(None, "console1")
        win32gui.ShowWindow(h,False);
        test_server();#test server link status
        self._init_ctrls(parent)
        self.lastusername.Show(False);
        self.lastpassword.Show(False);
        self.gauge1.SetValue(150);
       #to_bmp_image = wx.Image("back.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap() 
        #self.bitmap = wx.StaticBitmap(self, -1, to_bmp_image, (0, 0)) 
        self.login.SetBackgroundColour(wx.Colour(0,156,117))
        self.newuser.SetBackgroundColour(wx.Colour(0,156,117))
        #self.button1.SetTransparent(0)

    def OnUsernameLeftDown(self, event):
        self.gauge1.Show(False);
        self.username.Value="";
        event.Skip()

    def OnPasswordLeftDown(self, event):
        self.password.Value="";
        event.Skip()

    def OnLoginLeftUp(self, event):
        server_check_script_url=Server_login_script+"?username="+self.username.Value+"&password="+self.password.Value;
        #print server_check_script_url;
        http_handle=urlopen(server_check_script_url);
        status=http_handle.read();
        status=status.replace("\r\n","");
        status=status.replace("\n","");
        #print status;
        if status=="nouser":
            wx.MessageBox("This user does not exist!",'Error',wx.OK|wx.ICON_ERROR)
        elif status=="nopass":
            wx.MessageBox("The user password is incorrect!",'Error',wx.OK|wx.ICON_ERROR)
        elif status=="ok":
            self.lastusername.Value=self.username.Value;
            self.lastpassword.Value=self.password.Value;
            import select
            select=select.create(None);
            select.username.Value=self.lastusername.Value;
            select.password.Value=self.lastpassword.Value;
            select.password.Show(False);
            select.username.Show(False);
            select.Show(True);
            self.Destroy();
        else:
            wx.MessageBox("Please check the user login information",'Error',wx.OK|wx.ICON_ERROR)
        event.Skip()

    def OnNewuserLeftUp(self, event):
        import zhuce
        zhuce=zhuce.create(None);
        zhuce.Show(True);
        event.Skip()







