from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('⬅')
#Главные кнокпи
btnRasp = KeyboardButton('📋')
btnZam = KeyboardButton ('Замены🔄')
btnZvon = KeyboardButton('🔔')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnRasp, btnZam, btnZvon)

#Второстепенные кнопки
btnPn = KeyboardButton('Понедельник')
btnVt = KeyboardButton('Вторник')
btnSr = KeyboardButton('Среда')
btnCht = KeyboardButton('Четверг')
btnPt = KeyboardButton('Пятница')
btnSb = KeyboardButton('Суббота')
otherMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnPn, btnVt, btnSr, btnCht, btnPt, btnSb, btnMain)