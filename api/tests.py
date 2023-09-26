import pytest as pytest
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from api.test_fixtures import create_test_data
from api.models import Vote


# Create your tests here.

@pytest.mark.django_db
def test_get_results_for_current_day(client, create_test_data):

    user, restaurant, menu, employee, client = create_test_data

    # Make a GET request to the view
    url = reverse('api:get-results-for-current-day')
    response = client.get(url)

    # Check if the response status code is 200 OK
    assert response.status_code == status.HTTP_200_OK

    # Check if the menu item is present in the response
    assert menu.menu_item in str(response.content)

@pytest.mark.django_db
def test_vote(client, create_test_data):
    user, restaurant, menu, employee, client = create_test_data

    # Make a POST request to vote
    url = reverse('api:vote', kwargs={'employee_id': employee.id, 'menu_id': menu.id})
    response = client.post(url)

    # Check if the response status code is 201 Created
    assert response.status_code == status.HTTP_201_CREATED

    # Check if the vote was recorded in the database
    assert Vote.objects.filter(employee=employee, menu_item=menu).exists()