<?php

session_start();
session_regenerate_id();

$connection = mysql_connect("localhost", "root", "");
$db = mysql_select_db("test", $connection);

if(isset($_POST['submit'])) { 
	$id = $_POST['id'];
  $result = mysql_query("SELECT * FROM userlist WHERE id='$id' LIMIT 1");
  $num_rows = mysql_num_rows($result);

	if($id !='' and  $num_rows>0 ){
		$_SESSION['id']=$_POST['id'];
		$query = mysql_query("insert into registration(id) values ('$id') 
			ON DUPLICATE KEY UPDATE id=$id" );
		echo 'go to next page';
		header("Location: http://localhost/login5/semilogin5.html");
		exit();
	}
	else {
		echo ("<script LANGUAGE='JavaScript'>
          window.alert('Wrong user!');
          document.location.href='login5.html';
       </script>");
	}

}

?>