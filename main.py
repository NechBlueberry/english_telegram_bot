import asyncio
import telegram


async def main():
    bot = telegram.Bot("6552865075:AAF6E8YY26iTeqvv5-So46orv2Rs-XSRpBI")
    async with bot:
        print(await bot.get_me())

if __name__ == '__main__':8
asyncio.run(main())