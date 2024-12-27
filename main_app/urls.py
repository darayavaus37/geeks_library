from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('library_blog.urls')),  # Главная страница (главное приложение)
    path('books/', include('age_rest_books.urls')),  # Приложение для книг
    path('basket/', include('basket.urls')),  # Приложение для корзины
    path('parser/', include('parser_app.urls')),  # Приложение для парсинга
    path('users/', include('users.urls')),  # Приложение для пользователей
]

# Добавление медиа и статики
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
