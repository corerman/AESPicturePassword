#Boa:Frame:Frame1
global jsondata
import wx
import wx.stc
from urllib2 import urlopen



def create(parent):
    return Frame1(parent)

count=1;
[wxID_FRAME1, wxID_FRAME1CHOICE1, wxID_FRAME1COUNT, wxID_FRAME1LOGINPASSWORD, 
 wxID_FRAME1LOGINUSERNAME, wxID_FRAME1PANEL1, wxID_FRAME1STATICBOX1, 
 wxID_FRAME1STATICBOX2, wxID_FRAME1TEXTCTRL1, wxID_FRAME1TEXTCTRL2, 
 wxID_FRAME1TEXTCTRL3, 
] = [wx.NewId() for _init_ctrls in range(11)]

class Frame1(wx.Frame):
    
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(575, 160), size=wx.Size(356, 303),
              style=wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX),
              title='\xd5\xcb\xbb\xa7\xd0\xc5\xcf\xa2\xc1\xd0\xb1\xed')
        self.SetBackgroundColour(wx.Colour(24,24,24))
        self.SetClientSize(wx.Size(340, 265))
        self.SetTransparent(220)
        self.SetBackgroundColour(wx.Colour(24,24,24))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(340, 265),
              style=wx.TAB_TRAVERSAL)
        self.panel1.Bind(wx.EVT_MOUSE_EVENTS, self.OnPanel1MouseEvents)

        self.choice1 = wx.Choice(choices=[], id=wxID_FRAME1CHOICE1,
              name='choice1', parent=self.panel1, pos=wx.Point(8, 16),
              size=wx.Size(56, 22), style=0)
        self.choice1.Bind(wx.EVT_CHOICE, self.OnChoice1Choice,
              id=wxID_FRAME1CHOICE1)

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label='\xd5\xcb\xbb\xa7\xd0\xc5\xcf\xa2', name='staticBox1',
              parent=self.panel1, pos=wx.Point(72, 8), size=wx.Size(248, 100),
              style=0)
        self.staticBox1.SetForegroundColour(wx.Colour(255, 255, 0))

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self.panel1, pos=wx.Point(96, 32), size=wx.Size(200, 22),
              style=wx.TE_READONLY, value='\xb1\xea\xcc\xe2')
        self.textCtrl1.Bind(wx.EVT_LEFT_UP, self.OnTextCtrl1LeftUp)

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self.panel1, pos=wx.Point(96, 72), size=wx.Size(200, 22),
              style=wx.TE_READONLY, value='\xd5\xcb\xbb\xa7')
        self.textCtrl2.Bind(wx.EVT_LEFT_UP, self.OnTextCtrl2LeftUp)

        self.staticBox2 = wx.StaticBox(id=wxID_FRAME1STATICBOX2,
              label='\xb1\xb8\xd7\xa2\xd0\xc5\xcf\xa2', name='staticBox2',
              parent=self.panel1, pos=wx.Point(72, 120), size=wx.Size(248, 136),
              style=0)
        self.staticBox2.SetForegroundColour(wx.Colour(255, 255, 0))

        self.loginusername = wx.TextCtrl(id=wxID_FRAME1LOGINUSERNAME,
              name='loginusername', parent=self.panel1, pos=wx.Point(40, 288),
              size=wx.Size(104, 22), style=0, value='loginusername')

        self.loginpassword = wx.TextCtrl(id=wxID_FRAME1LOGINPASSWORD,
              name='loginpassword', parent=self.panel1, pos=wx.Point(200, 288),
              size=wx.Size(100, 22), style=0, value='loginpassword')

        self.count = wx.TextCtrl(id=wxID_FRAME1COUNT, name='count',
              parent=self.panel1, pos=wx.Point(312, 288), size=wx.Size(100, 22),
              style=0, value='1')

        self.textCtrl3 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL3, name='textCtrl3',
              parent=self.panel1, pos=wx.Point(88, 144), size=wx.Size(216, 96),
              style=wx.TE_READONLY | wx.TE_MULTILINE | wx.VSCROLL, value='')

    def __init__(self, parent):
        self._init_ctrls(parent)
        
    def OnTextCtrl1LeftUp(self, event):
        event.Skip()

    def OnTextCtrl2LeftUp(self, event):
        event.Skip()

    def OnButton1LeftUp(self, event):
        login_name=self.loginusername.Value;
        print login_name
        event.Skip()

    def OnPanel1MouseEvents(self, event):
        if self.count.Value=='1':
            self.count.Value='2';
            Server_List_url="http://lab.icorer.com/userinfolist.php";
            login_name=self.loginusername.Value;
            login_password=self.loginpassword.Value;
            url=Server_List_url+"?username="+login_name+"&password="+login_password;
            #print url;
            http_handle=urlopen(url);
            json_data=http_handle.read();
            import json
            json_data=json.loads(json_data);
            global jsondata;
            jsondata=json_data["list"]; #global var
            #print jsondata;
            num_top=len(jsondata);
            #print num_top;
            i=0;
            while i<num_top:
                self.choice1.Append(str(i+1));
                i=i+1;
            
            
        event.Skip()

    def OnChoice1Choice(self, event): 
        global jsondata;
        id=self.choice1.GetCurrentSelection();
        #print jsondata[id];
        title=jsondata[id]["title"];
        zhanghao=jsondata[id]["zhanghao"];
        lable=jsondata[id]["lable"];
        
        import  base64
        title=base64.b64decode(title);
        zhanghao=base64.b64decode(zhanghao);
        lable=base64.b64decode(lable);
        #print title,zhanghao,lable
        self.textCtrl1.Value=title;
        self.textCtrl2.Value=zhanghao;
        self.textCtrl3.Value=lable;
        #print jsondata;  
        event.Skip()
