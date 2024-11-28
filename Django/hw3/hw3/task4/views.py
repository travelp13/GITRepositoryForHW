import json
from django.http import HttpResponse, JsonResponse, FileResponse
from django.shortcuts import render


def home_view(request):
    return render(request, "task4/home.html")


def text_response(request):
    return HttpResponse(
        "Це текстова відповідь.", content_type="text/plain; charset=utf-8"
    )


def html_response(request):
    return render(request, "task4/sample.html")


def json_response(request):
    data = {"message": "Це JSON-відповідь"}
    return JsonResponse(data)


def file_response(request):
    content = "Це вміст файлу."
    response = HttpResponse(content, content_type="text/plain")
    response["Content-Disposition"] = 'attachment; filename="file.txt"'
    return response
