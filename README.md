#  Employee Management System (Django REST Framework)

##  Overview

A scalable and production-ready backend system built using Django REST Framework that manages employees, departments, and attendance with secure JWT-based authentication.

This project demonstrates real-world backend architecture including authentication, relational data handling, and business logic implementation.

---

##  Features

###  Authentication

* User Registration & Login
* JWT-based Authentication (Access & Refresh Tokens)
* Secure API endpoints with authentication

### 👨‍💼 Employee Management

* Create, update, delete, and view employees
* One-to-one mapping with user accounts
* Employee-specific data access

###  Department Management

* Create and manage departments
* Admin-only access for modification
* Integrated with Employee module

###  Attendance System

* Daily attendance tracking
* Automatic employee mapping (no manual ID input)
* One attendance per day constraint
* Check-in & Check-out functionality
* Late detection based on check-in time

---

##  Key Concepts Implemented

* RESTful API design
* Nested serializers
* JWT Authentication (Simple JWT)
* Role-based access control using `is_staff`
* One-to-One and ForeignKey relationships
* Custom business logic (attendance rules)
* Data validation and constraints

---

##  Tech Stack

* Python
* Django
* Django REST Framework
* Simple JWT
* SQLite (development)

---

## 📂 Project Structure

```
company_api/
│
├── accounts/        # Authentication & user management
├── employees/       # Employee module
├── departments/     # Department module
├── attendence/      # Attendance module
├── company_api/     # Main project settings
├── manage.py
```

---

## 🔗 API Endpoints

### Authentication

* `POST /api/register/`
* `POST /api/login/`

### Employee

* `GET /api/employees/`
* `POST /api/employees/`

### Department

* `GET /api/departments/`
* `POST /api/departments/`

### Attendance

* `POST /api/attendance/`
* `PATCH /api/attendance/{id}/checkout/`

---

##  Setup Instructions

```bash
# Clone the repository
git clone https://github.com/your-username/restful-employee-management-system.git

# Navigate to project
cd company_api

# Create virtual environment
python -m venv env

# Activate environment
env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run server
python manage.py runserver
```

---

##  Future Enhancements

* Monthly attendance reports
* Role-based user system (Admin/Employee roles)
* Pagination & filtering
* Deployment on cloud (AWS/Render)

---

##  Author

Yash Jaiswal

---

##  If you like this project

Give it a star ⭐ on GitHub!
