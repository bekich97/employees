from django.urls import path
from .views import index, employees, employees_detail

urlpatterns = [
    path('', index, name="index"),
    path('<int:id>/', employees, name="employees"),
    path('<int:id>/detail/', employees_detail, name="employees-detail"),
]
