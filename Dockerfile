FROM python:alpine
RUN pip install pyTelegramBotAPI
WORKDIR /usr/src/
COPY bot.py .
ENTRYPOINT ["python", "bot.py"]
