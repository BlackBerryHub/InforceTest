from django.contrib import admin

from api.models import Restaurant, Menu, Employee, Vote

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Employee)
admin.site.register(Vote)