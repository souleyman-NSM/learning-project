# Jour 3 : SSH & Gestion des Processus  
**Objectif** : Se connecter à distance et contrôler les applications en cours d'exécution.  

---

## 📦 Prérequis  
- Machine Linux (ou WSL pour Windows)  
- Accès terminal  
- Service SSH installé (`sudo apt install openssh-server`)  

---

## 🔑 SSH (Secure Shell)  

### 1. Connexion de base  
```bash
ssh utilisateur@ip_du_serveur  # Exemple : ssh souleyman@192.168.1.100

```

### 2. Authentification par clés (sans mot de passe)  

→ Les clés sont stockées dans ~/.ssh/id_ed25519 (privée) et ~/.ssh/id_ed25519.pub (publique).

ssh-keygen -t ed25519  # Génère une paire de clés (appuyez sur Entrée pour les valeurs par défaut)  
ssh-copy-id utilisateur@ip_du_serveur  # Copie la clé publique sur le serveur  

## 🖥 Gestion des Processus
### 1. Lister les processus

    ps aux | grep python  

Colonnes clés :

USER : Propriétaire

PID : ID du processus (à noter pour kill)

%CPU : Utilisation CPU

### 2. Tuer un processus

    kill -9 <PID>  # Remplacez <PID> par l'ID du processus  

### 3. Lancer un processus en arrière-plan


    python3 -m http.server 8000 &  # Le '&' détache le processus  

### 4. Garder un processus actif après déconnexion

nohup python3 -m http.server 8000 &  # Les logs sont dans `nohup.out`  

## 🚀 Exercices Pratiques

### 1. SSH Local

    ssh-copy-id souleyman@localhost  # Configure l'authentification sans mot de passe  
    ssh souleyman@localhost  # Connectez-vous  

### 2. Gestion de Processus

# Lancez un serveur Python  

    python3 -m http.server 8000 &  

# Trouvez et tuez-le  

ps aux | grep http.server  
kill -9 <PID>  

### 3. Transfert de Fichiers


    scp ~/test.txt souleyman@localhost:/home/souleyman/  

## 📚 Ressources

    Documentation OpenSSH

    Gestion des processus avec ps

    scp fichier.txt user@ip:/chemin/

---