#Boa:Frame:Frame2
#coding=UTF-8
import wx
import base64
from urllib2 import urlopen

pickey_server_url="http://lab.icorer.com/keypic.php";
aes_server_url="http://lab.icorer.com/aes/";




from PIL import Image

def ResolvePic(png_pic_location):
    img=Image.open(png_pic_location);
    pic_width=img.size[0];
    pic_height=img.size[1];
    password={}
    line=1;
    while line < pic_height:
        r,g,b=img.getpixel((0,line));
        if r==255 and g==255 and b==255:
            width=0;
            count=-1;
            while width< pic_width:
                r,g,b=img.getpixel((width,line));
                if r==255 and g==255 and b==255:
                    count=count+1;
                width=width+1;
            password[count]=chr(line);
            #print chr(line),count;
        line=line+1;
    #print len(password)
    str_password="";
    count=1;
    #print password;
    try:
        while count<=len(password):
            str_password=str_password+password[count];
            count=count+1;
        return str_password;
    except:
        wx.MessageBox("网络安全不佳，获取密钥失败，请重试！",'Error',wx.OK|wx.ICON_ERROR)

def create(parent):
    return Frame2(parent)



[wxID_FRAME2, wxID_FRAME2BUTTON1, wxID_FRAME2INFO_CTRL_ID, 
 wxID_FRAME2LOGINPASSWORD, wxID_FRAME2LOGINUSERNAME, wxID_FRAME2PANEL1, 
 wxID_FRAME2STATICTEXT1, wxID_FRAME2TEXTCTRL1, wxID_FRAME2TEXTCTRL2, 
 wxID_FRAME2TEXTCTRL3, wxID_FRAME2TEXTCTRL4, wxID_FRAME2TEXTCTRL5, 
] = [wx.NewId() for _init_ctrls in range(12)]

