<?php
session_start();

try  
 {  
      $connect = new PDO("mysql:host=localhost;port=3307;dbname=test", "root", "");  
      $connect->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);  
      if(isset($_POST['next'])){ 

		header("Location: http://localhost/login5/firstlanding5.html");
		exit();
		}
      	elseif (isset($_POST['search'])) {
		header("Location: http://localhost/login5/search5copy.php");
		exit();
	}
}

catch(PDOException $e)
    {
    echo "Connection failed: " . $e->getMessage();
    }

?>


