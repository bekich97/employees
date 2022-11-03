import random

from django.db import transaction
from django.core.management.base import BaseCommand

from employee.models import Department, Employee
from employee.factories import (
    DepartmentFactory,
    EmployeeFactory
)

NUM_DEPS = 25
NUM_EMPS = 50000


class Command(BaseCommand):
    help = "Generates db seeds"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Department, Employee]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        # Create all the departments
        departments = []
        for _ in range(NUM_DEPS):
            parent = None
            if len(departments) > 5:
                parent = random.choice(departments)
            department = DepartmentFactory(parent=parent)
            departments.append(department)

        # Create all the employees
        for _ in range(NUM_EMPS):
            department = random.choice(departments)
            EmployeeFactory(department=department)
