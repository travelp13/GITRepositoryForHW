# Online Store Django Project

This is a fully functional online store built with Django, featuring product catalog, cart, user authentication, and order processing.

---

## Features

- **Product Catalog**: Display products and categories.
- **Cart**: Add products to the cart and manage quantities.
- **User Authentication**: Register, login, logout, and profile management.
- **Order Processing**: Checkout functionality with saved user data.
- **Responsive Design**: Styled using Bootstrap 5 for a responsive user experience.

---

## Installation

1. Clone the repository:


2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

---

## Usage

- Access the application at `http://127.0.0.1:8000/`.
- Admin interface: `http://127.0.0.1:8000/admin/`.

---

## Dependencies

- Python 3.x
- Django 5.1.4
- Bootstrap 5

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
