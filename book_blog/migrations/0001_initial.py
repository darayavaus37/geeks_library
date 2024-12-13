# Generated by Django 5.1.3 on 2024-12-13 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='books/', verbose_name='Загрузите фото книги')),
                ('title', models.CharField(max_length=100, verbose_name='Укажите название книги')),
                ('description', models.TextField(blank=True, verbose_name='Укажите описание')),
                ('price', models.FloatField(default=10, verbose_name='Укажите цену книги')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('genre', models.CharField(choices=[('Ужасы', 'Ужасы'), ('Комедия', 'Комедия'), ('Фантастика', 'Фантастика')], default='Комедия', max_length=100)),
                ('time_watch', models.TimeField(blank=True, null=True, verbose_name='Укажите время прочтения книги')),
                ('director', models.CharField(default='А. С. Пушкин', max_length=100, verbose_name='Укажите автора книги')),
                ('trailer', models.URLField(null=True, verbose_name='Укажите ссылку аудиокниги')),
                ('author_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта автора')),
            ],
            options={
                'verbose_name': 'книгу',
                'verbose_name_plural': 'книги',
            },
        ),
    ]
