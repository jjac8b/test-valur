from django.urls import path
from django.http import JsonResponse


def multiply(request):
    try:
        num1 = float(request.GET.get("num1", 0))
        num2 = float(request.GET.get("num2", 0))
        result = num1 * num2
        return JsonResponse({"num1": num1, "num2": num2, "result": result})
    except (TypeError, ValueError) as e:
        return JsonResponse({"error": e}, status=400)


urlpatterns = [
    path("multiply/", multiply),
]
