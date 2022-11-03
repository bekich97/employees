from django.db import models
from django.core.exceptions import ValidationError
from mptt.models import MPTTModel, TreeForeignKey


# Модель отделов
class Department(MPTTModel):
    name = models.CharField(max_length=255, verbose_name="Название отдела")
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children", verbose_name="Родитель отдела")

    class Meta:
        verbose_name = "Подразделение"
        verbose_name_plural = "Подразделении"

    class MPTTMeta:
        order_insertion_by = ["name"]

    MAX_TREE_DEPTH = 5

    def clean(self):
        self.my_parent = self.parent
        if self.my_parent:
            parent_level = self.my_parent.get_level()
        else:
            parent_level = 0
        if parent_level + 1 > self.MAX_TREE_DEPTH:
            raise ValidationError({'parent': f"Отдел может быть вложен только {self.MAX_TREE_DEPTH} уровней в глубину"})

    def save(self, *args, **kwargs):
        self.clean()
        return super(Department, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Employee(models.Model):
    fullname = models.CharField(max_length=255, verbose_name="ФИО")
    job_title = models.CharField(max_length=255, verbose_name="Должность")
    employment_date = models.DateTimeField(verbose_name="Дата приема на работу")
    salary = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Размер заработной платы")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="employees", verbose_name="Подразделение")

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        ordering = ["fullname"]

    def __str__(self):
        return self.fullname
