# Dockerfile pour l'application Flask
FROM python:3.11-slim

WORKDIR /app

# Copier les fichiers source
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port Flask
EXPOSE 5000

# Commande pour exécuter l'application Flask
CMD ["python", "main.py"]
