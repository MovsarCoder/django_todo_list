from django.contrib import admin

# Register your models here.


from planner.models import Priority, Task, Tag, Category


admin.site.register(Priority)
admin.site.register(Task)
admin.site.register(Tag)
admin.site.register(Category)