from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Mon premier serveur Flask dans Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')