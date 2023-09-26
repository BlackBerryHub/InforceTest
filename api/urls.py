from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

from api.views import RestaurantSingleView, RestaurantView, EmployeeView, MenuView, MenuSingleView, EmployeeSingleView, \
    vote, get_current_day_menu, get_results_for_current_day

app_name = 'api'

urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path("api/v2/restaurants/", RestaurantView.as_view()),
    path("api/v2/restaurants/<int:id>", RestaurantSingleView.as_view()),

    path("api/v2/employees/", EmployeeView.as_view()),
    path("api/v2/employees/<int:id>", EmployeeSingleView.as_view()),

    path("api/v2/menus/", MenuView.as_view()),
    path("api/v2/menus/<int:id>", MenuSingleView.as_view()),
    path("api/v2/menus/current", get_current_day_menu, name='get-current-day-menu'),
    path("api/v2/menus/results/", get_results_for_current_day, name='get-results-for-current-day'),

    path("api/v2/<int:employee_id>/vote/<int:menu_id>/", vote, name='vote'),
]