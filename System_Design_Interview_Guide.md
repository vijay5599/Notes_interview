# Scenario-Based System Design Interview Guide
### A Practical Guide to Delivering Structured, Senior-Level Interview Answers

---

## Table of Contents
1. [API Response Time Increased](#1-api-response-time-increased)
2. [Website Crashes During Sale](#2-website-crashes-during-sale)
3. [Database is Slow](#3-database-is-slow)
4. [Millions Access Same Data](#4-millions-access-same-data)
5. [File Upload Service](#5-file-upload-service)
6. [Notification Service](#6-notification-service)
7. [Login Service Under Heavy Load](#7-login-service-under-heavy-load)
8. [Product Search is Slow](#8-product-search-is-slow)
9. [High Memory Usage](#9-high-memory-usage)
10. [One Server Goes Down](#10-one-server-goes-down)
11. [Database Failure](#11-database-failure)
12. [Too Many API Requests](#12-too-many-api-requests)
13. [Reduce API Latency](#13-reduce-api-latency)
14. [Scale to 1 Million Concurrent Users](#14-scale-to-1-million-concurrent-users)
15. [Slow Microservice](#15-slow-microservice)
16. [Reduce Database Load](#16-reduce-database-load)
17. [Prevent Duplicate Orders](#17-prevent-duplicate-orders)
18. [URL Shortener (System Design & FastAPI Code)](#18-url-shortener-system-design--fastapi-code)
19. [Chat Application](#19-chat-application)
20. [Video Streaming](#20-video-streaming)
21. [Ad-Click Tracking (High Write Throughput)](#21-ad-click-tracking-high-write-throughput)
22. [Web Crawler (Large Scale Ingestion)](#22-web-crawler-large-scale-ingestion)
23. [Real-time Leaderboard](#23-real-time-leaderboard)
24. [Design a Rate Limiter (Distributed System)](#24-design-a-rate-limiter-distributed-system)
25. [Stock Brokerage App (Real-time & High Consistency)](#25-stock-brokerage-app-real-time--high-consistency)
26. [Nearby Friends / Uber Driver Locator (Geospatial Queries)](#26-nearby-friends--uber-driver-locator-geospatial-queries)
27. [Design an API Gateway](#27-design-an-api-gateway)
28. [Distributed Transactions (Saga Pattern)](#28-distributed-transactions-saga-pattern)
29. [Design a Web Webhook System](#29-design-a-web-webhook-system)
30. [Ticket Booking System (Preventing Double Booking)](#30-ticket-booking-system-preventing-double-booking)
31. [Common Follow-up Questions](#common-follow-up-questions)

---

## 1. API Response Time Increased

### Scenario
API latency has increased from 200 ms to 5 seconds.

### Core Bottlenecks
- Unindexed or slow database queries.
- Downstream microservice dependencies failing or blocking.
- Application-level resource exhaustion (thread pool starvation, high CPU, memory leaks).
- Sub-optimal caching strategies (low cache hit ratio).

### Structured Interview Answer
> "To diagnose the latency spike, I would trace the request path systematically. First, I'd review APM metrics (like Datadog/New Relic) to isolate whether the bottleneck is inside our code, the database, or an external dependency. I would check system resource metrics (CPU, Memory, connection pools) to see if we have resource starvation. Next, I'd analyze database performance metrics, checking for slow query logs, N+1 query patterns, and connection limits. Finally, I would verify the cache hit ratio on Redis. Once the root cause is identified, I'd apply targeted optimizations: adding missing database indexes, introducing connection pooling, refactoring heavy computations into asynchronous background workers, or caching repetitive queries."

### Architectural Solution
```
[Client] ---> [API Gateway] ---> [App Server (Connection Pool)] ---> [Redis Cache]
                                       |
                                       v
                                [SQL Database (Indexed)]
```

---

## 2. Website Crashes During Sale

### Scenario
An e-commerce website crashes or becomes unresponsive during a high-traffic flash sale.

### Core Bottlenecks
- Sudden traffic spikes overwhelming application server capacity.
- Database write bottleneck due to thousands of concurrent transaction locks (inventory updates).
- Thread/connection exhaustion on API Gateways and load balancers.

### Structured Interview Answer
> "When a system crashes during a flash sale, it is typically caused by a cascading failure. To prevent this, we must implement scaling, caching, and rate limiting. First, I would introduce a Load Balancer (like NGINX or AWS ALB) with auto-scaling groups to distribute requests across stateless application instances. Second, we must shield the database from read traffic by caching hot data (like product details) in a distributed cache like Redis. To handle the write bottleneck on checkout/order placement, I would decouple the transaction flow using a Message Queue (like RabbitMQ or Kafka). The order service writes to the queue and returns an immediate 'processing' response, allowing background workers to consume and commit transactions at a rate the database can handle."

### Architectural Solution
```
[Flash Sale Traffic] 
        |
        v
 [Load Balancer]
   /    |     \
[App] [App]  [App] ---> [Redis (Hot Product Data)]
   \    |     /
  [Message Queue] ---> [Order Workers] ---> [Database (Write Replicas)]
```

---

## 3. Database is Slow

### Scenario
The relational database query latency has degraded, dragging down overall system throughput.

### Core Bottlenecks
- Table scans caused by missing indexes on fields used in `WHERE` and `JOIN` clauses.
- High connection overhead due to lack of connection pooling.
- Massive table sizes causing disk I/O bottlenecks.

### Structured Interview Answer
> "A slow database is resolved through query optimization, indexing, and resource management. First, I would check the Database Performance Analyzer or run `EXPLAIN` on the slowest queries to verify if they are performing Full Table Scans instead of Index Seeks. If indexes are missing, I'd create them, making sure to avoid over-indexing high-write tables. Next, I'd verify that the application uses Connection Pooling (like HikariCP) to avoid the overhead of establishing new connections. If reads are the primary bottleneck, I would spin up Read Replicas to offload read traffic. For very large datasets, I'd implement horizontal scaling through Database Sharding or table partitioning based on a partition key like `created_at` or `user_id`."

### Architectural Solution
```
                     [App Server]
                    /            \
             (Writes)            (Reads)
               /                  \
              v                    v
     [Primary DB] --Replication--> [Read Replica 1]
                                  [Read Replica 2]
```

---

## 4. Millions Access Same Data

### Scenario
Millions of users are concurrently requesting the same piece of popular data (e.g., a viral post or breaking news article).

### Core Bottlenecks
- The Cache Stampede (Dogpiling) effect: Cache expiration causes thousands of requests to hit the database simultaneously.
- Memory and network throughput saturation on a single database node.

### Structured Interview Answer
> "To serve hot data to millions of concurrent users, we must implement caching at multiple layers. First, I'd use a Content Delivery Network (CDN) like Cloudflare at the edge to cache static assets and API responses closest to the users. Second, inside our backend, I would implement a distributed caching layer using Redis. To prevent a Cache Stampede when the cache expires, I'd implement locking (only the first thread refreshes the cache, others wait) or set a background cron job to periodically refresh the cache before it expires. If the data is read-heavy and dynamic, I'd also scale the cache layer using Redis Cluster with read replicas."

### Architectural Solution
```
[Users] ---> [CDN (Edge Cache)] ---> [API Gateway] ---> [Redis Cluster] ---> [Database]
```

---

## 5. File Upload Service

### Scenario
Designing a service to handle uploading large files (e.g., videos, documents) efficiently.

### Core Bottlenecks
- Blocking application threads while uploading large files directly to application servers.
- High network bandwidth utilization on internal servers.

### Structured Interview Answer
> "For a scalable file upload service, we should never stream large payloads directly through our application servers. Instead, I would use the Presigned URL pattern. The client requests a presigned upload URL from our API, which generates a short-lived URL pointing directly to an Object Storage service like AWS S3 or Google Cloud Storage. The client then uploads the file directly to S3 via HTTP PUT. Once the upload completes, S3 triggers an asynchronous event notification (e.g., via SQS/Lambda) to notify our database of the new file's metadata and URL. This keeps our application servers stateless and free of heavy network I/O."

### Architectural Solution
```
1. Get Presigned URL: [Client] --------> [App Server] ---> [DB]
2. Direct Upload:     [Client] --------> [Object Storage (S3)]
3. Async Event:                          [Object Storage] ---> [Queue] ---> [App Server]
```

---

## 6. Notification Service

### Scenario
Designing a system capable of sending push, email, and SMS notifications at scale.

### Core Bottlenecks
- Third-party API latencies (Twilio, SendGrid) blocking application threads.
- Message loss during system crashes.
- Duplicate notifications sent to users.

### Structured Interview Answer
> "I would design a decoupled, message-driven notification system. The main application services publish a notification event (containing user ID and template metadata) to a Message Queue like RabbitMQ or Apache Kafka. We then deploy a fleet of stateless Notification Workers that consume messages from the queue. These workers format the template, resolve user preferences, and call external APIs (like SendGrid or Twilio). Using a queue ensures that we don't block main application APIs, and we get automatic retries with Dead Letter Queues (DLQ) if third-party providers are down. To prevent duplicate notifications, I would implement idempotency checks on the workers using a Redis cache to track processed notification UUIDs."

### Architectural Solution
```
[API Clients] ---> [App Services] ---> [Kafka/RabbitMQ] 
                                            |
                                            v
                                   [Notification Workers]
                                    /       |        \
                                [APNs]  [Twilio]  [SendGrid]
```

---

## 7. Login Service Under Heavy Load

### Scenario
The authentication and login service is experiencing heavy load, causing auth delays across the platform.

### Core Bottlenecks
- CPU-intensive password hashing algorithms (bcrypt/argon2) bottlenecking application servers.
- Excessive database reads/writes to verify sessions on every incoming request.

### Structured Interview Answer
> "To scale a login service under heavy load, we must offload both CPU hashing operations and session checks. First, I'd use Stateless JWT (JSON Web Tokens) instead of database-backed session state. The client stores the JWT, and our services decode and verify the cryptographically signed token locally using CPU, eliminating database lookups on every request. Second, to handle password hashing spikes, we can separate the authentication handler into a dedicated microservice that can be auto-scaled independently. We should also place a Rate Limiter (using a Token Bucket algorithm) on the login route to protect against brute-force attacks, and utilize Redis to blacklist revoked tokens."

### Architectural Solution
```
[Client] ---> [Rate Limiter (Redis)] ---> [Auth Service (Bcrypt)] ---> [DB]
    |                                          | (Generates JWT)
    v                                          v
[Gateway] --(Validates JWT Locally via CPU)--> [Resource Services]
```

---

## 8. Product Search is Slow

### Scenario
Searching products by keywords using SQL `LIKE %term%` queries is slow and does not scale as product inventory grows.

### Core Bottlenecks
- Relational databases cannot use indexes for queries starting with wildcards (`%`).
- Standard SQL cannot handle relevance ranking (TF-IDF), typo tolerance, or synonyms natively.

### Structured Interview Answer
> "Relational databases are not designed for full-text search. To solve this, I would decouple search from our primary database by indexing product records into a search-dedicated search engine like Elasticsearch or OpenSearch. The application reads directly from Elasticsearch for search queries, which supports inverted indexes, fuzzy matching (typo tolerance), and relevance scoring. To keep the search index in sync with our SQL database, I would use Change Data Capture (CDC) tools like Debezium with Kafka. Whenever a product is inserted, updated, or deleted, the change event is streamed to Kafka and consumed by an indexer service that updates Elasticsearch in near-real-time."

### Architectural Solution
```
[SQL Database] ---> [Debezium (CDC)] ---> [Kafka] ---> [Indexer Service] ---> [Elasticsearch]
                                                                                   ^
[Client] ------------------------(Search Query)------------------------------------+
```

---

## 9. High Memory Usage

### Scenario
Application servers are crashing due to Out of Memory (OOM) errors or consistently high memory usage.

### Core Bottlenecks
- Memory leaks (unclosed database connections, long-lived global objects).
- Loading entire database result sets into memory instead of streaming or paginating.
- Cache size growing indefinitely without eviction policies.

### Structured Interview Answer
> "To resolve high memory usage, I would profile the application heap. First, I'd capture a heap dump using profiling tools (like JProfiler, Go pprof, or Chrome DevTools for Node.js) during high load. I would analyze this dump to identify memory leaks, large object allocations, and unclosed resources. Second, I would check our database query layers: we must enforce query pagination (e.g., limit/offset) to ensure we never load millions of rows into application memory. Third, if in-memory caching is used, I would enforce a strict maximum cache size limit and use Least Recently Used (LRU) eviction policies. Finally, I'd configure garbage collection parameters and monitor connection pool exhaustion."

---

## 10. One Server Goes Down

### Scenario
A critical backend server hosting our APIs suddenly goes offline.

### Core Bottlenecks
- Single Point of Failure (SPOF) in the server architecture.
- Lack of automatic failover or load balancing.

### Structured Interview Answer
> "To ensure high availability and prevent downtime when a server goes down, we must design a stateless, redundant architecture. First, I would deploy multiple instances of our application server across different availability zones. These servers run behind a Load Balancer (such as AWS ALB or Cloudflare). The load balancer performs continuous HTTP health checks (e.g., `/health`) on each instance. If a server fails its health check, the load balancer automatically stops routing traffic to it. By keeping the application servers stateless—storing sessions in Redis or using client-side JWTs—any instance can handle any incoming request, allowing us to drop or add servers dynamically without interrupting user sessions."

### Architectural Solution
```
                 [Load Balancer (Health Checks)]
                 /              |              \
      [App Server 1]     [App Server 2 (Failed)]  [App Server 3]
       (Active/Multi-AZ)      (Routed Out)         (Active/Multi-AZ)
```

---

## 11. Database Failure

### Scenario
The primary database node crashes, causing database writes to fail.

### Core Bottlenecks
- Single Point of Failure (SPOF) on the primary database engine.
- Manual intervention required to promote a replica to primary.

### Structured Interview Answer
> "To recover from database failure, we must implement a Primary-Replica architecture with automatic failover. The primary database handles all writes and replicates data asynchronously to one or more read replicas. We run a cluster management tool (such as Orchestrator, PostgreSQL Patroni, or AWS RDS Multi-AZ). These tools continuously monitor the health of the primary node. If the primary node goes down, the cluster manager detects the failure, coordinates a consensus vote, and automatically promotes the most up-to-date read replica to be the new primary. The application's database connection pool is updated via DNS or a database proxy (like PgBouncer) to route write queries to the newly promoted primary without downtime."

### Architectural Solution
```
[Database Proxy] ---> [New Primary (Promoted)] <--- (Writes)
                            |
                   (Async Replication)
                            v
                      [Read Replica] <--- (Reads)
```

---

## 12. Too Many API Requests

### Scenario
The system is overwhelmed by a flood of API requests (DDoS attempt or scraping bots).

### Core Bottlenecks
- Lack of rate limiting at the entry points.
- Resource starvation on downstream web servers.

### Structured Interview Answer
> "To protect our system from being overwhelmed, we must implement rate limiting. I would deploy a Rate Limiter at the API Gateway level (such as Kong, AWS API Gateway, or NGINX). Under the hood, the rate limiter uses a distributed store like Redis to track request counts per client IP or API key using the Token Bucket or Sliding Window Log algorithm. If a client exceeds their allocated quota (e.g., 60 requests per minute), the API Gateway immediately short-circuits the request and returns an HTTP status code `429 Too Many Requests`. This prevents malicious or excessive traffic from reaching and starving resource-intensive downstream application servers."

### Architectural Solution
```
[Clients] ---> [API Gateway (Rate Limiter Middleware)] <---> [Redis (Quota Store)]
                     |
            (HTTP 429 if Exceeded)
                     |
                     v
             [Backend Services]
```

---

## 13. Reduce API Latency

### Scenario
The P99 API response latency is high, causing a sluggish user experience.

### Core Bottlenecks
- Network latency due to routing requests across the globe to a single server region.
- Slow disk I/O and database round-trips.
- Uncompressed payloads and blocking synchronous tasks.

### Structured Interview Answer
> "To reduce API latency, we must optimize at multiple levels. First, at the network edge, I would use a CDN to cache static assets and utilize edge-routing to terminate SSL handshakes closer to the user. Second, I would implement caching using Redis for expensive database query responses. Third, I'd review the backend codebase: we should use compression algorithms (like Gzip or Brotli) to reduce payload size, optimize database access by replacing slow queries with indexed queries, and handle non-blocking operations (like sending emails or logging analytics) asynchronously via a message queue rather than in the request-response thread."

---

## 14. Scale to 1 Million Concurrent Users

### Scenario
Designing a system architecture that can scale to support 1 million concurrent active users.

### Core Bottlenecks
- Monolithic database scalability limitations.
- Stateful application architectures that prevent horizontal scaling.
- Connection limits on network interfaces.

### Structured Interview Answer
> "Scaling to 1 million concurrent users requires a shared-nothing, horizontally scalable architecture. First, all application servers must be stateless so that we can scale them horizontally behind global load balancers. Second, we must minimize database pressure. We cache heavily at the CDN level and use a Redis cluster for database read caching. Third, for the database, we implement a read/write split with multiple read replicas. As we grow further, we shard the database horizontally based on a tenant or user ID. We must also use asynchronous messaging via Kafka to handle non-critical transactions, and utilize connection pooling and connection multiplexing (using tools like gRPC over HTTP/2) to manage network socket limits."

### Architectural Solution
```
[Users] ---> [Anycast DNS] ---> [CDN] ---> [Load Balancer]
                                                |
                                      [Stateless App Tier]
                                       /        |        \
                             [Redis Cluster] [Kafka] [Sharded DBs]
```

---

## 15. Slow Microservice

### Scenario
A specific microservice in a distributed system is causing cascading latency across other services.

### Core Bottlenecks
- Synchronous blocking HTTP/REST calls between services creating a dependency chain.
- Thread exhaustion on caller services.

### Structured Interview Answer
> "To address a slow microservice, I would first check distributed tracing logs (using Jaeger or Zipkin) to identify which downstream call is blocking. If services are chained synchronously (Service A waits for B, which waits for C), I would break this tight coupling. I would migrate non-blocking communication to asynchronous event-driven architectures using Apache Kafka or RabbitMQ. For remaining synchronous calls, I would implement the Circuit Breaker pattern (using tools like Resilience4j). If the downstream service latency exceeds a threshold, the circuit opens, and the caller immediately returns a fallback response instead of waiting, preventing thread exhaustion from propagating up the stack."

### Architectural Solution
```
[Service A] --(REST Sync)--> [Service B (Slow)] ---> Thread Pool Exhausted! (Cascading Failure)

-- Optimized with Circuit Breaker and Async Messaging --

[Service A] --(Circuit Breaker)--> [Service B (Slow)] --(Trips Open: Fast Fallback)
    |
(Publishes Event)
    v
[Kafka Queue] ------------------------------------> [Service B Processes Asynchronously]
```

---

## 16. Reduce Database Load

### Scenario
The primary database server's CPU utilization is hovering near 100%, causing query timeouts.

### Core Bottlenecks
- Repetitive read queries hitting disk.
- Analytical or reporting queries running on the primary transaction engine.

### Structured Interview Answer
> "To reduce database load, I would separate read traffic from write traffic. First, I would set up Read Replicas and configure the application routing layer to direct all `SELECT` queries to the replicas, reserving the primary database node strictly for write operations. Second, I would implement caching using Redis for frequently requested, slow-changing queries. Third, to prevent expensive aggregations from running on the live database, I would use Materialized Views or pre-compute reporting data into a data warehouse like Snowflake or BigQuery via ETL pipelines. Finally, I would enforce strict query limits and pagination to prevent large data transfers."

---

## 17. Prevent Duplicate Orders

### Scenario
A user double-clicks the "Place Order" button, causing duplicate charges and orders in the database.

### Core Bottlenecks
- Non-idempotent API endpoints.
- Network retries from clients.

### Structured Interview Answer
> "To prevent duplicate orders, we must make our checkout API endpoint Idempotent. I would implement an Idempotency Key pattern. When the user loads the checkout page, the client requests a unique idempotency token (UUID) from the server. When submitting the order, the client sends this token in the API request header. On the backend, we check Redis for the token: if the token is not present, we acquire a distributed lock in Redis for that token and process the order. Once processed, we save the order response in Redis mapped to the token. If a duplicate request arrives with the same token, the server detects it in Redis and immediately returns the cached response without reprocessing the order. The keys are configured to expire after 24 hours."

### Architectural Solution
```
[Client] --(POST Order / Key: xyz)--> [App Server] <---> [Redis (Check & Lock 'xyz')]
                                             |
                                  (Processed: Save order result)
                                             |
[Client] --(Retry POST / Key: xyz)---> [App Server] <---> [Redis finds 'xyz' -> Returns Cached Order]
```

---

## 18. URL Shortener (System Design & FastAPI Code)

### Scenario
Designing a scalable URL shortening service like TinyURL.

### Core Bottlenecks
- High read traffic for URL redirection.
- Generating unique short keys without collisions at scale.

### Structured Interview Answer
> "A URL shortener is a highly read-heavy system. To design it, I would use a Load Balancer, stateless app servers, a distributed cache (Redis), and a relational database (or NoSQL key-value store like DynamoDB). For the shortening algorithm, I would convert a unique sequential ID into a Base62 string (using characters `a-z, A-Z, 0-9`), which gives us 62^7 combinations for a 7-character key. To generate unique IDs without collisions in a distributed system, I would use a distributed ID generator like Twitter Snowflake or a range-allocation coordinator (Zookeeper). For redirection (`/abc` -> `/long-url`), the request hits the app server, which checks Redis first. On a cache hit, we return an HTTP 301 Permanent Redirect. On a cache miss, we load from the database, write back to Redis, and redirect."

### Architectural Solution
```
[Client] ---> [Load Balancer] ---> [App Servers] <---> [Redis Cache]
                                        |                  ^
                               (Distributed ID)            |
                                        v                  |
                                [Zookeeper Range]   [DB Mapping Table]
```

### Production Implementation (FastAPI + SQLite + Redis)
Below is the complete, production-ready implementation of a URL shortener service using **FastAPI**, **SQLite** (using SQLAlchemy for metadata tracking), and **Redis** (as the fast redirection cache).

```python
import string
import time
from typing import Optional
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, HttpUrl
import redis
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# ----------------- Database Setup -----------------
DATABASE_URL = "sqlite:///./url_shortener.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class URLModel(Base):
    __tablename__ = "urls"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    long_url = Column(String, nullable=False)
    short_code = Column(String, unique=True, index=True, nullable=True)

Base.metadata.create_all(bind=engine)

# ----------------- Redis Cache Setup -----------------
# Falls back to local memory if Redis is unavailable (Fail Open pattern)
try:
    redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
    redis_client.ping()
except Exception:
    redis_client = None

# ----------------- Base62 Encoding -----------------
BASE62_ALPHABET = string.ascii_letters + string.digits  # a-z, A-Z, 0-9

def encode_base62(num: int) -> str:
    """Encodes an integer database ID to a Base62 string."""
    if num == 0:
        return BASE62_ALPHABET[0]
    arr = []
    base = len(BASE62_ALPHABET)
    while num:
        num, rem = divmod(num, base)
        arr.append(BASE62_ALPHABET[rem])
    arr.reverse()
    return ''.join(arr)

# ----------------- FastAPI App -----------------
app = FastAPI(title="URL Shortener Service", version="1.0.0")

class URLRequest(BaseModel):
    url: HttpUrl

class URLResponse(BaseModel):
    long_url: str
    short_url: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/shorten", response_model=URLResponse, status_code=status.HTTP_201_CREATED)
def shorten_url(request: URLRequest, db: Session = Depends(get_db)):
    long_url_str = str(request.url)
    
    # 1. Insert URL to get the auto-increment ID
    db_url = URLModel(long_url=long_url_str)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    
    # 2. Encode auto-increment ID to Base62
    short_code = encode_base62(db_url.id)
    
    # 3. Update the entry with the generated short code
    db_url.short_code = short_code
    db.commit()
    
    # 4. Cache in Redis (Expire in 24 hours to prevent memory leaks)
    if redis_client:
        try:
            redis_client.setex(short_code, 86400, long_url_str)
        except Exception:
            pass  # Fail open
            
    return URLResponse(long_url=long_url_str, short_url=f"http://localhost:8000/{short_code}")

@app.get("/{short_code}")
def redirect_to_long_url(short_code: str, db: Session = Depends(get_db)):
    # 1. Try reading from Redis cache first
    if redis_client:
        try:
            cached_url = redis_client.get(short_code)
            if cached_url:
                return RedirectResponse(url=cached_url, status_code=status.HTTP_301_MOVED_PERMANENTLY)
        except Exception:
            pass  # Fallback to database on cache connection issues
            
    # 2. Cache miss: Read from relational database
    db_url = db.query(URLModel).filter(URLModel.short_code == short_code).first()
    if not db_url:
        raise HTTPException(status_code=404, detail="Short URL not found")
        
    # 3. Write back to Redis cache
    if redis_client:
        try:
            redis_client.setex(short_code, 86400, db_url.long_url)
        except Exception:
            pass
            
    return RedirectResponse(url=db_url.long_url, status_code=status.HTTP_301_MOVED_PERMANENTLY)
```

---

## 19. Chat Application

### Scenario
Designing a real-time chat application (like WhatsApp or Slack) supporting 1-on-1 and group messaging.

### Core Bottlenecks
- Maintaining thousands of persistent, open connections on servers.
- Syncing message delivery states (sent, delivered, read) across offline clients.

### Structured Interview Answer
> "To support real-time messaging, I would establish persistent bidirectional connections between clients and our servers using WebSockets. When a client connects, they are assigned to a specific WebSocket Server node. We store this mapping (User ID -> WebSocket Server IP) in a distributed hash table or Redis. When User A sends a message to User B, the request hits User A's WebSocket server. The server checks Redis to locate User B's active WebSocket connection node, publishes the message to a pub/sub layer (like Redis Pub/Sub or Kafka), and the target node delivers the message to User B. If User B is offline, we push the message to a message queue and save it to a NoSQL database (like Cassandra or DynamoDB, which are optimized for sequential writes) so B can retrieve it when they reconnect."

### Architectural Solution
```
[Client A] <---(WebSocket)---> [WS Server 1] ---> [Redis Pub/Sub] <--- [WS Server 2] <---(WS)---> [Client B]
                                     |
                             (If Offline: Queue)
                                     v
                              [Kafka Queue] ---> [Cassandra DB]
```

---

## 20. Video Streaming

### Scenario
Designing a video streaming platform (like Netflix or YouTube) supporting adaptive video quality.

### Core Bottlenecks
- Massive storage and network egress costs.
- Buffering and latency issues across different geographic locations.

### Structured Interview Answer
> "To build a scalable video streaming platform, we must separate the ingestion pipeline from the content delivery pipeline. When a creator uploads a video, it is saved in a raw format in Object Storage. This triggers an asynchronous transcoding pipeline (using AWS Elemental MediaConvert or similar tools) that processes the video into multiple resolutions (1080p, 720p, 480p) and splits them into small 2-10 second chunks. We package these chunks using adaptive streaming protocols like HLS (HTTP Live Streaming) or MPEG-DASH. The structured files and manifest files are stored on S3. For delivery, we cache these video segments across a global network of CDNs. When a user plays a video, they fetch the manifest file, and the player dynamically requests chunks from the CDN based on the user's real-time bandwidth."

### Architectural Solution
```
1. Ingestion:  [Creator Upload] ---> [S3 Raw] ---> [Transcoder Engine] ---> [S3 Processed Chunks]
2. Delivery:   [S3 Processed Chunks] ------------> [Global CDN Servers]
3. Playback:   [User Player] --------------------> [Global CDN (Fetches Manifest & Chunks)]
```

---

## 21. Ad-Click Tracking (High Write Throughput)

### Scenario
Designing a system to track billions of ad clicks daily with real-time analytics dashboards.

### Core Bottlenecks
- Extremely high write throughput overwhelming traditional SQL transactional databases.
- Network bandwidth saturation and hot partition issues on database clusters.

### Structured Interview Answer
> "To track billions of clicks, we must decouple ingestion from persistent storage. I would deploy a high-throughput API gateway layer that receives click payloads and immediately routes them to a distributed streaming platform like Apache Kafka. The click data is partitioned in Kafka using a partition key (such as `ad_id` or `user_id`) to distribute the load across multiple brokers. A streaming processing framework (like Apache Flink or Spark Streaming) consumes these events, aggregates metrics (clicks per ad in 1-minute windows), and writes the aggregated data into a NoSQL column family store like Apache Cassandra or a time-series database like InfluxDB. For raw storage (audit logs), we write batch files directly to S3/Cold Storage via a consumer service."

### Architectural Solution
```
[User Clicks] ---> [Ingestion LB] ---> [Kafka Event Log]
                                            |
                              +-------------+-------------+
                              v                           v
                      [Flink Analytics]            [Raw Archiver]
                              |                           |
                              v                           v
                       [Cassandra DB]               [Amazon S3]
```

---

## 22. Web Crawler (Large Scale Ingestion)

### Scenario
Designing a scalable web crawler to download and index billions of web pages.

### Core Bottlenecks
- Infinite cycles and link traps (deduplication of millions of crawled URLs).
- Respecting politeness policies (`robots.txt`) on millions of distinct host domains.
- Massive storage capacity requirements for page contents and links.

### Structured Interview Answer
> "A large-scale web crawler requires a modular, distributed queue architecture. First, we use a URL Frontier to maintain the list of URLs to crawl. The URL Frontier splits URLs into priority queues and politeness queues. A host partitioner ensures we do not hit the same domain concurrently, respecting `robots.txt` directives. Second, before crawling, we check a URL Filter and a duplicate checker (using a high-performance Bloom Filter or Redis Set) to ensure the URL hasn't been crawled before. Third, crawler workers fetch pages, extract text and links, and write the contents to an object store. Extracted links are pushed back to the URL Frontier. We use DNS caching on the workers to avoid overloading DNS servers."

### Architectural Solution
```
           +-------------------- [Link Extractor] <--------------------+
           v                                                           |
  [URL Frontier (Polite)] ---> [Crawler Workers] ---> [HTML Storage] --+
           ^
    (Bloom Filter DB Check)
```

---

## 23. Real-time Leaderboard

### Scenario
Designing a real-time gaming leaderboard showing the top 100 users out of 10 million active players.

### Core Bottlenecks
- SQL database queries using `ORDER BY score DESC LIMIT 100` do not scale when millions of scores update continuously.
- Lock contention on user record tables.

### Structured Interview Answer
> "For a high-performance real-time leaderboard, I would use the Redis Sorted Sets (ZSET) data structure. A Sorted Set internally maintains a dual structure containing a hash table and a skip list, giving us $O(\log N)$ complexity for additions and updates. When a player's score changes, we update their score in Redis using `ZADD leaderboard score user_id`. To fetch the top 100 players instantly, we run `ZREVRANGE leaderboard 0 99 WITHSCORES`, which runs in $O(\log N + M)$ where $M$ is the number of elements requested (100). To ensure reliability, we persist scores asynchronously to a database using a message queue, but serve all reads and updates directly through Redis."

### Architectural Solution
```
[Score Updates] ---> [API Service] ---> [Redis Sorted Set (ZSET)] ---> (Fast Read: ZREVRANGE)
                           |
                     (Async Event)
                           v
                     [Kafka Queue] ---> [SQL DB (Persistence)]
```

---

## 24. Design a Rate Limiter (Distributed System)

### Scenario
Designing a distributed rate limiting system that can scale across multiple data centers.

### Core Bottlenecks
- Race conditions (Concurrent requests from the same user modifying counters in Redis).
- Network latency overhead of querying a central database for every API call.

### Structured Interview Answer
> "To build a robust distributed rate limiter, I would implement a hybrid token bucket algorithm. I'd place rate-limiting middleware at our API Gateways. To prevent the network latency of calling Redis for every single request, the API Gateway local memory can cache token quotas (using local token buckets) and periodically sync counters with a centralized Redis cluster in batches. To resolve race conditions when multiple nodes write to Redis simultaneously, I would write Lua scripts to execute the rate checking and decrementing logic atomically inside Redis. If Redis becomes temporarily unreachable, the middleware fails open, falling back to local memory rate limiting to ensure system availability."

### Architectural Solution
```
[Client] ---> [API Gateway (Local Token Cache)] <---(Sync Batch)---> [Redis Cluster (Lua Scripts)]
                    |
          (Execute Rate Check)
                    v
            [Service Cluster]
```

---

## 25. Stock Brokerage App (Real-time & High Consistency)

### Scenario
Designing a stock trading platform (like Robinhood) handling millions of real-time price updates and order placements.

### Core Bottlenecks
- Real-time price distribution to millions of client devices.
- Transactions require absolute consistency (strictly serializable orders) to prevent selling shares twice.

### Structured Interview Answer
> "A stock trading platform requires a split path architecture. The Market Data Feed (prices) is read-heavy and eventually consistent. We stream price updates from stock exchanges into Kafka, and push them to client applications using a server-sent events (SSE) or WebSocket gateway. The Order Execution Path, however, requires strict consistency. I would design an in-memory Order Matching Engine. All active buy/sell orders for a stock are kept in memory on single-threaded partitions (grouped by stock ticker) to eliminate concurrent database locks. When a trade matches in memory, the engine publishes a matched event to a write-ahead transaction log and updates our transactional database (SQL/PostgreSQL with ACID transaction boundaries) to record the ownership transfer."

### Architectural Solution
```
Price Feed: [Exchange] ---> [Kafka] ---> [WebSocket Gateway] ---> [Clients]

Order Path: [Client] ---> [Order API] ---> [In-Memory Matching Engine]
                                                |
                                      (Write-Ahead Log/Event)
                                                v
                                         [Transactional DB]
```

---

## 26. Nearby Friends / Uber Driver Locator (Geospatial Queries)

### Scenario
Designing a service to locate nearby drivers or friends in real-time on a map.

### Core Bottlenecks
- Continuous location updates (e.g., every 3 seconds) from millions of mobile devices.
- Standard database indexes (B-Trees) cannot quickly search for coordinates in two dimensions ($X, Y$).

### Structured Interview Answer
> "Geospatial queries require dividing 2D space into hierarchical grid cells. I would use Geospatial index algorithms, specifically H3 (Hexagonal hierarchical spatial index) or Geohashes. For real-time updates (like Uber drivers), drivers push their latitude and longitude every few seconds via WebSockets. We store their current location in Redis using `GEOADD`, which uses a Sorted Set underneath to index geohashed values. When a rider opens their app, we run `GEORADIUS` (or `GEOSEARCH`) to query active drivers within a 5km radius. For static entities (like restaurants), we pre-calculate Geohashes and store them in a database with geospatial index support (like PostgreSQL with PostGIS)."

### Architectural Solution
```
[Driver Device] --(WS Location Updates)--> [WebSocket Server] ---> [Redis (GEOADD / Geohash)]
                                                                         ^
[Rider App] -----------------(Query 5km radius: GEOSEARCH)---------------+
```

---

## 27. Design an API Gateway

### Scenario
Designing a entry gateway for a microservice architecture handling authentication, routing, and rate limiting.

### Core Bottlenecks
- High overhead on routing logic introducing latency to all downstream calls.
- Single Point of Failure (SPOF) for all incoming API traffic.

### Structured Interview Answer
> "An API Gateway acts as the reverse proxy for our backend services. I would build it using high-performance, non-blocking I/O frameworks like NGINX, Envoy, or Spring Cloud Gateway. It handles:
  1. **Routing**: Dynamically maps incoming requests to downstream services using a service registry (Consul/Eureka).
  2. **Cross-Cutting Concerns**: Offloads Authentication (validates JWTs), Rate Limiting, CORS headers, and request logging.
  To prevent it from becoming a single point of failure, we run multiple gateway instances behind DNS-based load balancing (like Cloudflare or AWS Route 53) and utilize auto-scaling to scale the gateway fleet based on CPU and network utilization."

---

## 28. Distributed Transactions (Saga Pattern)

### Scenario
An order transaction span across multiple microservices (Order, Payment, Inventory) and must be rolled back if one step fails.

### Core Bottlenecks
- Two-Phase Commit (2PC) is a blocking protocol and does not scale in microservice environments.
- Network outages can cause data inconsistencies between databases.

### Structured Interview Answer
> "In microservice architectures, we replace blocking two-phase commits with the Saga Pattern, which manages distributed transactions using local transactions and compensating actions. I would implement an Orchestrator-Based Saga. An Order Saga Orchestrator manages the workflow:
  1. It tells the Order Service to create a pending order.
  2. It calls the Payment Service to authorize funds.
  3. It calls the Inventory Service to reserve items.
  If the inventory check fails, the orchestrator initiates compensating transactions in reverse order: it notifies the Payment Service to refund the charge and sets the Order Service state to failed. Communication is driven asynchronously via Kafka to handle network retries."

### Architectural Solution
```
[Saga Orchestrator] --(1. Create Order)--> [Order DB] (Success)
[Saga Orchestrator] --(2. Charge Card)---> [Payment DB] (Success)
[Saga Orchestrator] --(3. Reserve Item)--> [Inventory DB] (FAILED!)
[Saga Orchestrator] --(4. Compensation)---> [Payment DB] (Refund card)
[Saga Orchestrator] --(5. Compensation)---> [Order DB] (Set Order Failed)
```

---

## 29. Design a Web Webhook System

### Scenario
Designing a system to notify third-party developer URLs when events occur on our platform (like Stripe payment alerts).

### Core Bottlenecks
- Slow or unresponsive receiver servers block our notification threads.
- Ensuring delivery guarantees (at-least-once delivery) with exponential backoff retries.

### Structured Interview Answer
> "A webhook delivery system must be highly asynchronous and resilient to external receiver failures. When an event occurs on our platform, the core application writes a webhook task to Kafka. A fleet of Webhook Workers consumes these tasks. The worker retrieves the developer's registered webhook URL and payload, and executes an HTTP POST request. If the developer's server responds with an error (e.g., 500) or times out, the worker puts the message into a retry queue managed by a scheduling coordinator (like Redis or RabbitMQ delay exchanges). We retry delivery using exponential backoff (e.g., 5 min, 15 min, 1 hour) up to 24 hours. We must enforce strict connection timeouts (e.g., 5 seconds) to prevent unresponsive servers from locking our worker threads."

### Architectural Solution
```
[Event Trigger] ---> [Kafka Queue] ---> [Webhook Workers] ---> [Developer Endpoint]
                                             |
                                     (Fail: Exponential Retry)
                                             v
                                  [Retry Queue (Delay Queue)]
```

---

## 30. Ticket Booking System (Preventing Double Booking)

### Scenario
Designing a movie ticket or concert booking platform where thousands of users compete for the exact same seats.

### Core Bottlenecks
- Race conditions: Multiple users checking out the same seat concurrently, leading to double booking.
- Slow checkout flows locking seats indefinitely, preventing other buyers from checking out.

### Structured Interview Answer
> "To prevent double booking, I would implement a temporary reservation lock pattern using Redis. When a user selects a seat (e.g., Row A, Seat 10), the application attempts to set an exclusive lock in Redis: `SET seat_A10 user_123 NX PX 600000` (expires in 10 minutes). The `NX` flag ensures that the lock is only set if it does not already exist. If successful, the seat status is marked as 'Reserved' for 10 minutes, and the user proceeds to payment. If the payment succeeds within the window, we commit the booking to our relational database and release the Redis lock. If the user fails to pay or the window expires, the Redis key automatically deletes, instantly releasing the seat back to the pool for other buyers."

### Architectural Solution
```
[User 1] ---> [App API] ---> [Redis: SET seat_A10 user_1 NX PX 600000] (Lock Acquired)
[User 2] ---> [App API] ---> [Redis: SET seat_A10 user_2 NX PX 600000] (FAILED: Already locked)

[User 1] Pays ---> Commit Transaction to Relational Database ---> Release Redis Lock.
```

---
---

## Common Follow-up Questions

### What is the bottleneck?
- **Senior-Level Answer**: "The bottleneck is the slowest component in the request path that limits overall throughput. In system design, we find it by analyzing metrics like CPU utilization, disk I/O, network bandwidth, database lock contention, and thread pool queues. Once we identify the bottleneck, we scale or optimize that specific component—for instance, replacing synchronous database checks with an in-memory cache."

### How do you scale a system from 10K to 10M users?
- **Senior-Level Answer**: "Scaling from 10K to 10M users requires migrating from a monolithic, single-server setup to a distributed, decoupled architecture:
  1. **Stateless Services**: Remove session state from app servers to allow horizontal auto-scaling.
  2. **Introduce Caching**: Place Redis caches in front of the database and use a CDN for static assets.
  3. **Database split**: Move from a single DB instance to a Primary-Replica setup with read replicas, then implement database sharding.
  4. **Decouple writes**: Introduce message queues (like Kafka or RabbitMQ) to handle heavy write operations asynchronously.
  5. **Global routing**: Implement Anycast routing and multi-region deployments to reduce network latency."

### What if Redis fails?
- **Senior-Level Answer**: "To prevent a single point of failure at the cache layer:
  1. **High Availability**: Deploy Redis in a cluster configuration (Redis Sentinel or Redis Cluster) with primary-replica nodes spread across availability zones.
  2. **Cache Stampede Prevention**: If Redis fails entirely, the database must be protected from sudden traffic surges. We implement rate limiters and circuit breakers on the cache client. When the circuit breaker trips, it gracefully degrades the system or restricts traffic instead of allowing all requests to hit the database.
  3. **Cache Warming**: Once Redis recovers, we warm the cache gradually before exposing it to full traffic."

### Why use a message queue instead of synchronous calls?
- **Senior-Level Answer**: "Message queues provide key advantages in system reliability and user experience:
  - **Decoupling**: The producer does not need to know about the implementation details of the consumer.
  - **Latency reduction**: The API returns an immediate response (e.g., HTTP 202 Accepted) to the client, while slow operations (such as processing payments or generating PDFs) run in the background.
  - **Load smoothing (Throttling)**: During traffic spikes, the queue buffers incoming requests, allowing downstream workers to process tasks at their own pace without crashing.
  - **Fault tolerance**: If a worker fails, the message remains in the queue to be retried later, preventing data loss."

### Vertical vs Horizontal Scaling
- **Senior-Level Answer**: 
  - **Vertical Scaling (Scaling Up)**: Increasing the capacity of a single server (adding more CPU, RAM, or disk space). It is simple and requires no architectural changes, but has physical limits and introduces a single point of failure.
  - **Horizontal Scaling (Scaling Out)**: Adding more server nodes to the pool. It offers high availability and scale, but requires stateless application architecture and load-balancing layers.

### How do you avoid a Single Point of Failure (SPOF)?
- **Senior-Level Answer**: "To avoid a SPOF, we must eliminate any component that causes the entire system to stop if it fails. We achieve this by building redundancy into every layer:
  - **App layer**: Deploy multiple stateless servers behind load balancers.
  - **DB layer**: Use primary-replica configurations with automatic failover.
  - **Network layer**: Deploy across multiple Availability Zones (Multi-AZ) and use DNS-based failover.
  - **Monitoring**: Set up automated health checks to route traffic away from unhealthy nodes."

### How do you monitor a system in production?
- **Senior-Level Answer**: "I implement a monitoring system based on the Three Pillars of Observability:
  1. **Metrics**: Use Prometheus and Grafana to track CPU, memory, error rates, and latency.
  2. **Logs**: Aggregate log files using the ELK Stack (Elasticsearch, Logstash, Kibana) or Loki to search through trace logs.
  3. **Traces**: Use OpenTelemetry or Jaeger to trace requests across microservice boundaries to identify latency bottlenecks."

### What are the most important production metrics?
- **Senior-Level Answer**:
  - **Latency**: P95 and P99 response times (rather than average latency, which hides outliers).
  - **Throughput**: Requests per second (RPS).
  - **Error Rate**: Percentage of failed requests (e.g., HTTP 5xx responses).
  - **Resource Utilization**: CPU, Memory, Disk I/O, and database connection pool exhaustion rates.
  - **Cache Hit Ratio**: Percentage of read requests successfully served by the cache.

### Zero Downtime Deployment Strategies
- **Senior-Level Answer**: 
  - **Blue-Green Deployment**: We maintain two identical environments (Blue is active, Green is idle). We deploy the new code to Green, test it, and switch the load balancer routing target to Green. If issues occur, we instantly roll back by routing traffic back to Blue.
  - **Rolling Deployment**: We update servers in batches one by one. The load balancer temporarily drains traffic from a target instance, updates it, and places it back in service.
  - **Canary Deployment**: We roll out the new version to a small subset of servers (e.g., 5% of traffic) to monitor its error rate before rolling it out to the rest of the cluster.

### Consistency vs Availability (CAP Theorem)
- **Senior-Level Answer**: "According to the CAP Theorem, in the event of a network partition (P), a distributed system must choose between Consistency (C) or Availability (A):
  - **Consistency**: Every read query returns the most recent write or an error (e.g., financial ledger transactions).
  - **Availability**: Every request receives a non-error response, without guaranteeing that it contains the most recent write (e.g., social media likes).
  We design the architecture around these business needs: banking systems choose CP by blocking transactions during partitions, while social networks choose AP to keep services online using eventual consistency models."
