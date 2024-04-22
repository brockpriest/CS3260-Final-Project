from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

import Elite.models
from .forms import VehicleInformationForm, ExpenseForm
from .models import VehicleInformation
from .models import Expense
from .models import search_expenses


# Create Views Here

def index(request):
    return render(request, 'Elite/index.html')


def vehicles(request):
    vehicle_list = VehicleInformation.objects.all().order_by('dropdown_field', 'id')

    context = {'vehicle_list': vehicle_list}

    return render(request, 'Elite/Vehicles/vehicles.html', context)


def vehicle(request, vehicle_id, edit):
    # Initialize edit with a default value
    edit = edit.lower()

    vehicle_info = get_object_or_404(VehicleInformation, pk=vehicle_id)
    expenses_info = search_expenses(vehicle_id)

    if request.method == 'POST':
        form = VehicleInformationForm(request.POST, instance=vehicle_info)
        if form.is_valid():
            form.save()
            messages.success(request, f"{vehicle_info.Make} {vehicle_info.Model} updated successfully")
            return redirect('Elite:viewVehicle', vehicle_id=vehicle_info.id, edit='false')
    else:
        form = VehicleInformationForm(instance=vehicle_info)

    # Create context dictionary
    context = {'vehicle': vehicle_info,
               'editing': edit,
               'form': form,
               'expenses_info': expenses_info}

    # Render the template with the context
    return render(request, 'Elite/Vehicles/vehicleView.html', context)


def deleteVehicle(request, vehicle_id):
    vehicle = get_object_or_404(VehicleInformation, pk=vehicle_id)

    if request.method == 'POST':
        vehicle.delete()
        messages.success(request, f"<b>{vehicle.Make} {vehicle.Model} deleted successfully.</b>")
        return redirect('Elite:vehicles')

    context = {'vehicle': vehicle}

    return render(request, 'Elite/Vehicles/deleteVehicle.html', context)


def new_vehicle(request):
    if request.method == 'POST':
        form = VehicleInformationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"{form.Make} {form.Model} added successfully")
            return redirect('Elite:vehicles')

    else:
        form = VehicleInformationForm()

    return render(request, 'Elite/Vehicles/newVehicle.html', {'form': form})


def expenses(request):
    expense_list = Expense.objects.all()

    context = {'expenses_list': expense_list}

    return render(request, 'Elite/Expenses/expenses.html', context)


def view_expense(request, expense_id, edit):
    edit = edit.lower()
    expense = Expense.objects.get(pk=expense_id)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, f"Expense updated successfully for {expense.VehicleId.Make} {expense.VehicleId.Model}")
            return redirect('Elite:viewVehicle', vehicle_id=expense.VehicleId.id, edit='false')
    else:
        form = ExpenseForm(instance=expense)

    context = {'expense': expense,
               'edit': edit,
               'form': form}

    return render(request, 'Elite/Expenses/viewExpense.html', context)


def delete_expense(request, expense_id):
    expense = Expense.objects.get(pk=expense_id)
    if request.method == 'POST':
        expense.delete()
        messages.success(request, f"<b>Expense deleted successfully.</b>")
        return redirect('Elite:viewVehicle', vehicle_id=expense.VehicleId.id, edit='false')

    context = {'expense': expense}

    return render(request, 'Elite/Expenses/deleteExpense.html', context)


def add_expense(request):

    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Expense added.")
            return redirect('Elite:viewVehicle', form.VehicleId.id, "false")

    else:
        form = ExpenseForm()

    return render(request, 'Elite/Expenses/addExpense.html', {'form': form})

def add_expense_id(request, vehicle_id):

    vehicle_info = VehicleInformation.objects.get(pk=vehicle_id)

    if request.method == 'POST':
        form = ExpenseForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f"Expense added.")
            return redirect('Elite:viewVehicle', vehicle_id, "false")

    else:
        data = {
            'VehicleId': vehicle_info
        }
        form = ExpenseForm(initial=data)

    context = {'vehicle': vehicle_info, 'form': form, 'vehicle_id': vehicle_id}

    return render(request, 'Elite/Expenses/addExpense.html', context)
