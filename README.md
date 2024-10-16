# Inventory Management API (alx-capstone-project)

## Overview

The Inventory Management API is a RESTful API built with Django and Django Rest Framework (DRF). It allows users to manage inventory items, track product quantities, handle orders, and manage customer and supplier information. The API includes user authentication and supports various operations for inventory management.

## Features

- **CRUD Operations**: Create, Read, Update, and Delete inventory items, products, suppliers, customers, and orders.
- **User Authentication**: Secure user authentication using Django's built-in authentication system.
- **Inventory Tracking**: Log changes to inventory quantities and track inventory changes over time.
- **Filtering and Searching**: Filter inventory items by category, low stock, and price range.
- **Custom Actions**: View inventory levels with additional filtering options.

## Requirements

- Python 3.8+
- Django 3.2+
- Django Rest Framework 3.12+
- PostgreSQL/MySQL (or other databases supported by Django)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/inventory-management-api.git
   cd inventory-management-api
