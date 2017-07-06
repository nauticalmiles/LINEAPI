#!/usr/bin/python

from flask import Flask, request
from linebot import LineBotApi
from linebot.models import TextSendMessage 
from linebot.exceptions import LineBotApiError



# Create channel access token
line_bot_api = LineBotApi('S9fqp8x6Mttskfkv4TD48tV380ZL9boHkR1c5aB8rX3wkx5HeJZQYvD0TaOQoziLYXDdVkJ7XCeDypz6BkqAMT19uFUw0gfASBIc/EhFyYFhrMilITAbiDRqdfZK5ia1qjoZfenT+gmZGgEGfnEUzQdB04t89/1O/w1cDnyilFU=')


app = Flask(__name__)

@app.route('/')

def callback(): 
	json_line = request.get_json()
	json_line = json.dumps(json_line)
	decoded = json.loads(json_line)
	user = decoded["events"][0]['replyToken']
	text = decoded["events"][0]['text']
	return '', 200 


try: 
	line_bot_api.push_message(user, TextSendMessage(text=text))
except LineBotApiError as e:
	print (LineBotApiError) 

if __name__ == '__main__':
	app.run(debug=True)