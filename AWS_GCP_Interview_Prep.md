# Comprehensive Cloud Interview Guide: AWS, GCP & Azure

This guide covers AWS, GCP, and Azure. Each cloud provider has its own section broken down into Beginner (with real-world examples), Intermediate, Scenario-Based, and Rapid Fire questions.

---

# 🟠 PART 1: Amazon Web Services (AWS)

## AWS Beginner Level — Top 25 Questions (Expanded)

1. **What is AWS?** Amazon's cloud computing platform providing scalable infrastructure and services.
   *Use Case:* Hosting a global web application without buying physical data center hardware.
2. **What is EC2?** Elastic Compute Cloud. AWS's virtual machine service (IaaS).
   *Use Case:* Renting a Linux server to run a custom backend application like a Node.js API.
3. **What is S3?** Simple Storage Service. Object storage for files, backups, and static sites.
   *Use Case:* Storing user-uploaded profile pictures and video files.
4. **What is a VPC?** Virtual Private Cloud. A secure, isolated private network in the AWS cloud.
   *Use Case:* Ensuring your production databases are hidden from the public internet.
5. **What is IAM?** Identity and Access Management. Controls who can access what in your AWS account.
   *Use Case:* Creating a policy that gives a junior developer read-only access to an S3 bucket.
6. **What is CloudFront?** AWS’s Content Delivery Network (CDN) for fast global content delivery.
   *Use Case:* Caching website images globally so users in Asia experience fast load times for a US-hosted site.
7. **What is AWS Lambda?** A serverless compute service that runs code without provisioning servers.
   *Use Case:* Triggering a script that automatically resizes an image exactly when it's uploaded to S3.
8. **What is Route 53?** Highly available and scalable DNS web service.
   *Use Case:* Routing user traffic from `www.myapp.com` to your AWS Load Balancer.
9. **What is Amazon RDS?** Relational Database Service (managed MySQL, PostgreSQL, etc.).
   *Use Case:* Storing highly structured, transactional data like user accounts and billing records.
10. **What is DynamoDB?** A fully managed NoSQL key-value and document database.
    *Use Case:* Storing high-velocity, unstructured data like live gaming leaderboard scores or shopping carts.
11. **What is Auto Scaling?** Automatically adds or removes EC2 instances based on traffic demand.
    *Use Case:* Automatically adding 5 extra servers during a Black Friday sale to handle the traffic spike.
12. **What is an ELB?** Elastic Load Balancer. Distributes incoming traffic across multiple targets.
    *Use Case:* Distributing 10,000 incoming user requests evenly across 3 different EC2 instances.
13. **What is a Subnet?** A range of IP addresses in your VPC used to isolate resources.
    *Use Case:* Putting web servers in a 'Public' subnet and databases in a 'Private' subnet.
14. **What is a Security Group?** A virtual firewall at the EC2 instance level to control inbound/outbound traffic.
    *Use Case:* Configuring a rule to only allow incoming HTTP traffic on port 80.
15. **What is EBS?** Elastic Block Store. Persistent block storage volumes for EC2 instances.
    *Use Case:* Providing a 500GB C: drive for a Windows virtual machine so data persists after reboots.
16. **What is CloudWatch?** A monitoring service for AWS resources and applications.
    *Use Case:* Triggering an automated alarm to Slack if server CPU usage goes over 80%.
17. **What is CloudTrail?** Auditing service that records all API calls made in your AWS account.
    *Use Case:* Investigating which user accidentally deleted a critical production database yesterday.
18. **What is EKS?** Elastic Kubernetes Service. Managed Kubernetes by AWS.
    *Use Case:* Orchestrating hundreds of Dockerized microservices for a large enterprise application.
19. **What is ECS?** Elastic Container Service. AWS’s native container orchestration service.
    *Use Case:* Running a Dockerized API server natively without the complexity of managing Kubernetes.
