from django.shortcuts import render
from django.http import JsonResponse
from .forms import RegistrationForm
from django.contrib.auth.hashers import make_password

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data["password"])  # Хэшируем пароль
            user.save()
            return JsonResponse({"message": "Пользователь успешно зарегистрирован!", "salary": user.salary})
        return JsonResponse({"errors": form.errors}, status=400)
    
    return render(request, "users/register.html", {"form": RegistrationForm()})
