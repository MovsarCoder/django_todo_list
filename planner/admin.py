from django.contrib import admin

# Register your models here.


from planner.models import Priority, Task, Category


admin.site.register(Priority)
admin.site.register(Task)
admin.site.register(Category)