class Frame2(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME2, name='', parent=prnt,
              pos=wx.Point(590, 255), size=wx.Size(331, 212),
              style=wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX),
              title='\xcc\xed\xbc\xd3')
        self.SetClientSize(wx.Size(315, 174))
        self.SetTransparent(220)
        self.SetBackgroundColour(wx.Colour(24,24,24))

        self.panel1 = wx.Panel(id=wxID_FRAME2PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(315, 174),
              style=wx.TAB_TRAVERSAL)

        self.button1 = wx.Button(id=wxID_FRAME2BUTTON1,
              label='\xcf\xc2\xd2\xbb\xb2\xbd', name='button1',
              parent=self.panel1, pos=wx.Point(224, 136), size=wx.Size(80, 30),
              style=wx.ALWAYS_SHOW_SB)
        self.button1.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              ''))
        self.button1.SetForegroundColour(wx.Colour(255, 255, 255))
        self.button1.Bind(wx.EVT_LEFT_UP, self.OnButton1LeftUp)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME2BUTTON1)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL1, name='textCtrl1',
              parent=self.panel1, pos=wx.Point(48, 64), size=wx.Size(224, 28),
              style=0, value='\xb1\xea\xcc\xe2')
        self.textCtrl1.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))
        self.textCtrl1.Bind(wx.EVT_LEFT_UP, self.OnTextCtrl1LeftUp)

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL2, name='textCtrl2',
              parent=self.panel1, pos=wx.Point(48, 64), size=wx.Size(224, 28),
              style=0, value='\xd5\xca\xbb\xa7\xc3\xfb')
        self.textCtrl2.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, ''))
        self.textCtrl2.Bind(wx.EVT_LEFT_UP, self.OnTextCtrl2LeftUp)

        self.textCtrl3 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL3, name='textCtrl3',
              parent=self.panel1, pos=wx.Point(48, 64), size=wx.Size(224, 28),
              style=wx.TE_PASSWORD, value='....')
        self.textCtrl3.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Georgia'))
        self.textCtrl3.Bind(wx.EVT_LEFT_UP, self.OnTextCtrl3LeftUp)

        self.textCtrl4 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL4, name='textCtrl4',
              parent=self.panel1, pos=wx.Point(48, 64), size=wx.Size(224, 28),
              style=wx.TE_PASSWORD, value='....')
        self.textCtrl4.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Georgia'))
        self.textCtrl4.Bind(wx.EVT_LEFT_UP, self.OnTextCtrl4LeftUp)

        self.info_ctrl_id = wx.TextCtrl(id=wxID_FRAME2INFO_CTRL_ID,
              name='info_ctrl_id', parent=self.panel1, pos=wx.Point(432, 16),
              size=wx.Size(100, 22), style=0, value='0')

        self.textCtrl5 = wx.TextCtrl(id=wxID_FRAME2TEXTCTRL5, name='textCtrl5',
              parent=self.panel1, pos=wx.Point(48, 40), size=wx.Size(216, 72),
              style=wx.TE_MULTILINE, value='\xb1\xb8\xd7\xa2')
        self.textCtrl5.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Calibri'))
        self.textCtrl5.Bind(wx.EVT_LEFT_UP, self.OnTextCtrl5LeftUp)

        self.staticText1 = wx.StaticText(id=wxID_FRAME2STATICTEXT1,
              label='\xca\xe4\xc8\xeb\xb1\xea\xcc\xe2', name='staticText1',
              parent=self.panel1, pos=wx.Point(88, 16), size=wx.Size(144, 14),
              style=wx.ALIGN_CENTRE)
        self.staticText1.SetForegroundColour(wx.Colour(255, 255, 0))

        self.loginusername = wx.TextCtrl(id=wxID_FRAME2LOGINUSERNAME,
              name='loginusername', parent=self.panel1, pos=wx.Point(40, 184),
              size=wx.Size(100, 22), style=0, value='login_username')

        self.loginpassword = wx.TextCtrl(id=wxID_FRAME2LOGINPASSWORD,
              name='loginpassword', parent=self.panel1, pos=wx.Point(184, 184),
              size=wx.Size(100, 22), style=0, value='login_password')

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.info_ctrl_id.Show(False);
        self.textCtrl2.Show(False);
        self.textCtrl3.Show(False);
        self.textCtrl4.Show(False);
        self.textCtrl5.Show(False);
        self.button1.SetBackgroundColour(wx.Colour(0,156,117))

    def OnButton1LeftUp(self, event):
        id_number=int(self.info_ctrl_id.Value);
        if id_number==0: 
            self.textCtrl1.Show(False);
            self.textCtrl2.Show(True);
            id_number=id_number+1;
            self.info_ctrl_id.Value=str(id_number);
            self.staticText1.Label="输入账户名";
        elif id_number==1: 
            self.textCtrl2.Show(False);
            self.textCtrl3.Show(True);
            id_number=id_number+1;
            self.info_ctrl_id.Value=str(id_number);
            self.staticText1.Label="输入密码信息";
        elif id_number==2:
            self.textCtrl3.Show(False);
            self.textCtrl4.Show(True);
            id_number=id_number+1;
            self.info_ctrl_id.Value=str(id_number);
            self.staticText1.Label="再次输入密码";
        elif id_number==3:
            self.textCtrl4.Show(False);
            self.textCtrl5.Show(True);
            id_number=id_number+1;
            self.info_ctrl_id.Value=str(id_number);
            self.staticText1.Label="输入备注信息";
            self.button1.Label="提交"
        elif id_number>3:#submit
            self.button1.Show(False);
            login_username=self.loginusername.Value;
            login_password=self.loginpassword.Value;
            title=self.textCtrl1.Value;
            account=self.textCtrl2.Value;
            password=self.textCtrl3.Value;
            password2=self.textCtrl4.Value;
            account_info=self.textCtrl5.Value;
            #print login_username,login_password, title,account,password,password2,account_info;
            if password!=password2:
                wx.MessageBox("两次密码输入不相同！","信息错误",wx.OK|wx.ICON_ERROR);
                self.Destroy();
            #info=u"账户信息:\n    标题："+title+u"\n账户名："+account+u"\n密码："+password+u"\n备注信息："+account_info+"\n";
            else:
                info="Fill in the information you submit this confirmation ?";
                select=wx.MessageBox(info,"确认信息",wx.YES_NO|wx.ICON_INFORMATION);
                #print select;
                if select == 8 :
                    self.Destroy();
                #get server picture password
                
                http_handle=urlopen(pickey_server_url);
                pic_data=http_handle.read();
                file=open("key.png","wb");
                file.write(pic_data);
                file.close();
                
                
                # jiexi pic key
                pic_key=ResolvePic('key.png');
                #print pic_key;
                
                #server aes256 encode
                
                pic_key_base64=base64.b64encode(pic_key);
                #password_base64=base64.b64encode(password);
                #print aes_server_url+"?password="+password_base64+"&aeskey="+password_base64;
                #http_handle=urlopen(aes_server_url+"?password="+password+"&aeskey="+pic_key);
                #aes_data=http_handle.read();# read aes 256 key
                #print aes_data;
                #print pic_key;
                
                #send base64 infomation
                #login_username=base64.b64encode(login_username);
                #login_password=base64.b64encode(login_password);
                try:
                    title=base64.b64encode(title);
                    account=base64.b64encode(account);
                    account_info=base64.b64encode(account_info);
                    #aes aleady base64 encode
                    UserPassAddUrl="http://lab.icorer.com/addpass.php";
                    UserPassAddUrl=UserPassAddUrl+"?username="+login_username+"&password="+login_password+"&title="+title+"&zhanghao="+account;
                
                    UserPassAddUrl=UserPassAddUrl+"&key="+pic_key_base64+"&lable="+account_info+"&mima="+base64.b64encode(password);
                    #print UserPassAddUrl; #Add URL Done! 
                
                    http_handle=urlopen(UserPassAddUrl);
                    status=http_handle.read();
                    if status=='ok':
                        wx.MessageBox("密码添加成功！","信息",wx.OK|wx.ICON_INFORMATION);
                        import ShowPicKey;
                        Frame_PicKey=ShowPicKey.create(None);
                        Frame_PicKey.Show(True);
                        self.Destroy();
                except:
                    wx.MessageBox("Please check the Account information \n    Please Use English!",'Error',wx.OK|wx.ICON_ERROR);
                    self.Destroy();             
        event.Skip()
        
    def OnButton1Button(self, event):
        event.Skip()

    def OnTextCtrl1LeftUp(self, event):
        self.textCtrl1.Value="";
        event.Skip()

    def OnTextCtrl2LeftUp(self, event):
        self.textCtrl2.Value="";
        event.Skip()

    def OnTextCtrl3LeftUp(self, event):
        self.textCtrl3.Value="";
        event.Skip()

    def OnTextCtrl4LeftUp(self, event):
        self.textCtrl4.Value="";
        event.Skip()

    def OnTextCtrl5LeftUp(self, event):
        self.textCtrl5.Value="";
        event.Skip()
        
