from aiogram import Dispatcher

from app.handlers.private import start, last


def setup(dp: Dispatcher):
    start.setup(dp)
    last.setup(dp)
