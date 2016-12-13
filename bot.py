from telegram.ext import Updater , CommandHandler ,  MessageHandler, Filters,  InlineQueryHandler, CallbackQueryHandler
from telegram import KeyboardButton, ReplyKeyboardMarkup , InlineKeyboardMarkup
from answers import answers, get_answer, ask_user, zap



def main():
    updater = Updater("323969114:AAHaWaD1OcPqYiFi7ga9_8vakWWvdZJaXfI")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("wordcount", wordcount_user))
    dp.add_handler(CommandHandler("kalk", prov))
    dp.add_error_handler(show_error)
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    dp.add_handler(CommandHandler("новости", f_nov))
    dp.add_handler(CommandHandler("погода", f_weat))
    dp.add_handler(CommandHandler("kalk1", klava))
    dp.add_handler(CommandHandler("1", one))
    dp.add_handler(CommandHandler("2", two))
    dp.add_handler(CommandHandler("3", tree))
    dp.add_handler(CommandHandler("4", four))
    dp.add_handler(CommandHandler("5",five))
    dp.add_handler(CommandHandler("6", six))
    dp.add_handler(CommandHandler("7", seven))
    dp.add_handler(CommandHandler("8", eigtht))
    dp.add_handler(CommandHandler("9", nine)) 
    dp.add_handler(CommandHandler("0", zero)) 
    dp.add_handler(CommandHandler("-", minus))
    dp.add_handler(CommandHandler("÷", podel)) 
    dp.add_handler(CommandHandler("*", umn)) 
    dp.add_handler(CommandHandler("+", plus))
    dp.add_handler(CommandHandler("=", ravno))
    updater.start_polling()
    updater.idle()

q = []

def ravno  (bot, update):

    if "+" in  q:
        a=q.index("+")
        b=q[0:a]
        s=''
        b=s.join(b)
        z=q[(a+1):]
        z = s.join(z)
        b=float(b)
        z=float(z)
        bot.sendMessage(update.message.chat_id,(b+z))
        q.clear()        
    elif "-" in q:
        a=q.index("-")
        b=q[0:a]
        s=''
        b=s.join(b)
        z=q[(a+1):]
        z = s.join(z)
        b=float(b)
        z=float(z)
        bot.sendMessage(update.message.chat_id,(b-z))
        q.clear()
    elif "*" in q: 
        a=q.index("*")
        b=q[0:a]
        s=''
        b=s.join(b)
        bot.sendMessage(update.message.chat_id,(b))
        z=q[(a+1):]
        z = s.join(z)
        b=float(b)
        z=float(z)
        bot.sendMessage(update.message.chat_id,(b*z))
        q.clear()
    elif "÷" in q:     
        a=q.index("÷")
        b=q[0:a]
        s=''
        b=s.join(b)
        z=q[(a+1):]
        z = s.join(z)
        b=float(b)
        z=float(z)
        bot.sendMessage(update.message.chat_id,(b/z))
        q.clear()
q.clear()            

def one(bot, update):
    a="1"
    q.append(a)
    return a

def two(bot, update):
    b="2"
    q.append(b)
    return b

def tree(bot, update):
    c="3"
    q.append(c)
    return c  

def four(bot, update):
    d="4"
    q.append(d)
    return d    

def five(bot, update):
    e="5"
    q.append(e)
    return e    

def six(bot, update):
    f="6"
    q.append(f)
    return f           

def seven(bot, update):
    g="7"
    q.append(g)
    return g

def eigtht(bot, update):
    h="8"
    q.append(h)
    return h   

def nine(bot, update):
    i="9"
    q.append(i)
    return i

def zero(bot, update):
    j="0"
    q.append(j)
    return j

def minus(bot, update):
    k="-"
    q.append(k)
    return k

def podel(bot, update):
    l="÷"
    q.append(l)
    return l

def umn(bot, update):
    m="*"
    q.append(m)
    return m

def plus(bot, update):
    n="+"
    q.append(n)
    return n                           

def klava(bot, update):
    keyboard = [[KeyboardButton('/1'), KeyboardButton('/2'),KeyboardButton('/3')],
                [KeyboardButton('/4'), KeyboardButton('/5'),KeyboardButton('/6')],
                [KeyboardButton('/7'), KeyboardButton('/8'),KeyboardButton('/9')],
                [KeyboardButton('/0'), KeyboardButton('/+'),KeyboardButton('/-')],
                [KeyboardButton('/*'), KeyboardButton('/÷'),KeyboardButton('/=')]]
   
    reply_markup = ReplyKeyboardMarkup(keyboard)
    bot.sendMessage(update.message.chat_id, text='Вводи', reply_markup = reply_markup)
    print(q)





def kalk_user(bot, update):
    bot.sendMessage(update.message.chat_id,  text=  "введите выражение в виде : /kalk проблел значение пробел \
        знак пробел = ")
    i = update.message.text
    i= i.strip()
    if "=" in i: 
        if " " in i:
            i= i.split(" ")
            print(i)
            
            i.pop(0)
            i.pop()
            print(i)
            a=float(i[0])
            b=float(i[2])
            t= i.pop(1)
            if t == "+":
                bot.sendMessage(update.message.chat_id, (a+b))
            elif t == "-":
                bot.sendMessage(update.message.chat_id, (a-b))
            elif t == "/":
                bot.sendMessage(update.message.chat_id,(a/b))
            elif t == "*":
                bot.sendMessage(update.message.chat_id,(a*b))
            else:
                bot.sendMessage(update.message.chat_id,  text= "этот знак в разработке") 
        else:
            bot.sendMessage(update.message.chat_id,  text= "возможно вы что то не правильно ввели, забыли пробел между \
                символами или ещё что-то")    
    else:
        bot.sendMessage(update.message.chat_id,  text="вы забыли знак = ")

def prov(bot, update):
    ##проверка для элементарного калькулятора
    try:
        return kalk_user(bot, update)
    except (ZeroDivisionError , ValueError, TypeError, IndexError) :
        return bot.sendMessage(update.message.chat_id,  text="вы забыли ввести значение или поделили на 0 !")   


def wordcount_user(bot, update):
    b = update.message.text
    b=b.strip()
    b=b.split('"')
    if len(b[0].split(" ")) != 1:
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


if __name__ == '__main__':
    main()
