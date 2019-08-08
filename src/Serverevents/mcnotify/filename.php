<?php

$data = $_GET['var1'];

$fp = fopen('data.txt', 'w');
fwrite($fp, $data);        
fclose($fp);
?> 