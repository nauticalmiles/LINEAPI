<?php
$access_token = 'S9fqp8x6Mttskfkv4TD48tV380ZL9boHkR1c5aB8rX3wkx5HeJZQYvD0TaOQoziLYXDdVkJ7XCeDypz6BkqAMT19uFUw0gfASBIc/EhFyYFhrMilITAbiDRqdfZK5ia1qjoZfenT+gmZGgEGfnEUzQdB04t89/1O/w1cDnyilFU=';

$url = 'https://api.line.me/v1/oauth/verify';

$headers = array('Authorization: Bearer ' . $access_token);

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
$result = curl_exec($ch);
curl_close($ch);

echo $result;