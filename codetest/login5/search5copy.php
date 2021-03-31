<!DOCTYPE html>
<html>
<head>
<title>search5copy.php</title>
<link href="search5.css" rel="stylesheet" type="text/css">

<style>
table
{
border-style:solid;
border-width:4px;
border-color:;
}

</style>
</head>


<body>
<div class="maindiv">
<div class="divA" style="width: 77%">
<div class="title">
<h2>search other</h2>
</div>
<div class="divB">
<div class="divD">
<p>current user</p>

<?php
session_start();
$var1=$_SESSION['id'];

$connection = mysql_connect("localhost","root","");

if (!$connection)
  {  die('Could not connect: ' . mysql_error());  }

$db = mysql_select_db("test", $connection); // Selecting Database
$query = mysql_query("select * from userlist where user_id='$var1'", $connection);
$query0 = mysql_query("select * from userlist", $connection);
$query1 = mysql_query("select * from registration", $connection);

while ($row = mysql_fetch_array($query)) 
{
   echo $row['name'];
}   
?>
</div>


<div class="form">
<p>all</p>
<?php

echo "<table border='1'>

<tr>

<th>name</th>

<th>status</th>

<th>seat</th>

<th>place</th>

<th>return_time</th>

</tr>";

 

while($row0 = mysql_fetch_array($query0) and $row1 = mysql_fetch_array($query1))

  {

  echo "<tr>";

  echo "<td>" . $row0['name'] . "</td>";

  echo "<td>" . $row1['deptID'] . "</td>";

  echo "<td>" . $row1['seatID'] . "</td>";

  echo "<td>" . $row1['place'] . "</td>";

  echo "<td>" . $row1['return_time'] . "</td>";

  echo "</tr>";

  }

echo "</table>";

?>

<div class="clear"></div>
</div>
<div class="clear"></div>
</div>
</div>

<?php
mysql_close($connection);
?>

</body>
</html>