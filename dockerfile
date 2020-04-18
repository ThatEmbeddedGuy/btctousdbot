FROM python:3
RUN pip install cachetools requests httmock python-telegram-bot[socks] python-telegram-bot
ADD . /
CMD [ "python", "./__main__.py" ]