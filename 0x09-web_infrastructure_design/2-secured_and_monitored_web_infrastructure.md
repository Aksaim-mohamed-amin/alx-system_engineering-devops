# Infrastructure Overview

![Web Infrastructure](https://github.com/Aksaim-mohamed-amin/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/2-secured_and_monitored_web_infrastructure.png?raw=true)

## Additional Elements:

- **Firewalls (3):** Added to control and monitor incoming and outgoing network traffic to and from the servers. Firewalls enhance security by enforcing access control policies and protecting against unauthorized access and cyber threats.

- **SSL Certificate:** Added to serve www.foobar.com over HTTPS. HTTPS encrypts the data transmitted between the user's browser and the server, ensuring confidentiality, integrity, and authenticity of the communication. It protects sensitive information such as login credentials, payment details, and personal data from interception and tampering.

- **Monitoring Clients (3):** Added to collect data about the performance, availability, and security of the infrastructure. Monitoring tools such as Sumo Logic collect metrics, logs, and events from various components to detect issues, troubleshoot problems, and optimize performance.

## Specifics:

- **Firewalls:** Firewalls are added to enforce security policies and restrict unauthorized access to the servers. They inspect incoming and outgoing traffic, filter packets based on predefined rules, and block or allow traffic accordingly.

- **HTTPS Traffic:** Traffic is served over HTTPS to encrypt data transmitted between the user's browser and the server. This protects sensitive information from eavesdropping, tampering, and interception by malicious actors.

- **Monitoring:** Monitoring is used to track the health, performance, and security of the infrastructure. It provides insights into resource utilization, application performance, network traffic, and security events, enabling proactive management and timely resolution of issues.

- **Monitoring Data Collection:** Monitoring tools collect data through agents or APIs installed on servers and networking devices. These agents gather metrics, logs, and events, which are then aggregated, analyzed, and visualized to provide insights into the infrastructure's performance and health.

- **Monitoring Web Server QPS (Queries Per Second):** To monitor the web server's QPS, you can configure monitoring tools to track the number of HTTP requests received by the server per second. This metric helps assess the server's workload, identify traffic patterns, and plan for capacity scaling as needed.

## Issues with the Infrastructure:

- **Terminating SSL at the Load Balancer Level:** Terminating SSL at the load balancer level can be an issue because it introduces a potential security vulnerability. Decrypting SSL/TLS traffic at the load balancer exposes sensitive data to potential interception or tampering before re-encrypting it for transmission to the backend servers.

- **Single MySQL Server Capable of Accepting Writes:** Having only one MySQL server capable of accepting writes poses a single point of failure. If the MySQL server fails, it can result in data loss, downtime, and service disruption. Implementing a high availability solution with replication and failover mechanisms can mitigate this risk.

- **Uniformity of Server Components:** Having servers with all the same components (database, web server, and application server) might be a problem because it lacks separation of concerns and increases the risk of cascading failures. If a critical vulnerability or issue affects one component, it can impact all servers simultaneously, leading to widespread service outages.
