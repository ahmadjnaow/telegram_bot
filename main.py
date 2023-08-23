from aiogram import Bot, Dispatcher, types, executor
import random



bot = Bot(token='6265232949:AAHLhJwviSaII3_6CPjcbrWbx8hqq8-rdeY')
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(' Я загадал число от 1 до 3 угадайте ')

@dp.message_handler(lambda message:message.text.isdigit())
async def ques_number(message:types.Message):
    user_ques = int(message.text)
    random_number = random.randint(1, 3)

    if user_ques == random_number:
        with open('win.jpg','rb') as photo:
            await message.answer_photo(photo)
    else:
        with open('no.jpg','rb') as photo:
            await message.answer_photo(photo)

executor.start_polling(dp)
