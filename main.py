import logging
from aiogram import Bot, Dispatcher, executor, types
import knopki as nav
import parser as pr
import os

tokenb = os.getenv("TOKEN")
bot = Bot(token= tokenb)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(messange: types.Message):
    await bot.send_message(messange.from_user.id, 'Здрасте дети, вы расписание хотите,а оно вам надо? \n Если вы все равно не пойдете на пары {0.first_name}'.format(messange.from_user), reply_markup= nav.mainMenu)

@dp.message_handler()
async def bot_messange(messange: types.Message):

    if messange.text == 'Замены🔄':
        await bot.send_message(messange.from_user.id, pr.zaminka())
        await bot.delete_message(messange.from_user.id, messange.message_id)
    elif messange.text == '📋':
        await bot.send_message(messange.from_user.id, 'Выбери день мучений😩.', reply_markup= nav.otherMenu)
        await bot.delete_message(messange.from_user.id, messange.message_id)
    elif messange.text == '⬅':
        await bot.send_message(messange.from_user.id,'⬅', reply_markup= nav.mainMenu)
        await bot.delete_message(messange.from_user.id, messange.message_id)
    elif messange.text == '🔔':
        await bot.send_message(messange.from_user.id, pr.zvonki())
        await bot.delete_message(messange.from_user.id, messange.message_id)
    elif messange.text == 'Понедельник':
        await bot.send_message(messange.from_user.id, pr.ponedelnik() + "\n" + "Всего две пары, ты уверен, что ты хочешь просто потерять время?🙄.")
        await bot.delete_message(messange.from_user.id, messange.message_id)
    elif messange.text == 'Вторник':
        await bot.send_message(messange.from_user.id, pr.vtornik() + "\n" + "Топ, ко 2 паре, можно и поспать😴.")
        await bot.delete_message(messange.from_user.id, messange.message_id)
    elif messange.text == 'Среда':
        await bot.send_message(messange.from_user.id, pr.sreda() + "\n" + "Типо дефолт😐.")
        await bot.delete_message(messange.from_user.id, messange.message_id)
    elif messange.text == 'Четверг':
        await bot.send_message(messange.from_user.id, pr.chetverg() + "\n" + "Зачем ты на четверг смотришь если ДО🙄.")
        await bot.delete_message(messange.from_user.id, messange.message_id)
    elif messange.text == 'Пятница':
        await bot.send_message(messange.from_user.id, pr.pyatnica() + "\n" + "Четыре пары 🤬🤬🤬😭.")
        await bot.delete_message(messange.from_user.id, messange.message_id)
    elif messange.text == 'Суббота':
        await bot.send_message(messange.from_user.id, pr.sybbota() + "\n" + "Зачем вообще сегодня куда-то ехать?🥺")
        await bot.delete_message(messange.from_user.id, messange.message_id)
    else:
        await messange.reply('Ты дурак? Зачем🤬 ты мне пишешь? Просто нажимай на кнопки.', reply_markup= nav.mainMenu)
        await bot.delete_message(messange.from_user.id, messange.message_id)

   #...........................................Я НЕ ЗНАЮ КАК ВЫВЕСТИ ВОТ ЭТО, ТИПО ЕСЛИ ПОСЛЕ ЭТОГО ('Ты еблан? Нахуй ты мне пишешь? Просто нажимай на кнопки') ПОЛЬЗОВАТЕЛЬ ОТПРАВЛЯЕТ ЕЩЕ СООБЩЕНИЕ, ТО ОН ВЫВЕДЕТ СЛЕДУЮЩЕЕ, НИЖЕ, ПОМОГИ ПОЖАЛУЙСТА!!!!!!!
   #await messange.reply('Повторяю для одаренного, не заебывай меня, я создан только расписания. Если тебе не с кем пообщаться, то это уже не мои проблемы🖕.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
