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
    updater.start_polling()
    updater.idle()
    