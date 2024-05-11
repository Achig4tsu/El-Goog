FROM python:3.9

WORKDIR /app

# Copie des fichiers nécessaires dans le conteneur
COPY . .

# Création et activation de l'environnement virtuel Python
RUN python -m venv venv
RUN /bin/bash -c "source venv/bin/activate"

# Installation des dépendances Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Commande pour démarrer votre application
CMD [ "python", "test.py" ]