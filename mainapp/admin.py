from django.contrib import admin
from .models import Tasks, Status, Sub_tasks, Comments,Priority, Category

class TasksAdmin(admin.ModelAdmin):
    list_display = ['title', 'priority', 'author']
class StatusAdmin(admin.ModelAdmin):
    list_display = ['name']
class Sub_tasksAdmin(admin.ModelAdmin):
    list_display = ['title', 'task']
class PriorityAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Tasks, TasksAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Comments)
admin.site.register(Sub_tasks, Sub_tasksAdmin)
admin.site.register(Priority, PriorityAdmin)
admin.site.register(Category, CategoryAdmin)