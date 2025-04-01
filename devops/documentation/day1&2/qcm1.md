📝 QCM - Révision Jours 1 & 2
Coche la (ou les) bonne(s) réponse(s) pour chaque question.

1. Quelle commande permet de lister les fichiers/dossiers avec des détails comme les permissions ?

ls -a

ls -l

ls -h

cd /

Explication :

ls -l montre les permissions (rwxr-xr-x), le propriétaire et la taille.

ls -a affiche les fichiers cachés (. et ..).

2. Comment rendre un script backup.sh exécutable ?
chmod +r backup.sh

chmod +x backup.sh

chown root backup.sh

./backup.sh (sans modifier les permissions)

Explication :

+x ajoute le droit d’exécution.

./backup.sh ne marchera pas sans chmod +x d’abord.

3. Quel port est traditionnellement utilisé pour SSH ?
80

8000

22

443

Explication :

22 : SSH

80 : HTTP, 443 : HTTPS, 8000 : souvent utilisé pour des services dev.

4. Quelle commande permet de trouver quel processus utilise le port 8000 ?
ping 8000

sudo lsof -i :8000

netstat -a

ss -l

Explication :

lsof -i :8000 liste le processus écoutant sur le port 8000.

netstat -a montre toutes les connexions, mais moins lisible.

5. Que fait la commande python3 -m http.server 8080 ?
Installe un serveur web

Lance un serveur web local sur le port 8080

Télécharge une page HTML

Affiche la version de Python

Explication :

C’est un serveur web minimaliste pour partager des fichiers dans le dossier courant.

6. Comment copier un dossier projects vers backup en CLI ?

mv projects backup

cp -r projects backup

mkdir backup && ls projects > backup

rm -rf projects

Explication :

-r (récursif) est nécessaire pour copier un dossier.

mv déplace, ne copie pas.

📊 Correction
ls -l

chmod +x backup.sh

22

sudo lsof -i :8000

Lance un serveur web local sur le port 8080

cp -r projects backup


6/6