from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UrlModel
from django.views.csrf import csrf_failure
from validation.Validator import input_validation


def home(request):
    data = {'error': '', 'email_value': '', 'url_value': '', 'success_data': False}
    return render(request, 'index.html', data)


def error_403_view(request, reason=""):
    return render(request, '403.html', status=403)


def error_404_view(request, exception):
    return render(request, '404.html', status=404)


def process(request):
    try:
        if request.method == 'GET':
            return redirect('/')
        if request.method == 'POST':
            validation = input_validation(request.POST)
            print(validation)
            obj = redirect('/')
            return obj
    except UrlModel.DoesNotExist:
        return HttpResponse('404')
