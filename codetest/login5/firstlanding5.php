<?php
session_start();
// session_write_close();
//echo $_SESSION['id'];


$connection = mysql_connect("localhost", "root", "");
$db = mysql_select_db("test", $connection); 
	if(isset($_POST['submit'])and isset($_POST['deptID']) and isset($_POST['seatID'])){ 
		$deptID = $_POST['deptID'];
		$seatID = $_POST['seatID'];
		//$login = $_SESSION['login'] ;
		if($deptID !=''||$seatID !=''){
			$var1=$_SESSION['id'];
			$_SESSION['deptID']=$_POST['deptID'];
			$_SESSION['seatID']=$_POST['seatID'];

			$query = mysql_query("update registration set deptID='$deptID', seatID='$seatID'
				where date_time=CURDATE() and id='$var1'");
			echo 'go to next page';
			header("Location: http://localhost/login5/secondlanding5.html");
			session_write_close();
			exit();
		}
	}
mysql_close();
?>	