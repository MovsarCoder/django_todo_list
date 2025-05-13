from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя категориии')

    def __str__(self):
        return self.name


class Priority(models.Model):
    level = models.CharField(max_length=50, choices=[
        ('high', 'Высокий'),
        ('middle', 'Средний'),
        ('low', 'Низкий'),
    ])

    color = models.CharField(max_length=50, choices=[
        ('red', 'Красный'),
        ('yellow', 'Желтый'),
        ('green', 'Зеленый'),
    ])

    def __str__(self):
        return self.level


class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name='Имя задачи')
    description = models.TextField(blank=True)  # Можно оставить поле пустым
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    priority = models.ForeignKey('Priority', on_delete=models.SET_NULL, null=True)
    is_done = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
