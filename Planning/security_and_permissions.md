# eCommerce Application – Security and Permissions

## 1. Introduction

Security will be implemented to protect user accounts, personal information, store information and purchase records. Django's built-in authentication and permission features will be used wherever appropriate.

## 2. User Authentication

The application will provide:
- User registration.
- Secure login and logout.
- Password hashing through Django.
- Password recovery through email.
- Time-limited password-reset links.

Users must authenticate before accessing protected functionality.

## 3. User Roles and Permissions

### 3.1 Vendors

Vendors will be allowed to:
- Create and manage their own stores.
- Add, edit and remove products belonging to their stores.
- View their own store information.

Vendors must not be able to modify another vendor's stores or products.

### 3.2 Buyers

Buyers will be allowed to:
- Browse available products.
- Manage their shopping carts.
- Complete purchases.
- Submit product reviews.
- View their own purchase information.

Buyers must not access vendor-only management functionality.

### 3.3 Administrators

Administrators will use Django administration and appropriate permissions to manage application information and user accounts.

## 4. Access Control

The application will use:
- Django authentication.
- Login-required restrictions on protected views.
- Role-based access checks.
- Ownership checks for stores and products.
- Model permissions where appropriate.

Access will be checked on the server side rather than relying only on hiding interface buttons.

## 5. Data Protection

The application will:
- Store passwords using Django's password-hashing mechanisms.
- Validate user input.
- Use Django's CSRF protection.
- Protect database operations.
- Avoid exposing sensitive information.
- Use secure configuration for database credentials and email settings.
- Use HTTPS in production.

## 6. Shopping and Payment Security

The system will validate product availability and prices on the server during checkout. It will not rely on prices or totals submitted by the browser.

Database transactions will help ensure that orders and inventory updates remain consistent.

## 7. Password Recovery Security

Password-reset links will use secure, unique tokens with an expiry period. Tokens will be validated before allowing password changes.

## 8. Conclusion

Authentication, permissions, ownership checks and secure data-handling practices will help prevent unauthorised access and protect the integrity of the eCommerce application.