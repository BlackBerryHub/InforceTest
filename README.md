# InforceTest

### Run the project

    docker compose build

    docker compose up

    docker-compose run app python manage.py createsuperuser 

    docker-compose run app python manage.py makemigrations 

    docker-compose run app python manage.py migrate 

### Run the tests
    docker compose exec app bash

    pytest

## TODO list
1. Making separate logic (different apps) for Employee, Restaurants and Menu. Because there are all mixed logic in one api view.
2. Adding api v1 with similar logic (not enough time to do it)
3. Updating Authentication (there are not all api endpoints protected by authentication, need to investigate it deeply)

## API Endpoints
    api/token/ - Receive JWT token
    api/token/refresh/ - Refresh JWT token

    api/v2/restaurants/ - Get all restaurants
    api/v2/restaurants/<int:id> - CRUD operations for restaurants

    api/v2/employees/ - Get all employees
    api/v2/employees/<int:id> - CRUD operations for employees

    api/v2/menus/ - Get all menus
    api/v2/menus/<int:id> - CRUD operations for menus
    api/v2/menus/current - Get current date menus
    api/v2/menus/results/ - Get current date results with number of votes

    api/v2/<int:employee_id>/vote/<int:menu_id>/ - vote for menu