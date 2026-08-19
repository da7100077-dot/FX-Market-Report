import logging
import threading
from aiohttp import web
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from config import BOT_TOKEN, WEBHOOK_URL, WEBHOOK_SECRET, PORT
from utils import fetch_exchange_rates
from constants import (
    WELCOME_TEXT, HELP_TEXT, ABOUT_TEXT, DISCLAIMER_TEXT,
    EDUCATION_TOPICS, MAIN_MENU_BUTTONS
)

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

CB_MAIN_MENU = "menu"
CB_OVERVIEW = "overview"
CB_PAIRS = "pairs"
CB_EDUCATION = "education"
CB_CALENDAR = "calendar"
CB_ABOUT = "about"
CB_DISCLAIMER = "disclaimer"
CB_BACK = "back"
EDU_CB_PREFIX = "edu_"
PAIRS_CB_PREFIX = "pairs_"
PAIRS_BASES = ["USD", "EUR", "GBP", "JPY", "CHF", "AUD", "CAD", "NZD"]

def main_menu_keyboard():
    buttons = [[InlineKeyboardButton(text, callback_data=data)] for text, data in MAIN_MENU_BUTTONS]
    return InlineKeyboardMarkup(buttons)

def back_button():
    return InlineKeyboardMarkup([[InlineKeyboardButton("« Back", callback_data=CB_BACK)]])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_TEXT, reply_markup=main_menu_keyboard())

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP_TEXT, reply_markup=main_menu_keyboard())

async def market_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await show_overview(update, context, send_new=True)

async def pairs_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await show_pairs_menu(update, context, send_new=True)

async def education_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await show_education_menu(update, context, send_new=True)

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(ABOUT_TEXT, reply_markup=back_button())

async def disclaimer_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(DISCLAIMER_TEXT, reply_markup=back_button())

async def show_overview(update: Update, context: ContextTypes.DEFAULT_TYPE, send_new=False):
    if update.callback_query:
        await update.callback_query.answer()
    rates = await fetch_exchange_rates("USD")
    if rates is None:
        text = "Market data temporarily unavailable. Please try again later."
    else:
        pairs_display = []
        for pair in ["EUR", "GBP", "JPY", "CHF", "AUD", "CAD", "NZD"]:
            if pair in rates:
                pairs_display.append(f"{pair}/USD: {rates[pair]:.4f}")
        text = "📊 *Market Overview (base: USD)*\n\n" + "\n".join(pairs_display)
    if send_new:
        await update.message.reply_text(text, reply_markup=back_button(), parse_mode="Markdown")
    else:
        await update.callback_query.edit_message_text(text, reply_markup=back_button(), parse_mode="Markdown")

async def show_pairs_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, send_new=False):
    buttons = [[InlineKeyboardButton(base, callback_data=f"{PAIRS_CB_PREFIX}{base}")] for base in PAIRS_BASES]
    buttons.append([InlineKeyboardButton("« Back", callback_data=CB_BACK)])
    keyboard = InlineKeyboardMarkup(buttons)
    text = "Select a base currency to see exchange rates:"
    if send_new:
        await update.message.reply_text(text, reply_markup=keyboard)
    else:
        await update.callback_query.edit_message_text(text, reply_markup=keyboard)
        await update.callback_query.answer()

async def show_pairs_rates(update: Update, context: ContextTypes.DEFAULT_TYPE, base: str):
    await update.callback_query.answer()
    rates = await fetch_exchange_rates(base)
    if rates is None:
        text = "Market data temporarily unavailable. Please try again later."
    else:
        lines = [f"{curr}: {rates[curr]:.4f}" for curr in sorted(rates.keys()) if curr != base]
        lines = lines[:20]
        text = f"💱 *Exchange Rates (base: {base})*\n\n" + "\n".join(lines)
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("« Back to bases", callback_data=CB_PAIRS)]])
    await update.callback_query.edit_message_text(text, reply_markup=keyboard, parse_mode="Markdown")

async def show_education_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, send_new=False):
    buttons = [[InlineKeyboardButton(topic["title"], callback_data=f"{EDU_CB_PREFIX}{key}")]
               for key, topic in EDUCATION_TOPICS.items()]
    buttons.append([InlineKeyboardButton("« Back", callback_data=CB_BACK)])
    keyboard = InlineKeyboardMarkup(buttons)
    text = "📚 Select a topic to learn about forex:"
    if send_new:
        await update.message.reply_text(text, reply_markup=keyboard)
    else:
        await update.callback_query.edit_message_text(text, reply_markup=keyboard)
        await update.callback_query.answer()

