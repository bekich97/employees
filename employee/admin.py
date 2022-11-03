from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Department, Employee
# Register your models here.


admin.site.register(
    Department,
    DraggableMPTTAdmin,
    list_filter=["parent"],
    search_fields=["name"],
    list_display=(
        'tree_actions',
        'indented_title',
        'name',
        'parent',
    ),
    list_display_links=(
        'name',
    ),
)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["fullname", "job_title", "employment_date", "salary", "department"]
    list_filter = ["employment_date", "department"]
    search_fields = ["fullname", "job_title"]
    autocomplete_fields = ["department"]

    class Meta:
        model = Employee


admin.site.register(Employee, EmployeeAdmin)
