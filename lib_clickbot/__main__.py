from .clickbot import Clickbot as Bot

def main():
    bot = Bot()
    bot.configure()
    bot.run()
