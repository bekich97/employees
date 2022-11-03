from django.shortcuts import render, redirect
from employee.models import Department, Employee
from django.core.paginator import Paginator
from django.contrib import messages


def index(request):
    return redirect("/employees/0")


def employees(request, id):
    departments = Department.objects.all()
    if id == 0:
        department = None
    else:
        department = Department.objects.filter(id=id).first()

    if not department:
        employees = Employee.objects.all()
    else:
        employees = Employee.objects.filter(department=department)

    if request.GET.get('page'):
        page_number = request.GET.get('page')
    else:
        page_number = 1
    if request.GET.get('size'):
        page_size = request.GET.get('size')
    else:
        page_size = 25
    paginator = Paginator(employees, page_size)
    paginated_employees = paginator.get_page(page_number)

    context = {
        'departments_count': departments.count(),
        'departments': departments,
        'department': department,
        'employees': paginated_employees,
        'page_number': page_number,
        'page_size': page_size
    }
    return render(request, "home.html", context)


def employees_detail(request, id):
    employee = Employee.objects.filter(id=id).first()
    if not employee:
        messages.error(request, 'Сотрудник не найден!')
        return redirect('/employees/0')

    departments = Department.objects.all()
    context = {
        'employee': employee,
        'departments': departments
    }
    return render(request, "detail.html", context)
