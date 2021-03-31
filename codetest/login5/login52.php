<?php
session_start();

try  
 {  
      $connect = new PDO("mysql:host=localhost;port=3307;dbname=test", "root", "");  
      $connect->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);  
      if(isset($_POST['submit'])) { 
      	$id = $_POST['id'];
      	$result = $connect->query("SELECT * FROM userlist WHERE user_id='$id' LIMIT 1 ");
      	$num_rows = $result->fetch();
      	if($id !='' and  $num_rows > 0 ){
      		$_SESSION["id"] = $_POST["id"];
      		$statement = $connect->prepare("insert into registration(id) values (?)
      			ON DUPLICATE KEY UPDATE id =$id " );
      		$statement->execute(["$id"]);
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
}
catch(PDOException $e)
    {
    echo "Connection failed: " . $e->getMessage();
    }

?>