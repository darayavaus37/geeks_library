from django.shortcuts import render
from . import models

def all_products(request):
    if request.method == "GET":
        products = models.Product.objects.all().order_by('-id')  # Исправлено на objects
        context = {'products': products}
        return render(
            request,
            template_name='tags/all_products.html',
            context=context
        )

def books_by_tag(request, tag_name, template_name):
    if request.method == "GET":
        products = models.Product.objects.filter(tags__name=tag_name).order_by('-id')  # Исправлено на objects
        context = {'products': products}
        return render(
            request,
            template_name=template_name,
            context=context
        )

def child_books(request):
    return books_by_tag(request, '1.Книги для детей', 'tags/child_books.html')

def teen_books(request):
    return books_by_tag(request, '2.Книги для подростков', 'tags/teen_books.html')

def youth_books(request):
    return books_by_tag(request, '3.Книги для молодежи', 'tags/youth_books.html')

def elderly_books(request):
    return books_by_tag(request, '4.Книги для пенсионеров', 'tags/elderly_books.html')







# from django.shortcuts import render
# from . import models

# def all_product(request):
#     if request.method == "GET":
#         products = models.Product.objects.all().order_by('-id')
#         context = {'products': products}
#         return render(
#             request,
#             template_name='tags/all_products.html',
#             context=context
#         )
    

# def child_books(request):
#     if request.method == "GET":
#         products_ch = models.Product.object.filter(tags__name='1.Книги для детей').order_by('-id')
#         context = {'products_ch': products_ch}
#         return render(
#             request,
#             template_name='tags/child_books.html',
#             context=context
#         )
    

# def teen_books(request):
#     if request.method == "GET":
#         products_ch = models.Product.object.filter(tags__name='2.Книги для подростков').order_by('-id')
#         context = {'products_tn': teen_books}
#         return render(
#             request,
#             template_name='tags/teen_books.html',
#             context=context
#         )
    

# def youth_books(request):
#     if request.method == "GET":
#         products_ch = models.Product.object.filter(tags__name='3.Книги для молодежи').order_by('-id')
#         context = {'products_yo': youth_books}
#         return render(
#             request,
#             template_name='tags/youth_books.html',
#             context=context
#         )
    

# def elderly_books(request):
#     if request.method == "GET":
#         products_ch = models.Product.object.filter(tags__name='4.Книги для пенсионеров').order_by('-id')
#         context = {'products_el': elderly_books}
#         return render(
#             request,
#             template_name='tags/elderly_books.html',
#             context=context
#         )




# from django.shortcuts import render
# from . import models

# def all_product(request):
#     if request.method == "GET":
#         products = models.Product.objects.all().order_by('-id')
#         context = {'products': products}
#         return render(
#             request,
#             template_name='tags/all_products.html',
#             context=context
#         )

# def filter_books_by_tag(request, tag_name, template_name):
#     if request.method == "GET":
#         products = models.Product.objects.filter(tags__name=tag_name).order_by('-id')
#         context = {'products': products}
#         return render(
#             request,
#             template_name=template_name,
#             context=context
#         )

# def child_books(request):
#     return filter_books_by_tag(request, '1.Книги для детей', 'tags/child_books.html')

# def teen_books(request):
#     return filter_books_by_tag(request, '2.Книги для подростков', 'tags/teen_books.html')

# def youth_books(request):
#     return filter_books_by_tag(request, '3.Книги для молодежи', 'tags/youth_books.html')

# def elderly_books(request):
#     return filter_books_by_tag(request, '4.Книги для пенсионеров', 'tags/elderly_books.html')
