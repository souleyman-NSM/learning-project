# 🧱 C’est quoi un Node ?

## 🔬 Définition simple et scientifique :

    Un Node est une machine physique ou virtuelle dans un cluster Kubernetes, capable d’exécuter des pods (c’est-à-dire des conteneurs).

    C’est l’unité de calcul réelle du cluster.

Chaque Node contient :

    kubelet → l’agent qui parle au Control Plane

    container runtime (ex: Docker, containerd) → pour exécuter les conteneurs

    kube-proxy → pour gérer le réseau

## 🧠 Analogie :

    Si Kubernetes est une usine, le Control Plane est le cerveau/manager, et les Nodes sont les ouvriers qui font le boulot (faire tourner les apps dans des conteneurs).


## 🧠 JEU DE RÔLE : Tu es le Control Plane !

Prêt ? 😎
Je vais jouer le rôle de l’utilisateur DevOps. Toi, tu es le Control Plane Kubernetes. Tu as 4 fonctions principales :

🎤 API Server (tu reçois les requêtes)

🧠 etcd (tu stockes l’état)

🦾 Controller Manager (tu surveilles les objets et prends action)

🧭 Scheduler (tu choisis un nœud pour chaque Pod )