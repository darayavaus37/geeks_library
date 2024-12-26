from django.db import models

class TodoModel(models.Model):
    CHECKING = [
        ('✅', 'Выполнено'),
        ('❌', 'Не выполнено'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField(default='Начну с ...')  
    choice_check = models.CharField(max_length=10, choices=CHECKING)

    def __str__(self):
        return self.title
