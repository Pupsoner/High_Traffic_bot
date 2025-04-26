from os import getenv
from ast import literal_eval
from dotenv import load_dotenv

load_dotenv()


class Configuration:

    bot_token: str = getenv("BOT_TOKEN")

    admins: list[int] = [int(i) for i in literal_eval(getenv('ADMINS'))]
