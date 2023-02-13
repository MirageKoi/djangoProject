from django.http import HttpRequest
from django.shortcuts import render

tasks = [
    {"id": 1, "title": "Title 1", "description": "Some long task description...", "created": "2022-01-24 12:00",
     "updated": "2022-01-25 12:00", "completed": False},
    {"id": 2, "title": "Title 2", "description": "Some long task description...", "created": "2022-01-24 12:00",
     "updated": "2022-01-25 12:00", "completed": True},
    {"id": 3, "title": "Title 3", "description": "Some long task description...", "created": "2022-01-24 12:00",
     "updated": "2022-01-25 12:00", "completed": False},
]


def homepage(request: HttpRequest):
    return render(request, "base.html")


def task_list_view(request: HttpRequest):
    return render(request, "task_list.html", {"tasks": tasks})


def task_detailed_view(request: HttpRequest, number: int):
    for obj in tasks:
        if obj["id"] == number:
            return render(request, "task_detail.html", {"object": obj})


def form_view(request):
    return render(request, 'form.html')
