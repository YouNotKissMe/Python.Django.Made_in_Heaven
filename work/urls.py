from django.urls import path
from .views import publication

urlpatterns = [
    path('<int:id>/',publication, name='publication')

]