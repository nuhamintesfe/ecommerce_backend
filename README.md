# 🛒 E-commerce Backend

A fully-featured backend for an E-commerce application built with **Django** and **Django REST Framework (DRF)**.  
This backend powers product listings, orders, user management, and shop operations with advanced features like **filtering, sorting, and pagination**.

---

## 🚀 Features

### **Core**
- Project-wide settings and configurations.
- Environment variable management.
- DRF setup with JWT Authentication.

### **Products**
- Create, update, delete, and list products.
- **Filtering** by category, price range, and availability.
- **Sorting** by price, name, or date added.
- **Pagination** for efficient product browsing.

### **Orders**
- Place and manage orders.
- Track order status.
- Associate orders with users.
- Calculate totals dynamically.

### **Shop**
- Manage shop details and branding.
- Control visibility and inventory status.

### **Users**
- User registration and authentication.
- JWT-based secure login/logout.
- Role-based permissions (e.g., Admin, Customer).
- Profile management.

---

## 🛠️ Tech Stack

- **Backend Framework:** Django, Django REST Framework
- **Database:** PostgreSQL / MySQL (configurable)
- **Authentication:** JWT (JSON Web Tokens)
- **Filtering & Sorting:** `django-filter`
- **Pagination:** DRF’s built-in pagination
- **Environment Management:** `django-environ`

---

## 📦 Installation

## 1️⃣ Clone the Repository  
```bash
git clone https://github.com/nuhamintesfe/ecommerce_backend.git
cd ecommerce_backend
ls -l
2️⃣ Create a Virtual Environment
Linux/MacOS:

bash
python -m venv env
source env/bin/activate
Windows:

bash
python -m venv env
env\Scripts\activate
3️⃣ Install Dependencies
bash
pip install -r requirements.txt
4️⃣ Configure Environment Variables
Create a .env file in the root directory with your settings (e.g., database credentials, secret keys).

5️⃣ Run Database Migrations
bash
python manage.py migrate
6️⃣ Create an Admin Superuser
bash
python manage.py createsuperuser
7️⃣ Start the Development Server
bash
python manage.py runserver
Access the API at: http://127.0.0.1:8000/

📚 API Documentation
Automatically generated with Swagger/ReDoc:

http://127.0.0.1:8000/swagger/ → Interactive Swagger UI

http://127.0.0.1:8000/redoc/ → ReDoc Documentation

🔍 Key Endpoints
Products
GET /api/products/ → List all products (filter/sort supported)

POST /api/products/ → Create a new product (Admin only)

GET /api/products/{id}/ → Get product details

Orders
GET /api/orders/ → List user’s orders (Authentication required)

POST /api/orders/ → Create a new order

Users & Auth
POST /api/users/register/ → User registration

POST /api/token/ → Obtain JWT token (Login)

POST /api/token/refresh/ → Refresh JWT token

🧪 Run Tests
bash
python manage.py test
📜 License
MIT License © 2024 Nuhamin Tesfaye
