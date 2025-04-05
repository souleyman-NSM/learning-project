

# 🎯 Objectif du projet
### Créer une petite API Python (Flask) qui se connecte à une base de données PostgreSQL, le tout dans des conteneurs Docker isolés, grâce à Docker Compose.

🧠 En résumé :

🧰 docker-compose.yml	Décrit et lance toute l’infra (web + db + réseau + volumes)
📄 Dockerfile	Construit l’image du conteneur Flask à partir de ton code
🌐 Navigateur (client)	Utilisateur final qui teste l’API via l’URL http://localhost:5000
🚀 Flask App (web)	Appli Python qui traite les requêtes et parle à la DB
🐘 PostgreSQL (db)	Stocke les données, accessible via le conteneur web en interne


#### Mettre en place une architecture applicative moderne basée sur Docker, composée de :



┌────────────┐     HTTP      ┌────────────┐
│ Navigateur │  ─────────▶  │ Flask App  │                          
└────────────┘               └────┬───────┘
                                 │
                           Connexion TCP
                                 │
                           ┌─────▼─────┐
                           │PostgreSQL │
                           └───────────┘

┌────────────┐   🌐 HTTP (port 5000)   ┌─────────────────────────────┐
│ Navigateur │ ─────────────────────▶ │  🚀 Flask App (web)         │
│  (Client)  │                        │  ───────────────             │
└────────────┘                        │  📄 main.py                  │
                                     │  📦 Docker (Python:3.12-slim)│
                                     │  📁 requirements.txt         │
                                     └────────┬────────────────────┘
                                              │ Connexion TCP (5432)
                                              ▼
                                   ┌─────────────────────────────┐
                                   │ 🐘 PostgreSQL (db)          │
                                   │ ───────────────             │
                                   │ 📦 Image : postgres:15       │
                                   │ 📁 Volume persistant         │
                                   └─────────────────────────────┘
