from telegram import Bot
import asyncio
import json
import config

async def send_to_telegram_channel(image_url, description, telegram_bot_token, channel_id):
    bot = Bot(token=telegram_bot_token)
    await bot.send_photo(chat_id=channel_id, photo=image_url, caption=description)

async def main():
    with open("pins.json", "r") as json_file:
        pins = json.load(json_file)

    telegram_bot_token = config.token
    channel_id = config.channel_id
    
    for data in pins:
        await asyncio.sleep(5)
        await send_to_telegram_channel(data["image_url"], data["description"], telegram_bot_token, channel_id)

if __name__ == "__main__":
    asyncio.run(main())