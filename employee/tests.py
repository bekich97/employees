from django.test import TestCase
from .models import Employee, Department
from datetime import datetime


class BasicTest(TestCase):
    # def setUp(self):
    #     department = Department()
    #     department.name = "Test department"
    #     department.parent = None
    #     department.save()
        
    #     employee = Employee()
    #     employee.fullname = "Test Testowich Testow"
    #     employee.job_title = "Teacher"
    #     employee.salary = 123.12
    #     employee.employment_date = datetime.now()
    #     employee.department = department
    #     employee.save()
    #     return super().setUp()

    def test_fields(self):
        department = Department()
        department.name = "Test department"
        department.parent = None
        department.save()

        employee = Employee()
        employee.fullname = "Test Testowich Testow"
        employee.job_title = "Teacher"
        employee.salary = 123.12
        employee.employment_date = datetime.now()
        employee.department = department
        employee.save()

        record = Employee.objects.get(id=1)
        self.assertEqual(record, employee)