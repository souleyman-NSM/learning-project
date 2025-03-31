# Image de base ubuntu
FROM python

# Dossier de travail dans le conteneur  Le conteneur travaillera dans /app.
WORKDIR /app

# Copier les fichiers api et requirements  avec le . pour dire dans le dossier meme 
COPY app.py .
COPY requirements.txt .

# Installer les dépendances 
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade pip

# commande de demarrage
CMD ["python", "app.py"]