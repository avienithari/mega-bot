FROM python:3.10-slim

COPY main.py .

COPY ./ .

RUN pip3 install requests python_dotenv discord.py

CMD ["python3", "main.py"]
