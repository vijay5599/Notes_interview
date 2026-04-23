# System Design Concepts - Comprehensive Notes

## Table of Contents
1. [Performance vs Scalability](#performance-vs-scalability)
2. [Latency vs Throughput](#latency-vs-throughput)
3. [CAP Theorem and Consistency](#cap-theorem-and-consistency)
4. [Availability Patterns](#availability-patterns)
5. [Domain Name System (DNS)](#domain-name-system-dns)
6. [Content Delivery Network (CDN)](#content-delivery-network-cdn)
7. [Load Balancing](#load-balancing)
8. [System Architecture](#system-architecture)
9. [Databases](#databases)
10. [Caching](#caching)
11. [Asynchronous Processing](#asynchronous-processing)
12. [Communication Protocols](#communication-protocols)
13. [Security](#security)

---

## Performance vs Scalability

### Performance
- **Definition**: How fast a system processes a single request
- **Metrics**: Response time, latency, processing speed
- **Focus**: Optimizing for speed and efficiency
- **Example**: A web server that responds to requests in 50ms vs 200ms

### Scalability
- **Definition**: System's ability to handle increased load
- **Types**:
  - **Vertical Scaling (Scale Up)**: Adding more power (CPU, RAM) to existing machines
  - **Horizontal Scaling (Scale Out)**: Adding more machines to the pool of resources
- **Focus**: Handling more users, requests, or data
- **Example**: System handling 1000 concurrent users vs 10,000 concurrent users

### Key Differences
| Aspect | Performance | Scalability |
|--------|-------------|-------------|
| Goal | Speed | Capacity |
| Measurement | Response time | Throughput under load |
| Solution | Optimize code/hardware | Add resources/distribute load |

---

## Latency vs Throughput

### Latency
- **Definition**: Time to process a single request (end-to-end delay)
- **Units**: Milliseconds, seconds
- **Examples**:
  - Database query: 10ms
  - API call: 100ms
  - Cross-continent network call: 200ms

### Throughput
- **Definition**: Number of requests processed per unit time
- **Units**: Requests per second (RPS), transactions per second (TPS)
- **Examples**:
  - Web server: 1000 RPS
  - Database: 500 TPS
  - Message queue: 10,000 messages/sec

### Relationship
- Generally **inverse relationship**: Lower latency often means higher throughput
- **Trade-offs**: Optimizing for one may affect the other
- **Batching**: Can increase throughput but may increase latency

---

## CAP Theorem and Consistency

### CAP Theorem
**Theorem**: In a distributed system, you can only guarantee 2 out of 3 properties:

#### Consistency (C)
- All nodes see the same data simultaneously
- Every read receives the most recent write
- **Example**: Bank account balance must be consistent across all ATMs

#### Availability (A)
- System remains operational and responds to requests
- Every request receives a response (success or failure)
- **Example**: System continues to serve requests even if some nodes fail

#### Partition Tolerance (P)
- System continues to operate despite network partitions
- Communication breaks between nodes
- **Example**: System works even if network splits the cluster

### CAP Combinations

#### CA - Consistency and Availability
- **Characteristics**: Sacrifices partition tolerance for consistency and availability
- **Use Cases**: Traditional single-node databases, systems within same network
- **Examples**: Traditional RDBMS (MySQL, PostgreSQL) in single-node setup
- **Behavior**: System provides strong consistency and high availability but cannot handle network partitions
- **Limitation**: Not suitable for distributed systems since network partitions are inevitable in distributed environments
- **Note**: Often considered impractical for truly distributed systems

#### CP - Consistency and Partition Tolerance
- **Characteristics**: Sacrifices availability for consistency
- **Use Cases**: Financial systems, inventory management
- **Examples**: MongoDB, Redis, HBase
- **Behavior**: System may become unavailable during network partitions to maintain consistency

#### AP - Availability and Partition Tolerance
- **Characteristics**: Sacrifices consistency for availability
- **Use Cases**: Social media feeds, recommendation systems
- **Examples**: Cassandra, DynamoDB, CouchDB
- **Behavior**: System remains available but may serve stale data during partitions

### Consistency Patterns

#### Weak Consistency
- **Definition**: No guarantees when all nodes will be consistent
- **Characteristics**: Best effort approach
- **Use Cases**: Live streaming, online gaming, VoIP
- **Example**: Video chat - occasional packet loss is acceptable

#### Eventual Consistency
- **Definition**: System will become consistent over time
- **Characteristics**: 
  - No immediate consistency guarantee
  - Conflicts are resolved eventually
- **Use Cases**: DNS, email systems, social media feeds
- **Example**: Facebook post may take time to appear on all friends' feeds

#### Strong Consistency
- **Definition**: All reads receive the most recent write immediately
- **Characteristics**:
  - Immediate consistency across all nodes
  - Higher latency due to coordination overhead
- **Use Cases**: Banking, inventory systems, ACID transactions
- **Example**: Bank transfer must be immediately visible across all systems

---

## Availability Patterns

### Availability in Numbers
- **99%**: 3.65 days downtime/year
- **99.9%**: 8.76 hours downtime/year
- **99.99%**: 52.56 minutes downtime/year
- **99.999%**: 5.26 minutes downtime/year

### Fail-over
Process of switching to a backup system when primary fails.

#### Active-Passive (Hot Standby)
- **Setup**: Primary active, secondary on standby
- **Behavior**: Traffic only goes to secondary if primary fails
- **Pros**: Simple, cost-effective
- **Cons**: Waste of resources, potential data loss
- **Example**: Database master-slave setup

#### Active-Active (Hot-Hot)
- **Setup**: Both systems actively handle traffic
- **Behavior**: Traffic distributed across both systems
- **Pros**: Better resource utilization, faster recovery
- **Cons**: More complex, potential data conflicts
- **Example**: Load-balanced web servers

### Replication
Creating copies of data across multiple systems.

#### Types:
1. **Synchronous**: Write to all replicas before confirming
2. **Asynchronous**: Write to primary first, then replicas
3. **Semi-synchronous**: Write to primary and at least one replica

#### Benefits:
- **Fault tolerance**: System survives node failures
- **Read scaling**: Multiple replicas can serve read requests
- **Geographic distribution**: Replicas closer to users

---

## Domain Name System (DNS)

### Purpose
- Translates human-readable domain names to IP addresses
- Distributed hierarchical naming system

### DNS Hierarchy
```
Root Servers (.)
    ↓
Top-Level Domain (.com, .org)
    ↓
Authoritative Servers (google.com)
    ↓
Subdomains (www.google.com)
```

### DNS Record Types
- **A Record**: Maps domain to IPv4 address
- **AAAA Record**: Maps domain to IPv6 address
- **CNAME**: Maps domain to another domain
- **MX**: Mail exchange servers
- **TXT**: Text records (SPF, DKIM)
- **NS**: Name server records

### DNS Resolution Process
1. User types URL in browser
2. Browser checks local DNS cache
3. Query local DNS resolver
4. Query root server if needed
5. Query TLD server
6. Query authoritative server
7. Return IP address to user

---

## Content Delivery Network (CDN)

### Purpose
- Distribute content geographically closer to users
- Reduce latency and server load
- Improve user experience

### CDN Types

#### Push CDNs
- **How it works**: You upload content to CDN servers
- **Best for**: Small traffic, content doesn't change frequently
- **Pros**: Full control over content, good for small sites
- **Cons**: Manual upload process, storage costs
- **Example**: Uploading static assets manually

#### Pull CDNs
- **How it works**: CDN pulls content from origin when requested
- **Best for**: Heavy traffic, frequently changing content
- **Pros**: Automatic caching, only caches popular content
- **Cons**: Slower first request (cache miss)
- **Example**: CloudFlare, Amazon CloudFront

### CDN Benefits
- **Performance**: Faster content delivery
- **Availability**: Content available even if origin fails
- **Security**: DDoS protection, SSL termination
- **Cost**: Reduced bandwidth costs on origin server

---

## Load Balancing

### Purpose
- Distribute incoming requests across multiple servers
- Improve response time and availability
- Prevent server overload

### Load Balancer Types

#### Active-Passive
- **Setup**: Primary load balancer handles all traffic
- **Backup**: Secondary takes over if primary fails
- **Use case**: Cost-sensitive environments
- **Example**: Simple failover setup

#### Active-Active
- **Setup**: Multiple load balancers handle traffic simultaneously
- **Benefits**: Better performance and availability
- **Use case**: High-traffic applications
- **Example**: Multiple geographic load balancers

### Load Balancing Layers

#### Layer 4 Load Balancing (Transport Layer)
- **How it works**: Routes based on IP and port
- **Protocols**: TCP, UDP
- **Pros**: 
  - Fast (minimal processing)
  - Protocol agnostic
  - Lower resource usage
- **Cons**:
  - Limited routing options
  - No application awareness
- **Example**: Routing TCP connections to web servers

#### Layer 7 Load Balancing (Application Layer)
- **How it works**: Routes based on application data (HTTP headers, URLs)
- **Protocols**: HTTP, HTTPS, SMTP
- **Pros**:
  - Smart routing (URL-based, header-based)
  - SSL termination
  - Content-based decisions
- **Cons**:
  - Higher resource usage
  - More complex
- **Example**: Routing /api requests to API servers, /static to file servers

### Load Balancing Algorithms
- **Round Robin**: Requests distributed evenly
- **Weighted Round Robin**: Based on server capacity
- **Least Connections**: Route to server with fewest active connections
- **IP Hash**: Route based on client IP hash
- **Geographic**: Route based on client location

---

## System Architecture

### Horizontal Scaling
- **Definition**: Adding more servers to handle increased load
- **Benefits**:
  - Linear scaling potential
  - Fault tolerance
  - Cost-effective for commodity hardware
- **Challenges**:
  - Data consistency
  - Complex deployment
  - Network overhead
- **Example**: Adding more web servers behind load balancer

### Reverse Proxy (Web Server)
- **Purpose**: Sits between clients and backend servers
- **Functions**:
  - SSL termination
  - Compression
  - Caching
  - Request routing
  - Security filtering

#### Load Balancer vs Reverse Proxy
| Aspect | Load Balancer | Reverse Proxy |
|--------|---------------|---------------|
| Primary Purpose | Distribute load | Act as intermediary |
| Server Awareness | Multiple backend servers | Can work with one server |
| Features | Load distribution algorithms | SSL, caching, compression |
| Use Case | High traffic distribution | Security, caching, SSL |

### Application Layer

#### Microservices
- **Definition**: Architecture pattern with small, independent services
- **Characteristics**:
  - Single responsibility
  - Independent deployment
  - Own database per service
  - Communication via APIs

**Benefits**:
- **Scalability**: Scale individual services
- **Technology diversity**: Different tech stacks per service
- **Team autonomy**: Independent development teams
- **Fault isolation**: Service failures don't cascade

**Challenges**:
- **Complexity**: Distributed system challenges
- **Communication overhead**: Network calls between services
- **Data consistency**: Managing transactions across services
- **Monitoring**: Tracking requests across services

#### Service Discovery
- **Purpose**: How services find and communicate with each other
- **Methods**:
  - **Client-side discovery**: Client queries service registry
  - **Server-side discovery**: Load balancer queries service registry
- **Tools**: Consul, Eureka, etcd, Zookeeper

---

## Databases

### Relational Database Management System (RDBMS)
- **Characteristics**: ACID properties, structured data, SQL
- **Examples**: MySQL, PostgreSQL, Oracle, SQL Server
- **Use cases**: Financial systems, e-commerce, CRM

#### ACID Properties
- **Atomicity**: All operations in transaction succeed or fail together
- **Consistency**: Database remains valid state after transaction
- **Isolation**: Concurrent transactions don't interfere
- **Durability**: Committed transactions persist even after system failure

### Replication Patterns

#### Master-Slave Replication
- **Setup**: One master (writes), multiple slaves (reads)
- **Pros**: 
  - Read scaling
  - Simple consistency model
  - Backup capability
- **Cons**:
  - Single point of failure (master)
  - Write scaling limitations
- **Example**: MySQL master-slave setup

#### Master-Master Replication
- **Setup**: Multiple masters accepting writes
- **Pros**:
  - No single point of failure
  - Write scaling
  - Geographic distribution
- **Cons**:
  - Conflict resolution complexity
  - Consistency challenges
- **Example**: MySQL cluster with multiple masters

### Scaling Techniques

#### Federation
- **Definition**: Split databases by function/feature
- **Example**: 
  - Users database
  - Products database
  - Orders database
- **Pros**: Targeted optimization, reduced read/write traffic
- **Cons**: Complex joins, application complexity

#### Sharding
- **Definition**: Split database horizontally by rows
- **Sharding strategies**:
  - **Range-based**: Shard by data ranges (A-M, N-Z)
  - **Hash-based**: Shard by hash function
  - **Directory-based**: Lookup service determines shard
- **Pros**: Linear scaling, fault isolation
- **Cons**: Complex queries, rebalancing difficulty

#### Denormalization
- **Definition**: Redundant data storage to improve read performance
- **Trade-offs**: Storage space vs query performance
- **Examples**: 
  - Storing computed values
  - Duplicating frequently accessed data
- **Use cases**: Analytics, reporting, read-heavy applications

#### SQL Tuning
- **Indexing**: B-tree, hash, bitmap indexes
- **Query optimization**: Explain plans, query rewriting
- **Schema design**: Proper normalization, data types
- **Connection pooling**: Reuse database connections

### NoSQL

#### Key-Value Store
- **Structure**: Simple key-value pairs
- **Examples**: Redis, DynamoDB, Riak
- **Use cases**: Caching, session storage, shopping carts
- **Pros**: Simple, fast, scalable
- **Cons**: Limited query capabilities

#### Document Store
- **Structure**: Documents (JSON, XML) with nested structures
- **Examples**: MongoDB, CouchDB, Amazon DocumentDB
- **Use cases**: Content management, catalogs, user profiles
- **Pros**: Flexible schema, natural data representation
- **Cons**: Complex queries, consistency challenges

#### Wide Column Store
- **Structure**: Tables with dynamic columns
- **Examples**: Cassandra, HBase, Amazon SimpleDB
- **Use cases**: Time-series data, IoT, analytics
- **Pros**: Scalable, fast writes, flexible schema
- **Cons**: Complex data modeling

#### Graph Database
- **Structure**: Nodes and relationships
- **Examples**: Neo4j, Amazon Neptune, ArangoDB
- **Use cases**: Social networks, recommendation engines, fraud detection
- **Pros**: Complex relationship queries, intuitive modeling
- **Cons**: Limited scalability, complex operations

### SQL or NoSQL?

#### Choose SQL when:
- ACID compliance required
- Complex queries and relationships
- Structured data with clear schema
- Strong consistency needed

#### Choose NoSQL when:
- Massive scaling requirements
- Flexible/evolving schema
- Simple query patterns
- Eventual consistency acceptable

---

## Caching

### Purpose
- Store frequently accessed data in fast storage
- Reduce latency and database load
- Improve application performance

### Cache Types

#### Client Caching
- **Location**: User's device/browser
- **Examples**: Browser cache, mobile app cache
- **Pros**: Fastest access, reduces network traffic
- **Cons**: Limited control, cache invalidation challenges

#### CDN Caching
- **Location**: Edge servers globally distributed
- **Content**: Static assets, images, videos
- **Pros**: Geographic distribution, reduced origin load
- **Cons**: Cache invalidation complexity

#### Web Server Caching
- **Location**: Web server layer
- **Content**: Rendered pages, API responses
- **Examples**: Nginx proxy cache, Varnish
- **Pros**: Reduces application server load

#### Database Caching
- **Location**: In front of database
- **Content**: Query results, computed data
- **Examples**: Redis, Memcached
- **Pros**: Significant database load reduction

#### Application Caching
- **Location**: Within application code
- **Content**: Objects, computed results
- **Implementation**: In-memory data structures
- **Pros**: Fastest access, full control

### Cache Levels

#### Caching at Database Query Level
- **What**: Cache SQL query results
- **Pros**: Easy to implement, automatic
- **Cons**: Cache invalidation complexity
- **Example**: Caching "SELECT * FROM users WHERE active=1"

#### Caching at Object Level
- **What**: Cache application objects/entities
- **Pros**: Fine-grained control, semantic caching
- **Cons**: More complex implementation
- **Example**: Caching User object, Product object

### Cache Update Patterns

#### Cache-Aside (Lazy Loading)
```
if (data not in cache):
    data = fetch_from_database()
    cache.set(key, data)
return data
```
- **Pros**: Only caches requested data, resilient to cache failures
- **Cons**: Cache miss penalty, stale data possible

#### Write-Through
```
cache.set(key, data)
database.save(data)
```
- **Pros**: Cache always consistent, no cache miss penalty
- **Cons**: Write penalty, unnecessary caching

#### Write-Behind (Write-Back)
```
cache.set(key, data)
// Asynchronously write to database later
```
- **Pros**: Fast writes, good for write-heavy workloads
- **Cons**: Data loss risk, complex consistency

#### Refresh-Ahead
```
if (cache_expiry_time - current_time < threshold):
    background_refresh_cache()
```
- **Pros**: Low latency, fresh data
- **Cons**: Complex implementation, resource overhead

### When to Update Cache
- **TTL (Time To Live)**: Automatic expiration
- **Event-based**: Update on data changes
- **Manual**: Explicit cache invalidation
- **Write-through**: Update on every write

---

## Asynchronous Processing

### Purpose
- Decouple components for better scalability
- Handle time-consuming tasks without blocking
- Improve system resilience

#### Message Queues
- **Purpose**: Asynchronous communication between services
- **Pattern**: Producer → Queue → Consumer
- **Examples**: RabbitMQ, Amazon SQS, Apache Kafka
- **Use cases**: Order processing, email sending, image processing

**Benefits**:
- **Decoupling**: Services don't need direct communication
- **Reliability**: Messages persist until processed
- **Scalability**: Multiple consumers can process messages
- **Load leveling**: Smooth out traffic spikes

#### Task Queues
- **Purpose**: Distribute work across multiple workers
- **Pattern**: Task → Queue → Worker Pool
- **Examples**: Celery, Sidekiq, Bull
- **Use cases**: Background jobs, batch processing

**Benefits**:
- **Parallel processing**: Multiple workers handle tasks
- **Priority handling**: Important tasks processed first
- **Retry logic**: Failed tasks can be retried
- **Monitoring**: Track task status and performance

#### Back Pressure
- **Definition**: System's ability to handle overload gracefully
- **Strategies**:
  - **Buffering**: Queue requests temporarily
  - **Dropping**: Discard less important requests
  - **Throttling**: Limit request rate
  - **Load shedding**: Reject requests when overloaded

**Example**: Web server rejecting requests when queue is full

---

## Communication Protocols

### Transmission Control Protocol (TCP)
- **Characteristics**: Reliable, connection-oriented, ordered delivery
- **Features**:
  - **Reliability**: Guaranteed delivery with acknowledgments
  - **Flow control**: Prevents overwhelming receiver
  - **Congestion control**: Adapts to network conditions
  - **Error detection**: Checksums for data integrity

**Use cases**: HTTP, HTTPS, FTP, email
**Pros**: Reliable, ordered, error-free
**Cons**: Higher overhead, slower than UDP

### User Datagram Protocol (UDP)
- **Characteristics**: Unreliable, connectionless, fast
- **Features**:
  - **Speed**: Minimal overhead
  - **Simple**: No connection establishment
  - **Broadcast**: Can send to multiple recipients
  - **No guarantees**: Best-effort delivery

**Use cases**: DNS, video streaming, online gaming
**Pros**: Fast, low overhead, real-time friendly
**Cons**: No reliability guarantees

### Remote Procedure Call (RPC)
- **Definition**: Call functions on remote systems as if local
- **Types**:
  - **gRPC**: Google's modern RPC framework
  - **JSON-RPC**: Simple, text-based RPC
  - **Apache Thrift**: Cross-language RPC

**Benefits**:
- **Abstraction**: Hide network complexity
- **Type safety**: Strong typing across languages
- **Performance**: Binary protocols are fast
- **Code generation**: Automatic client/server code

**Drawbacks**:
- **Tight coupling**: Client depends on server interface
- **Network transparency**: Hides network failures
- **Complexity**: More complex than REST

### Representational State Transfer (REST)
- **Principles**:
  - **Stateless**: Each request contains all needed information
  - **Resource-based**: URLs represent resources
  - **HTTP methods**: GET, POST, PUT, DELETE
  - **Uniform interface**: Consistent API design

**Benefits**:
- **Simplicity**: Easy to understand and implement
- **Cacheable**: HTTP caching mechanisms
- **Scalable**: Stateless nature enables scaling
- **Interoperable**: Works across different platforms

**HTTP Methods**:
- **GET**: Retrieve resource
- **POST**: Create new resource
- **PUT**: Update/replace resource
- **DELETE**: Remove resource
- **PATCH**: Partial update

---

## Security

### 1. Authentication & Authorization

#### Authentication
- **Purpose**: Verify user identity ("Who are you?")
- **Methods**:
  - **Username/Password**: Traditional method
  - **Multi-factor Authentication (MFA)**: Multiple verification steps
  - **Biometric**: Fingerprint, facial recognition
  - **Certificate-based**: Digital certificates

#### Authorization
- **Purpose**: Control access to resources ("What can you do?")
- **Models**:
  - **Role-Based Access Control (RBAC)**: Permissions based on roles
  - **Attribute-Based Access Control (ABAC)**: Permissions based on attributes
  - **Access Control Lists (ACL)**: Explicit permissions per resource

#### Methods

**JWT (JSON Web Tokens)**
- **Structure**: Header.Payload.Signature
- **Benefits**: Stateless, self-contained, scalable
- **Use cases**: Single sign-on, API authentication
- **Security**: Must be signed/encrypted, short expiration

**OAuth 2.0**
- **Purpose**: Authorization framework for third-party access
- **Flow**: Authorization Code, Client Credentials, Resource Owner Password
- **Use cases**: Social login, API access delegation
- **Components**: Authorization Server, Resource Server, Client

**API Keys**
- **Purpose**: Simple authentication for API access
- **Implementation**: Unique key per client/application
- **Security**: Should be rotated regularly, use HTTPS
- **Limitations**: No user context, limited security

### 2. Data Protection

#### Encryption
**At Rest**:
- **Purpose**: Protect stored data
- **Methods**: AES-256, database encryption, file system encryption
- **Examples**: Encrypted database columns, encrypted storage volumes

**In Transit**:
- **Purpose**: Protect data during transmission
- **Methods**: TLS/SSL, VPN, encrypted messaging
- **Examples**: HTTPS, secure API calls

#### Hashing
- **Purpose**: One-way data transformation for passwords
- **Algorithms**: bcrypt, scrypt, Argon2, PBKDF2
- **Properties**: 
  - **Irreversible**: Cannot recover original password
  - **Salt**: Random data added to prevent rainbow table attacks
  - **Slow**: Intentionally slow to prevent brute force

**Example**:
```
Original: "password123"
Salt: "randomsalt"
Hash: bcrypt("password123" + "randomsalt") = "$2b$10$..."
```

#### Tokenization
- **Purpose**: Replace sensitive data with non-sensitive tokens
- **Use cases**: Credit card numbers, SSNs, personal data
- **Benefits**: Reduces scope of compliance, data breach impact
- **Example**: Credit card 4111-1111-1111-1111 → Token ABC123XYZ

### 3. Network Security

#### HTTPS
- **Purpose**: Secure HTTP communication
- **Components**: 
  - **TLS/SSL**: Encryption protocol
  - **Certificates**: Verify server identity
  - **Certificate Authority**: Trusted third party
- **Benefits**: Data encryption, server authentication, data integrity

#### VPC (Virtual Private Cloud)
- **Purpose**: Private network within cloud infrastructure
- **Features**:
  - **Subnets**: Segment network into smaller parts
  - **Security Groups**: Virtual firewalls for instances
  - **NACLs**: Network-level access control
  - **VPN Gateway**: Secure connection to on-premises

#### Firewalls
- **Purpose**: Control network traffic based on rules
- **Types**:
  - **Network Firewall**: Filters traffic between networks
  - **Host Firewall**: Protects individual machines
  - **Application Firewall**: Filters application-layer traffic

**Rules Example**:
- Allow: HTTP (port 80) from anywhere
- Allow: HTTPS (port 443) from anywhere
- Allow: SSH (port 22) from admin network only
- Deny: All other traffic

### Security Best Practices
1. **Principle of Least Privilege**: Minimum necessary access
2. **Defense in Depth**: Multiple security layers
3. **Regular Updates**: Keep software/systems updated
4. **Security Monitoring**: Log and monitor security events
5. **Incident Response**: Plan for security breaches
6. **Regular Audits**: Periodic security assessments
7. **Employee Training**: Security awareness programs

---

## Conclusion

This comprehensive guide covers the fundamental concepts of system design. Understanding these concepts helps in:

- **Designing scalable systems**: Handle growth in users and data
- **Making informed trade-offs**: Balance between different system properties
- **Choosing appropriate technologies**: Select right tools for specific requirements
- **Troubleshooting issues**: Identify and resolve system problems
- **Communicating effectively**: Discuss system architecture with teams

Remember that system design is about trade-offs. There's no perfect solution - only solutions that best fit your specific requirements, constraints, and context.

## Further Reading
- "Designing Data-Intensive Applications" by Martin Kleppmann
- "System Design Interview" by Alex Xu
- "Building Microservices" by Sam Newman
- High Scalability blog
- AWS Architecture Center
- Google Cloud Architecture Framework 