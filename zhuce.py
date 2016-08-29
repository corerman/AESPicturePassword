#Boa:Frame:Frame1
#coding=utf-8
import wx
import smtplib
server="lab.icorer.com";
def sendmail(username,password,usermailbox):
    mail_server="smtp.qq.com";
    mail_port=465 ;
    mail_from_address="";
    mail_to_address=usermailbox;
    mail_subject="E-mail verification --Cloud password";
    mail_login_name="";
    mail_login_pawssword="";
    msg_info="Hello , please click on this link to activate your account.\n\n http://"+server+"/signin.php?username="+username+"&password="+password+"&Email="+usermailbox;
    mail=smtplib.SMTP_SSL(mail_server,mail_port);
    mail.login(mail_login_name,mail_login_pawssword);
    mail.sendmail(mail_from_address,mail_to_address,"From:"+mail_from_address+"\nTo:"+mail_to_address+"\nSubject:"+mail_subject+"\n\n"+msg_info);
    mail.quit();
    
def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1EMAIL, wxID_FRAME1OK, wxID_FRAME1PANEL1, 
 wxID_FRAME1PASSWD, wxID_FRAME1PASSWD2, wxID_FRAME1USERNAME, 
] = [wx.NewId() for _init_ctrls in range(7)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(675, 293), size=wx.Size(293, 267),
              style=wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX),
              title='\xd3\xc3\xbb\xa7\xd7\xa2\xb2\xe1')
        self.SetClientSize(wx.Size(277, 229))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(277, 229), style=0)

        self.username = wx.TextCtrl(id=wxID_FRAME1USERNAME, name='username',
              parent=self.panel1, pos=wx.Point(56, 24), size=wx.Size(184, 24),
              style=0, value='\xd3\xc3\xbb\xa7\xc3\xfb')

        self.passwd2 = wx.TextCtrl(id=wxID_FRAME1PASSWD2, name='passwd2',
              parent=self.panel1, pos=wx.Point(56, 64), size=wx.Size(184, 24),
              style=wx.TE_PASSWORD, value='....a')

        self.passwd = wx.TextCtrl(id=wxID_FRAME1PASSWD, name='passwd',
              parent=self.panel1, pos=wx.Point(56, 104), size=wx.Size(184, 24),
              style=wx.TE_PASSWORD, value='.....')

        self.Email = wx.TextCtrl(id=wxID_FRAME1EMAIL, name='Email',
              parent=self.panel1, pos=wx.Point(56, 144), size=wx.Size(184, 24),
              style=0, value='\xb5\xe7\xd7\xd3\xd3\xca\xcf\xe4')

        self.ok = wx.Button(id=wxID_FRAME1OK, label='\xd7\xa2\xb2\xe1',
              name='ok', parent=self.panel1, pos=wx.Point(104, 184),
              size=wx.Size(80, 32), style=0)
        self.ok.SetForegroundColour(wx.Colour(255, 255, 255))
        self.ok.Bind(wx.EVT_LEFT_UP, self.OnOkLeftUp)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.SetTransparent(220)
        self.SetBackgroundColour(wx.Colour(24,24,24))
        self.ok.SetBackgroundColour(wx.Colour(0,156,117))

    def OnOkLeftUp(self, event):
        name=self.username.Value;
        password=self.passwd.Value;
        password2=self.passwd2.Value;
        mailbox=self.Email.Value;
        
        if password!=password2:
            wx.MessageBox("两次密码输入不相同！","信息错误",wx.OK|wx.ICON_ERROR);
        else:
            try:
                sendmail(name,password,mailbox);
                wx.MessageBox("邮件发送成功，请登录邮箱验证。","邮箱验证",wx.OK|wx.ICON_INFORMATION);
                self.Destroy();
            except:
                wx.MessageBox("发送失败：\n  请检查信息 格式\n    用户名，密码：英文\n    电子邮件格式。  ",'邮件发送失败',wx.OK|wx.ICON_ERROR)
                self.Destroy();
        
        event.Skip()

