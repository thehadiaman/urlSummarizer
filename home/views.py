from django.shortcuts import render, redirect


def home(request):
    data = {'error': '', 'email_value': '', 'url_value': ''}
    return render(request, 'index.html', data)
