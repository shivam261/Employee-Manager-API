# 🧩 Employee-Manager API

A scalable, production-ready REST API built with **Flask** that manages employees and their managers. It is designed using clean architecture principles like the **Factory pattern**, **Repository-Service pattern**, and includes modern backend features like **Redis caching**, **rate limiting**, and **Dockerized deployment**.

---

## 🚀 Features

- ✅ CRUD operations for **Employees** and **Managers**
- 🔁 Employees can **join or leave** managers
- 💾 **PostgreSQL** for persistent data storage
- 📦 **Redis** for caching and rate-limiting
- 🚦 Rate limiting via `Flask-Limiter` (Redis backend)
- 🧠 **Factory Pattern** used for app creation (`create_app`)
- 🧱 **Repository + Service Pattern** for clean separation of concerns
- 🐳 Fully containerized with **multi-stage Docker build**
- ⚡ Automatic database migrations on container startup (`flask db upgrade`)
- 📄 RESTful route structure with modular Blueprints
- ☁️ Redis can be self-hosted or cloud-hosted (e.g., Redis Cloud)

---

## 📦 Tech Stack

| Layer         | Tool/Library           |
|---------------|------------------------|
| Framework     | Flask                  |
| ORM           | SQLAlchemy             |
| DB Migrations | Alembic + Flask-Migrate|
| DB            | PostgreSQL             |
| Cache / Limit | Redis                  |
| Patterns      | Factory, Repository, Service |
| Container     | Docker (multi-stage)   |
| WSGI Server   | Gunicorn               |

---

## 📂 Folder Structure

```
├── app/
│ ├── models/ # SQLAlchemy models
│ ├── controllers/ # Handles HTTP requests
│ ├── services/ # Business logic
│ ├── repositories/ # Data access layer
│ ├── routes/ # Blueprint registrations
│ └── init.py # create_app() - Factory pattern
├── run.py # App entrypoint
├── migration
├── venv
├── entrypoint.sh # Runs migration & starts Gunicorn
├── requirements.txt
├── Dockerfile # Multi-stage build
├── docker-compose.yml
├── production.env
├── .gitignore
├── .dockerignonre
├── run.py
└── README.md


```
## Setup up enviroment
```
FLASK_ENV=production
SECRET_KEY=supersecretkey
FLASK_APP=run.py
POSTGRES_URL=postgresql://admin:admin@db:5432/gron
REDIS_HOST=your_redis_host
REDIS_PORT=your_redis_port
REDIS_PASSWORD=your_redis_password
```

## Build and Run
```
docker-compose up --build

```
## 🧠 Architectural Patterns

## 🏗️ Factory Pattern

`create_app()` initializes extensions and blueprints modularly.

---

### 🪝 Repository-Service Pattern

- **Repository** handles all DB logic (via SQLAlchemy).
- **Service** contains business rules and validation logic.
- Keeps controllers clean and focused only on routing.
---
### ⚙️ Rate Limiting + Caching

Redis powers both key performance and security mechanisms:

- **Rate Limiting**: Prevents API abuse by limiting traffic (e.g., 10 requests/minute for employee endpoints, 20/minute for manager endpoints).
- **Response Caching**: Frequently accessed data (e.g., list of employees) is cached in Redis for improved response time and reduced DB load.

---

### 📈 Scalability Considerations

The system is designed to be cloud-native and scalable:

- 🐳 **Stateless Docker container**: Easily deployable to cloud platforms like **AWS**, **GCP**, **Azure**, or **Kubernetes** clusters.
- ☁️ **Externalized services**: Redis and PostgreSQL are decoupled and can be scaled independently (e.g., using Redis Cloud or AWS RDS).
- 🧱 **Clean architecture**: Layered structure promotes easier testing, refactoring, and team collaboration.

---