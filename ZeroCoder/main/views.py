from django.shortcuts import render
from django.http import HttpResponse


def index(request):
#    return HttpResponse("<h2>28 июля 2024 года, воскресенье: это мой первый проект на Django</h2>")
    return render(request, 'main/index.html')
def new(request):
#    return HttpResponse("<h3>Это вторая страница моего первого проекта на Django</h3>")
    return render(request, 'main/new.html')
def data(request):
    return HttpResponse("<h3>Data-страница моего первого проекта на Django</h3>")

def test(request):
    return HttpResponse("<h3>Test-страница моего первого проекта на Django</h3>")
