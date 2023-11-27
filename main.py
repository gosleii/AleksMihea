import telebot
bot = telebot.TeleBot('6957176876:AAFHd5Zeu4eCR8u7BG7VkBsea_WaIjZIfQs')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Хочешь начать войну Ящеров против Русов?!')



@bot.message_handler(commands=['run'])

def main(message):
    bot.send_message(message.chat.id, 'Началась Война!')
    bot.send_message(message.chat.id, 'Итоги войны...')
    bot.send_message(message.chat.id, 'Победа Руссов!')


@bot.message_handler(commands=['link'])

def main(message):
    bot.send_message(message.chat.id, 'Держи [Сыллку](https://store.steampowered.com/app/2621150/_/?ref=dtf.ru) на войну', parse_mode='Markdown')


@bot.message_handler(commands=['pay'])

def main(message):
    bot.send_message(message.chat.id, 'Продал душу ящерам? Вы добровольно отдали последние РУБЛИ РУССКИЕ ящерам!!!', parse_mode='Markdown')


@bot.message_handler(commands=['who'])

def main(message):
    bot.send_message(message.chat.id, 'Богатырь Алескей Михеев!')


@bot.message_handler(commands=['exit'])

def main(message):
    bot.send_message(message.chat.id, 'Война окончена! Русы всегда побеждают!')



@bot.message_handler(commands=['help'])

def main(message):
    bot.send_message(message.chat.id, 'Вот команды для начала войны с ЯЩЕРАМИ! \n /start - Запуск бота \n /help - Узнать команды \n /link - Сыллка на войну \n /run - Начать войну! \n /exit - Закончить войну! \n /who - Узнать имя создателя бота(истинного Руса)')

bot.infinity_polling()
