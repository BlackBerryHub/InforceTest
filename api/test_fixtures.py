import pytest
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from .models import Restaurant, Menu, Employee, Vote
from django.test import Client

import pytest
from django.contrib.auth.models import User
from django.test import Client  # Import Client class
from api.models import Restaurant, Menu, Employee  # Import your models


@pytest.fixture
def create_test_data(db):
    # Create a test user
    user = User.objects.create_user(username='testuser', password='testpassword')

    # Create a test restaurant
    restaurant = Restaurant.objects.create(name='Test Restaurant', description='Test Description', location="Lviv")

    # Create test menu for the current day
    menu = Menu.objects.create(restaurant=restaurant, date='2023-09-26', menu_item='Test Menu Item')

    # Create test employee
    employee = Employee.objects.create(name='Test Employee', email='test@example.com')

    # Use the Django test client to log in the user
    client = Client()
    client.login(username='testuser', password='testpassword')

    return user, restaurant, menu, employee, client  # Return the client instance as well


