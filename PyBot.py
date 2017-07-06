#!/usr/bin/python

from linebot import LineBotApi
from linebot.models import TextSendMessage 
from linebot.exceptions import LineBotApiError

line_bot_api = LineBotApi('S9fqp8x6Mttskfkv4TD48tV380ZL9boHkR1c5aB8rX3wkx5HeJZQYvD0TaOQoziLYXDdVkJ7XCeDypz6BkqAMT19uFUw0gfASBIc/EhFyYFhrMilITAbiDRqdfZK5ia1qjoZfenT+gmZGgEGfnEUzQdB04t89/1O/w1cDnyilFU=')

try: 
	line_bot_api.push_message('U376499c1dd33003ea8e762dad9a1ab84', \
		TextSendMessage(text='Hello World!'))
except LineBotApiError as e:
	print (LineBotApiError) 
