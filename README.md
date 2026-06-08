# veterinary-patient-management-api
A FastAPI-based REST API for managing veterinary patients, visit records, and clinic operations using SQLAlchemy and SQLite.
## Features

- Register new pets
- Retrieve pet information
- Update pet details
- Delete pet records
- Create visit records for pets
- View complete visit history
- Input validation using Pydantic
- SQLite database persistence
- RESTful API design

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

## API Endpoints

### Pet Management
- POST /pets
- GET /pets
- GET /pets/{id}
- PUT /pets/{id}
- DELETE /pets/{id}

### Visit Management
- POST /pets/{id}/visits
- GET /pets/{id}/visits
