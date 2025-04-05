# Étape 1 : image légère
FROM python:3.12-slim

# Ajout utilisateur non-root
RUN addgroup --system app && adduser --system --group app

# Dossier de travail
WORKDIR /app

# Fichiers nécessaires
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Droits de l’utilisateur
USER app

CMD ["python", "main.py"]
