from django.http import HttpResponse
from django.shortcuts import render


def error_view(code, msg=""):
    def view(request, exception=""):
        response = render(request, "error.html", {'code': code, 'message': msg})
        response.status_code = code
        return response
    return

def home(request):
    #return HttpResponse("Welcome to BEnOG")
    return render(request, "home.html")