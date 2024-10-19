## Overview of API Endpoints

## Authentication
- Login: POST /api/token/login/
- Logout: POST /api/token/logout/
- Inventory Management

## Categories:
- GET /api/categories/
- POST /api/categories/
- GET /api/categories/{id}/
- PUT /api/categories/{id}/
- DELETE /api/categories/{id}/

## Products:
- GET /api/products/
- POST /api/products/
- GET /api/products/{id}/
- PUT /api/products/{id}/
- DELETE /api/products/{id}/

## Suppliers:
- GET /api/suppliers/
- POST /api/suppliers/
- GET /api/suppliers/{id}/
- PUT /api/suppliers/{id}/
- DELETE /api/suppliers/{id}/

## Customers:
- GET /api/customers/
- POST /api/customers/
- GET /api/customers/{id}/
- PUT /api/customers/{id}/
- DELETE /api/customers/{id}/

## Orders:
- GET /api/orders/
- POST /api/orders/
- GET /api/orders/{id}/
- PUT /api/orders/{id}/
- DELETE /api/orders/{id}/

## Inventories:
- GET /api/inventories/
- POST /api/inventories/
- GET /api/inventories/{id}/
- PUT /api/inventories/{id}/
- DELETE /api/inventories/{id}/
- Custom Action: GET /api/inventories/view_inventory_levels/

## Inventory Logs:
- GET /api/inventory-logs/
- GET /api/inventory-logs/{id}/


Check User Account Status:

Ensure that the user account you are trying to authenticate is active. If you're using Django's built-in User model, you can check this by:
Opening the Django shell:
bash
Copy code
python manage.py shell

from django.contrib.auth.models import User
user = User.objects.filter(username='sktzzzz').first()
print(user.is_active)  # Should return True for an active account

If the user is not found or is not active, you may need to create the user or reactivate the account.
Creating a New User (if needed): If you don’t have an active user account, you can create one:

python manage.py shell
Create a new user with a password:
python

from django.contrib.auth.models import User
User.objects.create_user(username='sktzzzz', password='0558218264')
Reset Password (if needed): If you think you might have forgotten your password or want to set a new one for the existing user, you can reset it using the Django shell:

user = User.objects.get(username='sktzzzz')
user.set_password('new_password')  # Set a new password
user.save()
Ensure User is Active: If you find that the user exists but is not active, you can activate it by setting is_active to True:

user.is_active = True
user.save()


http://127.0.0.1:8000/api/token/
{
    "username": "sktzzzz",
    "password": "0558218264"
}

Example Testing Scenario
Get tokens:
Send a POST request to /api/token/ with your username and password.

Use the access token in your requests:
Send a GET request to /api/inventory/ to list inventories.
Send a POST request to /api/inventory/ to create a new inventory item.
Send a PUT request to update an inventory item.
Send a DELETE request to remove an inventory item.