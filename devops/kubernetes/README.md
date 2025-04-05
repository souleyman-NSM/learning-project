# le Control Plane est essentiel, car c’est le cerveau de Kubernetes.


## ’est lui qui prend toutes les décisions, gère l’état global du cluster, et oriente ce qui se passe dans les nœuds (les machines qui font tourner tes apps).


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


