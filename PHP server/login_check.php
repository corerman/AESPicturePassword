<?php
	if(($_GET['username']!="")&&($_GET['password']!=""))
	{
		$status=CheckUser($_GET['username'],$_GET['password']);
		/*
		 1:无用户
		 2:密码错误
		 3:登录成功
		*/
		switch($status){
			case 1: print "nouser"; break;
			case 2: print "nopass"; break;
			case 3: print "ok"; break;
		}	
	}
?>

<?php
	function CheckUser($username,$password)
	{
		$dir="./total_data/";
		$user_dir=$dir.$username;
		if(!file_exists($user_dir))
		{
			return 1;
		}
		
		$user_input_password=md5($password); //加密用户输入的密码
		$user_passfile_dir=$user_dir."/pass.key"; //读取密钥文件
		$server_password=file($user_passfile_dir); //获取服务器储存的密码
		
		//print $user_input_password."<br />".$server_password;
		if($user_input_password==$server_password[0])
				return 3;
		else
				return 2;
		
	}

?>
