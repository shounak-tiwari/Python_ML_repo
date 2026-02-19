# py -m pip install googletrans==4.0.0-rc1

import asyncio
from googletrans import Translator
translator = Translator()

async def main():
    while True:
        text = input("Enter the English text or exit: ")

        if text.lower() == 'exit':
            break

        result = await translator.translate(text, src='en', dest='hi')
        print("Hindi:", result.text)
asyncio.run(main())