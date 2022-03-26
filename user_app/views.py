from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .form import Registration_form
from work.models import Publication
from django.contrib.auth.models import User


class RegistrationView(CreateView):
    template_name = 'registration_page.html'
    form_class = Registration_form
    model = User
    success_url = reverse_lazy('home_page')


def profile(request):
    if request.user.is_authenticated:
        publication = Publication.objects.filter(author__last_login=request.user.last_login)
        return render(request, 'profile_page.html', {'user': request.user, 'publication': publication})
    else:
        return render(request, 'registration/login.html')
