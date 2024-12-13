from django.db import models

class BookModel(models.Model):
    GENRE = (
        ('Ужасы', 'Ужасы'),
        ('Комедия', 'Комедия'),
        ('Фантастика', 'Фантастика'),
    )

    image = models.ImageField(upload_to='books/', verbose_name='Загрузите фото книги')
    title = models.CharField(max_length=100, verbose_name='Укажите название книги')
    description = models.TextField(verbose_name='Укажите описание', blank=True)
    price = models.FloatField(verbose_name='Укажите цену книги', default=10)
    created_at = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=100, choices=GENRE, default='Комедия')  
    time_watch = models.TimeField(verbose_name='Укажите время прочтения книги', blank=True, null=True)
    director = models.CharField(max_length=100, verbose_name='Укажите автора книги', default='А. С. Пушкин')
    trailer = models.URLField(verbose_name='Укажите ссылку аудиокниги', null=True)
    author_email = models.EmailField(verbose_name='Почта автора', blank=True, null=True)

   
    

    class Meta:
        verbose_name = 'книгу'
        verbose_name_plural = 'книги'

    def __str__(self):
        return self.title


class Review (models.Model):
    STARS = (
        ('⭐', '⭐'),
        ('⭐⭐', '⭐⭐'),
        ('⭐⭐⭐', '⭐⭐⭐'),
        ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
        ('⭐⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐⭐'),
    )
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name='reviews')
    created_at = models.DateField(auto_now_add=True)
    text_review = models.TextField(verbose_name='напишите отзыв о книге ')
    stars = models.CharField(max_length=100,choices=STARS, verbose_name='поставьте оценку', default='⭐')

    def __str__(self):
        return f'{self.book}:{self.stars}'




