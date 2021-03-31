<!DOCTYPE html>
<html>
<head>
<title>search5.php</title>
<meta content="noindex, nofollow" name="robots">
<link href="search5.css" rel="stylesheet" type="text/css">
</head>
<body>
<div class="maindiv">
<div class="divA">
<div class="title">
<h2>search employee</h2>
</div>
<div class="divB">
<div class="divD">
<p>current user</p>
<?php
session_start();
$var1=$_SESSION['id'];

$connection = mysql_connect("localhost", "root", ""); // Establishing Connection with Server
$db = mysql_select_db("test", $connection); // Selecting Database
//MySQL Query to read data
$query0 = mysql_query("select * from userlist", $connection);
$query = mysql_query("select * from userlist where id='$var1'", $connection);
while ($row = mysql_fetch_array($query)) 
{
   echo $row['name'];
}	
?>
</div>


<?php

$query1 = mysql_query("select * from registration", $connection);
while ($row1 = mysql_fetch_array($query1) and $row0 = mysql_fetch_array($query0)) {
?>
<div class="form">
<p>all</p>
<!-- Displaying Data Read From Database -->
<span>Name:</span> <?php echo $row0['name']; ?>
<span>status:</span> <?php echo $row1['deptID']; ?>
<span>seat:</span> <?php echo $row1['seatID']; ?>
<span>place:</span> <?php echo $row1['place']; ?>
<span>returning time:</span> <?php echo $row1['return_time']; ?>
</div>
<?php
}

?>
<div class="clear"></div>
</div>
<div class="clear"></div>
</div>
</div>
<?php
mysql_close($connection); // Closing Connection with Server
?>
</body>
</html>
