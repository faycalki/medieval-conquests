<?php

$var1 = $_GET['var1'];
$today = date("m.d.y");   
$break = ':';

$data = $var1;

$var = file_get_contents('data2.txt');
$date = split(':', $var);

if ($date['1'] == $today)
{

$date['0']++;

$data2 = $date['0'].$break.$today;  
$fp = fopen('data2.txt', 'w');
fwrite($fp, $data2);        
fclose($fp);
}
else {
$data2 = '1'.$break.$today;
$fp = fopen('data2.txt', 'w');
fwrite($fp, $data2);        
fclose($fp);
}

$fp = fopen('data.txt', 'w');
fwrite($fp, $data);        
fclose($fp);
?>
