# 🧠 System Design & Backend Engineering — Interview Q&A

> **Comprehensive answers for senior backend/full-stack developer interviews**
> Topics: Debugging, DI, Indexing, Error Handling, Serverless, Load Balancing, Middleware, RBAC, Projects, Event Loop, Sharding, Cluster Module

---

## Table of Contents

1. [How did you debug any issue in production?](#1-how-did-you-debug-any-issue-in-production)
2. [What is dependency injection and its types?](#2-what-is-dependency-injection-and-its-types)
3. [What is indexing and its types?](#3-what-is-indexing-and-its-types)
4. [How did you handle global level exceptions or errors?](#4-how-did-you-handle-global-level-exceptions-or-errors)
5. [What are serverless functions?](#5-what-are-serverless-functions)
6. [How did you handle load if a lot of users come to the platform?](#6-how-did-you-handle-load-if-a-lot-of-users-come-to-the-platform)
7. [What is middleware? What is authentication and authorization?](#7-what-is-middleware--what-is-authentication-and-authorization)
8. [How did you handle RBAC?](#8-how-did-you-handle-rbac)
9. [What projects have you worked on?](#9-what-projects-have-you-worked-on)
10. [What is the event loop?](#10-what-is-the-event-loop)
11. [What is sharding and partitioning?](#11-what-is-sharding-and-partitioning)
12. [What is the cluster module?](#12-what-is-the-cluster-module)

---

## 1. How did you debug any issue in production?

### 🎯 What the Interviewer is Really Asking

> **"Did you protect the user from having a bad experience while you were fixing the issue?"**

This is **not just a technical question** — it's a **product mindset + engineering maturity** question. The interviewer wants to know:
- Did you detect the issue **before users reported it**?
- Did you **shield users** from broken experiences while debugging?
- Did you fix it **without downtime or data loss**?
- Did you **prevent it from happening again**?

---

### The Golden Rule of Production Debugging

> **"Fix the user experience FIRST, then find the root cause."**

A bad engineer pushes a quick fix live and hopes for the best.  
A good engineer **protects users first**, then carefully debugs, then deploys a proper fix.

---

### My Approach — The 5-Phase Strategy

---

#### 🔴 Phase 1 — Detect BEFORE the User Does (Proactive Monitoring)

The best production issues are the ones **users never see** because you caught them first.

- Set up **real-time alerting** on key metrics (error rate, response time, CPU, memory)
- Use tools like **Sentry, Datadog, AWS CloudWatch, New Relic**
- Alert thresholds: error rate > 1%, p99 latency > 2s, 5xx spike > 5%
- **Synthetic monitoring** — automated health checks hitting critical endpoints every minute

```javascript
// Health check endpoint — always expose this
app.get('/health', async (req, res) => {
  const checks = {
    database: await checkDBConnection(),
    redis: await checkRedisConnection(),
    uptime: process.uptime(),
  };
  const isHealthy = Object.values(checks).every(Boolean);
  res.status(isHealthy ? 200 : 503).json(checks);
});
```

> 🎯 **Interview Point**: "We had Sentry and Datadog alerting us the moment error rates spiked. In most cases we knew about the problem 2–3 minutes before any user reported it."

---

#### 🟡 Phase 2 — Protect the User Immediately (Graceful Degradation)

When something breaks, **don't show a broken screen**. Show a fallback.

**Techniques:**

**1. Feature Flags — Disable broken features instantly**
```javascript
const featureFlags = await getFeatureFlags(); // from LaunchDarkly / Redis

if (featureFlags.SHOW_RECOMMENDATIONS) {
  const recommendations = await getRecommendations(userId);
  res.json({ products, recommendations });
} else {
  // Feature disabled — user still sees products, just no recommendations
  res.json({ products });
}
```
> ✅ Turn off a broken feature with one config change — no deployment needed.

**2. Circuit Breaker — Stop cascading failures**
```javascript
const CircuitBreaker = require('opossum');

const breaker = new CircuitBreaker(callPaymentService, {
  timeout: 3000,           // fail after 3 seconds
  errorThresholdPercentage: 50, // open circuit if 50% fail
  resetTimeout: 30000,     // try again after 30s
});

breaker.fallback(() => ({
  status: 'pending',
  message: 'Payment is being processed. You will be notified shortly.'
}));
// User sees a friendly message instead of a 500 error
```

**3. Graceful Error Pages — Never show a raw stack trace**
```javascript
// Global error handler
app.use((err, req, res, next) => {
  // Log internally (never expose to user)
  logger.error({ err, url: req.url, userId: req.user?.id });
  Sentry.captureException(err);

  // Show user-friendly message
  res.status(err.statusCode || 500).json({
    success: false,
    message: 'Something went wrong. Our team has been notified and is working on it.',
    supportCode: generateSupportCode(), // e.g., ERR-20240619-A3K9
    // Never send: err.stack, DB queries, internal paths
  });
});
```

**4. Retry with Backoff — for transient failures**
```javascript
const retry = async (fn, retries = 3, delay = 500) => {
  for (let i = 0; i < retries; i++) {
    try {
      return await fn();
    } catch (err) {
      if (i === retries - 1) throw err;
      await new Promise(r => setTimeout(r, delay * Math.pow(2, i))); // exponential backoff
    }
  }
};

// User's request retried silently — they don't even know there was a hiccup
const data = await retry(() => fetchFromExternalAPI(userId));
```

---

#### 🔵 Phase 3 — Investigate WITHOUT Touching Production

**Never add `console.log` in production and never debug live!**

Tools to investigate safely:
- **Sentry / Rollbar** — full stack traces with breadcrumbs (sequence of events before the error)
- **Distributed tracing** (AWS X-Ray, Jaeger) — trace a request across all microservices
- **Log correlation** — every request gets a `requestId`, propagated across services
- **Read-only DB replica** — run slow query analysis without impacting users

```javascript
// Attach requestId to every log line
app.use((req, res, next) => {
  req.requestId = crypto.randomUUID();
  req.log = logger.child({ requestId: req.requestId, url: req.url });
  res.setHeader('X-Request-Id', req.requestId); // return to client for support tickets
  next();
});

// Now every log line is correlated
req.log.info('Fetching user data');
req.log.error({ err }, 'DB query failed');
```

**Reproduce in staging** — never in production:
```
Production issue found → Replicate in staging (same data, same env vars) → Debug freely
```

---

#### 🟢 Phase 4 — Deploy the Fix Safely (Zero Downtime)

**Never deploy a fix that takes down the site.**

| Strategy | How | When to Use |
|----------|-----|-------------|
| **Blue-Green** | Two identical environments, switch traffic instantly | Critical services, instant rollback |
| **Canary Deploy** | Route 5% of traffic to new version first | Validate fix before full rollout |
| **Rolling Update** | Replace instances one by one | Kubernetes, ECS |
| **Hotfix Branch** | Fast-tracked fix directly to main/prod | Urgent P0 issues |

```bash
# Kubernetes rolling update — zero downtime
kubectl set image deployment/api api=myapp:v2.1.1 --record
kubectl rollout status deployment/api

# Instant rollback if something goes wrong
kubectl rollout undo deployment/api
```

---

#### ⚪ Phase 5 — Post-Mortem (Prevent Recurrence)

After the fix is deployed:
- **Root Cause Analysis (RCA)** — what actually caused it?
- **Blameless post-mortem** — focus on systems, not people
- **5 Whys** technique — keep asking "why" until you reach the root cause
- **Action items**: Add test coverage, improve alerting, add validation

| Item | Detail |
|------|--------|
| **What broke** | Payment service timeout causing 500s on checkout |
| **Root cause** | External API SLA degraded; no circuit breaker in place |
| **User impact** | ~200 users saw error page for 8 minutes |
| **Fix applied** | Added circuit breaker + fallback message |
| **Prevention** | Added integration test + latency alert < 1s |

---

### 🗣️ Sample Interview Answer (Speak This Out Loud)

> "My first priority when something breaks in production is always the **user experience** — I never let a broken backend show users a raw error or a blank screen.
>
> In one project, our checkout API started timing out. Sentry alerted us within 60 seconds. The **first thing I did was flip a feature flag** to route users to a fallback 'payment pending' flow — so they could still complete orders and we'd process payments in the background via a queue.
>
> Then I looked at our distributed traces and found the payment gateway's response time had jumped from 200ms to 8 seconds. I added a **circuit breaker** with a 3-second timeout and a friendly fallback message.
>
> Once users were protected, I investigated on our staging environment, identified the issue, wrote a fix with tests, and deployed it as a **canary release** to 10% of traffic first. After confirming the metrics were healthy, I rolled it out fully.
>
> Finally, we held a post-mortem, added better latency alerting on third-party APIs, and documented the runbook for next time."

---

### Quick Reference — User Protection Techniques

| Problem | User Protection Technique |
|---------|--------------------------|
| Feature bug | Feature Flag — disable instantly |
| External API down | Circuit Breaker + Fallback response |
| DB overload | Read from cache, queue writes |
| High traffic | Rate limiting + queue overflow |
| Deployment issue | Canary deploy + instant rollback |
| Unhandled error | Global error handler → friendly message |
| Slow response | Timeout + retry with backoff |

---

## 2. What is Dependency Injection and its types?

### Definition
**Dependency Injection (DI)** is a design pattern where an object receives its dependencies from an external source rather than creating them itself. It promotes **loose coupling**, **testability**, and **maintainability**.

> Instead of a class creating its own dependency, the dependency is **"injected"** from outside.

### Without DI vs With DI

```javascript
// ❌ Without DI — tightly coupled
class OrderService {
  constructor() {
    this.db = new MySQLDatabase(); // hard dependency
  }
}

// ✅ With DI — loosely coupled
class OrderService {
  constructor(db) {
    this.db = db; // injected from outside
  }
}
const service = new OrderService(new MySQLDatabase());
const testService = new OrderService(new MockDatabase()); // easy to test!
```

### Types of Dependency Injection

#### 1. Constructor Injection *(Most Common)*
Dependencies are provided through the class **constructor**.
```javascript
class UserService {
  constructor(userRepository, emailService) {
    this.userRepository = userRepository;
    this.emailService = emailService;
  }
}
```
✅ **Best practice** — dependencies are explicit and required.

---

#### 2. Setter Injection (Property Injection)
Dependencies are set via **setter methods** after object creation.
```javascript
class UserService {
  setRepository(repo) {
    this.userRepository = repo;
  }
}
const service = new UserService();
service.setRepository(new UserRepository());
```
⚠️ Risk: object can be in invalid state before setter is called.

---

#### 3. Interface Injection
The dependency provides an **injector interface** that the class must implement.
```java
// Common in Java/C#
interface RepositoryInjector {
  void injectRepository(Repository repo);
}
```
Rare in JavaScript, common in typed languages.

---

#### 4. Method Injection
Dependency is passed directly to a **specific method**.
```javascript
class ReportService {
  generateReport(formatter) { // formatter injected per-call
    return formatter.format(this.data);
  }
}
```
Useful when the dependency is only needed for one operation.

---

### DI in Frameworks
| Framework | DI Mechanism |
|-----------|-------------|
| NestJS | `@Injectable()`, constructor injection via decorators |
| Angular | Built-in DI container / providers |
| Spring (Java) | `@Autowired`, `@Component` |
| ASP.NET Core | `services.AddScoped<T>()` |

### Benefits of DI
- **Testability** — swap real dependencies with mocks
- **Loose coupling** — classes don't depend on concrete implementations
- **Single Responsibility** — classes focus on their core logic
- **Reusability** — same class works with different implementations

---

## 3. What is Indexing and its types?

### Definition
**Indexing** is a data structure technique to speed up data retrieval operations in a database without scanning every row in a table. Think of it like the **index of a book** — instead of reading every page, you jump to the right page directly.

> Without index: **O(n)** full table scan  
> With index: **O(log n)** or O(1) lookup

### How it works internally
Most databases use a **B-Tree** (Balanced Tree) or **B+ Tree** for indexes. The index stores the column values in sorted order with pointers to the actual row location.

---

### Types of Indexes

#### 1. Primary Index (Clustered Index)
- Created automatically on the **Primary Key**
- Data rows are **physically stored** in the order of the index
- Only **one clustered index** per table (since data can only be sorted one way)

```sql
CREATE TABLE users (
  id INT PRIMARY KEY,  -- clustered index auto-created
  name VARCHAR(100)
);
```

---

#### 2. Secondary Index (Non-Clustered Index)
- Created on **non-primary key columns**
- Stores a **copy of the indexed column(s)** + pointer to the actual row
- A table can have **multiple non-clustered indexes**

```sql
CREATE INDEX idx_users_email ON users(email);
```

---

#### 3. Unique Index
- Ensures all values in the indexed column are **unique**
- Similar to primary key but can be applied to any column

```sql
CREATE UNIQUE INDEX idx_unique_email ON users(email);
```

---

#### 4. Composite Index (Multi-Column Index)
- Index on **two or more columns**
- Follows **left-prefix rule** — useful for queries that filter on the leftmost columns

```sql
CREATE INDEX idx_name_dept ON employees(last_name, department_id);
-- This helps: WHERE last_name = 'Smith' AND department_id = 5
-- This does NOT help: WHERE department_id = 5 (no left-prefix match)
```

---

#### 5. Full-Text Index
- Used for **text search** operations (LIKE is slow, full-text is fast)
- Used in search engines, blog search features

```sql
CREATE FULLTEXT INDEX idx_ft_content ON articles(title, body);
SELECT * FROM articles WHERE MATCH(title, body) AGAINST('nodejs performance');
```

---

#### 6. Partial Index (Filtered Index)
- Index on a **subset of rows** based on a condition
- Saves storage and improves performance for filtered queries

```sql
-- Index only active users (PostgreSQL)
CREATE INDEX idx_active_users ON users(email) WHERE is_active = true;
```

---

#### 7. Hash Index
- Uses a **hash function** for exact-match lookups
- **O(1)** lookup but does NOT support range queries (`>`, `<`, `BETWEEN`)
- Used in **in-memory databases** like Redis, or specific PostgreSQL scenarios

---

#### 8. Bitmap Index
- Uses **bitmaps** (bit arrays) for columns with low cardinality (few distinct values)
- Example: `gender` (M/F), `status` (active/inactive)
- Very efficient for read-heavy data warehouses, not for write-heavy OLTP

---

### When to Use vs Avoid Indexes

| Scenario | Index? |
|----------|--------|
| Frequently queried columns (WHERE, JOIN) | ✅ Yes |
| Columns used in ORDER BY | ✅ Yes |
| High-cardinality columns (email, user_id) | ✅ Yes |
| Columns rarely queried | ❌ No |
| Tables with frequent INSERT/UPDATE/DELETE | ⚠️ Use sparingly |
| Low-cardinality columns (boolean, gender) | ❌ Bitmap instead |

---

## 4. How did you handle global level exceptions or errors?

### The Problem
Without global error handling, unhandled exceptions can:
- Crash the Node.js process
- Leak sensitive stack traces to clients
- Leave the application in an inconsistent state

### Layers of Error Handling

#### Layer 1 — Express Global Error Middleware
```javascript
// error.middleware.js
const errorHandler = (err, req, res, next) => {
  const statusCode = err.statusCode || 500;
  const isProduction = process.env.NODE_ENV === 'production';

  console.error(`[ERROR] ${err.message}`, {
    stack: err.stack,
    url: req.url,
    method: req.method,
    timestamp: new Date().toISOString(),
  });

  res.status(statusCode).json({
    success: false,
    message: isProduction ? 'Something went wrong' : err.message,
    ...(isProduction ? {} : { stack: err.stack }),
  });
};

// Must be registered LAST in the middleware chain
app.use(errorHandler);
```

---

#### Layer 2 — Custom AppError Class
```javascript
// errors/AppError.js
class AppError extends Error {
  constructor(message, statusCode = 500, isOperational = true) {
    super(message);
    this.statusCode = statusCode;
    this.isOperational = isOperational; // trusted vs programming error
    Error.captureStackTrace(this, this.constructor);
  }
}

// Usage
throw new AppError('User not found', 404);
throw new AppError('Unauthorized access', 401);
```

---

#### Layer 3 — Async Error Wrapper (Avoid try-catch repetition)
```javascript
// utils/asyncHandler.js
const asyncHandler = (fn) => (req, res, next) => {
  Promise.resolve(fn(req, res, next)).catch(next);
};

// Usage in route
router.get('/users/:id', asyncHandler(async (req, res) => {
  const user = await UserService.findById(req.params.id);
  if (!user) throw new AppError('User not found', 404);
  res.json(user);
}));
```

---

#### Layer 4 — Process-level unhandled errors
```javascript
// Handle unhandled promise rejections
process.on('unhandledRejection', (reason, promise) => {
  console.error('Unhandled Rejection at:', promise, 'reason:', reason);
  // Gracefully shut down
  server.close(() => {
    process.exit(1);
  });
});

// Handle uncaught synchronous exceptions
process.on('uncaughtException', (error) => {
  console.error('Uncaught Exception:', error);
  process.exit(1); // Restart via PM2 / container orchestrator
});
```

---

#### Layer 5 — Third-party error tracking (Sentry)
```javascript
const Sentry = require('@sentry/node');
Sentry.init({ dsn: process.env.SENTRY_DSN });

app.use(Sentry.Handlers.requestHandler());
// ... routes ...
app.use(Sentry.Handlers.errorHandler()); // must be before custom error handler
app.use(errorHandler);
```

### Error Classification
| Type | Example | Handling |
|------|---------|---------|
| **Operational** | DB down, 404, 401 | Return proper HTTP status |
| **Programmer** | null ref, type error | Log + restart process |
| **External** | 3rd-party API failure | Retry with backoff, fallback |

---

## 5. What are Serverless Functions?

### Definition
**Serverless functions** (also called **FaaS — Function as a Service**) are individual pieces of code that run in the cloud **on demand**, without the developer managing any server infrastructure. You write a function, deploy it, and the cloud provider handles scaling, availability, and execution.

> "Serverless" doesn't mean no servers — it means **you don't manage the servers**.

### How It Works
```
Client Request → API Gateway → Serverless Function (cold start if needed) → Response
```

### Key Characteristics
- **Event-driven** — triggered by HTTP, queue messages, file uploads, DB changes, cron jobs
- **Auto-scaling** — scales from 0 to millions automatically
- **Pay-per-use** — billed only when the function executes (millisecond billing)
- **Stateless** — each invocation is independent; no shared memory between calls
- **Ephemeral** — execution context lives only for the duration of the call

### Popular Platforms
| Platform | Service |
|----------|---------|
| AWS | Lambda |
| Google Cloud | Cloud Functions |
| Azure | Azure Functions |
| Vercel | Edge Functions |
| Netlify | Netlify Functions |
| Cloudflare | Workers |

### Example — AWS Lambda (Node.js)
```javascript
// handler.js
exports.handler = async (event) => {
  const { httpMethod, body, pathParameters } = event;

  if (httpMethod === 'GET') {
    const userId = pathParameters.id;
    const user = await getUserFromDB(userId);
    return {
      statusCode: 200,
      body: JSON.stringify(user),
    };
  }

  return { statusCode: 405, body: 'Method Not Allowed' };
};
```

### Cold Start Problem
- First invocation takes longer because the cloud provider must **spin up** a new container
- **Solutions**: Provisioned Concurrency (AWS), keep-warm pings, optimize package size, use lightweight runtimes

### Use Cases
- REST API endpoints
- Background jobs (image processing, email sending)
- Scheduled tasks (cron)
- Webhook handlers
- Real-time data processing (Kinesis, SQS triggers)

### Pros vs Cons
| Pros | Cons |
|------|------|
| No server management | Cold start latency |
| Auto-scaling | Vendor lock-in |
| Cost-efficient at low traffic | Stateless (session challenges) |
| Faster time to market | Difficult to debug locally |
| | 15-min timeout limit (Lambda) |

---

## 6. How did you handle load if a lot of users come to the platform?

### Answer Overview
Handling high traffic requires a **multi-layered strategy** across infrastructure, application, and data layers.

---

### 1. Horizontal Scaling (Scale Out)
Instead of upgrading one big server (vertical), run **multiple identical instances** behind a load balancer.
```
Users → Load Balancer (Nginx / ALB) → [Server 1] [Server 2] [Server 3]
```

### 2. Load Balancing
- **Round Robin** — distribute requests evenly
- **Least Connections** — route to the least busy server
- **IP Hash** — same client always hits the same server (session affinity)
- Tools: **Nginx, HAProxy, AWS ALB/NLB**

### 3. Caching Strategy
```
Request → Cache Hit? → Yes → Return from Redis (< 1ms)
                    → No  → Query DB → Cache result → Return
```
- **Redis / Memcached** for in-memory caching
- Cache: user sessions, frequently read data, API responses
- Cache strategies: **Cache-aside, Write-through, Write-behind**
- Set appropriate **TTL (Time To Live)** to prevent stale data

### 4. Database Optimization
- **Read Replicas** — primary handles writes, replicas handle reads
- **Connection Pooling** — reuse DB connections (pg-pool, mongoose connection pool)
- **Query Optimization** — proper indexes, avoid N+1 queries
- **Sharding** — split data across multiple databases (covered in Q11)

### 5. CDN (Content Delivery Network)
- Serve **static assets** (images, JS, CSS) from edge servers closest to the user
- Tools: **Cloudflare, AWS CloudFront, Fastly**
- Dramatically reduces origin server load

### 6. Message Queues (Async Processing)
Don't process everything synchronously. Offload heavy tasks to queues.
```
POST /send-email → Push to Queue (SQS/RabbitMQ) → Return 202 Accepted
                                                 ↓
                                           Worker processes email async
```
- Tools: **AWS SQS, RabbitMQ, Apache Kafka**
- Prevents request timeouts under heavy load

### 7. Rate Limiting & Throttling
```javascript
const rateLimit = require('express-rate-limit');
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // limit each IP to 100 requests per window
  message: 'Too many requests, please try again later.',
});
app.use('/api/', limiter);
```
- Protects from DDoS and abusive clients
- Per-user, per-IP, or per-endpoint limits

### 8. Auto-scaling
- **AWS Auto Scaling Groups** — add/remove EC2 instances based on CPU/request metrics
- **Kubernetes HPA (Horizontal Pod Autoscaler)** — scale pods based on metrics
- Scale up during peak, scale down during off-peak to save cost

### 9. Circuit Breaker Pattern
Prevent cascading failures when a downstream service is overloaded:
```
Normal → Service OK → Pass through
Failure threshold exceeded → Circuit OPEN → Return fallback immediately
After timeout → Circuit HALF-OPEN → Probe service → Close if healthy
```
- Libraries: **opossum** (Node.js), **Hystrix** (Java), **resilience4j**

### Architecture Summary Diagram
```
Users
  ↓
CDN (Static Assets)
  ↓
Load Balancer (Nginx / ALB)
  ↓
[App Server 1] [App Server 2] [App Server N]  ← Auto-scaled
       ↓               ↓
   Redis Cache    Message Queue (SQS)
       ↓               ↓
   DB Primary ← Read Replicas    Workers
```

---

## 7. What is Middleware? What is Authentication and Authorization?

### Middleware

**Middleware** is a function that sits **between the request and response cycle** in a web application. It has access to the `request` object, `response` object, and the `next` function. Middleware can:
- Execute any code
- Modify `req` and `res` objects
- End the request-response cycle
- Call the next middleware in the stack

#### Middleware Chain
```
Request → [Middleware 1] → [Middleware 2] → [Route Handler] → Response
              ↓ (calls next())    ↓ (calls next())
```

#### Express Middleware Example
```javascript
// Logger middleware
const logger = (req, res, next) => {
  console.log(`[${new Date().toISOString()}] ${req.method} ${req.url}`);
  next(); // pass control to next middleware
};

// Auth middleware
const authenticate = (req, res, next) => {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) return res.status(401).json({ message: 'No token provided' });

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded;
    next();
  } catch {
    res.status(401).json({ message: 'Invalid token' });
  }
};

app.use(logger);
app.use('/api/protected', authenticate);
```

#### Types of Middleware
| Type | Example |
|------|---------|
| Application-level | `app.use(cors())` |
| Router-level | `router.use(authenticate)` |
| Error-handling | `app.use((err, req, res, next) => {...})` |
| Built-in | `express.json()`, `express.static()` |
| Third-party | `helmet()`, `cors()`, `morgan()` |

---

### Authentication vs Authorization

| Aspect | Authentication | Authorization |
|--------|---------------|---------------|
| **What** | Verifies **who you are** | Verifies **what you can do** |
| **Question** | "Are you who you say you are?" | "Are you allowed to do this?" |
| **When** | First check | After authentication |
| **Example** | Login with email/password | Can this user DELETE this post? |
| **Failure Code** | 401 Unauthorized | 403 Forbidden |

---

### Authentication Methods

#### 1. JWT (JSON Web Token) — Stateless
```javascript
// Login — Generate token
const token = jwt.sign(
  { userId: user.id, role: user.role },
  process.env.JWT_SECRET,
  { expiresIn: '1h' }
);

// Middleware — Verify token
const decoded = jwt.verify(token, process.env.JWT_SECRET);
req.user = decoded; // { userId, role, iat, exp }
```
- Token stored on client (localStorage / httpOnly cookie)
- Server doesn't store session → scales horizontally

#### 2. Session-based — Stateful
```javascript
app.use(session({
  secret: process.env.SESSION_SECRET,
  resave: false,
  saveUninitialized: false,
  store: new RedisStore({ client: redisClient }), // store sessions in Redis
}));
```
- Session ID stored in cookie, actual session data in server-side store (Redis)
- Easier to revoke (just delete session), but requires shared session store

#### 3. OAuth 2.0 / OpenID Connect
- Delegate authentication to a trusted provider (Google, GitHub, Auth0)
- User logs into Google → Google returns an auth code → Your server exchanges it for tokens
- Libraries: **Passport.js**, **Auth0 SDK**

#### 4. API Keys
- Static keys for **machine-to-machine** communication
- Attached in headers: `X-API-Key: abc123`
- Should be hashed and stored securely

---

## 8. How did you handle RBAC?

### What is RBAC?
**Role-Based Access Control (RBAC)** is an authorization strategy where **permissions are assigned to roles**, and **roles are assigned to users**. Users inherit permissions through their roles.

```
User → has → Role(s) → has → Permission(s) → grants → Actions on Resources
```

### RBAC Data Model
```
User        ←→     UserRole      ←→     Role
                                          ↕
                                    RolePermission
                                          ↕
                                      Permission
                                  (resource + action)
```

### Database Schema
```sql
CREATE TABLE roles (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) UNIQUE  -- 'admin', 'editor', 'viewer'
);

CREATE TABLE permissions (
  id SERIAL PRIMARY KEY,
  resource VARCHAR(100),    -- 'articles', 'users', 'reports'
  action VARCHAR(50)        -- 'create', 'read', 'update', 'delete'
);

CREATE TABLE role_permissions (
  role_id INT REFERENCES roles(id),
  permission_id INT REFERENCES permissions(id),
  PRIMARY KEY(role_id, permission_id)
);

CREATE TABLE user_roles (
  user_id INT REFERENCES users(id),
  role_id INT REFERENCES roles(id),
  PRIMARY KEY(user_id, role_id)
);
```

### Implementation in Node.js

#### Step 1 — Encode role in JWT
```javascript
const token = jwt.sign(
  { userId: user.id, roles: ['editor', 'viewer'] },
  process.env.JWT_SECRET
);
```

#### Step 2 — RBAC Middleware
```javascript
// middleware/rbac.js
const authorize = (requiredPermission) => {
  return async (req, res, next) => {
    const { userId } = req.user;

    // Fetch user permissions (can be cached in Redis)
    const permissions = await getUserPermissions(userId);

    if (!permissions.includes(requiredPermission)) {
      return res.status(403).json({
        message: `Access denied. Required: ${requiredPermission}`
      });
    }
    next();
  };
};

// Usage
router.delete('/articles/:id',
  authenticate,
  authorize('articles:delete'),
  ArticleController.delete
);

router.get('/users',
  authenticate,
  authorize('users:read'),
  UserController.list
);
```

#### Step 3 — Cache permissions in Redis
```javascript
const getUserPermissions = async (userId) => {
  const cacheKey = `permissions:${userId}`;
  const cached = await redis.get(cacheKey);
  if (cached) return JSON.parse(cached);

  const permissions = await db.query(`
    SELECT p.resource, p.action
    FROM users u
    JOIN user_roles ur ON u.id = ur.user_id
    JOIN roles r ON ur.role_id = r.id
    JOIN role_permissions rp ON r.id = rp.role_id
    JOIN permissions p ON rp.permission_id = p.id
    WHERE u.id = $1
  `, [userId]);

  const permList = permissions.rows.map(p => `${p.resource}:${p.action}`);
  await redis.setex(cacheKey, 300, JSON.stringify(permList)); // cache 5 min
  return permList;
};
```

### RBAC vs ABAC vs ACL

| Model | Full Name | Basis | Best For |
|-------|-----------|-------|---------|
| **RBAC** | Role-Based AC | User roles | Most enterprise apps |
| **ABAC** | Attribute-Based AC | User/resource attributes | Fine-grained, dynamic policies |
| **ACL** | Access Control List | Per-resource permissions | File systems, simple apps |

---

## 9. What Projects Have You Worked On?

> ⚡ **Note**: This is a personal question. Tailor it to your actual experience. Below is a **template structure** you can use to frame your project explanations effectively.

### How to Structure Your Project Answer (STAR + Technical)

```
1. Project Name & Domain
2. Tech Stack used
3. Your role and team size
4. Problem it solved
5. Key technical challenges you faced
6. How you solved them
7. Impact / Results
```

### Example Project Template

#### Project 1: E-Commerce Platform
- **Role**: Backend Engineer (team of 5)
- **Stack**: Node.js, Express, PostgreSQL, Redis, AWS (EC2, S3, SQS)
- **Description**: Built a scalable e-commerce platform with product catalog, cart, checkout, and order management
- **Key Challenges**:
  - **Inventory concurrency**: Two users buying the last item simultaneously → Solved with **pessimistic locking** / Redis atomic operations
  - **Payment reliability**: Payment service timeouts → Used **idempotency keys** and **retry with exponential backoff**
  - **Performance**: Slow product search → Added **Elasticsearch** for full-text search
- **Impact**: Handled 10,000+ concurrent users, 99.9% uptime, < 200ms API response time

---

#### Project 2: Test Automation Framework
- **Role**: Senior QA/Automation Engineer
- **Stack**: Python, Pytest, Selenium, Playwright, Docker, GitHub Actions
- **Description**: Built a reusable, maintainable test automation framework for web applications
- **Key Challenges**:
  - Flaky tests due to timing issues → Implemented **explicit waits** and **retry decorators**
  - Slow test suite → Parallelized tests with **pytest-xdist** and Docker containers
  - Environment inconsistencies → Containerized everything with Docker Compose
- **Impact**: Reduced test execution time by 60%, caught 95% of regressions before production

---

## 10. What is the Event Loop?

### Definition
The **Event Loop** is the core mechanism of Node.js (and JavaScript in general) that allows it to perform **non-blocking I/O operations** despite being **single-threaded**. It continuously checks if there are tasks to execute and processes them in a specific order.

> Node.js is **single-threaded** but achieves concurrency through the event loop and libuv's thread pool.

### Visualization
```
   ┌───────────────────────────┐
   │         Call Stack         │  ← Executes synchronous code
   └───────────────────────────┘
              ↓ (empty)
   ┌───────────────────────────┐
   │         Event Loop         │  ← Picks next task to run
   └───────────────────────────┘
              ↓
   ┌─────────────────────────────────────────────┐
   │              Phase Queue Order               │
   │  timers → pending callbacks → idle/prepare  │
   │  → poll → check → close callbacks           │
   └─────────────────────────────────────────────┘
```

### Event Loop Phases (Node.js libuv)

| Phase | What runs here |
|-------|----------------|
| **timers** | `setTimeout()` and `setInterval()` callbacks |
| **pending callbacks** | I/O error callbacks from previous iteration |
| **idle, prepare** | Internal libuv use |
| **poll** | Retrieves new I/O events, executes I/O callbacks |
| **check** | `setImmediate()` callbacks |
| **close callbacks** | `socket.on('close', ...)` callbacks |

### Microtasks vs Macrotasks
**Microtasks** run **between** every phase, before the next macrotask:
```
Microtasks: Promise.then(), queueMicrotask(), process.nextTick()
Macrotasks: setTimeout(), setInterval(), setImmediate(), I/O
```

> `process.nextTick()` runs before all other microtasks!

### Example — Execution Order
```javascript
console.log('1. Synchronous');

setTimeout(() => console.log('5. setTimeout'), 0);
setImmediate(() => console.log('6. setImmediate'));

Promise.resolve().then(() => console.log('3. Promise microtask'));
process.nextTick(() => console.log('2. nextTick'));

console.log('4. Synchronous end');

// Output:
// 1. Synchronous
// 4. Synchronous end
// 2. nextTick          ← process.nextTick runs first (before promises)
// 3. Promise microtask ← then all promises
// 5. setTimeout        ← then macrotasks
// 6. setImmediate
```

### Why Node.js is Fast
- The **main thread** never blocks on I/O
- File reads, DB queries, HTTP calls are delegated to the **OS / libuv thread pool**
- When they complete, their callbacks are pushed to the event loop queue
- The main thread picks them up and executes callbacks

### Blocking the Event Loop (Anti-pattern)
```javascript
// ❌ This blocks the event loop — all other requests wait!
app.get('/heavy', (req, res) => {
  const result = doHeavyCpuCalculation(); // blocks for 5 seconds
  res.json(result);
});

// ✅ Offload to worker thread or child process
const { Worker } = require('worker_threads');
app.get('/heavy', (req, res) => {
  const worker = new Worker('./heavy-task.js');
  worker.on('message', result => res.json(result));
});
```

---

## 11. What is Sharding and Partitioning?

### Partitioning

**Partitioning** is dividing a **single database table** into smaller pieces to improve query performance and manageability. The data stays **within the same database/server** but is organized into sub-tables.

#### Types of Partitioning

**1. Horizontal Partitioning (Row-based)**
Split rows across multiple partitions based on a column value.
```sql
-- PostgreSQL: Partition orders by year
CREATE TABLE orders (
  id BIGINT,
  created_at DATE,
  amount DECIMAL
) PARTITION BY RANGE (created_at);

CREATE TABLE orders_2023 PARTITION OF orders
  FOR VALUES FROM ('2023-01-01') TO ('2024-01-01');

CREATE TABLE orders_2024 PARTITION OF orders
  FOR VALUES FROM ('2024-01-01') TO ('2025-01-01');
```

**2. Vertical Partitioning (Column-based)**
Split columns into separate tables. Put frequently accessed columns in one table, rarely accessed in another.
```sql
-- Users table split
CREATE TABLE users_core (id, email, created_at);  -- hot data
CREATE TABLE users_profile (id, bio, avatar, preferences);  -- cold data
```

**3. List Partitioning**
Partition by specific values (e.g., country, region):
```sql
CREATE TABLE sales PARTITION BY LIST (region);
CREATE TABLE sales_us PARTITION OF sales FOR VALUES IN ('US');
CREATE TABLE sales_eu PARTITION OF sales FOR VALUES IN ('EU', 'UK');
```

**4. Hash Partitioning**
Distribute data evenly using a hash function:
```sql
CREATE TABLE users PARTITION BY HASH (id);
CREATE TABLE users_0 PARTITION OF users FOR VALUES WITH (MODULUS 4, REMAINDER 0);
CREATE TABLE users_1 PARTITION OF users FOR VALUES WITH (MODULUS 4, REMAINDER 1);
-- ... etc
```

---

### Sharding

**Sharding** is **horizontal partitioning across multiple database servers** (nodes). Each shard is a completely separate database instance holding a subset of data.

```
Total Users: 100 million
  ↓
Shard 1: Users  0 - 25M  (Server 1)
Shard 2: Users 25M - 50M (Server 2)
Shard 3: Users 50M - 75M (Server 3)
Shard 4: Users 75M - 100M (Server 4)
```

#### Sharding Strategies

| Strategy | How | Pros | Cons |
|----------|-----|------|------|
| **Range-based** | Shard by value range (e.g., user_id 1-1M) | Simple, range queries easy | Uneven distribution (hotspots) |
| **Hash-based** | shard = hash(key) % N | Even distribution | Range queries hard, rebalancing painful |
| **Directory-based** | Lookup table maps key → shard | Flexible, can move data | Lookup table bottleneck |
| **Geographic** | Shard by region/country | Data locality, compliance | Complex cross-region queries |

#### Sharding Implementation (Conceptual)
```javascript
// Shard router
const getShardConnection = (userId) => {
  const shardIndex = userId % NUM_SHARDS; // Hash-based
  return shardConnections[shardIndex];
};

// Usage
const db = getShardConnection(user.id);
const result = await db.query('SELECT * FROM orders WHERE user_id = $1', [user.id]);
```

### Partitioning vs Sharding Summary

| Aspect | Partitioning | Sharding |
|--------|-------------|---------|
| **Location** | Same server | Multiple servers |
| **Scale** | Vertical + storage | Horizontal + compute |
| **Complexity** | Lower | Higher |
| **Use Case** | Large tables, archiving | Massive scale, distributed systems |
| **Managed by** | Database engine | Application layer / middleware |

### Real-world Usage
- **PostgreSQL** → native table partitioning
- **MySQL** → `PARTITION BY` clause
- **MongoDB** → built-in sharding with mongos router
- **Cassandra** → automatically distributed via consistent hashing
- **Vitess** → sharding middleware for MySQL (used by YouTube, GitHub)

---

## 12. What is the Cluster Module?

### Problem It Solves
Node.js runs on a **single thread** — it can only use **one CPU core** by default. On a machine with 8 cores, you're wasting 7 cores.

The **Cluster module** allows you to create **multiple Node.js processes** (workers) that all **share the same server port**, effectively utilizing all available CPU cores.

### How It Works
```
Master Process (1)
    ↓ fork()
Worker 1 (Core 1)
Worker 2 (Core 2)
Worker 3 (Core 3)
Worker N (Core N)
    ↑
All listen on port 3000
OS distributes incoming connections across workers
```

### Basic Implementation
```javascript
// cluster.js
const cluster = require('cluster');
const os = require('os');
const http = require('http');

const numCPUs = os.cpus().length;

if (cluster.isMaster) {
  console.log(`Master ${process.pid} is running`);
  console.log(`Forking ${numCPUs} workers...`);

  // Fork one worker per CPU core
  for (let i = 0; i < numCPUs; i++) {
    cluster.fork();
  }

  // Restart workers if they crash
  cluster.on('exit', (worker, code, signal) => {
    console.log(`Worker ${worker.process.pid} died (${signal || code}). Restarting...`);
    cluster.fork();
  });

} else {
  // Worker processes run the actual server
  const express = require('express');
  const app = express();

  app.get('/', (req, res) => {
    res.send(`Hello from Worker ${process.pid}`);
  });

  app.listen(3000, () => {
    console.log(`Worker ${process.pid} started`);
  });
}
```

### With PM2 (Production Alternative)
PM2 manages clustering automatically — no need to write cluster code manually:
```bash
# Start app with cluster mode — auto-detects CPU count
pm2 start app.js -i max

# Or specify number of instances
pm2 start app.js -i 4

# Monitor all workers
pm2 monit

# Zero-downtime reload
pm2 reload app.js
```

### Worker Communication (IPC)
Workers can communicate with the master via IPC (Inter-Process Communication):
```javascript
// In master process
worker.send({ type: 'CACHE_INVALIDATE', key: 'user:123' });

// In worker process
process.on('message', (msg) => {
  if (msg.type === 'CACHE_INVALIDATE') {
    cache.delete(msg.key);
  }
});
```

### Cluster vs Worker Threads

| Feature | Cluster | Worker Threads |
|---------|---------|---------------|
| **Isolation** | Separate processes | Shared memory |
| **Use Case** | Multiple server instances | CPU-heavy tasks |
| **Overhead** | Higher (separate processes) | Lower (threads) |
| **Crash Safety** | Worker crash doesn't kill master | Thread crash can kill main |
| **Shared State** | Via IPC or Redis | SharedArrayBuffer |
| **Node.js API** | `cluster` module | `worker_threads` module |

### When to Use Cluster
- Running an **Express/Fastify/NestJS API server** and want to use all CPU cores
- Need **zero-downtime restarts** (PM2 handles this)
- CPU-bound work across multiple requests

### When to Use Worker Threads instead
- **CPU-intensive computation** within a single request (image processing, parsing)
- Tasks that need **shared memory** (`SharedArrayBuffer`)

---

## 🎯 Quick Reference Summary

| Topic | Key Concept |
|-------|------------|
| **Production Debugging** | Logs → Traces → Reproduce → Fix → Post-mortem |
| **Dependency Injection** | Inject dependencies from outside; Constructor > Setter > Method injection |
| **Indexing** | B-Tree for reads; Composite (left-prefix rule); avoid over-indexing |
| **Global Error Handling** | AppError class + asyncHandler + process.on('unhandledRejection') |
| **Serverless** | Event-driven, auto-scaling, stateless, pay-per-use (Lambda, Cloud Functions) |
| **Load Handling** | LB + Caching + CDN + Queues + Rate Limiting + Auto-scaling |
| **Middleware** | Request pipeline functions; auth → validate → business logic → response |
| **RBAC** | User → Roles → Permissions; cache permissions in Redis |
| **Event Loop** | Single-threaded, non-blocking; nextTick > Promises > setTimeout > setImmediate |
| **Sharding** | Split data across servers; Hash/Range/Directory-based |
| **Partitioning** | Split table on same server; Range/List/Hash/Vertical |
| **Cluster Module** | Fork N workers (N = CPU cores); PM2 simplifies this in production |

---

*Generated for Senior Backend/Full-Stack Developer Interview Preparation*
*Last Updated: June 2026*
