from django.shortcuts import render, redirect
from validation.Validator import input_validation
from .models import UrlModel
from django.http import HttpResponse


def home(request):
    data = {'error': request.COOKIES['error'] if 'error' in request.COOKIES else False}
    success_data = False
    if 'success_data' in request.COOKIES:
        data['success_data'] = request.COOKIES['success_data']
        success_data = True

    if 'error' in request.COOKIES:
        data['url_value' if request.COOKIES['error'] == 'email' else 'email_value'] = request.COOKIES['url_value' if request.COOKIES['error'] == 'email' else 'email_value']
        if request.COOKIES != 'atc':
            data['checked'] = 'checked'

    obj = render(request, 'index.html', data)
    if 'error' in request.COOKIES:
        obj.delete_cookie('error')
        obj.delete_cookie('email_value')
        obj.delete_cookie('url_value')
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
            try:
                if UrlModel.objects.filter(original_url=request.POST["url"]).filter(email=request.POST["email"]):
                    summarized_url = \
                        UrlModel.objects.filter(original_url=request.POST["url"]).filter(email=request.POST["email"])[
                            0].summarized_url
                    summarized_url = str(summarized_url).replace('-', '')
                    obj.set_cookie('success_data', f'http://localhost:8000/{summarized_url}')

                else:
                    raise IndexError
            except IndexError:
                url_model = UrlModel(email=request.POST['email'], original_url=request.POST['url'])
                UrlModel.save(url_model)
                summarized_url = UrlModel.objects.filter(original_url=request.POST["url"]).filter(email=request.POST["email"])[0].summarized_url
                summarized_url = str(summarized_url).replace('-', '')
                obj.set_cookie('success_data', f'http://localhost:8000/{summarized_url}')
        else:
            obj.set_cookie('error', validation)
            obj.set_cookie('url_value' if validation == 'email' else 'email_value', request.POST['url' if validation == 'email' else 'email'])
        return obj


def get_url(request, url):
    data = UrlModel.objects.filter(summarized_url=url)
    if data:
        return redirect(data[0].original_url)
    else:
        return HttpResponse("ERROR")


def error_403_view(request, reason=""):
    return render(request, '403.html', status=403)


def error_404_view(request, exception):
    return render(request, '404.html', status=404)
