from flask import Flask
import redis
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration Redis
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def visits():
    try:
        count = cache.incr('visits')
        logger.info(f"Nouvelle visite! Compteur: {count}")
        return f"Vous êtes le visiteur numéro {count}"
    except Exception as e:
        logger.error(f"Erreur Redis: {str(e)}")
        return "Erreur de connexion à Redis", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)