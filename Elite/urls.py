"""
URL configuration for Elite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    # Vehicle Information
    path('vehicles/', views.vehicles, name='vehicles'),
    path('vehicles/view/<int:vehicle_id>/<str:edit>/', views.vehicle, name='viewVehicle'),
    path('vehicles/delete/<int:vehicle_id>', views.deleteVehicle, name='deleteVehicle'),
    path('vehicles/add/', views.new_vehicle, name='newVehicle'),
    path('vehicles/unlock/<int:vehicle_id>', views.unlockVehicle, name='unlockVehicle'),


    # Expense Information
    path('expenses/', views.expenses, name='expenses'),
    path('expenses/view/<int:expense_id>/<str:edit>/', views.view_expense, name='viewExpense'),
    path('expenses/delete/<int:expense_id>', views.delete_expense, name='deleteExpense'),
    path('expenses/add/', views.add_expense, name='newExpense'),
    path('expenses/add/<int:vehicle_id>', views.add_expense_id, name='newExpense')


]
app_name = 'Elite'
