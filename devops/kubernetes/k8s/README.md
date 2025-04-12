# Kubernetes Manifests - Web App

## 📄 Fichiers

- `deployment.yaml` : déploiement de l'image nginx
- `service.yaml` : service NodePort exposant l'application

## 🚀 Déploiement

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