20. **What is Amazon SQS?** Simple Queue Service. A fully managed message queuing service.
    *Use Case:* Queuing up 100,000 email-sending tasks so the main web application doesn't slow down while processing them.
21. **What is Amazon SNS?** Simple Notification Service. A pub/sub messaging and notification service.
    *Use Case:* Sending an automated SMS alert to on-call engineers when a production server crashes.
22. **What is an Elastic IP?** A static, public IPv4 address that doesn’t change if the instance stops.
    *Use Case:* Whitelisting your server's IP address in a third-party payment gateway's firewall.
23. **What is an AMI?** Amazon Machine Image. The template used to launch an EC2 instance.
    *Use Case:* Creating a custom Ubuntu image pre-installed with Node.js and Docker to boot new servers faster.
24. **What is an Availability Zone (AZ)?** Discrete data centers within a Region with redundant power/networking.
    *Use Case:* Deploying an app across two AZs so it stays online even if one entire data center loses power.
25. **What is an AWS Region?** A physical geographical location in the world containing multiple AZs.
    *Use Case:* Deploying your application in `us-east-1` (Virginia) to minimize latency for your primary US user base.

## AWS Intermediate Level — Top 25 Questions

1. **ALB vs NLB?** ALB operates at Layer 7 (HTTP routing). NLB operates at Layer 4 (TCP/UDP, high performance).
2. **Security Group vs NACL?** SGs operate at the instance level and are stateful. NACLs operate at the subnet level and are stateless.
3. **IAM Role vs Policy?** A policy defines permissions (JSON). A role is an identity that an entity (like EC2) assumes to gain those permissions.
4. **Internet Gateway vs NAT Gateway?** IGW connects public subnets to the internet. NAT Gateway allows private subnets to download from the internet without inbound exposure.
5. **DynamoDB vs RDS?** DynamoDB is NoSQL, infinitely scalable. RDS is SQL, good for complex relations and ACID transactions.
6. **S3 Storage Classes?** Standard, Intelligent-Tiering, Standard-IA, One Zone-IA, Glacier.
7. **SQS Standard vs FIFO?** Standard offers best-effort ordering and at-least-once delivery. FIFO strictly preserves order and exactly-once processing.
8. **What is a Lambda Cold Start?** The initialization delay when a Lambda function is invoked after being idle. Mitigate with Provisioned Concurrency.
9. **What is VPC Peering?** A networking connection between two VPCs allowing them to communicate via private IPs.
10. **What is Cross-Region Replication in S3?** Asynchronously copying objects across buckets in different AWS Regions for disaster recovery.
11. **AWS Secrets Manager vs Parameter Store?** Secrets Manager can auto-rotate DB credentials (costs more). Parameter Store is cheaper, mostly for config/secrets without auto-rotation.
12. **Blue-Green Deployment?** Two identical environments. Traffic is switched instantly from the old (Blue) to the new (Green).
13. **What is a Bastion Host?** A secure server in a public subnet used exclusively as an SSH jump point to private subnet instances.
14. **What is AWS WAF?** Web Application Firewall. Protects web apps from common exploits like SQL injection.
15. **Fargate vs EC2 in ECS?** Fargate is serverless (you don't manage the underlying EC2 servers). EC2 gives you full control over the host servers.
16. **Multi-AZ vs Read Replica in RDS?** Multi-AZ is for Disaster Recovery (synchronous). Read Replicas are for read scalability (asynchronous).
17. **CloudFormation vs Terraform?** Both are IaC. CloudFormation is AWS-specific. Terraform is cloud-agnostic.
18. **What is DynamoDB DAX?** DynamoDB Accelerator. An in-memory cache that reduces response times from milliseconds to microseconds.
19. **Amazon Aurora vs RDS?** Aurora is AWS's custom database engine compatible with MySQL/Postgres but 5x faster and highly distributed.
20. **ElastiCache Redis vs Memcached?** Redis supports advanced data structures, persistence, and clustering. Memcached is simple, multi-threaded caching.
21. **What is AWS Transit Gateway?** A central hub that connects VPCs and on-premises networks to simplify network topology.
22. **What is API Gateway?** A managed service that allows developers to create, publish, and secure REST and WebSocket APIs.
23. **Spot vs On-Demand instances?** Spot uses spare AWS capacity at up to 90% discount but can be interrupted. On-demand is guaranteed capacity billed by the second.
24. **What is Amazon Kinesis?** A service to collect, process, and analyze real-time streaming data.
25. **What is an S3 Pre-signed URL?** A URL that gives temporary access (download or upload) to an S3 object to someone without AWS credentials.

## AWS Scenario-Based Questions

1. **Scenario: Black Friday Traffic Spike.**
   *Answer:* Host frontend on S3 + CloudFront. Run backend APIs on ECS Fargate behind an ALB with Auto Scaling based on CPU. Use RDS Multi-AZ and ElastiCache for DB scalability. Put order processing into an SQS queue.
2. **Scenario: High Database CPU load on RDS.**
   *Answer:* Check CloudWatch metrics. If it's heavy read traffic, deploy an RDS Read Replica and route read queries there. If it's a slow query, use Performance Insights to find it and add an index to the table.
3. **Scenario: Secure 3-Tier Architecture.**
   *Answer:* ALB in a Public Subnet. EC2/ECS App servers in Private Subnet 1. RDS Database in Private Subnet 2. Restrict Security Groups: ALB allows 443 from 0.0.0.0/0. App allows traffic only from ALB. DB allows traffic only from App.
4. **Scenario: Reducing S3 Storage Costs.**
   *Answer:* Implement S3 Lifecycle Policies. Keep data in Standard for 30 days, move to Standard-IA for 60 days, and archive to Glacier Deep Archive after 90 days.
5. **Scenario: CI/CD Pipeline broke production.**
   *Answer:* Immediately trigger a rollback in GitLab/CodePipeline. Check CloudWatch logs to identify the error. Reproduce the bug in the staging environment, write a test, fix it, and redeploy.

## AWS Rapid Fire Questions

1. **Service for DNS?** Route 53
2. **Port for SSH?** 22
3. **Data warehouse in AWS?** Redshift
4. **Serverless compute?** Lambda
5. **Managed Kubernetes?** EKS
6. **Object storage?** S3
7. **Infrastructure as Code tool?** CloudFormation
8. **In-memory caching?** ElastiCache
9. **Message queue?** SQS
10. **Stateful firewall?** Security Group

---

# 🔵 PART 2: Google Cloud Platform (GCP)

## GCP Beginner Level — Top 25 Questions (Expanded)

1. **What is GCP?** Google Cloud Platform, a suite of cloud computing services.
   *Use Case:* Utilizing Google's high-speed internal fiber network to run global enterprise workloads.
2. **What is GCE?** Google Compute Engine. GCP’s virtual machine service (IaaS).
   *Use Case:* Spinning up a high-CPU Linux VM to process video rendering tasks.
3. **What is GCS?** Google Cloud Storage. Object storage for unstructured data.
   *Use Case:* Storing daily automated database backups safely and cheaply.
4. **What is a GCP VPC?** Virtual Private Cloud. In GCP, VPCs are global resources, while subnets are regional.
   *Use Case:* Creating a single global network to connect an app in Tokyo with a database in London securely.
5. **What is Cloud IAM?** Identity and Access Management for access control in GCP.
   *Use Case:* Ensuring external contractors can only read data, not delete it.
6. **What is Cloud CDN?** Google’s Content Delivery Network.
   *Use Case:* Serving heavy JavaScript bundles to users quickly from Google edge locations.
7. **What is Cloud Functions?** GCP’s serverless, event-driven compute service.
   *Use Case:* Running a lightweight Python script every time a new document is uploaded to GCS.
8. **What is Cloud DNS?** A managed, authoritative Domain Name System service.
   *Use Case:* Translating `mycompany.com` to the IP address of your load balancer.
9. **What is Cloud SQL?** A fully managed relational database service (MySQL/PostgreSQL).
   *Use Case:* Hosting a WordPress backend database without worrying about OS patching or backups.
10. **What is Cloud Spanner?** A globally distributed, strongly consistent relational database.
    *Use Case:* Building a global banking application where transactions must be strictly consistent worldwide.
11. **What is a Managed Instance Group (MIG)?** A group of identical VMs managed as a single entity.
    *Use Case:* Auto-scaling your web servers up and down based on traffic spikes.
12. **What is Cloud Load Balancing?** A distributed, software-defined service for routing traffic.
    *Use Case:* Distributing traffic across VMs in the US and Europe using a single global IP address.
13. **Are GCP Subnets Regional or Global?** Regional. (VPCs are global).
    *Use Case:* Placing frontend servers in a US-East subnet and backend servers in a US-West subnet within the same VPC.
14. **What are GCP Firewall Rules?** Rules that control inbound and outbound traffic to instances.
    *Use Case:* Blocking all inbound SSH traffic except from your company's corporate IP address.
15. **What is a Persistent Disk?** Durable block storage attached to GCE instances.
    *Use Case:* Providing reliable storage for a self-hosted MongoDB instance running on a VM.
16. **What is Cloud Monitoring?** Metrics and alerting service.
    *Use Case:* Setting up a dashboard to track the average response time of your API.
17. **What is Cloud Logging?** Centralized log management service.
    *Use Case:* Searching through millions of lines of logs to debug a 500 Internal Server Error.
18. **What is GKE?** Google Kubernetes Engine. Google’s managed Kubernetes service.
    *Use Case:* Deploying and scaling a massive e-commerce site built using microservices architecture.
19. **What is Cloud Run?** A fully managed serverless platform that automatically scales stateless containers.
    *Use Case:* Deploying a Next.js frontend wrapped in a Docker container that automatically scales to zero when nobody is visiting.
20. **What is Pub/Sub?** A serverless, asynchronous messaging service.
    *Use Case:* Ingesting thousands of events per second from IoT devices and sending them to analytics processors.
21. **What is BigQuery?** A serverless, highly scalable cloud data warehouse.
    *Use Case:* Running SQL queries over terabytes of sales data to generate a BI report in seconds.
22. **What is a Static IP in GCP?** An external IP address assigned to a project and retained until explicitly released.
    *Use Case:* Providing a fixed IP to a client so they can whitelist your API in their firewall.
23. **What are Custom Machine Types?** GCE allows you to create VMs with the exact amount of CPU and RAM you need.
    *Use Case:* Creating a VM with 6 vCPUs and 24GB RAM because standard sizes are either too small or too expensive.
24. **What is a Zone in GCP?** A deployment area within a region (e.g., us-central1-a).
    *Use Case:* Deploying resources close together for ultra-low network latency.
25. **What is a Region in GCP?** A specific geographical location containing multiple zones (e.g., us-central1).
    *Use Case:* Ensuring European user data physically stays within Europe to comply with GDPR.

## GCP Intermediate Level — Top 25 Questions

1. **Cloud Run vs Cloud Functions?** Cloud Run runs any Docker container based on HTTP requests. Cloud Functions runs code snippets triggered by GCP events (e.g., file upload).
2. **GKE vs Cloud Run?** GKE is full Kubernetes (you manage the cluster). Cloud Run is serverless containers (Google manages the infrastructure).
3. **Cloud SQL vs Spanner?** Cloud SQL is regional and scales vertically. Spanner is global, horizontally scalable, and highly available.
4. **GCS Storage Classes?** Standard, Nearline (once a month), Coldline (once a quarter), Archive (once a year).
5. **Global vs Regional Load Balancer?** Global routes traffic globally using a single Anycast IP. Regional limits routing to a specific region.
6. **Pub/Sub vs Kafka?** Pub/Sub is serverless and fully managed. Kafka requires managing brokers, partitions, and ZooKeeper.
7. **What is VPC Network Peering in GCP?** Connects two VPC networks so resources can communicate using internal IP addresses.
8. **What is Identity-Aware Proxy (IAP)?** Secures web apps and VMs by verifying user identity and context, removing the need for a VPN.
9. **What is Secret Manager?** A secure and convenient storage system for API keys, passwords, and certificates.
10. **What is Cloud Build?** A service that executes your builds on GCP infrastructure (CI/CD).
11. **Deployment Manager vs Terraform?** Deployment Manager is GCP’s native IaC tool. Terraform is cloud-agnostic and more widely adopted.
12. **Datastore (Firestore) vs Bigtable?** Firestore is a NoSQL document DB for web/mobile apps. Bigtable is a NoSQL wide-column DB for heavy analytical/IoT workloads.
13. **What is a Shared VPC?** Allows multiple GCP projects to share a common VPC network centrally managed by a host project.
14. **Cloud Interconnect vs Cloud VPN?** Interconnect is a dedicated, physical fiber connection. VPN goes over the public internet (encrypted).
15. **What is Cloud Armor?** GCP’s web application firewall (WAF) and DDoS protection service.
16. **Dataflow vs Dataproc?** Dataflow is for serverless stream/batch processing (Apache Beam). Dataproc is managed Hadoop/Spark clusters.
17. **Preemptible VMs vs Spot VMs?** Both are cheap, short-lived VMs. Spot VMs are the newer version with more flexible pricing and no maximum 24-hour runtime limit.
18. **What is Cloud Source Repositories?** Fully featured, private Git repositories hosted on Google Cloud.
19. **GKE Autopilot vs Standard?** Autopilot manages the entire underlying cluster and nodes for you. Standard requires you to manage the node pools.
20. **What is Cloud Scheduler?** A fully managed enterprise-grade cron job scheduler.
21. **What is Workload Identity?** The recommended way for GKE applications to authenticate securely to Google Cloud APIs using IAM.
22. **What is Memorystore?** A fully managed in-memory data store service for Redis and Memcached.
23. **What are Service Accounts?** Special Google accounts used by applications/VMs, not people, to interact with GCP APIs.
24. **What is Cloud NAT?** Allows instances without public IP addresses to access the internet for updates while blocking incoming connections.
25. **What is committed use discount?** A discount received by committing to use a certain amount of vCPU and memory for 1 or 3 years.

## GCP Scenario-Based Questions

1. **Scenario: Global App deployment with low latency.**
   *Answer:* Deploy the backend API as containers on Cloud Run across three regions (US, Europe, Asia). Put a Global HTTP(S) Load Balancer in front of them with a single Anycast IP. Use Cloud Spanner as the global database for consistent, cross-region data.
2. **Scenario: Building an Analytics Pipeline from IoT devices.**
   *Answer:* IoT devices send data to Cloud Pub/Sub. Use Cloud Dataflow to process/transform the streaming messages, and output the clean data into BigQuery for analysis.
3. **Scenario: Secure internal app access without a VPN.**
   *Answer:* Deploy the internal application on GCE or Cloud Run. Enable Identity-Aware Proxy (IAP) in front of it. Use Google Workspace or Cloud Identity to enforce policy (e.g., only the Engineering Group can access).
4. **Scenario: Deploying a legacy monolithic application.**
   *Answer:* Lift-and-shift the application onto a GCE Virtual Machine. Place it in a custom VPC. Connect it to a managed Cloud SQL instance. Use Cloud Load Balancing for SSL termination.
5. **Scenario: Massive unpredictable traffic for a marketing campaign.**
   *Answer:* Package the application in a Docker container and deploy it to Cloud Run. Cloud Run will automatically scale from zero to thousands of instances in seconds to handle the spike, and scale back to zero when traffic stops.

## GCP Rapid Fire Questions

1. **GCP Serverless container platform?** Cloud Run
2. **GCP Data Warehouse?** BigQuery
3. **Tool for CI/CD pipelines?** Cloud Build
4. **Global SQL database?** Cloud Spanner
5. **Managed Redis?** Memorystore
6. **NoSQL Document DB?** Firestore
7. **Alternative to AWS SQS/SNS?** Pub/Sub
8. **Command Line tool for GCP?** `gcloud`
9. **WAF & DDoS protection?** Cloud Armor
10. **Global network router?** Global HTTP(S) Load Balancer

---

# 🟢 PART 3: Microsoft Azure

## Azure Beginner Level — Top 25 Questions (Expanded)

1. **What is Microsoft Azure?** Microsoft's public cloud computing platform providing scalable infrastructure and services.
   *Use Case:* Building and deploying an enterprise .NET application into the cloud.
2. **What are Resource Groups?** Logical containers in Azure that hold related resources for an Azure solution.
   *Use Case:* Grouping a web app, its database, and its storage account together so they can be deleted or billed as a single unit.
3. **What is Azure Virtual Machine (VM)?** Azure's Infrastructure as a Service (IaaS) offering for running virtualized servers.
   *Use Case:* Running a legacy Windows Server application that cannot be containerized.
4. **What is Azure Blob Storage?** Object storage solution for the cloud, ideal for storing massive amounts of unstructured data.
   *Use Case:* Storing millions of PDF invoices generated by an e-commerce platform.
5. **What is Azure Virtual Network (VNet)?** The fundamental building block for your private network in Azure.
   *Use Case:* Creating a secure networking boundary so your internal HR tool isn't accessible from the internet.
6. **What is Azure Active Directory (Azure AD / Entra ID)?** Microsoft’s cloud-based identity and access management service.
   *Use Case:* Enabling Single Sign-On (SSO) so employees can use the same login for their laptop, Office 365, and your custom app.
7. **What is Azure App Service?** A fully managed Platform as a Service (PaaS) for building, deploying, and scaling web apps.
   *Use Case:* Deploying a React frontend and Node.js backend quickly without worrying about OS updates.
8. **What is Azure Functions?** An event-driven, serverless compute service.
   *Use Case:* Running a small C# script to send a welcome email every time a new row is added to a database.
9. **What is Azure SQL Database?** A fully managed relational database with auto-scaling and built-in intelligence.
   *Use Case:* Migrating an on-premise SQL Server database to the cloud without needing to manage database backups manually.
10. **What is Cosmos DB?** Azure's fully managed, globally distributed, multi-model NoSQL database.
    *Use Case:* Building a responsive IoT dashboard that ingests thousands of sensor readings per second globally.
11. **What is a Subnet in Azure?** A range of IP addresses in your VNet used to isolate resources.
    *Use Case:* Isolating the database tier from the web tier for better security architecture.
12. **What is a Network Security Group (NSG)?** A firewall containing security rules that allow or deny inbound/outbound network traffic to Azure resources.
    *Use Case:* Creating a rule to block all incoming traffic except HTTPS (port 443).
13. **What is Azure Load Balancer?** Operates at Layer 4 to distribute incoming network traffic across a group of backend resources.
    *Use Case:* Distributing heavy internal database traffic across multiple backend virtual machines.
14. **What is Azure Application Gateway?** A web traffic load balancer operating at Layer 7 (HTTP/HTTPS).
    *Use Case:* Routing traffic based on URL paths, e.g., sending `/images` to one server pool and `/video` to another.
15. **What is an Azure Region?** A set of data centers deployed within a latency-defined perimeter.
    *Use Case:* Deploying your application in `West Europe` to ensure low latency for European users.
16. **What is an Availability Zone?** Physically separate locations within an Azure region, providing high availability.
    *Use Case:* Replicating your database across two zones so a fire in one data center doesn't cause downtime.
17. **What is Azure Monitor?** A comprehensive solution for collecting, analyzing, and acting on telemetry from your cloud environments.
    *Use Case:* Setting up an alert that pages the on-call team if memory usage exceeds 90%.
18. **What is Azure Kubernetes Service (AKS)?** Azure's highly available, secure, and fully managed Kubernetes service.
    *Use Case:* Managing complex deployment scaling for a microservices architecture.
19. **What is Azure Container Instances (ACI)?** A service that allows you to run Docker containers in Azure without managing servers.
    *Use Case:* Quickly spinning up an isolated container to run a 5-minute data processing job without setting up an AKS cluster.
20. **What is Azure Service Bus?** A fully managed enterprise integration message broker.
    *Use Case:* Ensuring reliable, ordered message delivery between a financial order system and the billing system.
21. **What is Azure DevOps?** A suite of services providing developer tools for software teams (Boards, Repos, Pipelines).
    *Use Case:* Using Agile Boards to track work and Pipelines to automate code deployment.
22. **What is Azure Repos?** Provides unlimited, cloud-hosted private Git repos for your project.
    *Use Case:* Storing your source code securely with pull-request review policies.
23. **What is Azure Pipelines?** A cloud service that automatically builds and tests your code project (CI/CD).
    *Use Case:* Automatically running unit tests and deploying code to App Service every time code is merged to main.
24. **What is Azure Key Vault?** A cloud service for securely storing and accessing secrets (API keys, passwords, certificates).
    *Use Case:* Storing your database connection string so it doesn't get hardcoded into your GitHub repository.
25. **What is an Azure Subscription?** A logical container used to provision resources in Azure, tying them to an overarching billing account.
    *Use Case:* Creating a 'Production' subscription and a 'Development' subscription to keep billing completely separate.

## Azure Intermediate Level — Top 25 Questions

1. **App Service vs Azure Functions?** App Service is for hosting full web applications. Functions are for serverless, event-driven code snippets.
2. **AKS vs ACI?** ACI is for simple, isolated containers without orchestration. AKS is for orchestrating complex container clusters (Kubernetes).
3. **Azure SQL vs Cosmos DB?** Azure SQL is relational and transactional. Cosmos DB is NoSQL, schema-less, and globally distributed with single-digit ms latency.
4. **Storage Account Tiers?** Hot (frequently accessed), Cool (infrequently accessed, stored >=30 days), Archive (rarely accessed, stored >=180 days).
5. **Azure Load Balancer vs Application Gateway vs Front Door?** Load Balancer is regional Layer 4. App Gateway is regional Layer 7. Front Door is global Layer 7 with CDN.
6. **Service Bus vs Event Grid?** Service Bus is for high-value enterprise messaging (queues/topics). Event Grid is for event routing (pub/sub) at scale.
7. **What is VNet Peering?** Seamlessly connecting two VNets in Azure so traffic routes through Microsoft's private backbone infrastructure.
8. **Azure VPN Gateway vs ExpressRoute?** VPN goes over the public internet (encrypted). ExpressRoute is a dedicated, private, high-speed connection.
9. **NSG vs Azure Firewall?** NSG applies basic rules to subnets/NICs. Azure Firewall is a managed, stateful firewall service with threat intelligence.
10. **Azure AD Roles vs Azure RBAC?** Azure AD Roles manage directory resources (users, groups, domains). Azure RBAC manages access to Azure resources (VMs, VNets).
11. **What are ARM Templates?** Azure Resource Manager templates. JSON files that define the infrastructure and configuration for your project (IaC).
12. **Azure Bicep vs Terraform?** Bicep is Microsoft's native DSL for ARM templates (cleaner syntax). Terraform is open-source and multi-cloud.
13. **Blue-Green Deployment in App Service?** Use Deployment Slots. Deploy to the 'staging' slot, warm it up, and then swap it with the 'production' slot instantly.
14. **What are Managed Identities?** Automatically managed identities in Azure AD for applications to use when connecting to resources that support Azure AD auth.
15. **What are Azure Logic Apps?** A cloud service that helps you schedule, automate, and orchestrate tasks, business processes, and workflows.
16. **What are Azure Cognitive Services?** Cloud-based AI APIs that help developers build intelligent apps without direct AI/data science skills.
17. **Application Insights vs Log Analytics?** App Insights monitors application performance (APM). Log Analytics queries and analyzes log data across Azure resources.
18. **Cosmos DB Consistency Levels?** Strong, Bounded Staleness, Session (default), Consistent Prefix, Eventual.
19. **Access Keys vs SAS Tokens?** Access Keys grant full control to the storage account. Shared Access Signatures (SAS) grant restricted, time-limited access to specific objects.
20. **What is Azure Traffic Manager?** A DNS-based traffic load balancer that enables you to distribute traffic optimally to services across global Azure regions.
21. **Availability Sets vs Availability Zones?** Sets protect against hardware failures within a single datacenter. Zones protect against entire datacenter failures within a region.
22. **What are Ephemeral OS Disks?** OS disks created on the local VM storage. They are faster and cheaper but data is lost if the VM is deallocated.
23. **What is Azure Bastion?** A fully managed PaaS service that provides secure and seamless RDP/SSH connectivity to VMs directly from the Azure portal.
24. **What is Azure Arc?** A service that extends Azure management and services to any infrastructure (on-premises, multi-cloud, edge).
25. **What is a Service Principal?** An identity created for use with applications, hosted services, and automated tools to access Azure resources.

## Azure Scenario-Based Questions

1. **Scenario: Migrating a legacy web application to Azure.**
   *Answer:* I would migrate the frontend/backend code to Azure App Service (PaaS) to avoid managing VMs. The on-premise database would be migrated to Azure SQL Database using the Azure Database Migration Service. I'd use Azure Key Vault for connection strings.
2. **Scenario: Handling a sudden global traffic spike.**
   *Answer:* Deploy the application across multiple regions using Azure App Service with Auto-scale rules based on CPU/RAM. Place Azure Front Door ahead of the apps to route users to the closest healthy region and cache static content globally.
3. **Scenario: Secure secret management in CI/CD.**
   *Answer:* Never store secrets in code. Store them in Azure Key Vault. Enable a Managed Identity for the Azure App Service/VM, grant it read access to the Key Vault, and fetch the secrets at runtime. Use Azure Pipelines variables linked to Key Vault for deployment secrets.
4. **Scenario: Multi-region high availability database.**
   *Answer:* Use Cosmos DB configured for multi-region writes. If it must be relational, use Azure SQL Database with Active Geo-Replication, allowing secondary databases in different regions to take over if the primary fails.
5. **Scenario: Securing access to internal VMs.**
   *Answer:* Do not assign public IP addresses to the VMs. Place them in a private VNet and deploy Azure Bastion in a designated subnet. Developers can securely RDP/SSH into the VMs via the Azure Portal without exposing ports to the internet.

## Azure Rapid Fire Questions

1. **Port for RDP?** 3389
2. **Azure's NoSQL DB?** Cosmos DB
3. **Serverless compute?** Azure Functions
4. **Managed Kubernetes?** AKS
5. **Infrastructure as Code tool native to Azure?** ARM Templates (or Bicep)
6. **Global routing service?** Azure Front Door
7. **Pub/sub messaging?** Event Grid / Service Bus
8. **IAM equivalent?** Azure Active Directory (Entra ID)
9. **Object storage?** Azure Blob Storage
10. **WAF service?** Azure Application Gateway (or Front Door WAF)
