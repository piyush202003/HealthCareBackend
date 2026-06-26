# Hospital Management REST API

A RESTful API built using **Django**, **Django REST Framework**, **PostgreSQL**, and **JWT Authentication** for managing patients, doctors, and patient-doctor assignments.

## Features

* User Registration
* JWT Authentication
* Patient Management (CRUD)
* Doctor Management (CRUD)
* Patient-Doctor Mapping
* PostgreSQL Database
* Django REST Framework
* JWT Authentication using Simple JWT

---

## Tech Stack

* Python 3.x
* Django
* Django REST Framework
* PostgreSQL
* Simple JWT
* uv (Package Manager)

---

## Project Structure

```
hospital_management/
│
├── accounts/
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── patients/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── doctors/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── mappings/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── hospital_management/
│   ├── settings.py
│   └── urls.py
│
├── manage.py
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd hospital_management
```

### Create Virtual Environment

Using uv:

```bash
uv venv
```

Activate the virtual environment.

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
uv sync
```

or

```bash
uv pip install -r requirements.txt
```

---

## Configure PostgreSQL

Create a PostgreSQL database.

Example:

```sql
CREATE DATABASE hospital_db;
```

Update the `DATABASES` configuration in `settings.py`.

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "hospital_db",
        "USER": "postgres",
        "PASSWORD": "your_password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

---

## Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Create Superuser

```bash
python manage.py createsuperuser
```

---

## Run Server

```bash
python manage.py runserver
```

Server:

```
http://127.0.0.1:8000/
```

---

# Authentication

Authentication is implemented using **JWT (JSON Web Token)**.

Include the access token in every protected request.

```
Authorization: Bearer <access_token>
```

---

# API Endpoints

## Authentication

| Method | Endpoint              | Description                     |
| ------ | --------------------- | ------------------------------- |
| POST   | `/api/auth/register/` | Register a new user             |
| POST   | `/api/auth/login/`    | Login user and obtain JWT token |

---

## Patient APIs

| Method | Endpoint              | Description                    |
| ------ | --------------------- | ------------------------------ |
| POST   | `/api/patients/`      | Create Patient                 |
| GET    | `/api/patients/`      | List Logged-in User's Patients |
| GET    | `/api/patients/<id>/` | Retrieve Patient               |
| PUT    | `/api/patients/<id>/` | Update Patient                 |
| DELETE | `/api/patients/<id>/` | Delete Patient                 |

---

## Doctor APIs

| Method | Endpoint             | Description     |
| ------ | -------------------- | --------------- |
| POST   | `/api/doctors/`      | Create Doctor   |
| GET    | `/api/doctors/`      | List Doctors    |
| GET    | `/api/doctors/<id>/` | Retrieve Doctor |
| PUT    | `/api/doctors/<id>/` | Update Doctor   |
| DELETE | `/api/doctors/<id>/` | Delete Doctor   |

---

## Patient-Doctor Mapping APIs

| Method | Endpoint                      | Description                     |
| ------ | ----------------------------- | ------------------------------- |
| POST   | `/api/mappings/`              | Assign Doctor to Patient        |
| GET    | `/api/mappings/`              | List All Mappings               |
| GET    | `/api/mappings/<patient_id>/` | Get Doctors Assigned to Patient |
| DELETE | `/api/mappings/<mapping_id>/` | Remove Doctor from Patient      |

> **Note:** Since both patient IDs and mapping IDs are integers, you may need to use distinct URL patterns (for example, `/api/mappings/patient/<patient_id>/` and `/api/mappings/<mapping_id>/`) to avoid routing conflicts.

---

# Sample Login Request

```http
POST /api/auth/login/
```

```json
{
    "username": "admin",
    "password": "password123"
}
```

Response

```json
{
    "refresh": "refresh_token",
    "access": "access_token"
}
```

---

# Sample Protected Request

```
GET /api/patients/
```

Headers

```
Authorization: Bearer <access_token>
```

---

# Database Models

## Patient

* first_name
* last_name
* age
* gender
* phone
* address
* created_by

---

## Doctor

* first_name
* last_name
* specialization
* experience
* phone
* email
* created_by

---

## PatientDoctorMapping

* patient
* doctor
* assigned_at

---

# Authentication Flow

```
Register
      │
      ▼
Login
      │
      ▼
Receive JWT Token
      │
      ▼
Access Protected APIs
      │
      ▼
Manage Patients, Doctors and Mappings
```

---

# Future Improvements

* Custom User Model
* Pagination
* Search & Filtering
* Swagger/OpenAPI Documentation
* Docker Support
* Unit Testing
* CI/CD Pipeline
* Role-Based Access Control (Admin/Doctor/Receptionist)

---

# Author

Developed using Django REST Framework and PostgreSQL.
