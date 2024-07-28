from django.http import HttpResponse


def index(request):
    return HttpResponse("<h2>28 июля 2024 года, воскресенье: это мой первый проект на Django</h2>")

def new(request):
    return HttpResponse("<h3>Это вторая страница моего первого проекта на Django</h3>")

def data(request):
    return HttpResponse("<h3>Data-страница моего первого проекта на Django</h3>")

def test(request):
    return HttpResponse("<h3>Test-страница моего первого проекта на Django</h3>")
