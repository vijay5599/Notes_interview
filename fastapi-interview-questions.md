# FastAPI Interview Questions & Answers

> A comprehensive guide covering FastAPI fundamentals, advanced concepts, and production best practices.

---

## Table of Contents

1. [Basics & Core Concepts](#1-basics--core-concepts)
2. [Path & Query Parameters](#2-path--query-parameters)
3. [Request Body & Pydantic Models](#3-request-body--pydantic-models)
4. [Dependency Injection](#4-dependency-injection)
5. [Authentication & Security](#5-authentication--security)
6. [Async & Performance](#6-async--performance)
7. [Database Integration](#7-database-integration)
8. [Middleware & CORS](#8-middleware--cors)
9. [Background Tasks & Events](#9-background-tasks--events)
10. [Testing](#10-testing)
11. [Deployment & Production](#11-deployment--production)
12. [Advanced Topics](#12-advanced-topics)

---

## 1. Basics & Core Concepts

### Q1. What is FastAPI and what makes it different from Flask or Django?

**Answer:**

FastAPI is a modern, high-performance Python web framework for building APIs, released in 2018 by Sebastián Ramírez. It is built on top of **Starlette** (for the web layer) and **Pydantic** (for data validation).

| Feature | FastAPI | Flask | Django |
|---|---|---|---|
| Performance | Very High (async) | Moderate | Moderate |
| Type hints | Built-in, enforced | Optional | Optional |
| Auto docs | Yes (Swagger + ReDoc) | No (needs extension) | No (needs extension) |
| Async support | Native | Limited | Limited |
| Data validation | Pydantic (built-in) | Manual | Forms/Serializers |
| Learning curve | Low-Medium | Low | High |

Key differentiators:
- **Automatic API documentation** via OpenAPI (Swagger UI at `/docs` and ReDoc at `/redoc`)
- **Data validation and serialization** via Pydantic models
- **Native async support** from the ground up
- **Type inference** — return type hints become part of the response schema

---

### Q2. What are the core components/dependencies of FastAPI?

**Answer:**

- **Starlette** — ASGI framework providing routing, middleware, WebSocket support, request/response objects
- **Pydantic** — Data validation, serialization, settings management using Python type annotations
- **Uvicorn** — ASGI server (production server, often paired with Gunicorn)
- **python-multipart** — For form data and file uploads
- **python-jose / PyJWT** — JWT token handling (optional, for auth)

---

### Q3. What is ASGI and how does FastAPI use it?

**Answer:**

**ASGI (Asynchronous Server Gateway Interface)** is the spiritual successor to WSGI. It enables async communication between Python web applications and web servers.

- **WSGI** (Flask, Django) — synchronous, one request at a time per worker
- **ASGI** (FastAPI, Starlette) — asynchronous, can handle multiple concurrent connections without blocking

FastAPI is an ASGI application. It runs on ASGI servers like:
- **Uvicorn** — fast, recommended for development and production
- **Hypercorn** — supports HTTP/2
- **Daphne** — from Django Channels

```bash
# Running FastAPI with Uvicorn
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

---

### Q4. How do you create a basic FastAPI application?

**Answer:**

```python
from fastapi import FastAPI

app = FastAPI(
    title="My API",
    description="A sample FastAPI application",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}
```

Run with:
```bash
uvicorn main:app --reload
```

Auto docs available at:
- `http://localhost:8000/docs` — Swagger UI
- `http://localhost:8000/redoc` — ReDoc

---

### Q5. What HTTP methods does FastAPI support?

**Answer:**

FastAPI supports all standard HTTP methods as decorators:

```python
@app.get("/items")       # Read/Retrieve
@app.post("/items")      # Create
@app.put("/items/{id}")  # Full Update
@app.patch("/items/{id}")# Partial Update
@app.delete("/items/{id}")# Delete
@app.options("/items")   # Options (CORS preflight)
@app.head("/items")      # Like GET but no body
```

---

## 2. Path & Query Parameters

### Q6. What is the difference between path parameters and query parameters?

**Answer:**

**Path Parameters** — Part of the URL path, always required:
```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
# URL: /users/42
```

**Query Parameters** — Appended after `?`, can be optional:
```python
@app.get("/items")
def get_items(skip: int = 0, limit: int = 10, search: str = None):
    return {"skip": skip, "limit": limit, "search": search}
# URL: /items?skip=0&limit=10&search=laptop
```

FastAPI automatically distinguishes them based on whether they appear in the path string or as function parameters.

---

### Q7. How do you add validation to path and query parameters?

**Answer:**

Use `Path()` and `Query()` from `fastapi`:

```python
from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/items/{item_id}")
def get_item(
    item_id: int = Path(..., title="Item ID", ge=1, le=1000),
    q: str = Query(None, min_length=3, max_length=50, regex="^[a-zA-Z]+$")
):
    return {"item_id": item_id, "q": q}
```

Common validators:
- `ge` / `gt` — greater than or equal / greater than
- `le` / `lt` — less than or equal / less than
- `min_length` / `max_length` — for strings
- `regex` / `pattern` — regex pattern matching

---

### Q8. How do you handle optional parameters in FastAPI?

**Answer:**

Use `Optional` from `typing` or simply assign a default value of `None`:

```python
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_users(
    name: Optional[str] = None,
    active: bool = True,
    limit: int = 20
):
    return {"name": name, "active": active, "limit": limit}
```

In Python 3.10+, you can use the `|` union syntax:
```python
def get_users(name: str | None = None): ...
```

---

## 3. Request Body & Pydantic Models

### Q9. What is Pydantic and why is it important in FastAPI?

**Answer:**

**Pydantic** is a data validation and settings management library using Python type annotations. In FastAPI:

- **Request parsing** — Converts incoming JSON to Python objects and validates fields
- **Response serialization** — Converts Python objects to JSON
- **Schema generation** — Auto-generates OpenAPI/JSON Schema definitions
- **Error handling** — Returns structured validation error responses (422 Unprocessable Entity)

```python
from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int
    bio: Optional[str] = None

    @field_validator("age")
    @classmethod
    def validate_age(cls, v):
        if v < 18:
            raise ValueError("Must be at least 18")
        return v
```

---

### Q10. How do you use a Pydantic model as a request body?

**Answer:**

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_available: bool = True
    tags: list[str] = []

@app.post("/items/", status_code=201)
def create_item(item: Item):
    return {"created": item.model_dump()}
```

FastAPI automatically:
1. Reads the request body as JSON
2. Validates each field against the model
3. Returns `422` with clear error messages on validation failure

---

### Q11. What is the difference between `BaseModel` and `dataclasses` in Pydantic context?

**Answer:**

| Feature | Pydantic BaseModel | Python Dataclass |
|---|---|---|
| Validation | Yes (on assignment) | No by default |
| JSON serialization | `.model_dump()`, `.model_dump_json()` | Manual |
| Schema generation | Yes | Limited |
| Immutability | Via `model_config` | Via `frozen=True` |
| Performance | Slightly slower (validation overhead) | Faster |

FastAPI supports both, but `BaseModel` is preferred for API request/response models due to validation and serialization.

---

### Q12. How do you define nested models and model inheritance?

**Answer:**

**Nested Models:**
```python
from pydantic import BaseModel
from typing import List

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    name: str
    email: str
    address: Address
    tags: List[str] = []
```

**Model Inheritance:**
```python
class ItemBase(BaseModel):
    name: str
    price: float

class ItemCreate(ItemBase):
    pass  # Used for POST (no id)

class ItemRead(ItemBase):
    id: int
    class Config:
        from_attributes = True  # For ORM models (Pydantic v2)
```

---

### Q13. What are `response_model` and `response_model_exclude_unset`?

**Answer:**

`response_model` — Defines the shape of the response; FastAPI filters and validates the output:

```python
class UserOut(BaseModel):
    id: int
    name: str
    # email is intentionally excluded from response

@app.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: int):
    # Even if DB returns email, it won't be in the response
    return {"id": user_id, "name": "Alice", "email": "secret@example.com"}
```

`response_model_exclude_unset=True` — Excludes fields not explicitly set (avoids sending defaults):
```python
@app.patch("/users/{user_id}", response_model=UserOut, response_model_exclude_unset=True)
def update_user(user_id: int, user: UserUpdate):
    ...
```

---

## 4. Dependency Injection

### Q14. What is Dependency Injection in FastAPI and why use it?

**Answer:**

FastAPI has a built-in **Dependency Injection (DI)** system via `Depends()`. It allows you to declare shared logic (database sessions, auth, config) that gets automatically resolved before the route handler runs.

Benefits:
- **Reusability** — shared logic without repetition
- **Testability** — easily mock dependencies in tests
- **Clean code** — separates the "what" from the "how"
- **Composition** — dependencies can have their own dependencies

```python
from fastapi import FastAPI, Depends

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def common_pagination(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

@app.get("/items")
def get_items(
    pagination: dict = Depends(common_pagination),
    db = Depends(get_db)
):
    return pagination
```

---

### Q15. What is the difference between `Depends` and calling a function directly?

**Answer:**

| Aspect | `Depends()` | Direct call |
|---|---|---|
| Caching | Yes (per request, by default) | No |
| Sub-dependencies | Resolved automatically | Manual |
| Overridable in tests | Yes, via `app.dependency_overrides` | No |
| Lifecycle management | Supports `yield` for cleanup | No |

`Depends` with `use_cache=False`:
```python
# Forces fresh resolution even if the same dependency is used multiple times
Depends(get_db, use_cache=False)
```

---

### Q16. How do you override dependencies in tests?

**Answer:**

```python
from fastapi.testclient import TestClient
from main import app, get_db

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_read_items():
    response = client.get("/items")
    assert response.status_code == 200
```

---

## 5. Authentication & Security

### Q17. How do you implement JWT authentication in FastAPI?

**Answer:**

```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return username

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # validate user credentials from DB
    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/me")
def read_me(current_user: str = Depends(get_current_user)):
    return {"user": current_user}
```

---

### Q18. What security utilities does FastAPI provide out of the box?

**Answer:**

FastAPI (via Starlette) provides several security schemes under `fastapi.security`:

| Class | Use Case |
|---|---|
| `OAuth2PasswordBearer` | Bearer token from form login |
| `OAuth2AuthorizationCodeBearer` | OAuth2 authorization code flow |
| `HTTPBasic` | Basic HTTP authentication |
| `HTTPBearer` | Raw Bearer token |
| `APIKeyHeader` | API key in header |
| `APIKeyQuery` | API key in query param |
| `APIKeyCookie` | API key in cookie |

```python
from fastapi.security import APIKeyHeader

api_key_header = APIKeyHeader(name="X-API-Key")

@app.get("/secure")
def secure_route(api_key: str = Depends(api_key_header)):
    if api_key != "my-secret-key":
        raise HTTPException(status_code=403)
    return {"status": "authorized"}
```

---

## 6. Async & Performance

### Q19. When should you use `async def` vs `def` in FastAPI?

**Answer:**

| Scenario | Use |
|---|---|
| I/O bound (DB, HTTP calls, file I/O) | `async def` |
| CPU bound (image processing, ML inference) | `def` (runs in thread pool) |
| Calling sync libraries (SQLAlchemy sync, requests) | `def` |
| Calling async libraries (httpx, asyncpg, motor) | `async def` |

```python
import httpx

@app.get("/sync")
def sync_route():
    # FastAPI runs this in a thread pool — safe for blocking calls
    return {"type": "sync"}

@app.get("/async")
async def async_route():
    async with httpx.AsyncClient() as client:
        resp = await client.get("https://api.example.com/data")
    return resp.json()
```

> ⚠️ **Warning:** Never call blocking I/O inside `async def` — it blocks the entire event loop. Use `asyncio.to_thread()` or `run_in_executor()` if needed.

---

### Q20. What is `asyncio.to_thread()` and when would you use it?

**Answer:**

`asyncio.to_thread()` runs a blocking synchronous function in a separate thread without blocking the event loop.

```python
import asyncio

def blocking_task(data: str) -> str:
    # Simulates a CPU-heavy or blocking sync operation
    import time
    time.sleep(2)
    return f"Processed: {data}"

@app.get("/process")
async def process(data: str):
    result = await asyncio.to_thread(blocking_task, data)
    return {"result": result}
```

Use when you must call a sync library (e.g., `boto3`, `PIL`) from an async context.

---

## 7. Database Integration

### Q21. How do you integrate SQLAlchemy with FastAPI?

**Answer:**

```python
# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:password@localhost/dbname"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db  # Dependency that provides and closes DB session
    finally:
        db.close()
```

```python
# models.py
from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
```

```python
# main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
import models

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
```

---

### Q22. How do you use async SQLAlchemy (async ORM) with FastAPI?

**Answer:**

```python
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+asyncpg://user:password@localhost/dbname"

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

@app.get("/users/{user_id}")
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404)
    return user
```

---

### Q23. How do you run database migrations with Alembic in FastAPI?

**Answer:**

```bash
# Install Alembic
pip install alembic

# Initialize Alembic
alembic init alembic
```

In `alembic/env.py`, configure the target metadata:
```python
from models import Base
target_metadata = Base.metadata
```

```bash
# Create a new migration
alembic revision --autogenerate -m "create users table"

# Apply migrations
alembic upgrade head

# Rollback one step
alembic downgrade -1
```

---

## 8. Middleware & CORS

### Q24. How do you add middleware in FastAPI?

**Answer:**

**Using `@app.middleware("http")` decorator:**
```python
import time
from fastapi import Request

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
```

**Using `app.add_middleware()`:**
```python
from starlette.middleware.base import BaseHTTPMiddleware

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        print(f"Request: {request.method} {request.url}")
        response = await call_next(request)
        print(f"Response status: {response.status_code}")
        return response

app.add_middleware(LoggingMiddleware)
```

---

### Q25. How do you configure CORS in FastAPI?

**Answer:**

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://myfrontend.com", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)
```

> ⚠️ In production, avoid `allow_origins=["*"]` when `allow_credentials=True` — browsers will reject it.

---

## 9. Background Tasks & Events

### Q26. What are Background Tasks in FastAPI and how do you use them?

**Answer:**

Background Tasks allow you to run functions after the response has been sent, without blocking the response.

```python
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def send_welcome_email(email: str):
    # Simulate sending email (blocking is OK here)
    print(f"Sending email to {email}...")

@app.post("/register")
def register_user(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_welcome_email, email)
    return {"message": "User registered successfully"}
```

> 📝 Background tasks run in the **same process** after the response — not in a separate worker. For heavy work, use Celery or ARQ.

---

### Q27. How do you handle startup and shutdown events in FastAPI?

**Answer:**

**Using lifespan (recommended in FastAPI 0.93+):**
```python
from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code before yield runs at startup
    print("Application starting up...")
    db_pool = await create_db_pool()
    app.state.db_pool = db_pool
    yield
    # Code after yield runs at shutdown
    await db_pool.close()
    print("Application shutting down...")

app = FastAPI(lifespan=lifespan)
```

**Old approach (deprecated):**
```python
@app.on_event("startup")
async def startup():
    ...

@app.on_event("shutdown")
async def shutdown():
    ...
```

---

## 10. Testing

### Q28. How do you test FastAPI applications?

**Answer:**

FastAPI provides `TestClient` (built on `httpx`):

```python
# test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_create_item():
    response = client.post(
        "/items/",
        json={"name": "Widget", "price": 9.99}
    )
    assert response.status_code == 201
    assert response.json()["created"]["name"] == "Widget"
```

Run tests:
```bash
pytest tests/ -v
```

---

### Q29. How do you test async endpoints in FastAPI?

**Answer:**

Use `pytest-asyncio` and `httpx.AsyncClient`:

```python
import pytest
import httpx
from main import app

@pytest.mark.asyncio
async def test_async_endpoint():
    async with httpx.AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/async-endpoint")
    assert response.status_code == 200
```

Install dependencies:
```bash
pip install pytest pytest-asyncio httpx
```

---

## 11. Deployment & Production

### Q30. How do you deploy FastAPI in production?

**Answer:**

**Recommended production setup:**

```bash
# Install Gunicorn with Uvicorn workers
pip install gunicorn uvicorn[standard]

# Run with multiple workers
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

**Dockerfile example:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
```

**Number of workers rule of thumb:**
```
workers = (2 × CPU_cores) + 1
```

---

### Q31. How do you manage configuration/settings in FastAPI?

**Answer:**

Use Pydantic's `BaseSettings` for environment-based config:

```python
# config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    debug: bool = False
    allowed_hosts: list[str] = ["*"]

    class Config:
        env_file = ".env"

settings = Settings()
```

```python
# main.py
from config import settings
from functools import lru_cache
from fastapi import Depends

@lru_cache()
def get_settings():
    return Settings()

@app.get("/info")
def info(settings: Settings = Depends(get_settings)):
    return {"debug": settings.debug}
```

Using `lru_cache` ensures settings are loaded only once.

---

## 12. Advanced Topics

### Q32. How do you handle file uploads in FastAPI?

**Answer:**

```python
from fastapi import FastAPI, File, UploadFile
from typing import List

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(contents)
    }

@app.post("/upload/multiple/")
async def upload_multiple(files: List[UploadFile] = File(...)):
    return [{"filename": f.filename} for f in files]
```

To save the file:
```python
import shutil

@app.post("/upload/save/")
async def save_file(file: UploadFile = File(...)):
    with open(f"uploads/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"saved": file.filename}
```

---

### Q33. How do you implement WebSockets in FastAPI?

**Answer:**

```python
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Client #{client_id}: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
```

---

### Q34. How do you add custom exception handlers?

**Answer:**

```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

class ItemNotFoundException(Exception):
    def __init__(self, item_id: int):
        self.item_id = item_id

@app.exception_handler(ItemNotFoundException)
async def item_not_found_handler(request: Request, exc: ItemNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"detail": f"Item with id {exc.item_id} not found"}
    )

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id > 100:
        raise ItemNotFoundException(item_id=item_id)
    return {"item_id": item_id}
```

Override default validation error handler:
```python
from fastapi.exceptions import RequestValidationError

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"errors": exc.errors(), "body": exc.body}
    )
```

---

### Q35. How do you use `APIRouter` for organizing large applications?

**Answer:**

```python
# routers/users.py
from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
def list_users():
    return [{"id": 1, "name": "Alice"}]

@router.get("/{user_id}")
def get_user(user_id: int):
    return {"id": user_id}
```

```python
# main.py
from fastapi import FastAPI
from routers import users, items, auth

app = FastAPI()

app.include_router(users.router)
app.include_router(items.router, prefix="/api/v1")
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
```

---

### Q36. How does FastAPI handle versioning?

**Answer:**

**Option 1: URL prefix versioning (most common)**
```python
from fastapi import FastAPI
from routers.v1 import users as users_v1
from routers.v2 import users as users_v2

app = FastAPI()
app.include_router(users_v1.router, prefix="/api/v1")
app.include_router(users_v2.router, prefix="/api/v2")
```

**Option 2: Multiple app instances with mounting**
```python
from fastapi import FastAPI

app_v1 = FastAPI()
app_v2 = FastAPI()

app = FastAPI()
app.mount("/v1", app_v1)
app.mount("/v2", app_v2)
```

---

### Q37. What is `status_code` and how do you use custom status codes?

**Answer:**

```python
from fastapi import FastAPI, status

app = FastAPI()

@app.post("/items/", status_code=status.HTTP_201_CREATED)
def create_item(name: str):
    return {"name": name}

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    return None  # 204 has no body

# Using Response object for dynamic status codes
from fastapi import Response

@app.get("/dynamic")
def dynamic_status(response: Response):
    response.status_code = 202
    return {"status": "accepted"}
```

---

### Q38. How do you stream large responses in FastAPI?

**Answer:**

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()

async def fake_data_streamer():
    for i in range(10):
        yield f"data chunk {i}\n"
        await asyncio.sleep(0.1)

@app.get("/stream")
async def stream_data():
    return StreamingResponse(fake_data_streamer(), media_type="text/plain")

# Streaming a file
@app.get("/download/{filename}")
async def download_file(filename: str):
    def iterfile():
        with open(f"files/{filename}", "rb") as f:
            yield from f
    return StreamingResponse(iterfile(), media_type="application/octet-stream")
```

---

### Q39. What is the difference between `JSONResponse`, `HTMLResponse`, and `Response`?

**Answer:**

| Class | Use Case | Default Content-Type |
|---|---|---|
| `JSONResponse` | JSON data (default) | `application/json` |
| `HTMLResponse` | HTML pages | `text/html` |
| `PlainTextResponse` | Plain text | `text/plain` |
| `RedirectResponse` | URL redirects | N/A |
| `StreamingResponse` | Large files/streams | configurable |
| `FileResponse` | Static file download | auto-detected |
| `Response` | Full control | configurable |

```python
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse

@app.get("/html", response_class=HTMLResponse)
def html_page():
    return "<h1>Hello HTML</h1>"

@app.get("/redirect")
def redirect():
    return RedirectResponse(url="/new-url", status_code=301)

@app.get("/file")
def get_file():
    return FileResponse("report.pdf", filename="report.pdf")
```

---

### Q40. How do you implement rate limiting in FastAPI?

**Answer:**

Using `slowapi` (based on Flask-Limiter):

```python
from fastapi import FastAPI, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.get("/limited")
@limiter.limit("5/minute")
async def limited_route(request: Request):
    return {"message": "You're within the rate limit"}
```

---

## Quick Reference Cheat Sheet

```python
# Common status codes
status.HTTP_200_OK
status.HTTP_201_CREATED
status.HTTP_204_NO_CONTENT
status.HTTP_400_BAD_REQUEST
status.HTTP_401_UNAUTHORIZED
status.HTTP_403_FORBIDDEN
status.HTTP_404_NOT_FOUND
status.HTTP_422_UNPROCESSABLE_ENTITY
status.HTTP_500_INTERNAL_SERVER_ERROR

# Common imports
from fastapi import FastAPI, Depends, HTTPException, status, Request, Response
from fastapi import Path, Query, Body, File, Form, Header, Cookie, UploadFile
from fastapi import BackgroundTasks, WebSocket
from fastapi.security import OAuth2PasswordBearer, HTTPBearer, APIKeyHeader
from fastapi.responses import JSONResponse, HTMLResponse, StreamingResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, field_validator, EmailStr
```

---

*Good luck with your interview! 🚀*
