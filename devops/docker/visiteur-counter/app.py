from flask import Flask
import redis

app = Flask(__name__)

# Connexion à Redis (modifie 'redis' par l'adresse réelle du conteneur Redis si nécessaire)
cache = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def visits():
    # Incrémente le compteur de visites
    count = cache.incr('visits')
    return f"Vous êtes le visiteur numéro {count}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)