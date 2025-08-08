🛒 E-Commerce Backend
A Django REST Framework backend for a fully-featured e-commerce platform.
This repository powers product listings, shopping, order management, and user authentication with advanced features like filtering, sorting, and pagination for optimal API performance.

📂 Project Structure
bash
Copy
Edit
ecommerce_backend/
├── core/         # Project settings, middleware, utilities
├── orders/       # Order creation, tracking, and management
├── products/     # Product CRUD, filtering, sorting, and search
├── shop/         # Shop details and management
├── users/        # Authentication, registration, and user profiles
└── requirements.txt
✨ Features
🔹 Core
Centralized configuration and reusable utilities

Global exception handling

Custom middleware support

🔹 Products
CRUD operations for product management

Advanced filtering by category, price range, brand, etc.

Sorting (e.g., price low → high, newest first)

Pagination for efficient API responses

Database indexing on frequently queried fields

🔹 Shop
Shop profile and details management

Links products to a specific shop

🔹 Orders
Create and manage customer orders

Track order status (pending, shipped, delivered)

Order history for users

🔹 Users
JWT Authentication (login, registration)

User profile management

Permissions and role-based access

🛠️ Tech Stack
Backend Framework: Django, Django REST Framework (DRF)

Authentication: JWT (via djangorestframework-simplejwt)

Database: PostgreSQL / MySQL (configurable)

Filtering & Sorting: django-filter, DRF ordering

Pagination: DRF page and limit-based pagination

Environment Management: django-environ

🚀 Getting Started
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/nuhamintesfe/ecommerce_backend.git
cd ecommerce_backend
2️⃣ Create and Activate Virtual Environment
bash
Copy
Edit
python -m venv env
source env/bin/activate   # On macOS/Linux
env\Scripts\activate      # On Windows
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Set Up Environment Variables
Create a .env file in the project root:

env
Copy
Edit
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=postgres://user:password@localhost:5432/dbname
ALLOWED_HOSTS=localhost,127.0.0.1
5️⃣ Run Migrations
bash
Copy
Edit
python manage.py migrate
6️⃣ Create a Superuser
bash
Copy
Edit
python manage.py createsuperuser
7️⃣ Start the Development Server
bash
Copy
Edit
python manage.py runserver
📡 API Features
Filtering: /api/products/?category=electronics&min_price=100&max_price=500

Sorting: /api/products/?ordering=-price (prefix with - for descending)

Pagination: /api/products/?page=2&page_size=10

Search: /api/products/?search=keyword

📖 API Documentation
This project includes Swagger/Redoc API documentation.

Run the server and visit:

Swagger UI: http://127.0.0.1:8000/swagger/

Redoc: http://127.0.0.1:8000/redoc/

🔒 Authentication
JWT authentication is used for secure API access.

Obtain tokens at /api/auth/login/.

Include Authorization: Bearer <token> in headers for protected endpoints.

🧩 Future Enhancements
Payment gateway integration

Wishlist & cart features

Product reviews and ratings

Email notifications

📜 License
This project is licensed under the MIT License.

