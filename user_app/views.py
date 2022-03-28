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


def delete(request, id):
    if request.user.is_authenticated:
        publication = Publication.objects.get(id=id)
        publication.delete()
        new_publications = Publication.objects.filter(author__last_login=request.user.last_login)
        return render(request, "profile_page.html", {'publication': new_publications})
    else:
        return render(request, "registration/login.html")


def edit(request, id):
    if request.user.is_authenticated:
        publication = Publication.objects.get(id=id)
        if request.method == 'POST':
            if request.POST.get('title'):
                publication.title = request.POST.get('title')
            if request.POST.get('category'):
                publication.category = request.POST.get('category')
            if request.POST.get('synopsis'):
                publication.synopsis = request.POST.get('synopsis')
            if request.POST.get('file'):
                publication.title = request.POST.get('file')
            publication.save()
            publications = Publication.objects.all()
            return render(request, "profile_page.html", {'publications': publications})
    else:
        return render(request, "registration/login.html")
