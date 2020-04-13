import praw
import random
import requests
import yaml

reddit_config = 'auth.yaml'
with open("auth.yaml", 'r') as config_file:
    config = yaml.safe_load(config_file)

reddit = praw.Reddit(client_id=config['reddit']['client_id'],
                     client_secret=config['reddit']['client_secret'],
                     password=config['reddit']['password'],
                     user_agent=config['reddit']['user_agent'],
                     username=config['reddit']['username'])


class Funks():
    def meme(update, context):
        """sends meme from reddit"""
        subreddit_two = reddit.subreddit('programmingmemes+ProgrammerHumor').hot(limit=12)
        pics = []
        titles = []
        for submission in subreddit_two:
            title = submission.title
            url = submission.url
            if url.endswith(('.jpg', '.png', '.jpeg')):
                titles.append(title)
                pics.append(url)

        number = range(len(pics))
        choice = random.choice(number)

        context.bot.sendMessage(chat_id=update.message.chat_id, text=titles[choice])
        context.bot.sendPhoto(chat_id=update.message.chat_id, photo=pics[choice])

    def mayu(update, context):
        """Send miself"""
        picture = context.bot.get_user_profile_photos(context.bot.id, limit=1).photos[0]
        # link = context.bot.link
        # name = context.bot.username

        context.bot.sendMessage(chat_id=update.message.chat_id, text="Mayu desu!")
        context.bot.sendPhoto(chat_id=update.message.chat_id, photo=picture[0])

    def help(update, context):
        """Send a message when the command /help is issued."""
        update.message.reply_text('Help!')

    def echo(update, context):
        """Echo the user message."""
        update.message.reply_text(update.message.text)

    def start(update, context):
        """Send a message when the command /start is issued."""
        print(context.user_data)
        print(update.message)
        print(update._effective_user)
        update.message.reply_text('Hi! 😊')

    def location(update, context):
        user = update.message.from_user
        user_location = update.message.location
        print(user_location)
        print("*****")
        print(user)
        update.message.reply_text('Got your location :)')

    def coin(update, context):
        """Throws a coin"""
        choice = random.choice(['Heads!', 'Tails!'])
        update.message.reply_text(choice)

    def weather(update, context):
        """Shows Weather info"""
        message = update.message.text.split()
        try:
            location = message[1]
        except Exception:
            location = ""

        r = requests.get('https://wttr.in/{}?format=%l:+%c+%t+%w'.format(location))
        context.bot.sendMessage(chat_id=update.message.chat_id, text=r.text)

    def horos(update, context):
        message = update.message.text.split()
        sign = message[1]

        params = (('sign', sign),
                  ('day', 'today'))

        request = requests.post('https://aztro.sameerkumar.website/', params=params)
        signs = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra',
                 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']

        if sign.lower() == "help":
            context.bot.sendMessage(chat_id=update.message.chat_id, text=("Signs: " + str(signs)))

        if request.status_code == 200:
            data = request.json()
            lucky_time = data['lucky_time']
            description = data['description']
            color = data['color']
            mood = data['mood']
            lucky_number = int(data['lucky_number'])

            result = "{}\n🔮*Mood:* {}\n🌈*Color:* {}\n⏰*Lucky Time:* {}\n🔢*Lucky Number:* {}".format(description, mood, color, lucky_time, lucky_number)

            context.bot.sendMessage(chat_id=update.message.chat_id, text=result, parse_mode="Markdown")
