FROM python:3.9

ADD punishmentbot.py .

WORKDIR /usr/src/bot

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install -U git+https://github.com/Rapptz/discord.py

CMD ["python3", "./punishmentbot.py"]
