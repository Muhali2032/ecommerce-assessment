# eCommerce Application – System Requirements

## 1. Project Overview

The purpose of this project is to develop a Django-based eCommerce web application that allows users to register as vendors or buyers. Vendors will be able to create and manage online stores and their products, while buyers will be able to browse products, add items to shopping carts, make purchases and submit product reviews.

## 2. User Requirements

### 2.1 Vendors

Vendors must be able to:
- Register and log in as vendors.
- Create new stores.
- View their existing stores.
- Edit store information.
- Delete their stores.
- Add products to their stores.
- View products in their stores.
- Edit product information.
- Remove products from their stores.

### 2.2 Buyers

Buyers must be able to:
- Register and log in as buyers.
- Browse products from different stores.
- View product information.
- Add products to a shopping cart.
- Continue shopping while retaining cart contents.
- Checkout and complete purchases.
- Receive an invoice through email.
- Submit product reviews.
- View verified and unverified reviews.

### 2.3 System Administrator

The administrator should be able to:
- Access Django administration.
- Manage registered users.
- Monitor stores and products.
- Manage application records where authorised.

## 3. Functional Requirements

The application must:
1. Provide user registration and login.
2. Distinguish between vendor and buyer accounts.
3. Allow vendors to manage stores and products.
4. Allow buyers to browse and purchase products.
5. Use Django sessions to maintain shopping cart contents.
6. Generate invoices after successful checkout.
7. Email invoices to buyers.
8. Identify reviews as verified or unverified based on purchase history.
9. Provide forgotten-password recovery using secure, expiring reset links.
10. Store application information in a relational database.
11. Implement authentication and permissions to restrict access.

## 4. Non-Functional Requirements

The application should:
- Be user-friendly and easy to navigate.
- Protect user information and passwords.
- Validate information entered by users.
- Provide reliable database operations.
- Handle unexpected errors appropriately.
- Maintain data consistency during transactions.
- Support maintainable and organised Django code.

## 5. System Users

The main users are vendors, buyers and administrators. Each user category must have access only to the functionality permitted by their role.

## 6. Expected Outcome

A functional Django eCommerce application that allows vendors to operate online stores and buyers to purchase products securely, receive invoices and submit product reviews.