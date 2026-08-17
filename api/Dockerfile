# 1. Image de base : un Linux ultra-léger avec Python 3.11 préinstallé
FROM python:3.11-slim

# 2. Définir le dossier de travail à l'intérieur du conteneur
WORKDIR /app

# 3. Copier la liste des dépendances et les installer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copier le code source de l'API
COPY main.py .

# 5. Indiquer que le conteneur écoutera sur le port 8000
EXPOSE 8000

# 6. La commande exécutée au démarrage du conteneur
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
