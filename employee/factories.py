import factory
from factory.django import DjangoModelFactory
from .models import Department, Employee
import pytz


class DepartmentFactory(DjangoModelFactory):
    class Meta:
        model = Department

    name = factory.Faker("sentence", nb_words=2, variable_nb_words=True)


class EmployeeFactory(DjangoModelFactory):
    class Meta:
        model = Employee

    fullname = factory.Faker("name")
    job_title = factory.Faker("sentence", nb_words=2, variable_nb_words=True)
    employment_date = factory.Faker("date_time", tzinfo=pytz.UTC)
    salary = factory.Faker("pydecimal", left_digits=8, right_digits=2, positive=True, min_value=1, max_value=1000000)
    department = factory.SubFactory(DepartmentFactory)
