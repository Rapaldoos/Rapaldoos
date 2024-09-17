# Utiliser une image de base FastAPI avec Python 3.8
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

# Copier les fichiers de l'application dans le conteneur
COPY ./ /app

# Exposer le port 80 pour l'application
EXPOSE 80

# Lancer l'application avec Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
