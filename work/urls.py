from django.urls import path
from .views import publication, PublicationView

urlpatterns = [
    path('<int:id>/', publication, name='publication'),
    path('add/',  PublicationView.as_view() ,name='add_publication')

]
