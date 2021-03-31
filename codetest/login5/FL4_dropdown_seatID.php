<?php
$connection = mysql_connect("localhost", "root", "");
$db = mysql_select_db("test", $connection); 

$sql = mysql_query($connection, "SELECT deptID, seatID FROM deptseat");
$sql1 = mysql_query($connection, "SELECT deptID FROM registration");
echo"<select name='seatID'>";
while ($row = $sql->fetch_assoc() || $row1 = $sql1->fetch_assoc()) {
	unset($deptID,$deptID1,$seatID);
    $deptID = $row['deptID'];
    $deptID1 = $row1['deptID1'];
    $seatID = $row['seatID']; 
    if($deptID==$deptID1){
    	echo '<option value="'.$seatID.'">'.$seatID.'</option>';}
    	echo "</select>";}

    	?>