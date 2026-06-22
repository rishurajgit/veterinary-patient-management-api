# Veterinary Patient Management API

A FastAPI-based REST API for managing veterinary patients, owners, visits, and clinic operations using PostgreSQL, SQLAlchemy, JWT Authentication, Alembic, and Docker.

---

# Features

## Authentication

* User Registration
* User Login
* JWT Token Authentication
* Protected Routes
* Current User Context Endpoint

## Pet Management

* Create Pet
* Get Pet By ID
* Get All Pets
* Update Pet
* Soft Delete Pet
* Filtering, Search, Sorting & Pagination

## Owner Management

* Create Owner
* Get Owner
* Update Owner
* Delete Owner

## Visit Management

* Create Visit
* Update Visit
* Delete Visit
* Retrieve Visit History

## Additional Features

* PostgreSQL Database
* SQLAlchemy ORM
* Alembic Migrations
* Structured Logging
* Global Exception Handling
* Docker Support
* Environment Variables Configuration

---

# Project Setup

## Clone Repository

```bash
git clone <repository-url>
cd veterinary-patient-management-api
```

## Install Dependencies

Using UV:

```bash
uv sync
```

or

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://username:password@host/database

JWT_SECRET_KEY=your_secret_key

JWT_ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Variable Definitions

| Variable                    | Description                           |
| --------------------------- | ------------------------------------- |
| DATABASE_URL                | PostgreSQL database connection string |
| JWT_SECRET_KEY              | Secret key used for JWT token signing |
| JWT_ALGORITHM               | JWT encryption algorithm              |
| ACCESS_TOKEN_EXPIRE_MINUTES | Token expiration time                 |

---

# Neon PostgreSQL Setup

1. Create a Neon account.
2. Create a new PostgreSQL project.
3. Copy the connection string.
4. Paste it into:

```env
DATABASE_URL=
```

inside `.env`.

---

# Alembic Migration Guide

Create Migration:

```bash
alembic revision --autogenerate -m "migration_name"
```

Apply Migration:

```bash
alembic upgrade head
```

Check Current Revision:

```bash
alembic current
```

Migration History:

```bash
alembic history
```

---

# Run Application

```bash
uv run uvicorn main:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```text
http://127.0.0.1:8000/redoc
```

---

# Docker Setup

## Build Docker Image

```bash
docker build -t vet-api .
```

## Run Docker Container

```bash
docker run --env-file .env -p 8000:8000 vet-api
```

## Verify Container

```bash
docker ps
```

---

# Authentication Flow

## Register User

```http
POST /register
```

Creates a new user.

## Login

```http
POST /login
```

Returns JWT access token.

## Authorize

Click "Authorize" in Swagger UI and paste:

```text
Bearer <token>
```

## User Context

```http
GET /auth/user-context
```

Returns currently authenticated user information.

---

# API Endpoint Map

## Authentication

```http
POST /register
POST /login
GET /auth/user-context
```

## Owners

```http
POST /owners
GET /owners
GET /owners/{id}
PUT /owners/{id}
DELETE /owners/{id}
```

## Pets

```http
POST /pets
GET /pets
GET /pets/{id}
PUT /pets/{id}
DELETE /pets/{id}
```

## Visits

```http
POST /pets/{id}/visits
PUT /visits/{id}
DELETE /visits/{id}
```

---

# Logging

The application logs:

* Request Method
* Endpoint
* Status Code
* Execution Time
* Startup Events
* Shutdown Events
* Authentication Failures
* Unhandled Exceptions

---

# Error Response Format

```json
{
  "success": false,
  "message": "Error description"
}
```

---

# Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* Pydantic
* JWT
* Passlib
* Docker
* Uvicorn
* Python 3.13

```
```
