from django.shortcuts import render
from django.http import HttpResponse
import datetime

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
    

    
