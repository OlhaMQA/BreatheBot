import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
import time

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Let's do some breathing."
                                        "\nSelect the exercise:"
                                        "\n/box_breathing"
                                        "\n/deep_breathing"
                                        "\n/loud_breathing")


async def inhale(update: Update, context: ContextTypes.DEFAULT_TYPE, timer):
    time.sleep(timer)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Deep inhale")


async def exhale(update: Update, context: ContextTypes.DEFAULT_TYPE, timer):
    time.sleep(timer)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Slow exhale")


async def loud_exhale(update: Update, context: ContextTypes.DEFAULT_TYPE, timer):
    time.sleep(timer)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Slow exhale making a 'ha' sound")


async def hold(update: Update, context: ContextTypes.DEFAULT_TYPE, timer):
    time.sleep(timer)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Hold for 4 seconds")


async def namaste(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Thank you for breathing with me. Namaste")


async def box_breath(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                text=" Inhale through your nose for a count of 4. \nHold your breath for a count of 4. "
                                "\nExhale through your mouth for a count of 4. \nHold your breath for a count of 4. "
                                "\nRepeat for 4 rounds with me.")
    for i in range(4):
        await inhale(update, context, 4)
        await hold(update, context, 4)
        await exhale(update, context, 4)
        await hold(update, context, 4)
    time.sleep(4)
    await namaste(update, context)




async def deap_breath(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Place one hand on your belly and the other on your chest. "
                                        "Inhale deeply through your nose, feeling your belly rise as you breathe in."
                                        " Exhale slowly through your mouth, feeling your belly fall. "
                                        "Repeat for several breaths.")
    for i in range(4):
        await inhale(update, context, 6)
        await exhale(update, context, 7)
    time.sleep(6)
    await namaste(update, context)


async def loud_breath(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Inhale deeply through your nose. "
                                        "Exhale forcefully through your mouth, "
                                        "sticking out your tongue and making a 'ha' sound. "
                                        "Repeat for several breaths.")
    for i in range(4):
        await inhale(update, context, 4)
        await loud_exhale(update, context, 7)
    time.sleep(6)
    await namaste(update, context)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


if __name__ == '__main__':
    application = ApplicationBuilder().token('6157906978:AAFIekVe6AtDClBp_4SGrIs2oyQqvFD2G5k').build()

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    deep_breath_handler = CommandHandler('deep_breathing', deap_breath)
    box_breath_handler = CommandHandler('box_breathing', box_breath)
    loud_breath_handler = CommandHandler('loud_breathing', loud_breath)

    application.add_handler(start_handler)
    application.add_handler(deep_breath_handler)
    application.add_handler(loud_breath_handler)
    application.add_handler(box_breath_handler)
    application.add_handler(unknown_handler)

    application.run_polling()
