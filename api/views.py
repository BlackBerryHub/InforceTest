from datetime import date

from django.db.models import Count
from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Restaurant, Employee, Menu, Vote
from api.serializers import RestaurantSerializer, EmployeeSerializer, MenuSerializer, VoteSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_day_menu(request):
    today = date.today()
    menus = Menu.objects.filter(date=today)
    serializer = MenuSerializer(menus, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_results_for_current_day(request):
    today = date.today()
    menus = Menu.objects.filter(date=today)

    menus_with_votes = menus.annotate(vote_count=Count('vote'))

    serializer = MenuSerializer(menus_with_votes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def vote(request, employee_id, menu_id):
    try:
        employee = Employee.objects.get(pk=employee_id)
        menu = Menu.objects.get(pk=menu_id)
    except (Employee.DoesNotExist, Menu.DoesNotExist):
        return Response({'error': 'Employee or Menu not found'}, status=status.HTTP_404_NOT_FOUND)

    existing_vote = Vote.objects.filter(employee=employee, menu_item=menu, vote_date=menu.date).first()
    if existing_vote:
        return Response({'error': 'Employee has already voted for this menu item today'}, status=status.HTTP_400_BAD_REQUEST)

    vote_data = {'employee': employee.id, 'menu_item': menu.id}
    serialized_votes = VoteSerializer(data=vote_data)
    if serialized_votes.is_valid():
        serialized_votes.save()
        return Response(serialized_votes.data, status=status.HTTP_201_CREATED)
    return Response(serialized_votes.errors, status=status.HTTP_400_BAD_REQUEST)


class RestaurantView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        restaurants = Restaurant.objects.all()
        serialized_restaurants = RestaurantSerializer(restaurants, many=True)
        return Response(serialized_restaurants.data)


class RestaurantSingleView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, id):
        try:
            restaurant = Restaurant.objects.get(id=id)
            return restaurant
        except Restaurant.DoesNotExist:
            return None


    def get(self, request, id):
        restaurant = self.get_object(id)
        serialized_restaurant = RestaurantSerializer(restaurant)
        return Response(serialized_restaurant.data)


    def put(self, request, id):
        restaurant = self.get_object(id)
        if restaurant is None:
            serialized_restaurant = RestaurantSerializer(instance=restaurant, data=request.data)
            if serialized_restaurant.is_valid():
                serialized_restaurant.save()
                return Response(serialized_restaurant.data)
        return Response(None, status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        restaurant = self.get_object(id)
        if restaurant is not None:
            restaurant.delete()
            return Response(None, status.HTTP_204_NO_CONTENT)
        return Response(None, status.HTTP_400_BAD_REQUEST)

class EmployeeView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        employees = Employee.objects.all()
        serialized_employees = EmployeeSerializer(employees, many=True)
        return Response(serialized_employees.data)


class EmployeeSingleView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, id):
        try:
            employee = Employee.objects.get(id=id)
            return employee
        except Employee.DoesNotExist:
            return None


    def get(self, request, id):
        employee = self.get_object(id)
        serialized_employee = EmployeeSerializer(employee)
        return Response(serialized_employee.data)


    def put(self, request, id):
        employee = self.get_object(id)
        if employee is None:
            serialized_employee = EmployeeSerializer(instance=employee, data=request.data)
            if serialized_employee.is_valid():
                serialized_employee.save()
                return Response(serialized_employee.data)
        return Response(None, status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        employee = self.get_object(id)
        if employee is not None:
            employee.delete()
            return Response(None, status.HTTP_204_NO_CONTENT)
        return Response(None, status.HTTP_400_BAD_REQUEST)


class MenuView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        menus = Menu.objects.all()
        serialized_menus = MenuSerializer(menus, many=True)
        return Response(serialized_menus.data)


class MenuSingleView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, id):
        try:
            menu = Menu.objects.get(id=id)
            return menu
        except Menu.DoesNotExist:
            return None


    def get(self, request, id):
        menu = self.get_object(id)
        serialized_menu = MenuSerializer(menu)
        return Response(serialized_menu.data)


    def put(self, request, id):
        menu = self.get_object(id)
        if menu is None:
            serialized_menu = MenuSerializer(instance=menu, data=request.data)
            if serialized_menu.is_valid():
                serialized_menu.save()
                return Response(serialized_menu.data)
        return Response(None, status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        menu = self.get_object(id)
        if menu is not None:
            menu.delete()
            return Response(None, status.HTTP_204_NO_CONTENT)
        return Response(None, status.HTTP_400_BAD_REQUEST)