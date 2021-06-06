from django.shortcuts import render, redirect
from validation.Validator import input_validation


def home(request):
    data = {'error': request.COOKIES['error'] if 'error' in request.COOKIES else False, 'email_value': '', 'url_value': ''}
    success_data = False
    if 'success_data' in request.COOKIES:
        data['success_data'] = request.COOKIES['success_data']
        success_data = True
    obj = render(request, 'index.html', data)
    if 'error' in request.COOKIES:
        obj.delete_cookie('error')
    if success_data:
        obj.delete_cookie('success_data')
    return obj


def process(request):
    if request.method == 'GET':
        return redirect('/')
    if request.method == 'POST':
        validation = input_validation(request.POST)
        obj = redirect('/')
        if validation != 'email' and validation != 'url' and validation != 'atc':
            obj.set_cookie('success_data', 'successful')
        else:
            obj.set_cookie('error', validation)
        return obj


def error_403_view(request, reason=""):
    return render(request, '403.html', status=403)


def error_404_view(request, exception):
    return render(request, '404.html', status=404)
