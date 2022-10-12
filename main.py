import logging
from aiogram import Bot, Dispatcher, executor, types
import knopki as nav
import parser as pr
import os

bot = Bot(token= access_token)
dp = Dispatcher(bot)
access_token = os.environ['access_token']
@dp.message_handler(commands=['start'])
async def command_start(messange: types.Message):
    await bot.send_message(messange.from_user.id, 'Здрасте уебаны, вы расписание хотите,а оно вам надо? \n Если вы все равно не пойдете на пары {0.first_name}'.format(messange.from_user), reply_markup= nav.mainMenu)

@dp.message_handler()
async def bot_messange(messange: types.Message):
    #await bot.send_message(messange.from_user.id, messange.text)
    if messange.text == 'Замены!':
        await bot.send_message(messange.from_user.id, pr.zaminka())
    elif messange.text == 'Расписание':
        await bot.send_message(messange.from_user.id, 'Выбери день мучений', reply_markup= nav.otherMenu)
    elif messange.text == 'Назад':
        await bot.send_message(messange.from_user.id, 'Назад', reply_markup= nav.mainMenu)
    elif messange.text == 'Звонки':
        await bot.send_message(messange.from_user.id, pr.zvonki())
    elif messange.text == 'Понедельник':
        await bot.send_message(messange.from_user.id, pr.ponedelnik())
    elif messange.text == 'Вторник':
        await bot.send_message(messange.from_user.id, pr.vtornik())
    elif messange.text == 'Среда':
        await bot.send_message(messange.from_user.id, pr.sreda())
    elif messange.text == 'Четверг':
        await bot.send_message(messange.from_user.id, pr.chetverg()+ "\n" + "Нахуй ты на четверг смотришь если ДО")
    elif messange.text == 'Пятница':
        await bot.send_message(messange.from_user.id, pr.pyatnica())
    elif messange.text == 'Суббота':
        await bot.send_message(messange.from_user.id, pr.sybbota())
    else:
        await messange.reply('Ты еблан? Нахуй ты мне пишешь? Просто нажимай на кнопки')

bot.polling(none_stop=True)

