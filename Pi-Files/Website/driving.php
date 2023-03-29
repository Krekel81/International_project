<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="reset.css">
    <link rel="stylesheet" href="index.css">
    <link rel="stylesheet" href="driving.css">
</head>
<body>
    <form method="POST">
        <input type="submit" value="Forward" name="forward">
        <input type="submit" value="Left" name="left">
        <input type="submit" value="Right" name="right">
        <input type="submit" value="Backwards" name="backwards">
        <input type="submit" value="Stop" name="stop">
    </form>
    <?php 
        if(isset($_POST["forward"]))
        {
            echo "going forward";
            shell_exec('/usr/bin/python /home/pi/Website/scripts/forward.py');
        }
        if(isset($_POST["left"]))
        {
            echo "going left";
            shell_exec('/usr/bin/python /home/pi/Website/scripts/backward.py');
        }
        if(isset($_POST["right"]))
        {
            echo "going right";
            shell_exec('/usr/bin/python /home/pi/Website/scripts/right.py');
        }
        if(isset($_POST["backwards"]))
        {
            echo "going backwards";
            shell_exec('/usr/bin/python /home/pi/Website/scripts/backward.py');
        }
        if(isset($_POST["stop"]))
        {
            echo "stopping...";
            shell_exec('/usr/bin/python /home/pi/Website/scripts/stop.py');
        }
    
    ?>
</body>
</html>