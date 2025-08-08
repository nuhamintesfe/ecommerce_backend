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

### **1. Clone the Repository**
```bash
git clone https://github.com/nuhamintesfe/ecommerce_backend.git
cd ecommerce_backend
## 2. Create a Virtual Environment
```bash
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
## 3. Install Dependencies
```bash
pip install -r requirements.txt
## 4. Configure Environment Variables
Create a .env file in the root directory:

## 5. Run Migrations
``` bash
python manage.py migrate
## 6. Create a Superuser
``` bash
python manage.py createsuperuser
## 7. Start the Development Server
``` bash
python manage.py runserver
Visit: http://127.0.0.1:8000/

## 📚 API Documentation
The API comes with Swagger documentation.
Visit:
``` bash
/swagger/   → Swagger UI
/redoc/     → ReDoc Documentation
📌 Example API Endpoints
## Products
- ** GET /api/products/ → List products with filtering, sorting, and pagination.
- ** POST /api/products/ → Create a new product.
- ** GET /api/products/{id}/ → Retrieve a product.

## Orders
- ** GET /api/orders/ → List all orders for logged-in user.
- ** POST /api/orders/ → Create a new order.

## Users
- ** POST /api/users/register/ → Register a new user.
- ** POST /api/token/ → Login and get JWT token.
- ** POST /api/token/refresh/ → Refresh JWT token.

## 🧪 Running Tests
``` bash
python manage.py test
##📄 License
This project is licensed under the MIT License.

## 👩‍💻 Author
Nuhamin Tesfaye