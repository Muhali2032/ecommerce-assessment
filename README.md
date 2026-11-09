# eCommerce Application

## Project Overview

This project is a Django-based eCommerce application developed as part of the HyperionDev practical assessment.

The application supports two user roles: vendors and buyers.

## Main Features

### User Accounts
- User registration.
- Login and logout.
- Vendor and buyer roles.
- Password reset functionality.

### Vendor Features
- Create, view, update and delete stores.
- Add, view, update and delete products.
- Manage product quantities and prices.

### Buyer Features
- Browse products from different stores.
- Add products to a shopping cart.
- Remove products from the cart.
- Complete checkout.
- View order confirmation.
- Submit product reviews.

### Additional Features
- Session-based shopping cart.
- Order and order-item records.
- Stock quantity updates after checkout.
- Verified and unverified product reviews.
- Invoice email generation.
- Password reset links with expiring tokens.

## Technologies Used

- Python
- Django
- SQLite relational database
- HTML
- CSS

## Project Requirements

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

## Running the Application

1. Open Terminal.
2. Navigate to the `ecommerce_project` directory.
3. Activate the virtual environment.
4. Apply database migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

6. Open the application in your browser:

`http://127.0.0.1:8000/`

## Database

The application uses SQLite, a relational database supported by Django.

## Email Configuration

The development email backend prints generated emails to the Terminal. Actual email delivery requires SMTP configuration.

## Assessment Submission

The submission includes the Django source code, database migrations, templates, static files, planning documents and research document.