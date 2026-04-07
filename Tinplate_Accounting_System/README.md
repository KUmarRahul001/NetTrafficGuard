# Tinplate Accounting System — Complete System Design

*(Zoho Books–style Web & Mobile Accounting Platform)*

---

# 1. Project Overview

The **Tinplate Accounting System** is a **web and mobile-based accounting platform** designed for small businesses, training centers, and SMEs. The system will allow users to manage:

* Financial accounting
* Invoices
* GST reports
* Inventory
* Customer/vendor management
* Financial dashboards
* Mobile access for business owners

The system architecture must support:

* Multi-user access
* Secure financial data storage
* Real-time reporting
* Web + Mobile synchronization
* Future scalability

---

# 2. Technology Stack

| Layer           | Technology                     |
| --------------- | ------------------------------ |
| Web Frontend    | React (Next.js or Vite)        |
| Mobile App      | Flutter                        |
| Backend API     | Django + Django REST Framework |
| Database        | PostgreSQL                     |
| Authentication  | JWT                            |
| Caching         | Redis                          |
| File Storage    | AWS S3 / Local Storage         |
| Message Queue   | RabbitMQ / Celery              |
| DevOps          | Docker                         |
| Version Control | Git                            |
| CI/CD           | GitHub Actions                 |

---

# 3. High Level Architecture (HLD)

## System Architecture

```text
                +----------------------+
                |   Mobile App (Flutter)|
                +----------+-----------+
                           |
                           |
                +----------v-----------+
                |    API Gateway       |
                +----------+-----------+
                           |
        +------------------+------------------+
        |                  |                  |
+-------v-------+  +-------v-------+  +-------v-------+
| Auth Service  |  | Accounting    |  | Inventory     |
|               |  | Service       |  | Service       |
+-------+-------+  +-------+-------+  +-------+-------+
        |                  |                  |
        +------------------+------------------+
                           |
                    +------v------+
                    | PostgreSQL  |
                    | Database    |
                    +-------------+

        +-----------------------------+
        | Redis Cache                 |
        +-----------------------------+

        +-----------------------------+
        | Message Queue (Celery)      |
        +-----------------------------+
```

---

# 4. System Components

## 4.1 Frontend (Web)

Technology: **React**

Responsibilities:

* Dashboard
* Forms
* Financial reports
* Invoice generation
* Charts
* User management UI

Libraries:

```text
React
Redux / Zustand
Axios
Chart.js
TailwindCSS
```

---

## 4.2 Mobile Application

Technology: **Flutter**

Features:

* Invoice creation
* Expense tracking
* Dashboard analytics
* Customer management
* Notifications

Architecture:

```text
Flutter App
   |
   +--- Screens
   +--- Services
   +--- API Layer
   +--- Local Storage
```

---

## 4.3 Backend (Django)

Framework:

```text
Django
Django REST Framework
Celery
Redis
JWT Authentication
```

Modules:

```text
authentication
users
accounting
invoices
inventory
reports
notifications
audit_logs
```

---

# 5. Folder Structure

```text
Tinplate_Accounting_System

backend
│
├── core
├── authentication
├── accounting
├── invoices
├── inventory
├── reports
├── notifications
└── audit_logs

frontend
│
├── components
├── pages
├── services
└── store

mobile_app
│
├── screens
├── services
├── models
└── utils

docs
devops
scripts
```

---

# 6. Database Design

## Main Tables

### Users

```text
users
------
id
name
email
password
role
created_at
```

---

### Companies

```text
companies
---------
id
company_name
gst_number
address
owner_id
```

---

### Customers

```text
customers
---------
id
name
email
phone
company_id
```

---

### Invoices

```text
invoices
--------
id
invoice_number
customer_id
date
total_amount
status
```

---

### Invoice Items

```text
invoice_items
-------------
id
invoice_id
product_id
quantity
price
total
```

---

### Products

```text
products
--------
id
name
price
stock
company_id
```

---

### Ledger

```text
ledger_entries
--------------
id
account_name
debit
credit
transaction_date
```

---

# 7. API Design

## Authentication APIs

```text
POST /api/auth/register
POST /api/auth/login
POST /api/auth/logout
GET  /api/auth/profile
```

---

## Invoice APIs

```text
POST /api/invoices/create
GET  /api/invoices/list
GET  /api/invoices/{id}
PUT  /api/invoices/update
DELETE /api/invoices/delete
```

---

## Customer APIs

```text
POST /api/customers/create
GET  /api/customers/list
PUT  /api/customers/update
DELETE /api/customers/delete
```

---

## Inventory APIs

```text
POST /api/products/create
GET  /api/products/list
PUT  /api/products/update
DELETE /api/products/delete
```

---

# 8. Authentication Flow

```text
User Login
     |
     v
Send Credentials
     |
     v
Backend validates user
     |
     v
JWT Token Generated
     |
     v
Token stored in client
     |
     v
Authenticated API Requests
```

---

# 9. Data Flow

### Invoice Creation

```text
User Creates Invoice
        |
        v
Frontend Form
        |
        v
API Request
        |
        v
Backend Validation
        |
        v
Save Invoice
        |
        v
Update Ledger
        |
        v
Return Response
```

---

# 10. Security Architecture

Security measures:

```text
JWT Authentication
Role Based Access Control
Encrypted Passwords (bcrypt)
HTTPS
Rate Limiting
Audit Logs
Database Backup
```

---

# 11. Scalability Strategy

The system is designed to scale by separating services.

Future scaling:

```text
Auth Service
Invoice Service
Accounting Service
Notification Service
```

Load balancing can be added using:

```text
NGINX
Kubernetes
Docker Swarm
```

---

# 12. DevOps Pipeline

Deployment pipeline:

```text
Developer Push Code
        |
        v
GitHub Repository
        |
        v
CI Pipeline
        |
        v
Docker Build
        |
        v
Run Tests
        |
        v
Deploy to Server
```

Tools:

```text
Docker
GitHub Actions
Nginx
AWS / DigitalOcean
```

---

# 13. Monitoring

Tools:

```text
Prometheus
Grafana
Sentry
Elastic Stack
```

Monitoring tracks:

* API performance
* errors
* server health
* database usage

---

# 14. Development Workflow

Software development lifecycle:

```text
Requirement Analysis
      ↓
System Design
      ↓
Sprint Planning
      ↓
Development
      ↓
Testing
      ↓
Deployment
      ↓
Maintenance
```

Methodology:

```text
Agile Scrum
2-week sprints
Daily standups
```

---

# 15. Tools for Visual System Design

The development team should create diagrams using:

| Tool         | Purpose               |
| ------------ | --------------------- |
| Draw.io      | Architecture diagrams |
| Lucidchart   | System flows          |
| Figma        | UI design             |
| dbdiagram.io | Database schema       |
| Miro         | Team collaboration    |
| Jira         | Project management    |

---

# 16. Future Enhancements

Possible upgrades:

* AI financial insights
* Automated GST filing
* Bank API integration
* Multi-company support
* Mobile offline mode
* Payment gateway integration

---

# 17. Expected Project Timeline

| Phase                | Duration |
| -------------------- | -------- |
| System Design        | 1 Week   |
| Backend Development  | 5 Weeks  |
| Frontend Development | 4 Weeks  |
| Mobile App           | 4 Weeks  |
| Testing              | 2 Weeks  |
| Deployment           | 1 Week   |

Total Estimated Time:

**17 Weeks**
