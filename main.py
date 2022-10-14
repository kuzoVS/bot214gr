import logging
from aiogram import Bot, Dispatcher, executor, types
import knopki as nav
import parser as pr
import os

bot = Bot(token= "5643975948:AAFglFaqGKcXlQZcM-GP9xYqBRim_7Luv2Q")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(messange: types.Message):
    await bot.send_message(messange.from_user.id, 'Здрасте уебаны, вы расписание хотите,а оно вам надо? \n Если вы все равно не пойдете на пары {0.first_name}'.format(messange.from_user), reply_markup= nav.mainMenu)

@dp.message_handler()
async def bot_messange(messange: types.Message):
    await bot.delete_message(messange.from_user.id, messange.message_id, reply_markup= nav.mainMenu)
    if messange.text == 'Замены🔄':
        await bot.send_message(messange.from_user.id, pr.zaminka())
    elif messange.text == '📋':
        await bot.send_message(messange.from_user.id, 'Выбери день мучений😩.', reply_markup= nav.otherMenu)
    elif messange.text == '⬅':
        await bot.send_message(messange.from_user.id,'⬅', reply_markup= nav.mainMenu)
    elif messange.text == '🔔':
        await bot.send_message(messange.from_user.id, pr.zvonki())
    elif messange.text == 'Понедельник':
        await bot.send_message(messange.from_user.id, pr.ponedelnik() + "\n" + "Всего две пары, ты уверен, что ты хочешь просто проебать время?🙄.")
    elif messange.text == 'Вторник':
        await bot.send_message(messange.from_user.id, pr.vtornik() + "\n" + "Заебись, ко 2 паре, можно и поспать😴.")
    elif messange.text == 'Среда':
        await bot.send_message(messange.from_user.id, pr.sreda() + "\n" + "Типо дефолт😐.")
    elif messange.text == 'Четверг':
        await bot.send_message(messange.from_user.id, pr.chetverg() + "\n" + "Нахуй ты на четверг смотришь если ДО🙄.")
    elif messange.text == 'Пятница':
        await bot.send_message(messange.from_user.id, pr.pyatnica() + "\n" + "Четыре пары блять😭.")
    elif messange.text == 'Суббота':
        await bot.send_message(messange.from_user.id, pr.sybbota() + "\n" + "Зачем вообще сегодня куда-то ехать?🥺")
    else:
        await messange.reply('Ты дурак? Зачем🤬 ты мне пишешь? Просто нажимай на кнопки.', reply_markup= nav.mainMenu)
   #...........................................Я НЕ ЗНАЮ КАК ВЫВЕСТИ ВОТ ЭТО, ТИПО ЕСЛИ ПОСЛЕ ЭТОГО ('Ты еблан? Нахуй ты мне пишешь? Просто нажимай на кнопки') ПОЛЬЗОВАТЕЛЬ ОТПРАВЛЯЕТ ЕЩЕ СООБЩЕНИЕ, ТО ОН ВЫВЕДЕТ СЛЕДУЮЩЕЕ, НИЖЕ, ПОМОГИ ПОЖАЛУЙСТА!!!!!!!
   #await messange.reply('Повторяю для одаренного, не заебывай меня, я создан только расписания. Если тебе не с кем пообщаться, то это уже не мои проблемы🖕.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
