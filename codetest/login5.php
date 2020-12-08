<?php


$connection = mysql_connect("localhost", "root", "");
$db = mysql_select_db("test", $connection);

if(isset($_POST['submit'])) { 
	session_start();
	$id = $_POST['id'];
	$_SESSION['id']=$id;
	$result = mysql_query("SELECT * FROM userlist WHERE user_id='$id' LIMIT 1 ");
	$num_rows = mysql_num_rows($result);

	if($id !='' and  $num_rows>0 ){
		$delete = mysql_query("delete from registration where id='$id' and date_time=CURDATE()");
		$insert = mysql_query("insert into registration(id,date_time) values ('$id',CURDATE())");
		echo 'go to next page';
		header("Location: http://localhost/login5/semilogin5.html");
		session_write_close();
		exit();
	}
	else {
		echo ("<script LANGUAGE='JavaScript'>
          window.alert('Wrong user!');
          document.location.href='logint5.html';
       </script>");
	}

}
mysql_close();

?>
