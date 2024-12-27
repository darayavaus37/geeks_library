from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

class CheckSpecialistLevelMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Проверяем, что запрос идет к эндпоинту регистрации
        if request.path == "/register/" and request.method == "POST":
            level = request.POST.get("level")
            if not level:
                return JsonResponse({"error": "Не указан уровень специалиста"}, status=400)
            
            # Проверяем уровень и выставляем ЗП
            salary = None
            if level.lower() == "jun":
                salary = 700
            elif level.lower() == "middle":
                salary = 1000
            elif level.lower() == "senior":
                salary = 2000
            else:
                return JsonResponse({"error": "Пожалуйста, подтяните ваш уровень!"}, status=400)

            # Добавляем зарплату в запрос
            request.POST._mutable = True  # Для возможности изменения запроса
            request.POST["salary"] = salary
            request.POST._mutable = False
        return None
