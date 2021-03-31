<?php 
session_start();
$_SESSION['id'] = $_POST['id'];
//echo "Session variables are set.";

$connection = mysql_connect("localhost", "root", "");
$db = mysql_select_db("test", $connection);
<!DOCTYPE html>
<html>
  <head>
    <title>login4</title>
    <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
    <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
    <link href="resources/css/axure_rp_page.css" type="text/css" rel="stylesheet"/>
    <link href="data/styles.css" type="text/css" rel="stylesheet"/>
    <link href="files/login4/styles.css" type="text/css" rel="stylesheet"/>
    <script>
      $axure.utils.getTransparentGifPath = function() { return 'resources/images/transparent.gif'; };
      $axure.utils.getOtherPath = function() { return 'resources/Other.html'; };
      $axure.utils.getReloadPath = function() { return 'resources/reload.html'; };
    </script>
  </head>
  <body>   
    <div id="base" class="">
      <!-- Unnamed (Rectangle) -->
      <div id="u0" class="ax_default paragraph">
        <div id="u0_div" class=""></div>
        <div id="u0_text" class="text ">
          <p><span>Location </span></p><p><span>Registration</span></p><p><span>System</span></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u1" class="ax_default box_1">
        <div id="u1_div" class=""></div>
        <div id="u1_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

  <!-- Unnamed (Text Field) -->
      <div id="u2" class="ax_default text_field">
        <div id="u2_div" class=""></div>
        <input id="u2_input" name="id" type="text" value="" class="u2_input" placeholder="社員番号"/ autofocus required>
      </div>

      <!-- Unnamed (Shape) -->
      <div id="u3" class="ax_default primary_button">
        <img id="u3_img" class="img " src="images/login4/u3.svg"/>
        <div id="u3_text" class="text ">
          <div id="u3_input">
            <label>
              <span id="u3_input" class="search icon-small open-btn">NEXT</span>
              <input id="u3_input" name="submit" type="submit" style="display:none"/>
            </label>
          </div>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u4" class="ax_default paragraph">
        <div id="u4_div" class=""></div>
        <div id="u4_text" class="text ">
          <p><span>Copyright©2020 Nabtesco</span></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u5" class="ax_default paragraph">
        <div id="u5_div" class=""></div>
        <div id="u5_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u6" class="ax_default paragraph">
        <div id="u6_div" class=""></div>
        <div id="u6_text" class="text ">
          <p><span>User ID</span></p>
        </div>
      </div>

      <!-- Unnamed (Shape) -->
      <div id="u7" class="ax_default icon">
        <img id="u7_img" class="img " src="images/login4/u7.svg"/>
        <div id="u7_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Image) -->
      <div id="u8" class="ax_default image">
        <img id="u8_img" class="img " src="images/login4/u8.png"/>
        <div id="u8_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u9" class="ax_default" data-left="152" data-top="59" data-width="423" data-height="21">

        <!-- Unnamed (Rectangle) -->
        <div id="u10" class="ax_default paragraph">
          <div id="u10_div" class=""></div>
          <div id="u10_text" class="text ">
            <p><span>step1</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u11" class="ax_default paragraph">
          <div id="u11_div" class=""></div>
          <div id="u11_text" class="text ">
            <p><span>step2</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u12" class="ax_default paragraph">
          <div id="u12_div" class=""></div>
          <div id="u12_text" class="text ">
            <p><span>step3</span></p>
          </div>
        </div>
      </div>
    </div>
  </body>
</html>

if(isset($_POST['submit'])) { 
	$id = $_POST['id'];
	if($id !=''){
		$query = mysql_query("insert into registration(id) values ('$id')");
		
        echo 'go to next page';

        header("Location: http://localhost/login4/firstlanding4.html");
		echo "<br/><br/><span>Data Inserted successfully...!!</span>";
		exit();
	}
}

?>