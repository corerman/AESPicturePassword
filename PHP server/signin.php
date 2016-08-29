<!doctype html> 
<html lang="en" class="no-js"> 
<head> 
  <meta charset="utf-8" /> 
  <title>用户 注册 反馈</title> 
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="http://isaves.qiniudn.com/iccp/css/style2.css" />
  <script type='text/javascript' src='http://isaves.qiniudn.com/iccp%2Fjs%2Fjquery-1.11.1.min.js'></script>
  <script type='text/javascript' src='http://isaves.qiniudn.com/iccp%2Fjs%2Fjquery.particleground.min.js'></script>
  <script type='text/javascript' src='http://isaves.qiniudn.com/iccp%2Fjs%2Fdemo.js'></script>
</head> 

<body>

<div id="particles">
	<div class="intro">
		<h1>
		<?php
			if(CheckUser($_GET['username'])==0)
				print "Error: User exists";
			else
			{
				adduser($_GET['username'],$_GET['password'],$_GET['Email']);
				print "Now Successful !";
			}
				
		?>
		</h1>
		<p>在这里，我们基于工业级加密算法和图形化模糊数据，帮助您保存密码。</p>
		<a  class="btn">注册反馈</a>
	</div>
</div>

<?php
	function CheckUser($username){
		$dir="./total_data/";
		$user_dir=$dir.$username;
		$result=1;//可以注册
		if(file_exists($user_dir))
		{
			$result=0;
		}
		return $result;
	}
	
	function adduser($username,$password,$email)
	{
		$password=md5($password);
		$dir="./total_data/";
		$user_info_dir=$dir.$username;
		$user_pass_dir=$user_info_dir."/pass_list";
		//创建用户根目录
		//创建根目录下的 pass.key info.dat
		//创建根目录下的pass_list目录
		mkdir($user_info_dir);
		$fpass=fopen($user_info_dir."/pass.key","w");
		fprintf($fpass,"%s",$password);
		fclose($fpass);
		$fpass=fopen($user_info_dir."/info.dat","w");
		fprintf($fpass,"%s",$email);
		fclose($fpass);
		mkdir($user_pass_dir);
	}


?>



</body> 
</html> 