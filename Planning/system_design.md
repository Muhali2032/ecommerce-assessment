# eCommerce Application – System Design

## 1. Introduction

The eCommerce application will be developed using Django. It will provide an online platform where vendors can manage stores and products, while buyers can browse products, make purchases and submit reviews.

## 2. System Architecture

The application will use the Django Model-View-Template (MVT) architecture.

### Models
Models will define the application's database structure and relationships. They will represent:
- Users
- Stores
- Products
- Orders
- Order items
- Reviews

### Views
Views will process user requests and implement application functionality, including:
- User registration and authentication.
- Store and product management.
- Product browsing.
- Shopping cart operations.
- Checkout and invoice generation.
- Product reviews.
- Password recovery.

### Templates
Templates will provide the user interface using HTML, CSS and Bootstrap where appropriate.

## 3. Main System Components

### 3.1 User Management
Django authentication will manage registration, login, logout and password management. User roles will distinguish vendors from buyers.

### 3.2 Store Management
Vendors will be able to create, view, update and delete their own stores.

### 3.3 Product Management
Vendors will manage products belonging to their stores. Each product will be associated with a specific store.

### 3.4 Shopping Cart
The shopping cart will use Django sessions to retain product selections while buyers navigate the application.

### 3.5 Checkout and Orders
When a buyer checks out, the application will validate the cart, calculate the order total and save the purchase information. Database transactions will help maintain consistency.

### 3.6 Invoices and Email
After a successful purchase, the application will generate an invoice containing the purchased products, quantities and prices. The invoice will be emailed to the buyer.

### 3.7 Product Reviews
Buyers will be able to submit reviews. The application will check purchase records to determine whether a review is verified or unverified.

### 3.8 Password Recovery
Django's password-reset functionality will provide secure, time-limited password-reset links delivered through email.

## 4. Database Design Overview

The system will use a relational database.

The planned relationships include:
- One vendor can own multiple stores.
- One store can contain multiple products.
- One buyer can place multiple orders.
- One order can contain multiple order items.
- One product can receive multiple reviews.
- Each review will be associated with a user and a product.

## 5. Security and Access Control

Django authentication and permissions will protect application functionality. Vendors will only manage their own stores and products. Buyers will access shopping and review functionality. Sensitive information will be protected through appropriate security practices.

## 6. Conclusion

The proposed architecture separates database operations, application logic and presentation. This structure will make the application easier to maintain, test and extend.