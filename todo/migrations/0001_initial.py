# Generated by Django 5.1.3 on 2024-12-25 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(default='Начну с ...')),
                ('choice_check', models.CharField(choices=[('✅', 'Выполнено'), ('❌', 'Не выполнено')], max_length=10)),
            ],
        ),
    ]
