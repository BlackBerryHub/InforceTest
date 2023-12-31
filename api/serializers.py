from rest_framework import serializers
from api.models import Restaurant, Employee, Menu, Vote


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    vote_count = serializers.IntegerField()

    class Meta:
        model = Menu
        fields = '__all__'


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'