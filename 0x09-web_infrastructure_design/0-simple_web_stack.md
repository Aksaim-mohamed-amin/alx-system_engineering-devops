![Simple Web Stack](https://github.com/Aksaim-mohamed-amin/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/0-simple_web_stack.png?raw=true)

# Infrastructure Overview

## Server
A server is a computer program or device responsible for hosting the website and its associated services.

## Domain Name
The domain name serves as a human-readable address for the website, directing users to the server hosting the website.

## DNS Record for www.foobar.com
The DNS record for www.foobar.com is typically a CNAME (Canonical Name) record, directing traffic to the correct server.

## Web Server
The web server (Nginx) handles HTTP requests, serves static content, and routes dynamic requests to the application server.

## Application Server
The application server hosts the application codebase, processes dynamic content, interacts with the database, and executes the website's logic.

## Database
The database (MySQL) stores and manages the website's data, interacting with the application server to retrieve and manipulate data.

## Communication with User's Computer
The server communicates with the user's computer using the HTTP protocol over the Internet, establishing a TCP connection and exchanging HTTP requests and responses.

# Issues with the Infrastructure

## Single Point of Failure (SPOF)
The infrastructure has a single server hosting both the web server and application server, leading to complete downtime if the server fails.

## Downtime during Maintenance
Maintenance activities, such as deploying new code or updates, may require restarting the web server, causing downtime for users.

## Limited Scalability
With only one server, the infrastructure may struggle to handle a large volume of incoming traffic and cannot scale horizontally to distribute the load efficiently.
