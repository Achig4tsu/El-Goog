FROM python:3.9

WORKDIR /app

COPY . .

# Création et activation de l'environnement virtuel Python
RUN python -m venv venv
RUN /bin/bash -c "source venv/bin/activate"

# Installation des dépendances Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python3" , "./Scripts/Crawler.py"]