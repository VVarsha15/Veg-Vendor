# VeggieCart - Online Vegetable Ordering System

VeggieCart is a Django-based web application that allows users to browse and purchase vegetables online. It features separate user and admin dashboards, real-time stock management, cart handling, and order tracking.

---

## Features

### User Side
- Sign up and log in using phone number and password
- View available vegetables with price and stock details
- Add vegetables to the cart
- View and update cart items
- Place orders and view order history

### Admin Side
- View incoming user orders
- Mark orders as fulfilled (removes them from order queue)
- View and update vegetable stock in a tabular format
- Add new stock as needed

---

## Prerequisites

Make sure the following are installed:

- Python 3.8+
- pip
- MySQL Server (or SQLite by default)
- Pillow (for image support)
- Django (version 4+ recommended)

---

## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/VVarsha15/Veg-Vendor.git
cd Veg-Vendor
```
2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv env
# On macOS/Linux
source env/bin/activate
# On Windows
env\Scripts\activate
```

3. **Install required packages**
```bash
pip install -r requirements.txt
```

4. **Install Pillow manually if not in requirements**
Install Pillow manually if not in requirements

```bash
pip install Pillow
```
5. **Run migrations**

```bash
Edit
python manage.py makemigrations
python manage.py migrate
```
6. **Create a superuser (admin)**

```bash
python manage.py createsuperuser
# Use phone: 8754494959 (as per project setup)
```

7. **Run the development server**

```bash
python manage.py runserver
Visit the app in browser

User login: http://127.0.0.1:8000/login/
```

Static Images
Vegetable images are stored in the vegetable_static/ folder and rendered using Django's {% static %} tag. To use this:

Add vegetable images named as lowercase vegetable names (e.g., tomato.jpg, onion.jpeg) to vegetable_static/

Make sure 'django.contrib.staticfiles' is in INSTALLED_APPS

## Ensure STATICFILES_DIRS is configured in settings.py:

STATICFILES_DIRS = [ BASE_DIR / "vegetable_static" ]

##Database
Default: SQLite (db.sqlite3)

You can switch to MySQL in settings.py like this:

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```



