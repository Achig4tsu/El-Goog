FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN python -m venv /app/venv
RUN /bin/bash -c "source /app/venv/bin/activate && pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt"

COPY . .

# Installation de mariadb-client
RUN apt-get update && apt-get install -y mariadb-client

# Copie du script d'attente
COPY wait-for-it.sh /usr/local/bin/wait-for-it.sh
RUN chmod +x /usr/local/bin/wait-for-it.sh

# Commande pour lancer le programme Python
CMD ["sh", "-c", "source /app/venv/bin/activate && python my_crawler_app.py"]
