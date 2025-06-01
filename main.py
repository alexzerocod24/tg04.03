from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

API_TOKEN = '7609002030:AAE8gMC_oHPZz8UEhdS9yvDi7UXpGcSdNkQ'

async def dynamic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Показать больше", callback_data='show_more')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Нажмите кнопку ниже:", reply_markup=reply_markup)

async def show_more(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()


    keyboard = [
        [InlineKeyboardButton("Опция 1", callback_data='option_1')],
        [InlineKeyboardButton("Опция 2", callback_data='option_2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)


    await query.edit_message_text(text="Выберите опцию:", reply_markup=reply_markup)

async def option_1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Вы выбрали Опцию 1!")

async def option_2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Вы выбрали Опцию 2!")

if __name__ == '__main__':
    app = ApplicationBuilder().token(API_TOKEN).build()

    app.add_handler(CommandHandler("dynamic", dynamic))
    app.add_handler(CallbackQueryHandler(show_more, pattern='show_more'))
    app.add_handler(CallbackQueryHandler(option_1, pattern='option_1'))
    app.add_handler(CallbackQueryHandler(option_2, pattern='option_2'))

    print("Бот запущен...")
    app.run_polling()

