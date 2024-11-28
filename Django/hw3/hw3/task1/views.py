from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest


def main_page(request):
    return HttpResponse(
        """
        <h1>Головна сторінка</h1>
        <a href="/task1/">Сторінка task1</a><br>
        <a href="/task2/">Сторінка task2</a><br>
        <a href="/task3/">Сторінка task3</a><br>
        <a href="/task4/">Сторінка task4</a><br>
    """
    )


def tasks_view(request):
    lets_do_it = [
        {"priority": 100, "task": "Скласти перелік справ"},
        {"priority": 150, "task": "Вивчати Django"},
        {"priority": 1, "task": "Подумати про сенс життя"},
    ]
    sorted_tasks = sorted(lets_do_it, key=lambda x: x["priority"], reverse=False)
    return render(request, "task1/tasks.html", {"tasks": sorted_tasks})
