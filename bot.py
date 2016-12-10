from telegram.ext import Updater , CommandHandler ,  MessageHandler, Filters,  InlineQueryHandler, CallbackQueryHandler
from telegram import KeyboardButton, ReplyKeyboardMarkup , InlineKeyboardMarkup
from answers import answers, get_answer, ask_user, zap



def main():
    updater = Updater("323969114:AAHaWaD1OcPqYiFi7ga9_8vakWWvdZJaXfI")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("wordcount", wordcount_user))
    dp.add_error_handler(show_error)
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    dp.add_handler(CommandHandler("новости", f_nov))
    dp.add_handler(CommandHandler("погода", f_weat))
    updater.start_polling()
    updater.idle()
    dp.message_handler(content_types=["YA"])


def wordcount_user(bot, update):
    b = update.message.text
    b=b.strip()
    print(b)
    b=b.split('"')
    print(b)
    if len(b) == 1:
        bot.sendMessage(update.message.chat_id,  text=  " нет кавычек ")
    else:    
        c=b.pop(0)
        c= b.pop(-1)
        print(b)
        e = b[0].split(" ")
        print(e)
        r = len(e)
        print(r)
        if len(b[0])== 0:
            bot.sendMessage(update.message.chat_id,  text=  " нет слов ")

        else:    
            bot.sendMessage(update.message.chat_id,  text= str(r) + " слова")
        

def f_nov(bot, update):
    bot.sendMessage(update.message.chat_id, text= "https://telegram.me/lentach")

def f_weat(bot, update):
    bot.sendMessage(update.message.chat_id, text= "@pogod_bot")    

def greet_user(bot, update):
    keyboard = [[KeyboardButton('/новости'), KeyboardButton('/погода')]]
    reply_markup = ReplyKeyboardMarkup(keyboard)
    bot.sendMessage(update.message.chat_id, text='Выбирай', reply_markup = reply_markup)

def show_error(bot, update, error):
    print('Update "{}" caused error "{}"'.format(update, error))   

def talk_to_me(bot, update):
    print("Пришло сообщение: " + update.message.text)
    update.message.text=update.message.text.lower()
    bot.sendMessage(update.message.chat_id, get_answer(update.message.text,answers))

def default_test(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)    

if __name__ == '__main__':
    main()
