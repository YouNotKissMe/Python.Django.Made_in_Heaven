from django.shortcuts import render
from .models import Publication


def home(request):
    if 'search' in request.GET and request.GET['search']:
        if Publication.objects.filter(author__first_name__icontains=request.GET['search']):
            publication = Publication.objects.filter(author__first_name__icontains=request.GET['search'])
        elif Publication.objects.filter(author__last_name__icontains=request.GET['search']):
            publication = Publication.objects.filter(author__last_name__icontains=request.GET['search'])
        else:
            publication = Publication.objects.filter(title__icontains=request.GET['search'])
        if len(publication) != 0:
            return render(request, 'home_page.html', {'pubplications': publication})
        else:
            publication = Publication.objects.all()
            return render(request, 'home_page.html', {'pubplications': publication})
    else:
        publication = Publication.objects.all()
        return render(request, 'home_page.html', {'pubplications': publication})


def publication(request, id):
    try:
        page = Publication.objects.get(id=id)
        return render(request, 'publication_page.html', {'publication': page})
    except:
        publication = Publication.objects.all()
        return render(request, 'home_page.html', {'pubplications': publication})
