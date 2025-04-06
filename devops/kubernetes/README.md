# le Control Plane est essentiel, car c’est le cerveau de Kubernetes.


## C’est lui qui prend toutes les décisions, gère l’état global du cluster, et oriente ce qui se passe dans les nœuds (les machines qui font tourner tes apps).

### 🔗 Comment ça fonctionne ensemble ? (workflow simplifié)

## Tu fais un kubectl apply -f mon-app.yaml

kubectl parle à API Server

API Server écrit l’info dans etcd (état désiré)

Controller Manager voit qu’un objet Deployment est demandé

Il crée un ReplicaSet qui veut 3 pods par exemple

Scheduler choisit sur quels nœuds ces pods vont tourner

Les Workers exécutent les conteneurs


[kubectl] ───▶ [API Server] ───▶ [etcd] (stocke état désiré)
                         │
                         ▼
               [Controller Manager] (crée ReplicaSet → Pods)
                         ▼
                  [Scheduler] (choisit les Nodes)
                         ▼
        [Node A] ←───────────────→ [Node B]
        (Pod: nginx)               (Pod: nginx)



+-----------------------------+
|        Control Plane        |
|-----------------------------|
|                             |
|  [API Server]  ◄─────┐      |
|       ▲              │      |
|       │              ▼      |
|  [kubectl]       [etcd]     |  <- Stockage de l’état (pods, nodes, services, etc.)
|       ▼              ▲      |
|  [Controller Manager]│      |  <- Détecte les écarts entre réel et désiré
|       ▼              │      |
|  [Scheduler]─────────┘      |  <- Décide "où" placer les pods
+-----------------------------+



                       [ Kubernetes Cluster ]
                                 |
                    +-----------------------------+
                    |       Control Plane         |
                    |-----------------------------|
                    | - API Server                |
                    | - Scheduler                 |
                    | - Controller Manager        |
                    | - etcd (Cluster State DB)   |
                    +-----------------------------+
                                 |
       ┌────────────────────────────────────────────────────┐
       │                    Nodes (x2)                      │
       │────────────────────────────────────────────────────│
       │     Node A                          Node B         │
       │ ┌─────────────┐               ┌─────────────┐      │
       │ │ Pod: App v1 │◄───Load─────►│ Pod: App v1 │      │
       │ └─────────────┘   Balancer   └─────────────┘      │
       │ ┌─────────────┐               ┌─────────────┐      │
       │ │ Pod: App v1 │               │ Pod: App v1 │      │
       │ └─────────────┘               └─────────────┘      │
       └────────────────────────────────────────────────────┘
                                 |
                          [ Service ]
                                 |
                    [ Expose via Ingress / LoadBalancer ]
                                 |
                         🌍 Internet / Clients