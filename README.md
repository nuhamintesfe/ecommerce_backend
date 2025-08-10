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
```
git clone https://github.com/nuhamintesfe/ecommerce_backend.git
cd ecommerce_backend
```
## 2️⃣ Create a Virtual Environment
Linux/MacOS:
```
python -m venv env
source env/bin/activate
```
Windows:
```
python -m venv env
env\Scripts\activate
```
## 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
## 4️⃣ Configure Environment Variables
Create a .env file in the root directory with your settings (e.g., database credentials, secret keys).

## 5️⃣ Run Database Migrations
```
python manage.py migrate
```
## 6️⃣ Create an Admin Superuser
```
python manage.py createsuperuser
```
## 7️⃣ Start the Development Server
```
python manage.py runserver
```
Access the API at: (https://ecommerce-backend-4-4y57.onrender.com/)

## 📚 API Documentation
- Automatically generated with Swagger:
- https://ecommerce-backend-4-4y57.onrender.com/swagger/ → Interactive Swagger UI

## 🔍 Key Endpoints
## Admin
/admin/shop/  → admin page api to  manage the endpoints
## Products
- GET /api/products/ → List all products (filter/sort supported)
- POST /api/products/ → Create a new product (Admin only)
- GET /api/products/{id}/ → Get product details
- 
##Category
- GET /api/catagories/ → List all category (filter/sort supported)
- POST /api/catagories/ → Create a new category (Admin only)
- GET /api/catagories/{id}/ → Get category details

  ## Users & Auth
- POST /api/auth/register/ → User registration
- POST /api/auth/token/ → Obtain JWT token (Login)
- POST /api/auth/token/refresh/ → Refresh JWT token
  
## Orders
- GET /api/orders/ → List user’s orders (Authentication required)
- POST /api/orders/ → Create a new order

## 🧪 Run Tests
```
python manage.py test
```
## 📜 License
MIT License © 2025 Nuhamin Tesfaye
