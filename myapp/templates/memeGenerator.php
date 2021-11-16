<?php

$ranImage = "no image";

if(isset($_POST['button']))
{
    $dirPath = "images";
    $files = scandir($dirPath);

    $count = count($files);
    $index = rand(2,($count-1));
    $fileName = $files[$index];

    $ranImage = '<img src="'.$dirPath."/".$fileName.'" alt="'.$fileName.'">'  ;

}


?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">

    <title>Cloud Computing Final</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<h2 class="appTitle">Meme Generator</h2>
<div class="meme">
        <p> <?php  echo $ranImage?></p>
</div>
<div>
<form action="memeGenerator.php" method="post">
    <input type="submit" value ="Generate!"  name="button" class="generatorButton">
</form>
</div>
</body>
</html>