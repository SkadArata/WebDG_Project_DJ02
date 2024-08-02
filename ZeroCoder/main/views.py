from django.shortcuts import render
from django.http import HttpResponse


def index(request):
#    return HttpResponse("<h2>28 июля 2024 года, воскресенье: это мой первый проект на Django</h2>")
    return render(request, 'main/index.html')
def new(request):
#    return HttpResponse("<h3>Это страница №2 для урока DJ02</h3>")
    return render(request, 'main/new.html')
#def data(request):
#    return HttpResponse("<center><h3>Data-страница</h3><h4> моего первого проекта на Django</h4></center>")

def data(request):
    return render(request, 'data.html')


# def test(request):
#    return HttpResponse("<center><h3>Test-страница моего первого проекта на Django</h3></center>")

def data2(request):
    return render(request, 'data2.html')

# def home(request):
#	return render(request, 'main/news.html')