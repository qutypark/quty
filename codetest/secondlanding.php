<?php
session_start();


$connection = mysql_connect("localhost", "root", "");
$db = mysql_select_db("test", $connection); 
	if(isset($_POST['submit'])and isset($_POST['stat']) and isset($_POST['place']) and isset($_POST['return_time'])){ 
		$stat = $_POST['stat'];
		$place = $_POST['place'];
		$return_time = $_POST['return_time'];
		//$login = $_SESSION['login'] ;
		if($stat !=''||$place !=''||$return_time !=''){
			$var1=$_SESSION['id'];
			$var2=$_SESSION['deptID'];
			$var3=$_SESSION['seatID'];
			$query = mysql_query("update registration set stat='$stat', place='$place',
				return_time='$return_time' where date_time=CURDATE() and id='$var1'");
			
			header("Location: http://localhost/login5/finish5.html");
			exit();			
		}

	}
mysql_close();
session_destroy();
	
?>	
