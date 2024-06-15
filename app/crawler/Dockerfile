FROM python:3.9-slim

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

RUN apt-get update && apt-get install -y netcat-openbsd

COPY . .

COPY wait-for-it.sh /usr/local/bin/wait-for-it.sh
RUN chmod +x /usr/local/bin/wait-for-it.sh

CMD ["/usr/local/bin/wait-for-it.sh", "mariadb:3306", "--", "python", "./Scripts/Crawler.py"]
