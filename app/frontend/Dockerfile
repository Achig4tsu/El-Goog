# Etape de build pour Node.js
FROM node:14 AS build-stage

WORKDIR /app
COPY . /app
RUN cd server && npm install

# Etape finale avec PHP et Apache
FROM php:7.4-apache

# Copier les fichiers depuis l'étape de build
COPY --from=build-stage /app /var/www/html

# Activer le module de réécriture Apache
RUN a2enmod rewrite

# Installer Node.js dans l'étape finale
RUN apt-get update && apt-get install -y curl && \
    curl -sL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get install -y nodejs && \
    cd /var/www/html/ && npm install

# Définir le répertoire de travail
WORKDIR /var/www/html

# Exposer le port 80 pour Apache
EXPOSE 80

# Commande pour lancer Apache en mode non-détaché et le serveur Node.js
CMD ["bash", "-c", "service apache2 start && cd /var/www/html/ && node ./server/server.js"]
