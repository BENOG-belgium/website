from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from users.forms import UserCreationForm

def login_view(request):
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        next = request.GET.get("next", "/")
        next = next if next != "" else "/"
        return HttpResponseRedirect(next)
    else:
        messages.error(request, "Aucun compte correspondant à cet identifiant n'a été trouvé")
        return HttpResponseRedirect(request.META["HTTP_REFERER"])

class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = '/'

    def get_initial(self):
        initial = super(RegisterView, self).get_initial()
        initial = initial.copy()
        initial['username'] = self.request.GET.get("username")
        return initial

    def form_valid(self, form):
        ret = super(RegisterView, self).form_valid(form)
        user = form.auth_user()
        if user:
            login(self.request, user)
        return ret