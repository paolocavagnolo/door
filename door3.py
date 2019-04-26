from gpiozero import LED

import sys
import time
import asyncio
import telepot
import telepot.aio
from telepot.aio.loop import MessageLoop

led = LED(27)
big = LED(23)

async def handle(msg):
	chat_id = msg['chat']['id']
	command = msg['text']

	print(str(chat_id))

	if chat_id == *********:
		if command == '/entro'':
			led.on()
			await bot.sendMessage(chat_id, "Benvenuto!")
			time.sleep(0.5)
			led.off()

		elif command == '/esco':
			led.on()
			await bot.sendMessage(chat_id, "Ciao, a presto!")
			time.sleep(0.5)
			led.off()

		elif command == '/portone':
			big.on()
			await bot.sendMessage(chat_id, "Portone aperto!")
			time.sleep(0.5)
			big.off()

	else:
		await bot.sendMessage(chat_id, "Tu non puoi entrare")


bot = telepot.aio.Bot('************')
loop = asyncio.get_event_loop()

loop.create_task(MessageLoop(bot, handle).run_forever())
print('Listening ...')

loop.run_forever()

