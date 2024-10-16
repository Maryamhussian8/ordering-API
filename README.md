# Meal Ordering API

## Overview
This project is a **Meal Ordering API** built with Django and Django REST Framework. The API provides endpoints for managing meals and orders, including functionality for creating, updating, and deleting both meals and orders. It also includes pagination and filtering options to handle a large dataset efficiently.

## Features
- **Meals API:**
  - List available meals with filtering options (`name`, `price`, `available`).
  - Create, update, and delete meal entries.
  
- **Orders API:**
  - List all orders.
  - Create, update, and delete orders.
  - Add multiple items to an order and automatically calculate the total price.

- **Authentication:**
  - API requires authentication for creating and updating orders (uses Django’s authentication system).

## API Endpoints

### Meals Endpoints

1. **List Meals**
   - **URL:** `/api/meals/`
   - **Method:** `GET`
   - **Description:** Retrieve a list of meals. Supports filtering by `name`, `price`, and `available`.
   - **Filters:**
     - `name`: Filter by meal name.
     - `price`: Filter by meal price.
     - `available`: Filter by meal availability (boolean).

   - **Example Request:**
     ```
     GET /api/meals/?available=true&price__lte=20
     ```

2. **Create a Meal**
   - **URL:** `/api/meals/create/`
   - **Method:** `POST`
   - **Description:** Create a new meal.

   - **Request Body Example:**
     ```json
     {
       "name": "Pasta",
       "price": 15.99,
       "available": true
     }
     ```

3. **Update a Meal**
   - **URL:** `/api/meals/update/<int:pk>/`
   - **Method:** `PUT`
   - **Description:** Update an existing meal.

   - **Request Body Example:**
     ```json
     {
       "name": "Burger",
       "price": 12.99,
       "available": false
     }
     ```

4. **Delete a Meal**
   - **URL:** `/api/meals/delete/<int:pk>/`
   - **Method:** `DELETE`
   - **Description:** Delete a specific meal.

---

### Orders Endpoints

1. **List Orders**
   - **URL:** `/api/orders/`
   - **Method:** `GET`
   - **Description:** Retrieve a list of orders.

2. **Create an Order**
   - **URL:** `/api/orders/create/`
   - **Method:** `POST`
   - **Description:** Create a new order with multiple items. Automatically calculates the total price based on the meal prices and quantities.

   - **Request Body Example:**
     ```json
     {
       "order_items": [
         {
           "meal": 1,
           "quantity": 2
         },
         {
           "meal": 3,
           "quantity": 1
         }
       ]
     }
     ```

3. **Update an Order**
   - **URL:** `/api/orders/update/<int:pk>/`
   - **Method:** `PUT`
   - **Description:** Update an existing order, including the items and their quantities.

4. **Delete an Order**
   - **URL:** `/api/orders/delete/<int:pk>/`
   - **Method:** `DELETE`
   - **Description:** Delete a specific order.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/meal-ordering-api.git
   cd meal-ordering-api
