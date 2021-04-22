from django.http import HttpResponse
from django.shortcuts import render


def error_view(code, msg=""):
    def view(request, exception=""):
        response = render(request, "error.html", {'code': code, 'message': msg})
        response.status_code = code
        return response
    return


def home(request):
    return render(request, "home.html")


def contact(request):
    return render(request, "contact.html")


def construction(request):
    return render(request, "construction.html")
