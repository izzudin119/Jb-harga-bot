from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes, CommandHandler

TOKEN = "8921874654:AAGRjru_vemyoJhZrQklI5sOt3B7xuag9VQ"

HARGA = {
    "MESSI": 80, "RONALDO": 70, "HAALAND": 60, "MBAPPE": 50, "NEYMAR": 40,
    "BELLINGHAM": 55, "VINI": 60, "PEDRI": 45
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hantar je nama player cth: Messi Ronaldo Haaland\nAku terus kira harga 💰")

async def kira(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.upper()
    total = 0
    jumpa = ""
    for nama, harga in HARGA.items():
        if nama in text:
            jumpa += f"- {nama} RM{harga}\n"
            total += harga
    if total == 0:
        await update.message.reply_text("Tak jumpa player tu bro.")
    else:
        await update.message.reply_text(f"✅ JUMPA:\n{jumpa}\n💰 TOTAL: RM{total} - RM{total+30}")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, kira))
app.run_polling()
