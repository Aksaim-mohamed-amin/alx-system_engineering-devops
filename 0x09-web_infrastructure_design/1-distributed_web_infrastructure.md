![Web Infrastructure](https:qsdqsd//github.com/Aksaim-mohamed-amin/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/1-distributed_web_infrastructure.png?raw=true)

# Specifics About the Infrastructure

## Additional Elements:

- **Load Balancer (HAProxy):** Added to distribute incoming traffic across multiple Nginx Servers, improving scalability, reliability, and fault tolerance.
- **Second Nginx Server:** Added for redundancy and high availability. In case one Nginx server fails, the other can continue serving traffic seamlessly.
- **Database Server (MySQL):** Added to store and manage the website's data. Separating the database from the application server enhances scalability and allows for efficient data management.

## Load Balancer Distribution Algorithm:

The HAProxy load balancer is configured with a Round Robin distribution algorithm. This algorithm distributes incoming requests evenly across all available Nginx servers in a cyclic manner. Each request is sent to the next server in the list, ensuring a balanced load distribution.

## Active-Active vs. Active-Passive Setup:

- **Active-Active Setup:** In this setup, both Nginx servers actively serve incoming traffic simultaneously. Each server independently handles requests, providing redundancy and load distribution. If one server fails, the other continues to serve traffic.
- **Active-Passive Setup:** In this setup, one Nginx server (active) serves traffic while the other (passive) remains idle as a backup. If the active server fails, the passive server takes over to serve traffic. This setup provides redundancy but may result in underutilization of resources.

## Database Primary-Replica (Master-Slave) Cluster:

In a Primary-Replica (or Master-Slave) database cluster, the Primary node (Master) handles write operations (e.g., INSERT, UPDATE, DELETE), while the Replica nodes (Slaves) replicate data from the Primary node and serve read operations (SELECT). Replication ensures data consistency and fault tolerance.

## Difference Between Primary and Replica Nodes:

- **Primary Node:** Handles write operations and is the authoritative source of data. It processes changes to the database and replicates them to Replica nodes.
- **Replica Node:** Replicates data from the Primary node and serves read operations. It provides scalability for read-heavy workloads and serves as a backup in case the Primary node fails.

# Issues with the Infrastructure:

1. **Single Point of Failure (SPOF):** The HAProxy load balancer may become a single point of failure. If it fails, traffic distribution will stop, leading to service disruption.
2. **Security Issues:** Lack of firewall protection and HTTPS encryption leaves the infrastructure vulnerable to unauthorized access, data interception, and other security threats.
3. **No Monitoring:** Without monitoring systems in place, it's challenging to identify and address performance issues, security breaches, or system failures promptly. This can lead to downtime and compromised user experience.