async def show_education_topic(update: Update, context: ContextTypes.DEFAULT_TYPE, topic_key: str):
    await update.callback_query.answer()
    topic = EDUCATION_TOPICS.get(topic_key)
    text = f"*{topic['title']}*\n\n{topic['content']}" if topic else "Sorry, that topic is not available."
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("« Back to topics", callback_data=CB_EDUCATION)]])
    await update.callback_query.edit_message_text(text, reply_markup=keyboard, parse_mode="Markdown")

async def show_calendar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    text = "📅 Economic Calendar is not configured. You can add an Alpha Vantage API key later to enable this feature."
    await update.callback_query.edit_message_text(text, reply_markup=back_button())

async def show_about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(ABOUT_TEXT, reply_markup=back_button())

async def show_disclaimer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(DISCLAIMER_TEXT, reply_markup=back_button())

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data
    if data == CB_MAIN_MENU:
        await show_main_menu(update, context)
    elif data == CB_OVERVIEW:
        await show_overview(update, context)
    elif data == CB_PAIRS:
        await show_pairs_menu(update, context)
    elif data.startswith(PAIRS_CB_PREFIX):
        await show_pairs_rates(update, context, data[len(PAIRS_CB_PREFIX):])
    elif data == CB_EDUCATION:
        await show_education_menu(update, context)
    elif data.startswith(EDU_CB_PREFIX):
        await show_education_topic(update, context, data[len(EDU_CB_PREFIX):])
    elif data == CB_CALENDAR:
        await show_calendar(update, context)
    elif data == CB_ABOUT:
        await show_about(update, context)
    elif data == CB_DISCLAIMER:
        await show_disclaimer(update, context)
    elif data == CB_BACK:
        await show_main_menu(update, context)
    else:
        await query.answer("Unknown option", show_alert=False)

async def show_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.edit_message_text(
        "Welcome to FX Market Report. Please select an option:",
        reply_markup=main_menu_keyboard()
    )
    await update.callback_query.answer()

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(msg="Exception:", exc_info=context.error)
    if update and update.effective_message:
        await update.effective_message.reply_text("An unexpected error occurred. Please try again later.")

async def health_check(request):
    return web.Response(text="OK", status=200)

def run_health_server():
    """Run a minimal HTTP server for health checks (used in polling mode)."""
    app = web.Application()
    app.router.add_get("/", health_check)
    app.router.add_get("/health", health_check)
    web.run_app(app, host="0.0.0.0", port=PORT)

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("market", market_command))
    application.add_handler(CommandHandler("pairs", pairs_command))
    application.add_handler(CommandHandler("education", education_command))
    application.add_handler(CommandHandler("about", about_command))
    application.add_handler(CommandHandler("disclaimer", disclaimer_command))
    application.add_handler(CallbackQueryHandler(button_callback))
    application.add_error_handler(error_handler)

    commands = [
        BotCommand("start", "Start the bot and show menu"),
        BotCommand("help", "Get help"),
        BotCommand("market", "Show market overview"),
        BotCommand("pairs", "View exchange rates"),
        BotCommand("education", "Learn about forex"),
        BotCommand("about", "About this bot"),
        BotCommand("disclaimer", "Legal disclaimer"),
    ]
    application.bot.set_my_commands(commands)

    if WEBHOOK_URL:
        webhook_path = f"/{BOT_TOKEN}"
        full_webhook_url = f"{WEBHOOK_URL.rstrip('/')}{webhook_path}"
        application.bot.set_webhook(url=full_webhook_url, secret_token=WEBHOOK_SECRET)
        logger.info(f"Webhook set to {full_webhook_url}")
        web_app = web.Application()
        web_app.router.add_get("/", health_check)
        web_app.router.add_get("/health", health_check)
        application.run_webhook(
            listen="0.0.0.0", port=PORT, url_path=webhook_path,
            webhook_url=full_webhook_url, secret_token=WEBHOOK_SECRET,
            webhook_app=web_app
        )
    else:
        logger.info("WEBHOOK_URL not set. Starting in polling mode with health server.")
        thread = threading.Thread(target=run_health_server, daemon=True)
        thread.start()
        application.run_polling()

if __name__ == "__main__":
    main()
