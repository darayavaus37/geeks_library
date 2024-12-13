from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
from . import models



def book_detail_view(request, id):
     if request.method == "GET":
        book_id = get_object_or_404(models.BookModel, id=id)
        context = {
            'book': book_id,
        }
        return render(request, template_name='show_detail.html', context=context)
 

def book_list_view(request):
    if request.method == "GET":
        book_list = models.BookModel.objects.all().order_by('-id')

        context = {
            'book_list': book_list,
        }
        return render(request, template_name='show.html', context=context)

def about_view(request):
    if request.method == "GET":
        return HttpResponse('Привет!это мой первый проект')
    
def emoji_view(request):
    if request.method == "GET":
        return HttpResponse('👌🦊😋')
    
def image_library_view(request):
    if request.method == "GET":
        return HttpResponse('<img src="https://cdn.culture.ru/images/4774003b-ab33-5fd1-a983-714c7a78fc31">')
    
def aboutmypets_view(request):
    if request.method == "GET":
        return HttpResponse(' Доберман. ему 3 года . ')
    
def time_view(request):
    current_time = datetime.datetime.now()
    return HttpResponse(f"Привет! Это мой первый проект. Текущее время: {current_time}")

def contact_view(request):
    return render(request, 'contact.html') 

