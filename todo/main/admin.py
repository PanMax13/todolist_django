from django.contrib import admin
from .models import Tables, Tasks
# Register your models here.


@admin.register(Tables)
class TablesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("category", )}


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    pass