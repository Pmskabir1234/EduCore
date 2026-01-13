from django.contrib import admin
from .models import students,courses

# Register your models here.
admin.site.register(courses)

@admin.register(students)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']