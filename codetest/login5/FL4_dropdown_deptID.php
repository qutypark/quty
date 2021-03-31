<?php
$connection = mysql_connect("localhost", "root", "");
$db = mysql_select_db("test", $connection); 

if(isset($_POST['deptID'])) { 
	$deptID = $_POST['deptID'];
	if($deptID !=''){
		$query = mysql_query("insert into registration(deptID) values ('$deptID')");
	}
}
?>