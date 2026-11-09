# eCommerce Application – Database Design

## 1. Introduction

The application will use a relational database to store and manage information about users, stores, products, purchases and reviews.

Django models will define the database tables and their relationships.

## 2. Planned Database Tables

### 2.1 User

Stores registered user information.

Fields:
- ID (Primary Key)
- Username
- Email
- Password
- Role (Vendor or Buyer)

Django authentication will manage passwords securely.

### 2.2 Store

Stores information about vendor stores.

Fields:
- ID (Primary Key)
- Vendor (Foreign Key referencing User)
- Store name
- Description
- Date created

Relationship: One vendor can own multiple stores.

### 2.3 Product

Stores information about products available for purchase.

Fields:
- ID (Primary Key)
- Store (Foreign Key referencing Store)
- Product name
- Description
- Price
- Quantity available

Relationship: One store can contain multiple products.

### 2.4 Order

Stores information about buyer purchases.

Fields:
- ID (Primary Key)
- Buyer (Foreign Key referencing User)
- Order date
- Total amount
- Order status

Relationship: One buyer can place multiple orders.

### 2.5 OrderItem

Stores individual products included in an order.

Fields:
- ID (Primary Key)
- Order (Foreign Key referencing Order)
- Product (Foreign Key referencing Product)
- Quantity purchased
- Unit price at purchase

Relationship: One order can contain multiple order items.

The unit price will be recorded at the time of purchase to preserve the original purchase amount.

### 2.6 Review

Stores product reviews submitted by buyers.

Fields:
- ID (Primary Key)
- Buyer (Foreign Key referencing User)
- Product (Foreign Key referencing Product)
- Rating
- Comment
- Verified status
- Date created

Relationship: One product can receive multiple reviews.

The verified status will be determined by checking whether the buyer has a completed purchase containing that product.

## 3. Database Relationships

The planned relationships are:

- User to Store: One-to-Many.
- Store to Product: One-to-Many.
- User to Order: One-to-Many.
- Order to OrderItem: One-to-Many.
- Product to OrderItem: One-to-Many.
- User to Review: One-to-Many.
- Product to Review: One-to-Many.

## 4. Shopping Cart

The shopping cart will use Django sessions to temporarily store the buyer's selected products and quantities.

The cart does not need a permanent database table for this implementation.

## 5. Invoice Management

Invoices will be generated from successfully processed orders and their associated order items.

The order records will preserve the information required to reproduce the invoice.

## 6. Database Integrity

The application will use:
- Primary keys to uniquely identify records.
- Foreign keys to establish relationships.
- Appropriate field validation.
- Database transactions during checkout.
- Appropriate deletion rules to protect important purchase records.

## 7. Database Engine

MariaDB or another supported relational database engine will be used as the application's database backend.

Django migrations will create and update the database structure.

## 8. Conclusion

The proposed database design will provide an organised structure for managing users, stores, products, purchases and reviews while maintaining relationships and data integrity.