import feedparser
import telebot

bot = telebot.TeleBot('EH VOLEVI')

feed = feedparser.parse('http://www.xvideos.com/rss/rss.xml')

def message_handler(messages):

    for message in messages:

        if message.text:

            if message.text == '/start':
                bot.reply_to(message, 'Hey Fapper, thank you!' )

            if message.text == '/lastfeed':
                bot.send_message(message.chat.id, '<b>' + feed['entries'][1]['title'] + '</b> \n\n' + str(feed['entries'][1]['links'][0]['href']), parse_mode='HTML')


bot.set_update_listener(message_handler)
bot.polling()
