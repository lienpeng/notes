kubectl 配置文件路径$HOME/.kube 下的config文件，其中$HOME为 /root或者 /admin

kubectl get pod/pods/po (name) (-o wide)-n jmq
kubectl describe pod -n jmq
kubectl exec -it name bash -n jmq



kubectl
kubectl

kubectl
kuBEctl

- Master
kube-apiserver
kube-controller-manager
kube-scheduler
etcd
- Node
kubelet 负责Pod对应容器的创建、启停
kube-proxy 实现service通信和负责均衡
Docker Engine

kubectl get nodes
kubectl describe node {name}

- Pod
1. 根容器 pause容器
    判断整组容器的存活状态
    业务容器共享pause容器的IP和挂载的volume
    在Kubernetes里，一个Pod里的容器与另外主机上的Pod容器能够直接通信。
2. 业务容器

静态Pod和普通Pod
静态Pod数据存储在具体Node上的具体文件里
普通Pod数据存入etcd


在8080端口（containerPort）启动容器进程。Pod的IP加上这里的容器端口（containerPort），组成了一个新的概念——Endpoint,用于对外通信

所以在Kubernetes里通常以千分之一的CPU配额为最小单位，用m来表示。通常一个容器的CPU配额被定义为100～300m，即占用0.1～0.3个CPU。

Requests：该资源的最小申请量，系统必须满足要求。
Limits：该资源最大允许使用的量，不能被突破，当容器试图使用超过这个量的资源时，可能会被Kubernetes“杀掉”并重启。

- label
基于等式的（Equality-based）和基于集合的（Set-based）
name = {}  name != {}
name in ({},{}) name not in 
可以通过多个Label Selector表达式的组合实现复杂的条件选择，多个表达式之间用“，”进行分隔即可，几个条件之间是“AND”的关系

作用：Pod副本数量、网络路由、负载均衡、Pod定向调度

rc Replicaton Controller
kubectl scale rc redis-slave --replicas=3

升级 Replica Set,支持基于集合的Label selector,主要被Deployment使用
matchExpressions:
    -{key:,operator:,value:[]}




