# Mobile Phone and Gadget Sales System

This is a web application built using Django to manage a mobile phone and gadget sales business. It allows users to register, login, browse products, and manage orders, while providing an admin interface to manage products, users, and orders.

## Features

- **User Registration & Login**: Allows users to register and authenticate through a custom `CustomUser` model.
- **Product Management**: Admin can add, edit, and delete products available for sale.
- **Order Management**: Users can place orders for products. Admin can view and manage orders.
- **Admin Panel**: A complete Django admin interface for managing users, products, orders, and more.
- **Custom Authentication**: Built-in user authentication using custom user models.
  
## Requirements

- Python 3.8 or higher
- Django 4.x
- Django REST Framework (if APIs are used)
- Pillow (for handling image fields in models)
- SQLite (default database, but can be swapped for others like PostgreSQL)
  
## Installation

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
