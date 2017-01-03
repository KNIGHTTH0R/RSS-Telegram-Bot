import feedparser
import telebot
import thread
import time

bot = telebot.TeleBot('EH VOLEVI!')

def check():
    while True:
        time.sleep(20)
        fappers_update()
        feed_update()

def fappers_update():
    global ffile
    global fappers
    global fappersl
    ffile = open('fappers.txt', 'r+')
    fappers = ffile.read()
    fappersl = fappers.split('\n')

fappers_update()

feed = feedparser.parse('http://www.xvideos.com/rss/rss.xml')

def feed_update():
    global feed
    global feed2
    feed2 = feedparser.parse('http://www.xvideos.com/rss/rss.xml')
    if not feed2['entries'][1]['title'] == feed['entries'][1]['title']:
        feed = feed2
        if not fappers == '':
            for element in fappersl:
                if not element == '':
                    bot.send_message(element, '<b>' + feed['entries'][1]['title'] + '</b> \n\n' + str(feed['entries'][1]['links'][0]['href']), parse_mode='HTML')

thread.start_new_thread( check, ())

def message_handler(messages):
    global f

    for message in messages:

        if message.text:

            if message.text == '/start':
                f = 0
                for element in fappersl:
                    if not message.from_user.id == element:
                        f += 1

                if f + 1 == len(fappersl):
                    ffile = open('fappers.txt', 'a')
                    ffile.write(str(message.from_user.id) + '\n')
                bot.reply_to(message, 'Hey Fapper, thank you!' )

            if message.text == '/lastfeed':
                bot.send_message(message.chat.id, '<b>' + feed['entries'][1]['title'] + '</b> \n\n' + str(feed['entries'][1]['links'][0]['href']), parse_mode='HTML')


bot.set_update_listener(message_handler)
bot.polling(none_stop=True)
