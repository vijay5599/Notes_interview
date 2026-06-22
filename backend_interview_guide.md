# 🚀 Backend Interview Preparation Guide
### Senior Backend Engineer · 4 Years Experience · Product Companies

> **Tech Stack**: FastAPI · Node.js · Express.js · Python · TypeScript · PostgreSQL · MongoDB · Docker · Redis · Microservices

---

## Table of Contents

1. [Core Backend Concepts](#1-core-backend-concepts)
2. [FastAPI Deep Dive](#2-fastapi-deep-dive)
3. [Node.js + Express.js Deep Dive](#3-nodejs--expressjs-deep-dive)
4. [Database Questions](#4-database-questions)
5. [Production & Debugging](#5-production--debugging)
6. [System Design](#6-system-design)
7. [Scenario-Based Questions](#7-scenario-based-questions)
8. [Coding Round Questions](#8-coding-round-questions)
9. [Behavioral Questions (STAR)](#9-behavioral-questions-star-format)

---

## 🗂️ Your 12 Questions — Categorized

| # | Your Question | Section | Question # | Status |
|---|---|---|---|---|
| 1 | How did you debug any issue in production? | §5 Production & Debugging | Q24 | ✅ Covered |
| 2 | What is Dependency Injection and its types? | §1 Core Backend | Q1 | ✅ Covered |
| 3 | What is Indexing and its types? | §4 Database | Q18 | ✅ Covered |
| 4 | How did you handle global level exception/errors? | §2 FastAPI / §3 Node.js | Q12, Q15 | ✅ Covered |
| 5 | What is Serverless Functions? | §1 Core Backend | **Q9-A** | 🆕 Added |
| 6 | How did you handle load if lot of users come? | §5 Production & Debugging | Q27 | ✅ Covered |
| 7 | What is Middleware? What is AuthN & AuthZ? | §1 Core Backend | Q2, Q3 | ✅ Covered |
| 8 | How did you handle RBAC? | §1 Core Backend | **Q3-B** | 🆕 Added |
| 9 | What projects you worked on — explain? | §9 Behavioral | **Q42** | 🆕 Added |
| 10 | What is Event Loop? | §3 Node.js | Q14 | ✅ Covered |
| 11 | What is Sharding, Partitioning? | §4 Database | **Q23-A** | 🆕 Added |
| 12 | What is Cluster Module? | §3 Node.js | Q16 | ✅ Covered |

---

# 1. Core Backend Concepts

---

## Q1. What is Dependency Injection and why is it important in backend systems?

### 🎯 Short Version (30 sec)
> Dependency Injection is a design pattern where a class/function receives its dependencies from the outside rather than creating them internally. It decouples components, improves testability, and enables easier swapping of implementations.

### 💬 Interview Answer

**Dependency Injection (DI)** is a technique where dependencies (services, database connections, config objects) are "injected" into a component rather than being created inside it.

**Without DI:**
```python
class UserService:
    def __init__(self):
        self.db = PostgresDB()  # tightly coupled

    def get_user(self, user_id):
        return self.db.query(f"SELECT * FROM users WHERE id={user_id}")
```

**With DI:**
```python
class UserService:
    def __init__(self, db: DatabaseInterface):
        self.db = db  # injected from outside

    def get_user(self, user_id):
        return self.db.query(user_id)

# In tests: inject MockDB
# In production: inject PostgresDB
service = UserService(db=PostgresDB())
test_service = UserService(db=MockDB())
```

**In FastAPI:**
```python
from fastapi import Depends

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users/{id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    return db.query(User).filter(User.id == user_id).first()
```

**Benefits:**
- **Testability**: Swap real DB with mocks in unit tests
- **Separation of concerns**: Each component does one thing
- **Flexibility**: Change implementation without touching consumer code
- **Single Responsibility**: Business logic stays clean

### 🧠 Deep Explanation

DI is the "D" in **SOLID** principles (Dependency Inversion Principle). There are 3 types:
1. **Constructor Injection** - passed via `__init__`
2. **Method Injection** - passed as function argument
3. **Property Injection** - set after construction

DI Containers (like FastAPI's `Depends`) manage the lifecycle of dependencies — when to create, cache, and destroy them.

### ❓ Follow-up Questions
- How does FastAPI handle dependency lifecycle (scoped, singleton)?
- Can you chain dependencies? (Yes — `Depends(get_db)` itself can `Depends(get_settings)`)
- How do you test endpoints with injected dependencies?

### 💡 Senior-level Tips
> Mention that DI enables **IoC (Inversion of Control)** — the framework controls object creation, not the business logic. In large systems, use a proper DI container to avoid "constructor injection hell."

---

## Q2. What is Middleware and how does it work?

### 🎯 Short Version (30 sec)
> Middleware is code that runs between receiving a request and sending a response. It's used for cross-cutting concerns like logging, authentication, CORS, and request transformation.

### 💬 Interview Answer

Middleware intercepts every HTTP request/response. It forms a pipeline — each middleware can pass control to the next or short-circuit the chain.

**Middleware Pipeline:**
```
Request → [Auth MW] → [Logging MW] → [CORS MW] → Route Handler → Response
```

**Express.js Example:**
```javascript
// Logging middleware
app.use((req, res, next) => {
    console.log(`[${new Date().toISOString()}] ${req.method} ${req.path}`);
    next(); // pass to next middleware
});

// Auth middleware
app.use((req, res, next) => {
    const token = req.headers['authorization'];
    if (!token) return res.status(401).json({ error: 'Unauthorized' });
    req.user = verifyToken(token);
    next();
});
```

**FastAPI Example:**
```python
from starlette.middleware.base import BaseHTTPMiddleware

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.time()
        response = await call_next(request)
        duration = time.time() - start
        logger.info(f"{request.method} {request.url} - {response.status_code} - {duration:.3f}s")
        return response

app.add_middleware(LoggingMiddleware)
```

**Common Middleware Use Cases:**
| Middleware | Purpose |
|---|---|
| Authentication | Validate tokens |
| CORS | Handle cross-origin headers |
| Rate Limiting | Throttle requests |
| Compression | gzip responses |
| Request ID | Inject trace IDs |
| Error Handling | Catch unhandled exceptions |

### ❓ Follow-up Questions
- What's the difference between middleware and a decorator in FastAPI?
- How would you apply middleware to only specific routes?
- What happens if a middleware doesn't call `next()`?

### 💡 Senior-level Tips
> Mention middleware **ordering matters** — auth before logging means you log authenticated requests only. Also, be aware of **performance overhead** — every middleware adds latency, so keep them lean.

---

## Q3. Authentication vs Authorization — What's the difference?

### 🎯 Short Version (30 sec)
> Authentication is *who you are* (identity verification). Authorization is *what you can do* (permission check). AuthN happens first, AuthZ after.

### 💬 Interview Answer

| | Authentication | Authorization |
|---|---|---|
| **Definition** | Verify identity | Verify permissions |
| **Question** | "Who are you?" | "Can you do this?" |
| **Example** | Login with email/password | Admin can delete users |
| **Protocols** | OAuth2, SAML, JWT | RBAC, ABAC, ACL |
| **Error Code** | 401 Unauthorized | 403 Forbidden |

**Implementation Flow:**
```
Request
  → [Auth Middleware] → Verify JWT → Set req.user (AuthN)
  → [RBAC Middleware] → Check req.user.role (AuthZ)
  → Route Handler
```

**FastAPI Implementation:**
```python
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Authentication - who are you?
async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_jwt(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    return payload

# Authorization - can you do this?
def require_admin(user = Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return user

@app.delete("/users/{id}", dependencies=[Depends(require_admin)])
def delete_user(user_id: int, db = Depends(get_db)):
    # Only admins reach here
    ...
```

**RBAC vs ABAC:**
- **RBAC** (Role-Based): `admin`, `editor`, `viewer` roles
- **ABAC** (Attribute-Based): `resource.owner == user.id`

### ❓ Follow-up Questions
- How would you implement row-level security?
- What's the difference between OAuth2 and JWT?
- How do you revoke a JWT token?

### 💡 Senior-level Tips
> Mention JWT token revocation strategies: short expiry + refresh tokens, token blacklist in Redis, or switching to opaque tokens with token introspection.

---

## Q3-B. How did you handle RBAC (Role-Based Access Control)?

### 🎯 Short Version (30 sec)
> RBAC restricts system access based on user roles. Each user is assigned one or more roles (admin, editor, viewer). Each role has a set of permissions. I implemented it using a middleware/dependency that checks `user.role` and `user.permissions` against the required permission for each route.

### 💬 Interview Answer

**RBAC vs ABAC vs ACL:**
| | RBAC | ABAC | ACL |
|---|---|---|---|
| **Based on** | Roles | Attributes | Explicit user list |
| **Example** | Admin can delete | Owner can edit their own | User A can read file X |
| **Scalability** | High | Very High | Low |
| **Complexity** | Low | High | Medium |

**Database Schema:**
```sql
CREATE TABLE roles (
    id    SERIAL PRIMARY KEY,
    name  VARCHAR(50) UNIQUE NOT NULL  -- 'admin', 'editor', 'viewer'
);

CREATE TABLE permissions (
    id       SERIAL PRIMARY KEY,
    resource VARCHAR(100) NOT NULL,    -- 'orders', 'users', 'reports'
    action   VARCHAR(50)  NOT NULL,    -- 'read', 'write', 'delete'
    UNIQUE(resource, action)
);

CREATE TABLE role_permissions (
    role_id       INT REFERENCES roles(id),
    permission_id INT REFERENCES permissions(id),
    PRIMARY KEY (role_id, permission_id)
);

CREATE TABLE user_roles (
    user_id INT REFERENCES users(id),
    role_id INT REFERENCES roles(id),
    PRIMARY KEY (user_id, role_id)
);
```

**FastAPI Implementation:**
```python
from fastapi import Depends, HTTPException
from functools import wraps
from enum import Enum

class Permission(str, Enum):
    ORDERS_READ   = "orders:read"
    ORDERS_WRITE  = "orders:write"
    ORDERS_DELETE = "orders:delete"
    USERS_READ    = "users:read"
    USERS_MANAGE  = "users:manage"

# Role → Permissions mapping (can come from DB/Redis cache)
ROLE_PERMISSIONS = {
    "admin":   {Permission.ORDERS_READ, Permission.ORDERS_WRITE,
                Permission.ORDERS_DELETE, Permission.USERS_READ, Permission.USERS_MANAGE},
    "editor":  {Permission.ORDERS_READ, Permission.ORDERS_WRITE},
    "viewer":  {Permission.ORDERS_READ, Permission.USERS_READ},
}

def require_permission(permission: Permission):
    """Dependency factory — checks if user has required permission"""
    async def checker(user = Depends(get_current_user)):
        user_permissions = set()
        for role in user["roles"]:
            user_permissions |= ROLE_PERMISSIONS.get(role, set())

        if permission not in user_permissions:
            raise HTTPException(
                status_code=403,
                detail=f"Permission denied. Required: {permission}"
            )
        return user
    return checker

# Usage on routes
@app.get("/orders")
async def list_orders(user = Depends(require_permission(Permission.ORDERS_READ))):
    return await db.get_all_orders()

@app.delete("/orders/{order_id}")
async def delete_order(
    order_id: int,
    user = Depends(require_permission(Permission.ORDERS_DELETE))
):
    return await db.delete_order(order_id)

@app.post("/admin/users/{user_id}/roles")
async def assign_role(
    user_id: int,
    role: str,
    admin = Depends(require_permission(Permission.USERS_MANAGE))
):
    return await db.assign_role(user_id, role)
```

**Caching permissions in Redis (avoid DB hit every request):**
```python
async def get_user_permissions(user_id: int) -> set:
    cache_key = f"perms:{user_id}"
    cached = await redis.smembers(cache_key)
    if cached:
        return {p.decode() for p in cached}

    # Load from DB
    permissions = await db.fetch("""
        SELECT DISTINCT p.resource || ':' || p.action as permission
        FROM user_roles ur
        JOIN role_permissions rp ON ur.role_id = rp.role_id
        JOIN permissions p ON rp.permission_id = p.id
        WHERE ur.user_id = $1
    """, user_id)

    perm_set = {row["permission"] for row in permissions}
    if perm_set:
        await redis.sadd(cache_key, *perm_set)
        await redis.expire(cache_key, 300)  # 5 min cache
    return perm_set
```

**Node.js / Express Implementation:**
```javascript
const ROLE_PERMISSIONS = {
    admin:  ["orders:read", "orders:write", "orders:delete", "users:manage"],
    editor: ["orders:read", "orders:write"],
    viewer: ["orders:read"],
};

const requirePermission = (permission) => (req, res, next) => {
    const userRoles = req.user?.roles || [];
    const userPermissions = new Set(
        userRoles.flatMap(role => ROLE_PERMISSIONS[role] || [])
    );

    if (!userPermissions.has(permission)) {
        return res.status(403).json({
            error: "FORBIDDEN",
            message: `Permission '${permission}' required`
        });
    }
    next();
};

// Usage
router.get("/orders",   requirePermission("orders:read"),   getOrders);
router.delete("/orders/:id", requirePermission("orders:delete"), deleteOrder);
```

### ❓ Follow-up Questions
- How do you handle permission changes in real-time (Redis cache invalidation)?
- What's the difference between RBAC and ABAC?
- How do you handle row-level security (user can only see their own orders)?

### 💡 Senior-level Tips
> For **row-level security** (a user should only see their own data), combine RBAC with ABAC: `permission check` + `owner check`. In PostgreSQL you can use `ROW LEVEL SECURITY` policies directly in the DB as a second line of defense.

---

## Q4. Session vs JWT — When to use which?

### 🎯 Short Version (30 sec)
> Sessions store state server-side and use a session ID in cookies. JWTs are self-contained tokens stored client-side. Sessions work well for monoliths; JWTs are better for microservices and APIs.

### 💬 Interview Answer

| | Session | JWT |
|---|---|---|
| **Storage** | Server (Redis/DB) | Client (localStorage/cookie) |
| **Stateful?** | Yes | No |
| **Scalability** | Needs sticky sessions or shared store | Scales horizontally easily |
| **Revocation** | Easy (delete session) | Hard (need blacklist) |
| **Payload** | Minimal (just ID) | Full user data embedded |
| **Best for** | Web apps, monoliths | APIs, microservices, mobile |

**JWT Structure:**
```
Header.Payload.Signature
eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMjN9.signature
```

**JWT Flow:**
```
Login → Server signs JWT → Client stores it
Request → Client sends JWT in Authorization header
Server → Verifies signature (no DB lookup needed)
```

**JWT Problem — Revocation:**
```python
# Solution 1: Short expiry + refresh tokens
ACCESS_TOKEN_EXPIRE = timedelta(minutes=15)
REFRESH_TOKEN_EXPIRE = timedelta(days=7)

# Solution 2: Redis blacklist
async def logout(token: str):
    payload = decode_jwt(token)
    ttl = payload["exp"] - time.time()
    await redis.setex(f"blacklist:{token}", int(ttl), "revoked")

async def verify_token(token: str):
    if await redis.exists(f"blacklist:{token}"):
        raise HTTPException(status_code=401, detail="Token revoked")
    return decode_jwt(token)
```

**When to use Session:**
- Traditional web apps with server-side rendering
- When you need instant revocation
- When you need to store server-side state per user

**When to use JWT:**
- Stateless REST APIs
- Microservices (shared secret or public key)
- Mobile apps
- Cross-domain authentication

### ❓ Follow-up Questions
- How do you handle JWT token refresh securely?
- What's the difference between RS256 and HS256 in JWT?
- Can you store sensitive data in JWT?

### 💡 Senior-level Tips
> RS256 (asymmetric) is preferred in microservices — the auth service signs with a private key, other services verify with the public key. No need to share the private key across services.

---

## Q5. Synchronous vs Asynchronous — When to use async?

### 🎯 Short Version (30 sec)
> Sync blocks execution until a task completes. Async allows the event loop to handle other tasks while waiting for I/O. Use async for I/O-bound tasks (DB, HTTP calls). Sync is fine for CPU-bound tasks unless offloaded to a thread pool.

### 💬 Interview Answer

**The Problem with Sync I/O:**
```python
# Sync - blocks the thread
def get_user(user_id):
    result = db.execute("SELECT * FROM users WHERE id = ?", user_id)  # blocks here
    return result
# With 100 concurrent requests → 100 threads → memory exhaustion
```

**Async Solution:**
```python
# Async - non-blocking
async def get_user(user_id):
    result = await db.execute("SELECT * FROM users WHERE id = ?", user_id)
    return result
# Single thread handles 100 concurrent requests efficiently
```

**Python asyncio Flow:**
```
Event Loop
├─ Task 1: await db.query()     → yields control
├─ Task 2: await redis.get()    → yields control
├─ Task 3: await http.get()     → yields control
└─ Task 1 resumed when DB responds
```

**FastAPI async example:**
```python
import httpx

@app.get("/dashboard")
async def get_dashboard(user_id: int):
    async with httpx.AsyncClient() as client:
        # These run concurrently
        user_task = client.get(f"/users/{user_id}")
        orders_task = client.get(f"/orders?user_id={user_id}")
        user, orders = await asyncio.gather(user_task, orders_task)
    return {"user": user.json(), "orders": orders.json()}
```

**When NOT to use async:**
```python
# CPU-bound task — async doesn't help, use ProcessPoolExecutor
import asyncio
from concurrent.futures import ProcessPoolExecutor

async def process_image(image_data: bytes):
    loop = asyncio.get_event_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, cpu_intensive_transform, image_data)
    return result
```

### ❓ Follow-up Questions
- What happens if you call a blocking function inside an async route in FastAPI?
- What's `asyncio.gather` vs `asyncio.wait`?
- How does Node.js achieve concurrency with a single thread?

### 💡 Senior-level Tips
> In FastAPI, if you define a route as `async def`, it runs in the async event loop. If you define it as `def` (sync), FastAPI runs it in a **thread pool** automatically. Calling a sync blocking library in an `async def` route **blocks the event loop** — always use `run_in_executor` for that.

---

## Q6. What is Stateless Architecture?

### 🎯 Short Version (30 sec)
> A stateless server doesn't retain client state between requests. Each request must carry all necessary information. This enables horizontal scaling because any server can handle any request.

### 💬 Interview Answer

**Stateful vs Stateless:**
```
Stateful:                          Stateless:
Client ──► Server A (session)      Client ──► Server A ✓
Client ──► Server B (no session!)  Client ──► Server B ✓ (JWT carries state)
```

**How to make APIs stateless:**
1. **JWT tokens** — user data embedded in token
2. **External session store** — Redis (shared across servers)
3. **No server-side state** — DB is the source of truth

```python
# ❌ Stateful - bad for scaling
active_users = {}  # in-memory, only on this server instance

@app.post("/login")
def login(credentials: LoginSchema):
    user = authenticate(credentials)
    active_users[user.id] = user  # stored in memory
    return {"session_id": generate_id()}

# ✅ Stateless - good for scaling
@app.post("/login")
def login(credentials: LoginSchema):
    user = authenticate(credentials)
    token = create_jwt({"user_id": user.id, "role": user.role})
    return {"token": token}
    # No server-side state stored
```

**Benefits:**
- Horizontal scaling (any instance handles any request)
- No sticky sessions needed
- Fault tolerant (server crash doesn't lose sessions)
- Easy blue-green deployments

### 💡 Senior-level Tips
> Even with stateless APIs, you still have state — in the database. "Stateless" means the **application server** doesn't hold state. Idempotent API design + stateless servers = highly scalable systems.

---

## Q7. API Gateway — What is it and why do you need it?

### 🎯 Short Version (30 sec)
> An API Gateway is a single entry point for all client requests. It handles routing, authentication, rate limiting, load balancing, and request transformation before forwarding to downstream microservices.

### 💬 Interview Answer

**Without API Gateway (Chaos):**
```
Mobile App ──► Auth Service (port 8001)
Mobile App ──► User Service (port 8002)
Mobile App ──► Order Service (port 8003)
# Client knows all service URLs — tight coupling
```

**With API Gateway (Clean):**
```
Mobile App ──► API Gateway ──► Auth Service
                           ──► User Service
                           ──► Order Service
```

**API Gateway Responsibilities:**
| Function | How |
|---|---|
| Routing | `/users/*` → User Service |
| Authentication | Verify JWT before forwarding |
| Rate Limiting | 100 req/min per user |
| Load Balancing | Round-robin across instances |
| SSL Termination | HTTPS → HTTP internally |
| Request Transformation | Add headers, reshape payloads |
| Response Aggregation | Combine multiple service responses |
| Caching | Cache frequent responses |

**Tools:** Kong, AWS API Gateway, NGINX, Traefik, Envoy

```nginx
# NGINX as API Gateway
location /api/users/ {
    proxy_pass http://user-service:8001/;
    proxy_set_header X-Request-ID $request_id;
    limit_req zone=api_limit burst=20;
}

location /api/orders/ {
    proxy_pass http://order-service:8002/;
}
```

### ❓ Follow-up Questions
- What's the difference between an API Gateway and a Load Balancer?
- How do you handle API versioning at the gateway level?
- What is a BFF (Backend for Frontend) pattern?

### 💡 Senior-level Tips
> API Gateways introduce a **single point of failure** — always deploy them in HA mode with multiple instances. Also, avoid putting business logic in the gateway; keep it as pure infrastructure.

---

## Q8. Rate Limiting — Algorithms and Implementation

### 🎯 Short Version (30 sec)
> Rate limiting controls how many requests a client can make in a time window. Common algorithms: Fixed Window, Sliding Window, Token Bucket, Leaky Bucket. Implemented at the gateway or middleware level using Redis for distributed systems.

### 💬 Interview Answer

**Rate Limiting Algorithms:**

| Algorithm | How It Works | Pros | Cons |
|---|---|---|---|
| Fixed Window | Count resets every N seconds | Simple | Burst at window edge |
| Sliding Window | Rolling count over last N seconds | Smooth | More memory |
| Token Bucket | Tokens replenish at fixed rate | Allows bursts | More complex |
| Leaky Bucket | Queue drains at fixed rate | Smooth output | Can delay requests |

**Token Bucket with Redis:**
```python
import redis
import time

async def rate_limit(user_id: str, limit: int = 100, window: int = 60):
    r = redis.Redis()
    key = f"rate_limit:{user_id}"
    now = time.time()
    window_start = now - window

    pipe = r.pipeline()
    pipe.zremrangebyscore(key, 0, window_start)  # Remove old entries
    pipe.zadd(key, {str(now): now})              # Add current request
    pipe.zcard(key)                               # Count requests in window
    pipe.expire(key, window)
    results = pipe.execute()

    request_count = results[2]
    if request_count > limit:
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded",
            headers={"Retry-After": str(window)}
        )
```

**FastAPI Rate Limiter Middleware:**
```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

@app.get("/api/search")
@limiter.limit("10/minute")
async def search(request: Request, q: str):
    return await do_search(q)
```

### 💡 Senior-level Tips
> Always return proper rate limit headers: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`, and `Retry-After`. Different endpoints may have different limits — public vs authenticated, read vs write.

---

## Q9. CORS — How does it work and how do you configure it?

### 🎯 Short Version (30 sec)
> CORS (Cross-Origin Resource Sharing) is a browser security mechanism that blocks requests from different origins. The server adds `Access-Control-Allow-*` headers to permit cross-origin requests. Preflight OPTIONS requests check permissions before actual requests.

### 💬 Interview Answer

**What is an "Origin"?**
```
https://myapp.com:3000  ← scheme + domain + port = origin
https://api.myapp.com   ← different subdomain = different origin
```

**The Preflight Flow:**
```
Browser                              Server
  │                                    │
  │─── OPTIONS /api/users ────────────►│
  │    Origin: https://app.com         │
  │    Access-Control-Request-Method:  │
  │◄── Access-Control-Allow-Origin ───│
  │    Access-Control-Allow-Methods   │
  │                                    │
  │─── GET /api/users ────────────────►│
  │◄── Response ──────────────────────│
```

**FastAPI CORS:**
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://myapp.com", "https://admin.myapp.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
    max_age=600,  # Cache preflight for 10 minutes
)
```

**Common Mistakes:**
```python
# ❌ Never do this in production
allow_origins=["*"]
allow_credentials=True  # This combination is actually invalid

# ✅ Correct approach
allow_origins=["https://trusted-domain.com"]
allow_credentials=True
```

### 💡 Senior-level Tips
> CORS is a **browser** restriction — it doesn't protect your API from non-browser clients (Postman, curl, etc.). For API security, you still need proper authentication. Use specific origins in production, never `*` with credentials.

---

## Q9-A. What is Serverless? How does it differ from traditional servers?

### 🎯 Short Version (30 sec)
> Serverless means you write functions that are deployed and executed on-demand by a cloud provider — you don't manage servers, scaling, or OS. You pay per invocation, not for idle time. Examples: AWS Lambda, Google Cloud Functions, Azure Functions.

### 💬 Interview Answer

**Traditional Server vs Serverless:**
```
Traditional:                        Serverless:
┌──────────────────┐               ┌──────────────────────┐
│ Server (always   │               │  Cloud Provider       │
│ running, you     │               │  ┌────────────────┐   │
│ manage scaling,  │  vs           │  │ Function (wakes│   │
│ patching, infra) │               │  │ up per request)│   │
└──────────────────┘               │  └────────────────┘   │
  Pay 24/7                         └──────────────────────┘
                                     Pay per invocation
```

**Key Characteristics:**
| Feature | Traditional Server | Serverless |
|---|---|---|
| **Scaling** | Manual / auto-scale groups | Automatic, instant |
| **Billing** | Per hour (even idle) | Per invocation + duration |
| **Cold Start** | No (always warm) | Yes (50ms–2s delay) |
| **State** | Can maintain state | Stateless (must use external store) |
| **Max Duration** | Unlimited | Limited (15 min in AWS Lambda) |
| **Control** | Full OS access | Limited to function code |

**AWS Lambda with Python (FastAPI via Mangum adapter):**
```python
# lambda_handler.py
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id, "name": "John"}

# Mangum adapts FastAPI to AWS Lambda + API Gateway
handler = Mangum(app)

# AWS Lambda calls: handler(event, context)
```

**Serverless with Node.js (AWS Lambda):**
```javascript
// handler.js
exports.handler = async (event) => {
    const userId = event.pathParameters?.userId;

    try {
        const user = await db.findUser(userId);
        return {
            statusCode: 200,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(user)
        };
    } catch (error) {
        return {
            statusCode: 500,
            body: JSON.stringify({ error: error.message })
        };
    }
};
```

**Cold Start Problem & Solutions:**
```
Cold Start Timeline:
Request → [Container Spin-up ~500ms] → [Code Load ~200ms] → [Handler ~50ms]

Warm Request:
Request → [Handler ~50ms]  ← Much faster!
```

```python
# Solutions to cold starts:
# 1. Provisioned Concurrency (AWS Lambda) — keeps containers warm
# 2. Keep functions small and dependencies minimal
# 3. Use /tmp for file caching across invocations
# 4. Use connection pooling-friendly drivers (RDS Proxy)

import os
import boto3

# ✅ Initialize outside handler — reused across warm invocations
db_client = boto3.client("dynamodb")  # Created once, reused

def handler(event, context):
    # This reuses db_client on warm invocations
    result = db_client.get_item(TableName="users", Key={"id": {"S": "123"}})
    return {"statusCode": 200, "body": str(result)}
```

**When to use Serverless:**
- ✅ Event-driven tasks (file upload triggers, webhook handlers)
- ✅ Infrequent or spiky traffic
- ✅ Background jobs (email sending, data processing)
- ✅ Scheduled tasks (cron jobs)
- ❌ Long-running processes (>15 min)
- ❌ WebSocket / persistent connections
- ❌ High-throughput consistent traffic (costly vs containers)

**Serverless Frameworks:**
```yaml
# serverless.yml (Serverless Framework)
service: my-api

provider:
  name: aws
  runtime: python3.11
  region: us-east-1

functions:
  getUser:
    handler: handler.get_user
    events:
      - httpApi:
          path: /users/{userId}
          method: GET
    environment:
      DB_URL: ${env:DB_URL}

  processOrder:
    handler: handler.process_order
    events:
      - sqs:
          arn: !GetAtt OrderQueue.Arn
```

### ❓ Follow-up Questions
- How do you handle DB connections in serverless? (Use RDS Proxy / connection-per-invocation)
- What is the Lambda execution context lifecycle?
- How do you do local development for serverless? (AWS SAM, Serverless Offline)
- How do you manage secrets in Lambda? (AWS Secrets Manager / SSM Parameter Store)

### 💡 Senior-level Tips
> The biggest serverless anti-pattern is putting **long-running or stateful logic** inside a Lambda. Always externalize state to DynamoDB/RDS/Redis. Also, for APIs with sustained traffic, a containerized service (ECS/EKS) is often cheaper than Lambda at scale.

---

# 2. FastAPI Deep Dive

---

## Q10. Explain FastAPI's Dependency Injection System

### 🎯 Short Version (30 sec)
> FastAPI's `Depends()` implements IoC — dependencies are declared as function parameters, and FastAPI resolves them automatically. They support nesting, caching within a request, and teardown via `yield`.

### 💬 Interview Answer

```python
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

app = FastAPI()

# 1. Simple dependency
def get_settings():
    return Settings()

# 2. Database dependency with cleanup
def get_db():
    db = SessionLocal()
    try:
        yield db          # Provide the dependency
    finally:
        db.close()        # Always runs (cleanup)

# 3. Chained dependency
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.token == token).first()
    if not user:
        raise HTTPException(status_code=401)
    return user

# 4. Using dependencies
@app.get("/profile")
def get_profile(user: User = Depends(get_current_user)):
    return user

# 5. Dependency with caching (same instance per request)
@app.get("/info")
def info(
    db1: Session = Depends(get_db),
    db2: Session = Depends(get_db)  # Same instance as db1 within request
):
    assert db1 is db2  # True! FastAPI caches per request
```

**Dependency Scopes:**
```python
# Request-scoped (default)
Depends(get_db)  # New instance per request

# Override caching
Depends(get_db, use_cache=False)  # New instance every time

# App-level (singleton pattern)
@app.on_event("startup")
async def startup():
    app.state.redis = await create_redis_pool()
```

**Testing with Overrides:**
```python
def override_get_db():
    return TestDatabase()

app.dependency_overrides[get_db] = override_get_db

# Now all tests use TestDatabase
```

### 💡 Senior-level Tips
> Use `yield`-based dependencies for any resource that needs cleanup (DB connections, file handles, HTTP clients). FastAPI guarantees the code after `yield` runs even if an exception occurs.

---

## Q11. Background Tasks in FastAPI

### 🎯 Short Version (30 sec)
> FastAPI's `BackgroundTasks` runs functions after the response is sent, without blocking the client. For heavy tasks, use Celery + Redis/RabbitMQ. Background tasks are lightweight; Celery is for distributed, retryable, scheduled work.

### 💬 Interview Answer

```python
from fastapi import BackgroundTasks, FastAPI
import smtplib

app = FastAPI()

# 1. Simple background task
def send_welcome_email(email: str, username: str):
    # Runs after response is sent
    smtp = smtplib.SMTP("smtp.gmail.com")
    smtp.sendmail("no-reply@app.com", email, f"Welcome {username}!")
    smtp.quit()

@app.post("/register")
async def register(user: UserCreate, background_tasks: BackgroundTasks):
    db_user = create_user(user)
    background_tasks.add_task(send_welcome_email, user.email, user.username)
    return {"message": "Registered successfully"}  # Returns immediately
    # Email sends in background

# 2. Multiple background tasks
@app.post("/orders")
async def create_order(order: OrderCreate, background_tasks: BackgroundTasks):
    db_order = save_order(order)
    background_tasks.add_task(send_confirmation_email, order.email)
    background_tasks.add_task(update_inventory, order.items)
    background_tasks.add_task(notify_warehouse, order.id)
    return {"order_id": db_order.id}
```

**When to use Celery instead:**
```python
# Heavy tasks, retries, scheduling, distributed workers → Celery
from celery import Celery

celery_app = Celery("tasks", broker="redis://localhost:6379/0")

@celery_app.task(bind=True, max_retries=3, default_retry_delay=60)
def process_video(self, video_id: str):
    try:
        # Heavy CPU task
        transcode_video(video_id)
    except Exception as exc:
        raise self.retry(exc=exc)

@app.post("/videos/upload")
async def upload_video(file: UploadFile):
    video_id = save_video(file)
    process_video.delay(video_id)  # Async Celery task
    return {"status": "Processing started", "video_id": video_id}
```

| | BackgroundTasks | Celery |
|---|---|---|
| **Retries** | No | Yes |
| **Scheduling** | No | Yes |
| **Distributed** | No | Yes |
| **Progress tracking** | No | Yes |
| **Suitable for** | Lightweight, fire-and-forget | Heavy, reliable processing |

---

## Q12. Exception Handling in FastAPI

### 💬 Interview Answer

```python
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exception_handlers import http_exception_handler

app = FastAPI()

# Custom exception class
class BusinessException(Exception):
    def __init__(self, code: str, message: str, status_code: int = 400):
        self.code = code
        self.message = message
        self.status_code = status_code

# Global exception handler
@app.exception_handler(BusinessException)
async def business_exception_handler(request: Request, exc: BusinessException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.code,
            "message": exc.message,
            "path": str(request.url),
            "timestamp": datetime.utcnow().isoformat()
        }
    )

# Catch-all handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"error": "INTERNAL_ERROR", "message": "Something went wrong"}
    )

# Validation error handler
from fastapi.exceptions import RequestValidationError
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "error": "VALIDATION_ERROR",
            "details": exc.errors()
        }
    )

# Usage
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    user = await db.find_user(user_id)
    if not user:
        raise BusinessException(
            code="USER_NOT_FOUND",
            message=f"User {user_id} not found",
            status_code=404
        )
    return user
```

---

## Q13. Pydantic — Advanced Patterns

### 💬 Interview Answer

```python
from pydantic import BaseModel, validator, Field, EmailStr
from typing import Optional, List
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"
    MODERATOR = "moderator"

class UserCreate(BaseModel):
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50, regex="^[a-zA-Z0-9_]+$")
    password: str = Field(..., min_length=8)
    age: Optional[int] = Field(None, ge=13, le=120)
    role: UserRole = UserRole.USER

    @validator("password")
    def password_strength(cls, v):
        if not any(c.isupper() for c in v):
            raise ValueError("Password must contain uppercase letter")
        if not any(c.isdigit() for c in v):
            raise ValueError("Password must contain a digit")
        return v

    @validator("username")
    def username_lowercase(cls, v):
        return v.lower()

    class Config:
        # Allow ORM objects (SQLAlchemy models)
        orm_mode = True
        # Example schema in docs
        schema_extra = {
            "example": {
                "email": "john@example.com",
                "username": "john_doe",
                "password": "SecurePass1"
            }
        }

# Response model (hide sensitive data)
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    username: str
    role: UserRole
    created_at: datetime

    class Config:
        orm_mode = True

# Nested models
class OrderItem(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0)
    price: float = Field(..., gt=0)

class Order(BaseModel):
    items: List[OrderItem] = Field(..., min_items=1)
    shipping_address: str
    total: float = 0.0

    @validator("total", always=True)
    def calculate_total(cls, v, values):
        if "items" in values:
            return sum(item.price * item.quantity for item in values["items"])
        return v
```

### 💡 Senior-level Tips
> Pydantic V2 (used in FastAPI 0.100+) is significantly faster due to Rust-based core. Use `model_validator` (V2) instead of `validator` (V1). Use `response_model_exclude_none=True` on endpoints to clean up null fields in responses.

---

# 3. Node.js + Express.js Deep Dive

---

## Q14. Explain the Node.js Event Loop

### 🎯 Short Version (30 sec)
> The Event Loop is Node.js's mechanism for handling async operations in a single thread. It processes tasks in phases: timers, I/O callbacks, idle, poll, check (setImmediate), close. The call stack must be empty for the event loop to pick up callbacks.

### 💬 Interview Answer

```
Event Loop Phases:
┌─────────────────────────────────┐
│           timers                │  ← setTimeout, setInterval callbacks
│  ──────────────────────────────  │
│        pending callbacks        │  ← I/O errors from previous loop
│  ──────────────────────────────  │
│           idle, prepare         │  ← Internal use
│  ──────────────────────────────  │
│             poll                │  ← Retrieve new I/O events
│  ──────────────────────────────  │
│             check               │  ← setImmediate callbacks
│  ──────────────────────────────  │
│         close callbacks         │  ← socket.on('close', ...)
└─────────────────────────────────┘
        ↑________________________↓
```

```javascript
// Execution order example
console.log("1: Sync");

setTimeout(() => console.log("2: setTimeout 0"), 0);

Promise.resolve().then(() => console.log("3: Promise (microtask)"));

setImmediate(() => console.log("4: setImmediate"));

process.nextTick(() => console.log("5: nextTick (microtask)"));

console.log("6: Sync end");

// Output order:
// 1: Sync
// 6: Sync end
// 5: nextTick (runs before other microtasks)
// 3: Promise (microtask)
// 2: setTimeout 0
// 4: setImmediate
```

**Why blocking the event loop is catastrophic:**
```javascript
// ❌ This blocks EVERYTHING for all users
app.get("/compute", (req, res) => {
    const result = computeFibonacci(10000000); // Blocks for seconds!
    res.json({ result });
});

// ✅ Offload to Worker Thread
const { Worker } = require("worker_threads");

app.get("/compute", (req, res) => {
    const worker = new Worker("./fibonacci.worker.js", {
        workerData: { n: 10000000 }
    });
    worker.on("message", (result) => res.json({ result }));
    worker.on("error", (err) => res.status(500).json({ error: err.message }));
});
```

### 💡 Senior-level Tips
> `process.nextTick()` runs before any I/O events and even before Promises — it can starve the event loop if called recursively. Use `setImmediate()` when you want to yield to I/O between tasks.

---

## Q15. Express.js Middleware Flow

### 💬 Interview Answer

```javascript
const express = require("express");
const app = express();

// Application-level middleware (all routes)
app.use((req, res, next) => {
    req.requestId = crypto.randomUUID();
    console.log(`[${req.requestId}] ${req.method} ${req.path}`);
    next();
});

// Route-level middleware (specific route)
const authMiddleware = (req, res, next) => {
    const token = req.headers.authorization?.split(" ")[1];
    if (!token) return res.status(401).json({ error: "No token" });
    try {
        req.user = jwt.verify(token, process.env.JWT_SECRET);
        next();
    } catch {
        res.status(401).json({ error: "Invalid token" });
    }
};

// Error-handling middleware (4 params!)
app.use((err, req, res, next) => {
    console.error(err.stack);
    const status = err.statusCode || 500;
    res.status(status).json({
        error: err.message || "Internal Server Error",
        requestId: req.requestId
    });
});

// Middleware execution flow
app.get("/orders", authMiddleware, roleCheck("admin"), async (req, res, next) => {
    try {
        const orders = await Order.find({ userId: req.user.id });
        res.json(orders);
    } catch (err) {
        next(err); // Pass to error handler
    }
});
```

---

## Q16. Node.js Clustering and Worker Threads

### 🎯 Short Version (30 sec)
> Clustering forks multiple Node.js processes, each with its own event loop, to utilize multiple CPU cores. Worker Threads share memory within a single process for CPU-intensive tasks. Clustering is for scaling I/O-bound servers; Workers are for CPU-bound computation.

### 💬 Interview Answer

```javascript
// cluster.js — Utilize all CPU cores
const cluster = require("cluster");
const os = require("os");
const express = require("express");

if (cluster.isPrimary) {
    const numCPUs = os.cpus().length;
    console.log(`Primary ${process.pid} running — forking ${numCPUs} workers`);

    for (let i = 0; i < numCPUs; i++) {
        cluster.fork();
    }

    cluster.on("exit", (worker, code, signal) => {
        console.log(`Worker ${worker.process.pid} died — restarting`);
        cluster.fork(); // Auto-restart dead workers
    });
} else {
    const app = express();
    app.get("/", (req, res) => {
        res.json({ pid: process.pid, message: "Hello from worker" });
    });
    app.listen(3000, () => {
        console.log(`Worker ${process.pid} started`);
    });
}
```

```javascript
// Worker Threads — CPU-bound tasks
// main.js
const { Worker, isMainThread, parentPort, workerData } = require("worker_threads");

if (isMainThread) {
    app.post("/analyze", (req, res) => {
        const worker = new Worker(__filename, {
            workerData: { data: req.body.data }
        });
        worker.on("message", (result) => res.json(result));
        worker.on("error", (err) => res.status(500).json({ error: err.message }));
    });
} else {
    // This runs in worker thread
    const result = heavyComputation(workerData.data);
    parentPort.postMessage(result);
}
```

| | Cluster | Worker Threads |
|---|---|---|
| **Process** | Separate processes | Threads in same process |
| **Memory** | Isolated | Shared (SharedArrayBuffer) |
| **Use case** | Scaling HTTP servers | CPU-bound computation |
| **IPC** | Inter-process messaging | Message passing / shared memory |

### 💡 Senior-level Tips
> In production, use **PM2** instead of raw cluster module — it handles clustering, auto-restart, zero-downtime reloads, and monitoring: `pm2 start app.js -i max`

---

## Q17. Memory Leaks in Node.js — Detection and Prevention

### 💬 Interview Answer

**Common Causes:**
```javascript
// 1. Global variable accumulation
global.cache = {};
app.get("/user/:id", async (req, res) => {
    if (!global.cache[req.params.id]) {
        global.cache[req.params.id] = await fetchUser(req.params.id); // Grows forever!
    }
    res.json(global.cache[req.params.id]);
});
// Fix: Use Redis with TTL instead of in-memory global

// 2. Event listener accumulation
const EventEmitter = require("events");
const emitter = new EventEmitter();

app.get("/subscribe", (req, res) => {
    emitter.on("data", (data) => res.json(data)); // Added every request, never removed!
});
// Fix: Remove listeners
const handler = (data) => res.json(data);
emitter.on("data", handler);
req.on("close", () => emitter.removeListener("data", handler));

// 3. Unclosed database connections
app.get("/users", async (req, res) => {
    const conn = await pool.connect(); // Never released!
    const result = await conn.query("SELECT * FROM users");
    res.json(result.rows);
});
// Fix: Always release in finally
app.get("/users", async (req, res) => {
    const conn = await pool.connect();
    try {
        const result = await conn.query("SELECT * FROM users");
        res.json(result.rows);
    } finally {
        conn.release(); // Always released
    }
});
```

**Detection:**
```bash
# Heap snapshot comparison
node --inspect app.js

# Memory profiling
node --prof app.js
node --prof-process isolate-*.log > profile.txt

# Production monitoring
# 1. Watch process.memoryUsage()
setInterval(() => {
    const mem = process.memoryUsage();
    console.log(`Heap used: ${Math.round(mem.heapUsed / 1024 / 1024)}MB`);
}, 5000);
```

---

# 4. Database Questions

---

## Q18. Indexing — Types and When to Use Each

### 🎯 Short Version (30 sec)
> An index speeds up reads by creating a data structure (usually B-tree) for quick lookups. Trade-off: faster reads, slower writes, more storage. Use on frequently queried columns, foreign keys, and sort columns. Avoid on small tables or rarely-queried columns.

### 💬 Interview Answer

**Index Types:**

| Type | Use Case | Example |
|---|---|---|
| B-Tree (default) | Range queries, equality | `WHERE created_at > '2024-01-01'` |
| Hash | Equality only | `WHERE user_id = 123` |
| GIN | Full-text search, arrays, JSONB | `WHERE tags @> ARRAY['python']` |
| GiST | Geometric, custom types | Geographic queries |
| Partial | Subset of rows | `WHERE status = 'active'` |
| Composite | Multi-column queries | `WHERE user_id = 1 AND status = 'active'` |
| Covering | All data in index | Avoid table lookup |

```sql
-- Single column index
CREATE INDEX idx_users_email ON users(email);

-- Composite index (order matters!)
-- Good for: WHERE user_id = 1 AND status = 'active'
-- Also good for: WHERE user_id = 1
-- Bad for: WHERE status = 'active' alone
CREATE INDEX idx_orders_user_status ON orders(user_id, status);

-- Partial index (only index active users)
CREATE INDEX idx_active_users ON users(email) WHERE status = 'active';

-- Covering index (all needed data is in index)
CREATE INDEX idx_users_covering ON users(email) INCLUDE (id, name);

-- Full-text search
CREATE INDEX idx_posts_search ON posts USING GIN (to_tsvector('english', title || ' ' || body));
```

**EXPLAIN ANALYZE:**
```sql
EXPLAIN ANALYZE
SELECT * FROM orders
WHERE user_id = 123 AND status = 'pending'
ORDER BY created_at DESC;

-- Look for:
-- Seq Scan → No index used (bad for large tables)
-- Index Scan → Index used (good)
-- Index Only Scan → Covering index (best)
-- Bitmap Heap Scan → Multiple indexes combined
```

### 💡 Senior-level Tips
> The **selectivity** of an index matters. An index on a boolean column with 50/50 distribution is useless — PostgreSQL may ignore it. Use `VACUUM ANALYZE` to keep statistics fresh so the query planner makes good decisions.

---

## Q19. SQL Transactions and ACID Properties

### 🎯 Short Version (30 sec)
> ACID: Atomicity (all or nothing), Consistency (valid state transitions), Isolation (concurrent transactions don't interfere), Durability (committed data survives crashes). Implemented via WAL (Write-Ahead Logging) and MVCC in PostgreSQL.

### 💬 Interview Answer

```sql
-- Atomicity: Bank transfer — both operations succeed or both fail
BEGIN;
    UPDATE accounts SET balance = balance - 100 WHERE user_id = 1;
    UPDATE accounts SET balance = balance + 100 WHERE user_id = 2;
    -- If error occurs here, both updates are rolled back
COMMIT;

-- Isolation levels
-- Read Uncommitted → Dirty reads possible (rarely used)
-- Read Committed → Default in PostgreSQL — no dirty reads
-- Repeatable Read → Same row returns same value in same transaction
-- Serializable → Transactions appear sequential

SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN;
    SELECT balance FROM accounts WHERE user_id = 1; -- Returns 100
    -- Another transaction changes balance to 50 here
    SELECT balance FROM accounts WHERE user_id = 1; -- Still returns 100 (snapshot)
COMMIT;
```

**Concurrency Problems and Solutions:**

| Problem | Description | Solved By |
|---|---|---|
| Dirty Read | Read uncommitted data | Read Committed+ |
| Non-repeatable Read | Same query returns different values | Repeatable Read+ |
| Phantom Read | New rows appear in range query | Serializable |
| Lost Update | Two updates, one is lost | SELECT FOR UPDATE |

```sql
-- Optimistic Locking (application-level)
-- 1. Read with version
SELECT id, balance, version FROM accounts WHERE id = 1;
-- Returns: {id: 1, balance: 100, version: 5}

-- 2. Update only if version matches
UPDATE accounts
SET balance = 150, version = version + 1
WHERE id = 1 AND version = 5;
-- If 0 rows affected → someone else updated → retry

-- Pessimistic Locking (database-level)
BEGIN;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE; -- Locks the row
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
```

---

## Q20. SQL vs NoSQL — When to Use Which?

### 💬 Interview Answer

| | SQL (PostgreSQL) | NoSQL (MongoDB) |
|---|---|---|
| **Schema** | Fixed, structured | Flexible, dynamic |
| **Relationships** | JOINs, FKs | Embedded documents / references |
| **Scaling** | Vertical (scale-up) primary | Horizontal (scale-out) |
| **Transactions** | Full ACID | Limited (MongoDB 4+ has multi-doc) |
| **Query Language** | SQL (standardized) | MongoDB query language |
| **Best for** | Financial, relational data | Catalogs, user profiles, logs |

**Choose PostgreSQL when:**
- Data has complex relationships
- You need ACID transactions (payments, inventory)
- Reporting and analytics queries
- Data integrity is critical
- Team knows SQL well

**Choose MongoDB when:**
- Schema changes frequently (agile development)
- Document-oriented data (product catalogs)
- High write throughput needed
- Hierarchical data (nested documents avoid JOINs)
- Geospatial queries

**Choose Both (Polyglot Persistence):**
```
User Service → PostgreSQL (user accounts, transactions)
Product Service → MongoDB (product catalog, reviews)
Session Service → Redis (sessions, cache)
Search Service → Elasticsearch (full-text search)
Analytics → ClickHouse (OLAP queries)
```

---

## Q21. Query Optimization — Real Scenarios

### 💬 Interview Answer

**Scenario: Slow API — Finding the bottleneck**

```sql
-- Step 1: Enable slow query log
ALTER SYSTEM SET log_min_duration_statement = 1000; -- Log queries > 1 second

-- Step 2: Identify slow queries
SELECT query, mean_exec_time, calls, total_exec_time
FROM pg_stat_statements
ORDER BY mean_exec_time DESC
LIMIT 10;

-- Step 3: EXPLAIN ANALYZE
EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON)
SELECT u.name, COUNT(o.id) as order_count, SUM(o.total) as revenue
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE o.created_at >= '2024-01-01'
  AND o.status = 'completed'
GROUP BY u.id, u.name
ORDER BY revenue DESC;
```

**Common optimizations:**
```sql
-- 1. N+1 Query Problem (very common!)
-- ❌ N+1: 1 query for users + 1 query per user for orders
users = SELECT * FROM users;
for user in users:
    orders = SELECT * FROM orders WHERE user_id = {user.id}

-- ✅ One query with JOIN
SELECT u.*, o.id as order_id, o.total
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;

-- 2. SELECT * is expensive
-- ❌ Fetches all columns including BLOBs
SELECT * FROM products;

-- ✅ Only needed columns
SELECT id, name, price FROM products;

-- 3. OFFSET pagination is slow on large tables
-- ❌ Database scans 1 million rows to skip
SELECT * FROM orders ORDER BY id LIMIT 20 OFFSET 1000000;

-- ✅ Cursor-based pagination
SELECT * FROM orders WHERE id > :last_seen_id ORDER BY id LIMIT 20;
```

---

## Q22. Database Connection Pooling

### 💬 Interview Answer

```
Without pooling:               With pooling:
Request 1 → new DB conn       Request 1 ─┐
Request 2 → new DB conn       Request 2 ─┼─► Pool (10 connections) ──► DB
Request 3 → new DB conn       Request 3 ─┘
(expensive, slow)              (reused, fast)
```

```python
# SQLAlchemy connection pool
from sqlalchemy import create_engine

engine = create_engine(
    DATABASE_URL,
    pool_size=10,           # Number of connections to maintain
    max_overflow=20,        # Extra connections allowed temporarily
    pool_timeout=30,        # Wait time before giving up
    pool_recycle=3600,      # Recreate connections older than 1 hour
    pool_pre_ping=True,     # Verify connections before using
)

# Asyncpg pool (async)
import asyncpg

pool = await asyncpg.create_pool(
    DATABASE_URL,
    min_size=5,
    max_size=20,
    command_timeout=60,
)
```

**Pool sizing formula:**
```
Optimal pool size ≈ (Core count × 2) + effective_spindle_count
For a 4-core machine: (4 × 2) + 1 = 9 connections per app instance
```

### 💡 Senior-level Tips
> A large connection pool doesn't always mean better performance. PostgreSQL has a **max_connections** limit (default 100). Each connection uses ~10MB RAM. With 10 app instances × 20 pool size = 200 connections → over limit! Use **PgBouncer** as a connection proxy for high-scale systems.

---

## Q23-A. What is Sharding and Partitioning?

### 🎯 Short Version (30 sec)
> **Partitioning** splits a single table into smaller physical pieces within the same database server. **Sharding** splits data across multiple database servers (horizontal scaling). Partitioning improves query performance; sharding improves write throughput and storage capacity.

### 💬 Interview Answer

**Partitioning (Single Server):**
```
orders table (1 billion rows)
         ↓ PARTITION BY RANGE (created_at)
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│orders_2023      │  │orders_2024      │  │orders_2025      │
│(Jan-Dec 2023)   │  │(Jan-Dec 2024)   │  │(Jan-Dec 2025)   │
└─────────────────┘  └─────────────────┘  └─────────────────┘
  All on same DB server — managed by PostgreSQL automatically
```

```sql
-- PostgreSQL Table Partitioning
CREATE TABLE orders (
    id          BIGSERIAL,
    user_id     BIGINT,
    total       NUMERIC(10,2),
    status      VARCHAR(20),
    created_at  TIMESTAMPTZ NOT NULL
) PARTITION BY RANGE (created_at);

-- Create partitions (can be automated)
CREATE TABLE orders_2024_q1 PARTITION OF orders
    FOR VALUES FROM ('2024-01-01') TO ('2024-04-01');

CREATE TABLE orders_2024_q2 PARTITION OF orders
    FOR VALUES FROM ('2024-04-01') TO ('2024-07-01');

-- Query only hits relevant partition (partition pruning)
SELECT * FROM orders
WHERE created_at BETWEEN '2024-01-01' AND '2024-03-31';
-- PostgreSQL scans only orders_2024_q1 — not all partitions!
```

**Partition Types:**
| Type | How | Use Case |
|---|---|---|
| **Range** | Partition by value range | Dates, IDs |
| **List** | Partition by exact values | Country, status |
| **Hash** | Partition by hash of key | Even distribution |

```sql
-- List partitioning (by region)
CREATE TABLE users PARTITION BY LIST (region);
CREATE TABLE users_us PARTITION OF users FOR VALUES IN ('us-east', 'us-west');
CREATE TABLE users_eu PARTITION OF users FOR VALUES IN ('eu-west', 'eu-central');

-- Hash partitioning (even distribution)
CREATE TABLE events PARTITION BY HASH (user_id);
CREATE TABLE events_0 PARTITION OF events FOR VALUES WITH (MODULUS 4, REMAINDER 0);
CREATE TABLE events_1 PARTITION OF events FOR VALUES WITH (MODULUS 4, REMAINDER 1);
```

**Sharding (Multiple Servers):**
```
App
 ├── Shard 1 (user_id 0-999,999)    → PostgreSQL Server A
 ├── Shard 2 (user_id 1M-1,999,999) → PostgreSQL Server B
 └── Shard 3 (user_id 2M-2,999,999) → PostgreSQL Server C
```

**Sharding Strategies:**
```python
# 1. Range-based sharding
def get_shard(user_id: int) -> str:
    if user_id < 1_000_000:
        return "shard_1"
    elif user_id < 2_000_000:
        return "shard_2"
    else:
        return "shard_3"

# 2. Hash-based sharding (even distribution)
def get_shard_hash(user_id: int, num_shards: int = 3) -> str:
    shard_index = user_id % num_shards
    return f"shard_{shard_index + 1}"

# 3. Directory-based sharding (lookup table)
async def get_shard_directory(user_id: int) -> str:
    shard = await redis.get(f"shard_map:{user_id}")
    if not shard:
        shard = await db.lookup("shard_directory", user_id=user_id)
        await redis.setex(f"shard_map:{user_id}", 3600, shard)
    return shard

# Shard-aware DB client
class ShardedDatabase:
    def __init__(self):
        self.shards = {
            "shard_1": create_engine(SHARD_1_URL),
            "shard_2": create_engine(SHARD_2_URL),
            "shard_3": create_engine(SHARD_3_URL),
        }

    def get_engine(self, user_id: int):
        shard_name = get_shard_hash(user_id)
        return self.shards[shard_name]

    async def get_user(self, user_id: int):
        engine = self.get_engine(user_id)
        return await engine.execute("SELECT * FROM users WHERE id = $1", user_id)
```

**Sharding vs Partitioning — Key Differences:**
| | Partitioning | Sharding |
|---|---|---|
| **Location** | Same server | Multiple servers |
| **Managed by** | Database (auto) | Application / middleware |
| **Joins** | Work normally | Cross-shard joins are hard |
| **Transactions** | Full ACID | Distributed transactions (complex) |
| **When to use** | Performance on large tables | Write scaling, data volume |
| **Complexity** | Low | High |

**Sharding Problems to mention:**
- **Cross-shard queries** — joining data across shards is expensive
- **Rebalancing** — adding a new shard requires data migration
- **Hot spots** — one shard gets all the traffic (bad sharding key)
- **Distributed transactions** — 2-phase commit needed across shards

### ❓ Follow-up Questions
- What is a hotspot shard and how do you avoid it?
- How do you rebalance shards when adding a new server?
- What is consistent hashing and why is it used for sharding?
- How does MongoDB handle sharding?

### 💡 Senior-level Tips
> Always exhaust vertical scaling, read replicas, caching, and partitioning **before** sharding. Sharding adds enormous operational complexity. If you must shard, use consistent hashing so adding/removing shards only remaps a small percentage of keys.

---

## Q23. Pagination Strategies

### 💬 Interview Answer

```python
# Strategy 1: Offset Pagination (simple but slow at scale)
@app.get("/users")
async def get_users(page: int = 1, page_size: int = 20):
    offset = (page - 1) * page_size
    users = await db.execute(
        "SELECT * FROM users ORDER BY id LIMIT :limit OFFSET :offset",
        {"limit": page_size, "offset": offset}
    )
    total = await db.execute("SELECT COUNT(*) FROM users")
    return {
        "data": users,
        "page": page,
        "total_pages": ceil(total / page_size)
    }
    # ❌ Problem: OFFSET 1,000,000 scans 1 million rows!

# Strategy 2: Cursor-based Pagination (fast, scalable)
@app.get("/users")
async def get_users(cursor: Optional[str] = None, limit: int = 20):
    if cursor:
        last_id = decode_cursor(cursor)
        users = await db.execute(
            "SELECT * FROM users WHERE id > :last_id ORDER BY id LIMIT :limit",
            {"last_id": last_id, "limit": limit + 1}
        )
    else:
        users = await db.execute(
            "SELECT * FROM users ORDER BY id LIMIT :limit",
            {"limit": limit + 1}
        )

    has_more = len(users) > limit
    if has_more:
        users = users[:-1]

    next_cursor = encode_cursor(users[-1].id) if has_more else None

    return {
        "data": users,
        "next_cursor": next_cursor,
        "has_more": has_more
    }
```

| | Offset | Cursor |
|---|---|---|
| **Performance** | Degrades at scale | Consistent O(1) |
| **Arbitrary jump** | Yes (page 100) | No |
| **Real-time data** | Misses new items | Stable |
| **Best for** | Admin panels | Feeds, infinite scroll |

---

# 5. Production & Debugging

---

## Q24. How do you debug a production issue?

### 🎯 Short Version (30 sec)
> First, define and isolate the problem. Check monitoring dashboards, correlate with recent deployments, examine logs with error traces, reproduce locally if possible, fix with minimal blast radius, then do a post-mortem.

### 💬 Interview Answer

**Systematic Debugging Process:**

```
Step 1: Define the problem clearly
├── What is the exact error? (500? Timeout? Wrong data?)
├── When did it start? (Correlate with deployments)
├── Who is affected? (All users? Specific region? Specific feature?)
└── How often? (Every request? 1% of traffic?)

Step 2: Gather data
├── Check monitoring dashboards (CPU, memory, DB connections, error rate)
├── Examine logs with the request ID from affected users
├── Check recent deployments (git log, deployment history)
└── Look for anomalies (traffic spike? New third-party API issue?)

Step 3: Form a hypothesis and test
├── "DB queries are slow" → Check pg_stat_activity
├── "Memory leak" → Check process.memoryUsage() trend
├── "Downstream service failing" → Check service health endpoints
└── "Redis connection exhausted" → Check Redis connections

Step 4: Fix with minimal blast radius
├── Can we roll back? (Safest option)
├── Feature flag to disable affected feature?
└── Hotfix with careful review

Step 5: Verify and monitor
Step 6: Post-mortem (5 Whys analysis)
```

**Practical debugging commands:**
```bash
# Check live logs with filtering
kubectl logs -f deployment/api-service | grep "ERROR"

# Find all logs for a specific request
grep "request_id=abc123" /var/log/app/*.log

# Database slow queries
SELECT query, state, wait_event_type, wait_event, duration
FROM pg_stat_activity
WHERE state != 'idle'
ORDER BY duration DESC;

# Memory usage
ps aux --sort=-%mem | head -20
cat /proc/meminfo

# Redis connections
redis-cli CLIENT LIST | wc -l
redis-cli INFO stats | grep rejected_connections
```

---

## Q25. How do you investigate a slow API?

### 💬 Interview Answer

**Methodical approach:**

```python
# 1. Add timing middleware to identify bottleneck
import time
import logging

class TimingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.monotonic()
        response = await call_next(request)
        duration_ms = (time.monotonic() - start) * 1000
        response.headers["X-Response-Time"] = f"{duration_ms:.2f}ms"
        if duration_ms > 1000:
            logger.warning(
                f"Slow request",
                extra={
                    "path": request.url.path,
                    "method": request.method,
                    "duration_ms": duration_ms,
                    "status_code": response.status_code
                }
            )
        return response

# 2. Distributed tracing (OpenTelemetry)
from opentelemetry import trace
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

FastAPIInstrumentor.instrument_app(app)

@app.get("/orders/{order_id}")
async def get_order(order_id: int):
    tracer = trace.get_tracer(__name__)
    with tracer.start_as_current_span("fetch_order") as span:
        span.set_attribute("order_id", order_id)
        order = await db.get_order(order_id)

    with tracer.start_as_current_span("fetch_order_items"):
        items = await db.get_order_items(order_id)

    return {**order, "items": items}
```

**Checklist:**
```
☐ Is it the DB? → EXPLAIN ANALYZE slow queries
☐ Is it network latency? → External API call timing
☐ Is it the payload size? → Check response size, add pagination
☐ Is it N+1 queries? → Check query count per request
☐ Is it missing cache? → Redis cache hit/miss ratio
☐ Is it cold starts? → Container startup time
☐ Is it connection pool exhausted? → Check pool wait time
```

---

## Q26. Logging Strategy for Production

### 💬 Interview Answer

**Structured Logging (JSON):**
```python
import structlog
import logging

# Configure structured logging
structlog.configure(
    processors=[
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.stdlib.add_logger_name,
        structlog.processors.JSONRenderer()
    ]
)

logger = structlog.get_logger()

# Usage
logger.info(
    "order_created",
    order_id=order.id,
    user_id=user.id,
    total=order.total,
    items_count=len(order.items),
    request_id=request.state.request_id
)
# Output: {"level": "info", "event": "order_created", "order_id": 123, ...}
```

**Log Levels:**
```python
logger.debug("Detailed diagnostic info")    # Development only
logger.info("Normal operations")            # Successful requests, key events
logger.warning("Unexpected but handled")    # Degraded mode, retries
logger.error("Error occurred, handled")     # Exceptions caught
logger.critical("System may be down")       # Alert immediately
```

**Log Aggregation Stack:**
```
App Logs (stdout/file)
    → Fluentd/Logstash (collection)
    → Elasticsearch (storage/indexing)
    → Kibana (visualization/search)
    OR
    → CloudWatch / Datadog / New Relic
```

**What to log:**
```python
# ✅ Log these
- Request start: method, path, user_id, request_id
- Request end: status_code, duration_ms
- Business events: order_placed, payment_failed, user_registered
- Errors with full stack trace
- External API calls: service, duration, status

# ❌ Never log
- Passwords or secrets
- Credit card numbers
- JWT tokens
- PII without masking
```

---

## Q27. Handling Sudden Traffic Spikes

### 💬 Interview Answer

**Defense in depth strategy:**

```
Traffic Spike
    ↓
[CDN / Edge Caching] → Serve 80% from cache, no origin hit
    ↓
[Rate Limiter] → Shed load from bots/abuse
    ↓
[Load Balancer] → Distribute across instances
    ↓
[Auto-scaling] → Add instances (HPA in Kubernetes)
    ↓
[Circuit Breaker] → Fail fast if downstream is overwhelmed
    ↓
[Queue] → Buffer requests, process at sustainable rate
    ↓
[Database] → Read replicas for read traffic, connection pooling
```

```python
# Circuit Breaker Pattern
from circuitbreaker import circuit

@circuit(failure_threshold=5, recovery_timeout=30)
async def call_payment_service(order_id: int):
    async with httpx.AsyncClient(timeout=5.0) as client:
        response = await client.post(f"/payments/{order_id}")
        return response.json()

# When payment service fails 5 times:
# Circuit opens → returns immediately with error (fail fast)
# After 30 seconds: half-open → tries one request
# If success: closes circuit
```

**Kubernetes HPA:**
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: api-service
spec:
  minReplicas: 3
  maxReplicas: 50
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
```

---

# 6. System Design

---

## Q28. Design a URL Shortener

### 💬 Interview Answer

**Requirements:**
- Shorten URLs (e.g., `bit.ly/abc123`)
- Redirect to original URL
- 100M URLs, 10:1 read:write ratio
- P99 redirect latency < 100ms

**High-Level Architecture:**
```
User → [API Gateway] → [URL Service] → [PostgreSQL]
                              ↓
                          [Redis Cache]
                              ↓
[CDN] ← [Redirect Service] ←────────
```

**Key Design Decisions:**

```python
# 1. ID Generation — How to create short codes?
# Option A: Hash (MD5/SHA) + truncate (collision risk)
import hashlib
short_code = hashlib.md5(long_url.encode()).hexdigest()[:7]

# Option B: Auto-increment ID → Base62 encode (no collision)
CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def encode_base62(num: int) -> str:
    result = ""
    while num > 0:
        result = CHARS[num % 62] + result
        num //= 62
    return result or "0"

# ID 1000 → "G8" (short code)

# 2. Database Schema
CREATE TABLE urls (
    id          BIGSERIAL PRIMARY KEY,
    short_code  VARCHAR(10) UNIQUE NOT NULL,
    long_url    TEXT NOT NULL,
    user_id     BIGINT REFERENCES users(id),
    created_at  TIMESTAMP DEFAULT NOW(),
    expires_at  TIMESTAMP,
    click_count BIGINT DEFAULT 0
);
CREATE INDEX idx_short_code ON urls(short_code);

# 3. Redirect Flow
@app.get("/{short_code}")
async def redirect(short_code: str, redis: Redis = Depends(get_redis)):
    # Check cache first
    long_url = await redis.get(f"url:{short_code}")

    if not long_url:
        # Cache miss — check DB
        url_record = await db.get_url_by_code(short_code)
        if not url_record:
            raise HTTPException(status_code=404)
        if url_record.expires_at and url_record.expires_at < datetime.now():
            raise HTTPException(status_code=410, detail="URL expired")
        long_url = url_record.long_url
        # Cache for 24 hours
        await redis.setex(f"url:{short_code}", 86400, long_url)

    # Async click tracking (don't slow down redirect)
    background_tasks.add_task(track_click, short_code)
    return RedirectResponse(url=long_url, status_code=301)
```

**Scalability:**
- Redis cache for 95%+ cache hit rate
- Read replicas for DB reads
- CDN caches popular redirects at edge
- Click counting via Redis INCR (async batch write to DB)
- Multiple regions for global low latency

---

## Q29. Design a Notification Service

### 💬 Interview Answer

**Multi-channel notification system (Email, SMS, Push, In-App)**

```
Producer Services
(Order, Auth, etc.)
        ↓
[Message Queue (Kafka)]
        ↓
[Notification Service]
    ├── Email Worker (SendGrid)
    ├── SMS Worker (Twilio)
    ├── Push Worker (FCM/APNs)
    └── In-App Worker (WebSocket/DB)
```

```python
# Event-driven notification
# 1. Producer publishes event
async def process_order(order: Order):
    await save_order(order)
    await kafka.publish("order.placed", {
        "event": "order.placed",
        "order_id": order.id,
        "user_id": order.user_id,
        "total": order.total,
        "timestamp": datetime.utcnow().isoformat()
    })

# 2. Notification service consumes
@kafka.consumer("order.placed")
async def handle_order_placed(event: dict):
    user = await get_user(event["user_id"])
    preferences = await get_notification_prefs(event["user_id"])

    tasks = []
    if preferences.email:
        tasks.append(send_email(user.email, "order_confirmation", event))
    if preferences.sms:
        tasks.append(send_sms(user.phone, f"Order #{event['order_id']} confirmed!"))
    if preferences.push:
        tasks.append(send_push(user.device_tokens, event))

    await asyncio.gather(*tasks, return_exceptions=True)

# Database schema
CREATE TABLE notifications (
    id              BIGSERIAL PRIMARY KEY,
    user_id         BIGINT NOT NULL,
    type            VARCHAR(50) NOT NULL,  -- email, sms, push, in_app
    status          VARCHAR(20) DEFAULT 'pending',  -- sent, failed, delivered
    payload         JSONB NOT NULL,
    retry_count     INT DEFAULT 0,
    scheduled_at    TIMESTAMP,
    sent_at         TIMESTAMP,
    created_at      TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_notifications_user ON notifications(user_id, created_at DESC);
CREATE INDEX idx_notifications_pending ON notifications(status, scheduled_at)
    WHERE status = 'pending';
```

**Key Features:**
- **Retry with exponential backoff** for failed deliveries
- **User preferences** — opt-out per channel
- **Rate limiting** — max 5 notifications/hour per user
- **Template engine** — Jinja2 for email templates
- **Deduplication** — idempotency key to prevent duplicate sends

---

## Q30. Design a Rate Limiter

### 💬 Interview Answer

**Distributed Rate Limiter using Redis + Token Bucket:**

```python
import redis.asyncio as aioredis
import time
from fastapi import HTTPException, Request

class DistributedRateLimiter:
    def __init__(self, redis_url: str):
        self.redis = aioredis.from_url(redis_url)

    async def check_rate_limit(
        self,
        identifier: str,     # user_id or IP
        limit: int,          # max requests
        window: int          # time window in seconds
    ) -> dict:
        key = f"rate_limit:{identifier}"
        now = time.time()
        window_start = now - window

        pipe = self.redis.pipeline()
        # Sliding window log algorithm
        pipe.zremrangebyscore(key, 0, window_start)     # Remove old
        pipe.zadd(key, {str(now): now})                  # Add current
        pipe.zcard(key)                                  # Count
        pipe.expire(key, window)                         # Set TTL
        results = await pipe.execute()

        request_count = results[2]
        remaining = max(0, limit - request_count)

        return {
            "limit": limit,
            "remaining": remaining,
            "reset": int(now + window),
            "allowed": request_count <= limit
        }

# Middleware
limiter = DistributedRateLimiter("redis://localhost:6379")

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    user_id = getattr(request.state, "user_id", request.client.host)
    result = await limiter.check_rate_limit(user_id, limit=100, window=60)

    if not result["allowed"]:
        return JSONResponse(
            status_code=429,
            content={"error": "Rate limit exceeded"},
            headers={
                "X-RateLimit-Limit": str(result["limit"]),
                "X-RateLimit-Remaining": "0",
                "X-RateLimit-Reset": str(result["reset"]),
                "Retry-After": "60"
            }
        )

    response = await call_next(request)
    response.headers["X-RateLimit-Limit"] = str(result["limit"])
    response.headers["X-RateLimit-Remaining"] = str(result["remaining"])
    return response
```

---

## Q31. Design a File Upload Service

### 💬 Interview Answer

```
Client → [Presigned URL API] → [File Storage (S3/GCS)]
                                        ↓
                            [Message Queue (SQS/Kafka)]
                                        ↓
                            [Processing Workers]
                            ├── Virus Scan
                            ├── Image Resize
                            └── Metadata Extraction
                                        ↓
                                [Database Update]
                                [CDN Distribution]
```

```python
# 1. Presigned URL upload (no files through your server)
import boto3
from botocore.exceptions import ClientError

s3 = boto3.client("s3")

@app.post("/files/upload-url")
async def get_upload_url(
    file_name: str,
    content_type: str,
    user = Depends(get_current_user)
):
    # Validate file type
    allowed_types = {"image/jpeg", "image/png", "application/pdf"}
    if content_type not in allowed_types:
        raise HTTPException(status_code=400, detail="File type not allowed")

    file_id = str(uuid.uuid4())
    s3_key = f"uploads/{user.id}/{file_id}/{file_name}"

    # Generate presigned URL (expires in 15 minutes)
    presigned_url = s3.generate_presigned_url(
        "put_object",
        Params={
            "Bucket": "my-uploads",
            "Key": s3_key,
            "ContentType": content_type,
            "ContentLength": 10 * 1024 * 1024  # Max 10MB
        },
        ExpiresIn=900
    )

    # Save pending record to DB
    await db.create_file_record({
        "id": file_id,
        "user_id": user.id,
        "s3_key": s3_key,
        "status": "pending",
        "original_name": file_name
    })

    return {"upload_url": presigned_url, "file_id": file_id}

# 2. Post-upload webhook
@app.post("/files/{file_id}/complete")
async def file_upload_complete(file_id: str, user = Depends(get_current_user)):
    file_record = await db.get_file(file_id)

    # Verify file exists in S3
    try:
        s3.head_object(Bucket="my-uploads", Key=file_record.s3_key)
    except ClientError:
        raise HTTPException(status_code=400, detail="File not found in storage")

    # Trigger async processing
    await sqs.send_message(
        QueueUrl=PROCESSING_QUEUE,
        MessageBody=json.dumps({"file_id": file_id, "s3_key": file_record.s3_key})
    )

    await db.update_file_status(file_id, "processing")
    return {"status": "processing", "file_id": file_id}
```

---

## Q32. Design a Chat System

### 💬 Interview Answer

```
Client A ─WebSocket─► [WebSocket Server] ─► [Redis Pub/Sub]
                                                   ↓
Client B ◄─WebSocket─ [WebSocket Server] ◄─────────
                              ↓
                      [Message Queue] → [Message Service] → [PostgreSQL]
```

```python
# WebSocket chat with Redis Pub/Sub for multi-server support
import asyncio
from fastapi import WebSocket
from redis.asyncio import Redis

active_connections: dict[str, WebSocket] = {}

@app.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str, user_id: str):
    await websocket.accept()
    active_connections[user_id] = websocket

    redis = Redis()
    pubsub = redis.pubsub()
    await pubsub.subscribe(f"room:{room_id}")

    async def listen_to_redis():
        async for message in pubsub.listen():
            if message["type"] == "message":
                await websocket.send_text(message["data"].decode())

    listener_task = asyncio.create_task(listen_to_redis())

    try:
        while True:
            data = await websocket.receive_text()
            msg = json.dumps({
                "user_id": user_id,
                "content": data,
                "timestamp": datetime.utcnow().isoformat()
            })
            # Publish to all subscribers (all server instances)
            await redis.publish(f"room:{room_id}", msg)
            # Persist to DB
            await save_message(room_id, user_id, data)
    except WebSocketDisconnect:
        listener_task.cancel()
        del active_connections[user_id]
```

**Database Schema:**
```sql
CREATE TABLE rooms (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name        VARCHAR(255),
    type        VARCHAR(20),  -- 'direct', 'group'
    created_at  TIMESTAMP DEFAULT NOW()
);

CREATE TABLE messages (
    id          BIGSERIAL PRIMARY KEY,
    room_id     UUID REFERENCES rooms(id),
    sender_id   BIGINT REFERENCES users(id),
    content     TEXT,
    created_at  TIMESTAMP DEFAULT NOW()
) PARTITION BY RANGE (created_at);  -- Partition by month

CREATE INDEX idx_messages_room_time ON messages(room_id, created_at DESC);
```

---

# 7. Scenario-Based Questions

---

## Q33. SCENARIO: Your API response times increased 10x after a deploy

**Situation:** Post-deployment monitoring shows P99 latency jumped from 50ms to 500ms.

**Expected Thinking Process:**
```
1. Check if the deploy is the cause → rollback readiness
2. What changed in this deploy? → Code diff, config changes, dependencies
3. Is it all endpoints or specific ones?
4. Is it the DB, external APIs, or application code?
5. Can we mitigate without rollback?
```

**Strong Answer:**
```
1. Immediately check rollback feasibility and alert the team.

2. Compare the deploy diff:
   - New ORM query? (N+1 problem)
   - New synchronous external API call?
   - Missing index on new query?
   - Disabled cache?

3. Investigate with data:
   - EXPLAIN ANALYZE on new queries
   - Check external API call timing
   - Check Redis hit/miss ratio
   - Review pg_stat_activity for blocking queries

4. Most common root cause for this pattern:
   - A new feature made N+1 queries
   - A missing index on a newly queried column
   - An async operation was made synchronous

5. Fix: Add index, fix N+1, restore cache, or rollback
```

**Common Mistakes:**
- Jumping to rollback without understanding the root cause
- Not preserving the "broken" state for debugging
- Not communicating status to stakeholders during incident

---

## Q34. SCENARIO: Database is the bottleneck, reads are 10x writes

**Strong Answer:**
```python
# Solution: Read replicas + intelligent routing

class DatabaseRouter:
    def __init__(self):
        self.primary = create_engine(PRIMARY_DB_URL)
        self.replicas = [
            create_engine(REPLICA_1_URL),
            create_engine(REPLICA_2_URL),
        ]
        self._replica_index = 0

    def get_read_connection(self):
        # Round-robin across replicas
        replica = self.replicas[self._replica_index % len(self.replicas)]
        self._replica_index += 1
        return replica.connect()

    def get_write_connection(self):
        return self.primary.connect()

# FastAPI dependency
db_router = DatabaseRouter()

def get_read_db():
    return db_router.get_read_connection()

def get_write_db():
    return db_router.get_write_connection()

@app.get("/users")  # Read → replica
async def list_users(db = Depends(get_read_db)):
    return db.execute("SELECT * FROM users").fetchall()

@app.post("/users")  # Write → primary
async def create_user(user: UserCreate, db = Depends(get_write_db)):
    return db.execute("INSERT INTO users ...", user.dict())
```

**Additional strategies:**
1. **Redis cache** for frequently read data (user profiles, product catalog)
2. **CQRS** — separate read and write models entirely
3. **Read replicas** with streaming replication lag monitoring
4. **Connection pooling** (PgBouncer) between app and DB

---

# 8. Coding Round Questions

---

## Q35. Design a Rate Limiter API

```python
"""
Design an API endpoint that:
1. Limits users to 5 requests per minute
2. Returns remaining quota in headers
3. Supports per-user and per-IP limiting
"""
from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import JSONResponse
import redis.asyncio as aioredis
import time
from functools import wraps

app = FastAPI()

class RateLimiter:
    def __init__(self, redis_url="redis://localhost:6379"):
        self.redis = aioredis.from_url(redis_url)

    def limit(self, requests: int, window: int):
        """Decorator factory for rate limiting"""
        def decorator(func):
            @wraps(func)
            async def wrapper(request: Request, *args, **kwargs):
                # Use authenticated user ID or fall back to IP
                user_id = getattr(request.state, "user_id", None)
                identifier = f"user:{user_id}" if user_id else f"ip:{request.client.host}"
                key = f"rl:{func.__name__}:{identifier}"

                now = time.time()
                window_start = now - window

                async with self.redis.pipeline() as pipe:
                    pipe.zremrangebyscore(key, 0, window_start)
                    pipe.zadd(key, {str(now): now})
                    pipe.zcard(key)
                    pipe.expire(key, window)
                    _, _, count, _ = await pipe.execute()

                remaining = max(0, requests - count)
                reset_time = int(now + window)

                if count > requests:
                    raise HTTPException(
                        status_code=429,
                        detail=f"Rate limit exceeded. Retry after {window} seconds.",
                        headers={
                            "X-RateLimit-Limit": str(requests),
                            "X-RateLimit-Remaining": "0",
                            "X-RateLimit-Reset": str(reset_time),
                            "Retry-After": str(window),
                        }
                    )

                response = await func(request, *args, **kwargs)
                response.headers["X-RateLimit-Limit"] = str(requests)
                response.headers["X-RateLimit-Remaining"] = str(remaining - 1)
                response.headers["X-RateLimit-Reset"] = str(reset_time)
                return response
            return wrapper
        return decorator

limiter = RateLimiter()

@app.get("/api/search")
@limiter.limit(requests=5, window=60)
async def search(request: Request, q: str):
    return JSONResponse({"results": [], "query": q})
```

---

## Q36. Database Schema Design — E-commerce System

```sql
-- Design database for e-commerce with products, orders, payments

-- Users
CREATE TABLE users (
    id              BIGSERIAL PRIMARY KEY,
    email           VARCHAR(255) UNIQUE NOT NULL,
    username        VARCHAR(100) UNIQUE NOT NULL,
    password_hash   VARCHAR(255) NOT NULL,
    status          VARCHAR(20) DEFAULT 'active',
    created_at      TIMESTAMPTZ DEFAULT NOW(),
    updated_at      TIMESTAMPTZ DEFAULT NOW()
);

-- Products
CREATE TABLE categories (
    id      BIGSERIAL PRIMARY KEY,
    name    VARCHAR(100) NOT NULL,
    slug    VARCHAR(100) UNIQUE NOT NULL,
    parent_id BIGINT REFERENCES categories(id)
);

CREATE TABLE products (
    id              BIGSERIAL PRIMARY KEY,
    category_id     BIGINT REFERENCES categories(id),
    name            VARCHAR(500) NOT NULL,
    description     TEXT,
    price           NUMERIC(10, 2) NOT NULL,
    stock_quantity  INT NOT NULL DEFAULT 0,
    sku             VARCHAR(100) UNIQUE,
    status          VARCHAR(20) DEFAULT 'active',
    metadata        JSONB,
    created_at      TIMESTAMPTZ DEFAULT NOW()
);

-- Cart
CREATE TABLE carts (
    id          BIGSERIAL PRIMARY KEY,
    user_id     BIGINT REFERENCES users(id),
    session_id  VARCHAR(100),  -- For guest users
    expires_at  TIMESTAMPTZ,
    created_at  TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE cart_items (
    id          BIGSERIAL PRIMARY KEY,
    cart_id     BIGINT REFERENCES carts(id) ON DELETE CASCADE,
    product_id  BIGINT REFERENCES products(id),
    quantity    INT NOT NULL CHECK (quantity > 0),
    price       NUMERIC(10, 2) NOT NULL,  -- Snapshot price
    UNIQUE(cart_id, product_id)
);

-- Orders
CREATE TABLE orders (
    id              BIGSERIAL PRIMARY KEY,
    user_id         BIGINT REFERENCES users(id),
    status          VARCHAR(30) DEFAULT 'pending',
    subtotal        NUMERIC(10, 2) NOT NULL,
    tax             NUMERIC(10, 2) DEFAULT 0,
    shipping        NUMERIC(10, 2) DEFAULT 0,
    total           NUMERIC(10, 2) NOT NULL,
    shipping_addr   JSONB NOT NULL,
    idempotency_key VARCHAR(100) UNIQUE,  -- Prevent duplicate orders
    created_at      TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE order_items (
    id          BIGSERIAL PRIMARY KEY,
    order_id    BIGINT REFERENCES orders(id),
    product_id  BIGINT REFERENCES products(id),
    quantity    INT NOT NULL,
    unit_price  NUMERIC(10, 2) NOT NULL,
    total_price NUMERIC(10, 2) NOT NULL
);

-- Payments
CREATE TABLE payments (
    id              BIGSERIAL PRIMARY KEY,
    order_id        BIGINT REFERENCES orders(id),
    provider        VARCHAR(50) NOT NULL,  -- stripe, paypal
    provider_txn_id VARCHAR(200) UNIQUE,
    amount          NUMERIC(10, 2) NOT NULL,
    currency        CHAR(3) DEFAULT 'USD',
    status          VARCHAR(30) DEFAULT 'pending',
    metadata        JSONB,
    created_at      TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_products_status ON products(status) WHERE status = 'active';
CREATE INDEX idx_orders_user ON orders(user_id, created_at DESC);
CREATE INDEX idx_payments_order ON payments(order_id);
```

---

## Q37. Backend Machine Coding — Async Job Queue

```python
"""
Implement a simple in-memory job queue with:
- Priority levels (HIGH, MEDIUM, LOW)
- Worker pool
- Retry on failure
- Job status tracking
"""
import asyncio
import uuid
from enum import Enum
from dataclasses import dataclass, field
from typing import Callable, Any
from datetime import datetime

class Priority(int, Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3

class JobStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

@dataclass(order=True)
class Job:
    priority: Priority
    created_at: datetime = field(compare=False, default_factory=datetime.utcnow)
    id: str = field(compare=False, default_factory=lambda: str(uuid.uuid4()))
    func: Callable = field(compare=False, default=None)
    args: tuple = field(compare=False, default=())
    kwargs: dict = field(compare=False, default_factory=dict)
    max_retries: int = field(compare=False, default=3)
    retry_count: int = field(compare=False, default=0)
    status: JobStatus = field(compare=False, default=JobStatus.PENDING)
    result: Any = field(compare=False, default=None)
    error: str = field(compare=False, default=None)

class AsyncJobQueue:
    def __init__(self, workers: int = 5):
        self.queue = asyncio.PriorityQueue()
        self.jobs: dict[str, Job] = {}
        self.workers_count = workers
        self._running = False

    async def enqueue(self, func: Callable, *args, priority: Priority = Priority.MEDIUM,
                      max_retries: int = 3, **kwargs) -> str:
        job = Job(priority=priority, func=func, args=args,
                  kwargs=kwargs, max_retries=max_retries)
        self.jobs[job.id] = job
        await self.queue.put(job)
        return job.id

    async def get_status(self, job_id: str) -> dict:
        job = self.jobs.get(job_id)
        if not job:
            return {"error": "Job not found"}
        return {
            "id": job.id,
            "status": job.status,
            "result": job.result,
            "error": job.error,
            "retry_count": job.retry_count
        }

    async def _worker(self, worker_id: int):
        while self._running:
            try:
                job = await asyncio.wait_for(self.queue.get(), timeout=1.0)
                job.status = JobStatus.RUNNING
                print(f"Worker {worker_id} processing job {job.id}")

                try:
                    if asyncio.iscoroutinefunction(job.func):
                        job.result = await job.func(*job.args, **job.kwargs)
                    else:
                        job.result = job.func(*job.args, **job.kwargs)
                    job.status = JobStatus.COMPLETED
                except Exception as e:
                    job.retry_count += 1
                    if job.retry_count < job.max_retries:
                        job.status = JobStatus.PENDING
                        delay = 2 ** job.retry_count  # Exponential backoff
                        await asyncio.sleep(delay)
                        await self.queue.put(job)
                        print(f"Retrying job {job.id} (attempt {job.retry_count})")
                    else:
                        job.status = JobStatus.FAILED
                        job.error = str(e)

                self.queue.task_done()
            except asyncio.TimeoutError:
                continue

    async def start(self):
        self._running = True
        workers = [asyncio.create_task(self._worker(i))
                   for i in range(self.workers_count)]
        await asyncio.gather(*workers)

    async def stop(self):
        self._running = False

# Usage
queue = AsyncJobQueue(workers=3)

async def main():
    asyncio.create_task(queue.start())

    # Enqueue jobs
    id1 = await queue.enqueue(send_email, "user@example.com", priority=Priority.HIGH)
    id2 = await queue.enqueue(resize_image, "img.jpg", priority=Priority.LOW)

    # Check status
    await asyncio.sleep(2)
    print(await queue.get_status(id1))
```

---

## Q38. Optimization — Fix the N+1 Query Problem

```python
# ❌ N+1 Problem: 1 + N queries
@app.get("/orders")
async def get_orders_bad():
    orders = await db.fetch("SELECT * FROM orders WHERE status = 'pending'")
    result = []
    for order in orders:
        # Fires 1 query PER order (N queries!)
        user = await db.fetchrow("SELECT * FROM users WHERE id = $1", order["user_id"])
        result.append({**order, "user": user})
    return result
# 100 orders = 101 queries!

# ✅ Solution 1: JOIN
@app.get("/orders")
async def get_orders_join():
    rows = await db.fetch("""
        SELECT o.*, u.name as user_name, u.email as user_email
        FROM orders o
        JOIN users u ON o.user_id = u.id
        WHERE o.status = 'pending'
    """)
    return rows
# 1 query!

# ✅ Solution 2: Batch loading (for ORM)
@app.get("/orders")
async def get_orders_batch():
    orders = await db.fetch("SELECT * FROM orders WHERE status = 'pending'")
    user_ids = list({o["user_id"] for o in orders})

    users = await db.fetch("SELECT * FROM users WHERE id = ANY($1)", user_ids)
    users_by_id = {u["id"]: u for u in users}

    return [{**order, "user": users_by_id.get(order["user_id"])} for order in orders]
# 2 queries!

# ✅ Solution 3: SQLAlchemy eager loading
orders = (
    db.query(Order)
    .options(joinedload(Order.user))  # Eager load users
    .filter(Order.status == "pending")
    .all()
)
```

---

# 9. Behavioral Questions (STAR Format)

---

## Q39. Tell me about a time you improved system performance significantly.

### STAR Answer:

**Situation:**
> Our main product API had P99 latency of 3 seconds on the listings endpoint. Users were complaining and the conversion rate was dropping.

**Task:**
> I was tasked with reducing latency to under 500ms without a full rewrite.

**Action:**
```
1. Profiled the endpoint — discovered 3 issues:
   - N+1 query: 1 product fetch + 47 individual seller queries
   - No caching: Popular products fetched from DB every time
   - SELECT * returning 40+ columns, many unused

2. Fixed N+1 with JOIN query (47 queries → 1 query)

3. Added Redis cache:
   - Product listings cached for 5 minutes
   - Cache invalidated on product update via event

4. Added database index on (category_id, status, price)

5. Reduced SELECT columns from 40 to 8 needed ones
```

**Result:**
> P99 latency dropped from 3000ms to 180ms (94% improvement). DB load reduced by 60%. Cache hit rate reached 87%.

---

## Q40. Describe a time you handled a production incident.

### STAR Answer:

**Situation:**
> At 2 AM, our payment service started returning 500 errors for 30% of transactions. Revenue was impacting at ~$5k/minute.

**Task:**
> As on-call engineer, I needed to identify and resolve the issue with minimal customer impact.

**Action:**
```
1. Checked dashboards — saw DB connection pool exhausted

2. Root cause: A new background job deployed that afternoon
   was running a non-paginated query on 10M records,
   holding connections for 45 seconds each.

3. Immediate mitigation:
   - Disabled the background job via feature flag
   - Scaled up connection pool temporarily
   - Restarted affected pods to clear stuck connections

4. Permanent fix:
   - Added pagination to background job
   - Added connection timeout and circuit breaker
   - Added monitoring alert for pool exhaustion

5. Post-mortem: Documented timeline, root cause, and
   added the scenario to our staging load tests
```

**Result:**
> Incident resolved in 23 minutes. Added automated staging performance tests to catch similar issues before deploy.

---

## Q41. How do you handle technical disagreements with teammates?

### STAR Answer:

**Situation:**
> Senior engineer proposed using MongoDB for a financial transaction system. I believed PostgreSQL was more appropriate due to ACID requirements.

**Task:**
> Present my case without creating conflict, while being genuinely open to the other perspective.

**Action:**
```
1. Acknowledged the valid points of MongoDB (flexible schema,
   horizontal scaling).

2. Wrote a brief technical document comparing both:
   - ACID guarantees for financial data
   - PostgreSQL JSONB for flexibility if schema changes
   - MongoDB's eventual consistency risks for double-spending

3. Proposed a POC: implement a money transfer in both
   and compare correctness, performance, and developer experience.

4. After the POC, the team agreed PostgreSQL was the right
   choice. I also learned from my colleague's concern about
   schema flexibility and we used JSONB columns for metadata.
```

**Result:**
> Team alignment on the right tool. Created a decision doc that became our template for future DB selection discussions.

---

## 🏁 Final Tips for the Interview

### Before the Interview:
- [ ] Review your most impactful projects — have concrete metrics
- [ ] Practice `EXPLAIN ANALYZE` on PostgreSQL
- [ ] Implement a basic rate limiter and JWT auth from scratch
- [ ] Draw system designs on paper/whiteboard

### During the Interview:
- Clarify before you code — ask about scale, constraints, edge cases
- Think out loud — interviewers value your thought process
- Start simple, then optimize
- Mention trade-offs for every design decision

### Red Flags to Avoid:
- ❌ "We just used it because everyone uses it"
- ❌ Overcomplicating simple problems (not everything needs microservices)
- ❌ Ignoring security, validation, or error handling
- ❌ Hardcoding values that should be configurable
- ✅ Always mention: scalability, observability, security, and failure modes

---

## Q42. Tell me about the projects you've worked on.

> ⚠️ **Note**: This is your personal answer. Below is a **template framework** — fill in your actual project details.

### 🎯 Short Version (30 sec)
> I've worked on [2-3 key projects]. The most impactful was [Project X] where I built [core feature] that [measurable outcome]. I owned the backend architecture using [tech stack], handled [specific challenges], and delivered [result].

### 💬 Interview Answer Framework (STAR)

**Structure for each project:**
```
1. Context     — What was the product/company? What was the scale?
2. Your Role   — What did YOU specifically own?
3. Tech Stack  — FastAPI/Node, PostgreSQL, Redis, Docker, etc.
4. Challenge   — What was the hardest technical problem?
5. Solution    — How did you solve it?
6. Result      — Metrics: latency, throughput, uptime, users served
```

**Project 1 Template — Core API Platform:**
```
Context:
  "At [Company], I worked on [product description].
  The platform served [X] daily active users with [Y] requests/day."

Your Role:
  "I was the lead backend engineer responsible for [auth service /
   order system / notification pipeline]."

Tech Stack:
  "Built with FastAPI + PostgreSQL + Redis + Docker + AWS."

Challenge:
  "The biggest challenge was [scaling the notification system /
   reducing API latency / handling concurrent writes]."

Solution:
  "I [implemented Kafka-based async notifications /
   added Redis caching with a cache-aside pattern /
   introduced optimistic locking for inventory updates]."

Result:
  "This reduced [latency from 2s to 150ms /
   error rate from 5% to 0.1% /
   DB load by 60%]."
```

**Example Answer (fill with your details):**
```
"One of the most technically challenging projects I worked on was
building a multi-tenant SaaS platform at [Company].

The platform handled employee management for 200+ enterprise clients.
I was responsible for the backend API (FastAPI + PostgreSQL) and the
authentication layer.

The key challenge was implementing proper tenant isolation — each
client's data had to be strictly separated. I designed a row-level
security model in PostgreSQL where every query automatically filters
by tenant_id, enforced both at the API layer (JWT contains tenant_id)
and at the database layer (RLS policies).

I also built the async notification system using Celery + Redis to
handle bulk email campaigns without blocking the main API. This
allowed sending 100k emails without impacting API response times.

Result: The platform onboarded 50 new enterprise clients in 3 months,
API latency was under 100ms P99, and we had 99.95% uptime."
```

**Talking Points to Always Include:**
- **Scale numbers**: users, RPS, data volume
- **Your ownership**: "I designed", "I implemented", "I led"
- **Technical decisions with trade-offs**: Why did you choose X over Y?
- **Measurable outcomes**: latency, uptime, cost savings, user growth
- **Learnings**: What would you do differently?

### ❓ Follow-up Questions (expect these after your answer)
- What was the biggest technical mistake you made on this project?
- If you could redo this project, what would you change?
- How did you handle disagreements about technical direction?
- What was the most complex piece of code you wrote?
- How did you ensure reliability / handle failures?

### 💡 Senior-level Tips
> Interviewers are evaluating **ownership**, **impact**, and **technical depth**. Saying "we built" is weaker than "I designed the schema and led the implementation". Always tie your work to **business outcomes** — not just technical achievements.

---

## 🏁 Final Tips for the Interview

### Before the Interview:
- [ ] Review your most impactful projects — have concrete metrics
- [ ] Practice `EXPLAIN ANALYZE` on PostgreSQL
- [ ] Implement a basic rate limiter and JWT auth from scratch
- [ ] Draw system designs on paper/whiteboard
- [ ] Prepare 2-3 project stories with STAR format

### During the Interview:
- Clarify before you code — ask about scale, constraints, edge cases
- Think out loud — interviewers value your thought process
- Start simple, then optimize
- Mention trade-offs for every design decision

### Red Flags to Avoid:
- ❌ "We just used it because everyone uses it"
- ❌ Overcomplicating simple problems (not everything needs microservices)
- ❌ Ignoring security, validation, or error handling
- ❌ Hardcoding values that should be configurable
- ✅ Always mention: scalability, observability, security, and failure modes

---

*Good luck! You've got this. 🚀*
