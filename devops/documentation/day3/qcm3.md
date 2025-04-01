# 📝 QCM de Révision - Jours 1 à 3

## Jour 1 : Bases Linux

### 1. Quelle commande crée un dossier "devops" et un fichier "test.txt" à l'intérieur ?
```bash
[ ] A. mkdir devops && cd test.txt
[✓] B. mkdir devops && touch devops/test.txt
[ ] C. ls devops/test.txt
[ ] D. cat devops > test.txt

```

### 2. Que montre ls -l ?

```bash
    [ ] A. Les fichiers cachés
    [✓] B. Les permissions, propriétaire et taille des fichiers
    [ ] C. L'historique des commandes
    [ ] D. L'utilisation du disque

```

Explication :
-l affiche le format long : -rw-r--r-- 1 user group 0 Mar 31 file.txt.

## Jour 2 : Permissions & Réseau

### 3.Comment rendre un script backup.sh exécutable ?

```bash

[ ] A. chmod +r backup.sh
[✓] B. chmod +x backup.sh
[ ] C. chown root backup.sh
[ ] D. ./backup.sh (sans modifier les permissions)

```

Astuce :
x = eXécution. Testez avec ./backup.sh après.

## Jour 3 : SSH & Processus

### 5. Que fait nohup python3 -m http.server & ?

```bash

[ ] A. Installe un serveur web
[✓] B. Lance un serveur web persistant après déconnexion
[ ] C. Affiche les processus Python
[ ] D. Tue le serveur web

nohup donne la persistance dans le code 
```

Détail :
nohup ignore le signal de déconnexion, & met en arrière-plan.

### 6. Comment transférer un fichier vers un serveur ?

```bash

[ ] A. ssh user@ip < fichier.txt
[✓] B. scp fichier.txt soule@ip:/chemin/
[ ] C. cp fichier.txt ssh:/chemin/
[ ] D. rsync fichier.txt user@ip

```

Bonus :
SCP = Secure Copy (basé sur SSH).

```bash

🔍 Correction
Question	Réponse	Points clés
1	B	mkdir + touch
2	B	ls -l = permissions
3	B	chmod +x pour exécution
4	C	Port 22 = SSH
5	B	nohup + & = persistant
6	B	scp pour transfert sécurisé  ## scp fichier.txt souleyman@1

```