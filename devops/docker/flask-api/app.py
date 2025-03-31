from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur mon API Dockerisée !"

@app.route('/api/hello')
def hello():
    return {"message": "Hello World!"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Permet d'écouter sur toutes les interfaces