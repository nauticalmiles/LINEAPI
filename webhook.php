<?php
$access_token = 'S9fqp8x6Mttskfkv4TD48tV380ZL9boHkR1c5aB8rX3wkx5HeJZQYvD0TaOQoziLYXDdVkJ7XCeDypz6BkqAMT19uFUw0gfASBIc/EhFyYFhrMilITAbiDRqdfZK5ia1qjoZfenT+gmZGgEGfnEUzQdB04t89/1O/w1cDnyilFU=';

// Get POST body content
$content = file_get_contents('php://input')

$events = json_decode($content, true);

if(!is_null($events['events'])) {

	foreach($events['events'] as $event){
		if($event['type'] == 'message' && $event['message']['type']) {
			// Get text sent
			$text = $events['message']['text'];
			// Get replyToken
			$replyToken = $events['replyToken'];
		}
	}
}
echo $replyToken . "\r\n"; 
echo $text . "\r\n";
echo "OK";